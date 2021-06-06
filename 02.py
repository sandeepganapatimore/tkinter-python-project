from tkinter import *
from tkinter import ttk
from tkinter import pymysql

import mysql.connector

from tkinter import messagebox
class Student:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Sandeep Mobile Shopee")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text="Sandeep Mobile shoppe ", bd=8,
                      relief=SUNKEN, font=("times new roman", 30, "bold"), bg="red")
        title.pack(side=TOP, fill=X)

        ## All varaibles####
        "Name", "Contact_Number", "Date", "Address"

        # self.Name_var=StringVar()
        self.Contact_Number_var = StringVar()
        self.Date_var = StringVar()
        self.Address_var = StringVar()
        self.model_var = StringVar()
        self.Madein_var = StringVar()
        self.price_var = StringVar()
        self.cust_Name_var = StringVar()

        self.search_by= StringVar()
        self.search_txt = StringVar()



    def window(self):
        #######    MANAGE FRAME  ######
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#363945")
        Manage_frame.place(x=20,y=100,width=450,height=560)

        m_title=Label(Manage_frame,text="DETAILS",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_model=Label(Manage_frame,text="Model",fg="black",font=("times new roman",20,"bold"))
        lbl_model.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        txt_model=Entry(Manage_frame,textvariable=self.model_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_model.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_model=Label(Manage_frame,text="MADE_IN",fg="black",font=("times new roman",20,"bold"))
        lbl_model.grid(row=2,column=0,pady=10,padx=10,sticky="w")

        combo_madein=ttk.Combobox(Manage_frame,font=("times now roman",10,"bold"),state="readonly")
        combo_madein["values"]=("INDIA","CHINA","USA","THIALAND")
        combo_madein.grid(row=2,column=1,pady=10,padx=10)
        
        # txt_model=Entry(Manage_frame,font=("times new roman",13,"bold"),bd=2,relief=GROOVE)
        # txt_model.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Price=Label(Manage_frame,text="PRICE",fg="black",font=("times new roman",20,"bold"))
        lbl_Price.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        txt_Price=Entry(Manage_frame,textvariable=self.price_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_Price.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Name=Label(Manage_frame,text="CUST_NAME",fg="black",font=("times new roman",20,"bold"))
        lbl_Name.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        txt_Name=Entry(Manage_frame,textvariable=self.cust_Name_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact=Label(Manage_frame,text="CONTACT",fg="black",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        txt_Contact=Entry(Manage_frame,textvariable=self.Contact_Number_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

         

        txt_Contact=Entry(Manage_frame,textvariable=self.Date_var,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_sold=Label(Manage_frame,text="DATE",fg="black",font=("times new roman",20,"bold"))
        lbl_sold.grid(row=6,column=0,pady=10,padx=10,sticky="w")


        lbl_Address=Label(Manage_frame,text="ADDRESS",fg="black",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=10,sticky="w")

        txt_Address=Entry(Manage_frame,textvariable=self.Address_var,font=("",10))
        txt_Address.grid(row=7,column=1,pady=15,padx=20,sticky="w")








# BUTTONS
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=15,y=500,width=450)

        Addbtn=Button(btn_frame,text="Add",font="bold",width=7,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)

        updatebtn=Button(btn_frame,text="Update",font="bold",width=7,command=Update_data).grid(row=0,column=1,padx=10,pady=10)

        deletebtn=Button(btn_frame,text="Delete",font="bold",width=7,command=delete_data).grid(row=0,column=2,padx=10,pady=10)

        clearbtn=Button(btn_frame,text="clear",font="bold",width=7,command=self.clear).grid(row=0,column=3,padx=10,pady=10)















# DETAILS FRAME #################m_
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        Detail_frame.place(x=500,y=100,width=850,height=560)

        D_title=Label(Detail_frame,text="Repair_Details",fg="black",font=("times new roman",20,"bold"))
        D_title.grid(row=0,columnspan=2,pady=20)

        
        lbl_search=Label(Detail_frame,text="Search By",fg="black",font=("times new roman",20,"bold"))
        lbl_search.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        combo_search=ttk.Combobox(Detail_frame,textvariable=self.search_by,width=20,font=("times now roman",10,"bold"),state="readonly")
        combo_search["values"]=("cust_Name","Contact_Number.","Address")
        combo_search.grid(row=1,column=1,pady=10,padx=10)

        txt_search=Entry(Detail_frame,textvaraible=self.search_txt,width=19,font=("times of roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=1,column=2,pady=10,padx=15,sticky="w")

        searchbtn=Button(Detail_frame,text="search",width=7,command=search_txt).grid(row=2,column=1,padx=20,pady=10)
        showallbtn=Button(Detail_frame,text="Show All",width=7,command=fetch_data).grid(row=2,column=2,padx=20,pady=10)



        # lbl_type=Label(Detail_frame,text="Type",fg="black",font=("times new roman",20,"bold"))
        # lbl_type.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        # combo_typeof=ttk.Combobox(Detail_frame,font=("times now roman",10,"bold"),state="readonly")
        # combo_typeof["values"]=("Display","Touch_screen","Screen_gaurd")
        # combo_typeof.grid(row=3,column=1,pady=10,padx=10)


        # lbl_Price=Label(Detail_frame,text="PRICE",fg="black",font=("times new roman",20,"bold"))
        # lbl_Price.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        # txt_Price=Entry(Detail_frame,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        # txt_Price.grid(row=4,column=1,pady=10,padx=20,sticky="w")


        # lbl_Admitdate=Label(Detail_frame,text="Admit_Date",fg="black",font=("times new roman",20,"bold"))
        # lbl_Admitdate.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        # txt_Admitdate=Entry(Detail_frame,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        # txt_Admitdate.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        # lbl_Dischargedate=Label(Detail_frame,text="Discharge_Date",fg="black",font=("times new roman",20,"bold"))
        # lbl_Dischargedate.grid(row=6,column=0,pady=10,padx=10,sticky="w")

        # txt_Dischargedate=Entry(Detail_frame,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        # txt_Dischargedate.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        












        Table_Frame=Frame(Detail_frame,bd=4,relief=RIDGE)
        Table_Frame.place(x=10,y=190,width=760,height=350)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_Y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.table=ttk.Treeview(Table_Frame,columns=( "Model","Made_In","Price","Name","Contact_Number","Date","Address"),yscrollcommand=scroll_Y.set,xscrollcommand=scroll_x.set)
  
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=table.xview)
        scroll_Y.config(command=table.yview)
        self.table.heading("Model",text="Model")
        self.table.heading("Made_In",text="Made_In")
        self.table.heading("Price",text="Price")
        self.table.heading("Name",text="Name")
        self.table.heading("Contact_Number",text="Phone number")
        self.table.heading("Date",text="Date")
        self.table.heading("Address",text="Address")
        self.table['show']="headings"
        self.table.pack(fill=BOTH)
        self.table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()






def add_student(self):
        if self.cust_Name_var.get()=="" or self.Contact_Number_var.get()=="" or self.Address_var.get()=="":

                messagebox.showerror("Erro","All fields are required!!")
        else:
                
                con=pymysql.conect(host="localhost",user="root",password="sandy@23.",database="shop")
                cur=con.cursor()
                cur.execute("insert into mbshop values(%s,%s,%s,%s,%s,%s,%s)",(
                self.model_var.get(),
                self.Madein_var.get(),
                self.price_var.get(),
                self.cust_Name_var.get(),
                self.Contact_Number_var.get(),
                self.Date_var.get(),
                self.Address_var.get()

        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


def fetch_data(self):
        con=pymysql.conect(host="localhost",user="root",password="sandy@23.",database="shop")
        cur=con.cursor()
        cur.execute("select * from mbshop")
        rows=cur.fetchall()
        if(len(rows)!=0):
                self.table.delete(*self.table.get_Sdata)
                for row in rows:
                        self.mbshop_table.insert(''.END,values=row)
                con.commit()
        con.close()


def clear(self):
        self.model_var.set("")
        self.Madein_var.set("")
        self.price_var.set("")
        self.cust_Name_var.set("")
        self.Contact_Number_var.set("")
        self.Date_var.set("")
        self.Address_var.set("")


def get_cursor(self,ev):
        cursor_row=self.table.focus()
        contents=self.table.item(cursor_row)
        row=contents['values']
        print(row)
        # con=pymysql.connect(host="localhost",user="root",password="sandy@23.",database="stm")
        # cur=con.cursor()
        # cur.execute("select * from student where ")
        # rows=cur.fetchall()
        # if(len(rows)!=0):
        #         self.table.delete(*self.table.get_Sdata)
        #         for row in rows:
        #                 self.student_table.insert(''.END,values=row)
        #         con.commit()
        # con.close()
        self.model_var.set(row[0])
        self.Madein_var.set(row[1])
        self.price_var.set(row[2])
        self.cust_Name_var.set(row[3])
        self.Contact_Number_var.set(row[4])
        self.Date_var.set(row[5])
        self.Address_var.set(row[6])
       
def Update_data(self):
        con=pymysql.conect(host="localhost",user="root",password="sandy@23.",database="shop")
        cur=con.cursor()
        cur.execute("update mbshop set model=%s,MadeIn=%s,price=%s,cust_Name=%s,Contact_Number=%s,Date_var=%s,Address_var=%s where model_var=%s",(
                self.model_var.get(),
                self.Madein_var.get(),
                self.price_var.get(),
                self.cust_Name_var.get(),
                self.Contact_Number_var.get(),
                self.Date_var.get(),
                self.Address_var.get()

        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

def delete_data(self):
        con=pymysql.conect(host="localhost",user="root",password="sandy@23.",database="shop")
        cur=con.cursor()
        cur.execute("Delete from mbshop where model_var=%s",self.model_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        

def search_data(self):
        con=pymysql.conect(host="localhost",user="root",password="sandy@23.",database="shop")
        cur=con.cursor()
        cur.execute("select * from mbshop where "+str(self.search_by.get()+"LIKE '%"+str(self.search_txt.get()))+"%'")
        rows=cur.fetchall()
        if(len(rows)!=0):
                self.table.delete(*self.table.get_Sdata)
                for row in rows:
                        self.mbshop_table.insert(''.END,values=row)
                con.commit()
        con.close()




root=Tk()
obj=Student(root)
obj.window()
root.mainloop()