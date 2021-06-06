from tkinter import *
from tkinter import ttk
# import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Sandeep Mobile Shopee")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text="Sandeep Mobile shoppe ", bd=8,
                      relief=SUNKEN, font=("times new roman", 40, "bold"), bg="red")
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


    def window(self):
        #######    MANAGE FRAME  ######
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="grey")
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
        txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

# BUTTONS
        btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=15,y=500,width=450)

        Addbtn=Button(btn_frame,text="Add",width=7).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Update",width=7).grid(row=0,column=1,padx=10,pady=10)

        deletebtn=Button(btn_frame,text="Delete",width=7).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="clear",width=7).grid(row=0,column=3,padx=10,pady=10)



# DETAILS FRAME #################m_
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        Detail_frame.place(x=500,y=100,width=850,height=560)

        D_title=Label(Detail_frame,text="Repair_Details",fg="black",font=("times new roman",20,"bold"))
        D_title.grid(row=0,columnspan=2,pady=20)

        
        lbl_search=Label(Detail_frame,text="Search By",fg="black",font=("times new roman",20,"bold"))
        lbl_search.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        combo_search=ttk.Combobox(Detail_frame,width=20,font=("times now roman",10,"bold"),state="readonly")
        combo_search["values"]=("Name","Contact_NO.","Address")
        combo_search.grid(row=1,column=1,pady=10,padx=10)

        txt_search=Entry(Detail_frame,width=19,font=("times of roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=1,column=2,pady=10,padx=15,sticky="w")

        searchbtn=Button(Detail_frame,text="search",width=7).grid(row=2,column=1,padx=20,pady=10)
        showallbtn=Button(Detail_frame,text="Show All",width=7).grid(row=2,column=2,padx=20,pady=10)



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
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_Y=Scrollbar(Table_Frame,orient=VERTICAL)
        table=ttk.Treeview(Table_Frame,columns=("Name","Contact_Number","Date","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=table.xview)
        scroll_Y.config(command=table.yview)
        table.heading("Name",text="Name")
        table.heading("Contact_Number",text="Phone number")
        table.heading("Date",text="Name")
        table.heading("Address",text="Address")
        table['show']="headings"
        table.pack(fill=BOTH)




root=Tk()
obj=Student(root)
obj.window()
root.mainloop()