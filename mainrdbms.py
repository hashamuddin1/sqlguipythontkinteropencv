import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hashamsql",
    database="railwaystation"
    )
print(mydb)

mycursor=mydb.cursor()


mycursor.execute("create table customer5 (first_name VARCHAR(20),last_name VARCHAR(20),mobile varchar(20),customer_id int(20),cnic_number varchar(35),date_of_journey date,way_of_payment varchar(20),amount_of_payment int,train VARCHAR(20),no_of_ticket int,location varchar(20),primary key(customer_id))")

mycursor.execute("create table station (station_name varchar(20), station_id int(8),location varchar(25),number_of_track int(8),number_of_train int(8),manager_name varchar(20),city varchar(20),primary key(station_id))")


mycursor.execute("create table train (train_name VARCHAR(20),train_id int(10),shift varchar(15),route varchar(30),timing time,capacity int(5),station_id int(8),number_of_station int(5),fault VARCHAR(20),next_journey varchar(15),recent_journey varchar(15),primary key(train_id),foreign key(station_id) references station(station_id))")

mycursor.execute("create table employee1 (first_name VARCHAR(20),last_name VARCHAR(20),mobile varchar(20),department varchar(20),station_id int(8),employee_id varchar(15),salary int,joining_date date,address VARCHAR(30),father_name varchar(25),date_of_birth date,primary key(employee_id),foreign key(station_id) references station(station_id))")


mycursor.execute("create table inventory1 (inventory_name VARCHAR(20),inventory_id VARCHAR(20),station_id int(8),product_needed varchar(20),no_of_material int(10),item_id varchar(15),modified_date date,primary key(inventory_id),foreign key(station_id) references station(station_id))")

mycursor.execute("create table ticket (ticket_id VARCHAR(10),train_id int(10),issue_date date,route varchar(20),payment int(10),ticket_category varchar(25),timing time,primary key(ticket_id),foreign key(train_id) references train(train_id))")


mycursor.execute("create table payment1 (payment_id VARCHAR(10),payment_date date,tax int(10),customer_id int(20),receiving_date date,way_of_payment varchar(15),primary key(payment_id),foreign key(customer_id) references customer5(customer_id))")

mycursor.execute("create table newschedule (train_name VARCHAR(20),train_id int(11),route varchar(35),passenger_capacity int(10),journey_date date,timing time,foreign key(train_id) references train(train_id))")



from tkinter import *
from tkinter import messagebox
from tkhtmlview import HTMLLabel
import tkinter.font as font
from tkinter import ttk

root=Tk()
root.geometry("1340x680+0+0")
root.title("PAKISTAN RAILWAY")
my_label1 = HTMLLabel(root, html="""<h2>WELCOME TO PAKISTAN RAILWAY</h2>""")


  
# Adjust label
my_label1.pack(pady=0, padx=0)

import cv2
capture=cv2.VideoCapture(0)

if capture.isOpened():
    ret,frame=capture.read()
    cv2.imwrite("osman1.jpg",frame)

l=cv2.imread("osman1.jpg")

aaa=0
while aaa<=200:
    aaa+=1
 #   cv2.imshow("window",l)
    if cv2.waitKey()=="q":
        break

capture.release()
cv2.destroyAllWindows()

def call_me1():
    window=Tk()
    window.title("CUSTOMER FORM")
    window.geometry("1340x680+0+0")
    b=Label(window,text="FIRST NAME")
    b.place(x=10,y=120)
    c=Label(window,text="LAST NAME")
    c.place(x=10,y=160)
    d=Label(window,text="MOBILE NUMBER")
    d.place(x=10,y=200)
    e=Label(window,text="CUSTOMER ID")
    e.place(x=10,y=320)
    f=Label(window,text="CNIC NUMBER")
    f.place(x=10,y=360)
    g=Label(window,text="DATE OF JOURNEY")
    g.place(x=10,y=400)
    h=Label(window,text="WAY OF PAYMENT")
    h.place(x=10,y=520)
    i=Label(window,text="AMOUNT OF PAYMENT")
    i.place(x=10,y=560)
    j=Label(window,text="NUMBER OF TICKET")
    j.place(x=10,y=440)
    k=Label(window,text="ADDRESS")
    k.place(x=10,y=480)
    b_entry=Entry(window)
    b_entry.place(x=150,y=120)
    c_entry=Entry(window)
    c_entry.place(x=150,y=160)
    d_entry=Entry(window)
    d_entry.place(x=150,y=200)
    e_entry=Entry(window)
    e_entry.place(x=150,y=320)
    f_entry=Entry(window)
    f_entry.place(x=150,y=360)
    g_entry=Entry(window)
    g_entry.place(x=150,y=400)
    h_entry=Entry(window)
    h_entry.place(x=150,y=520)
    i_entry=Entry(window)
    i_entry.place(x=150,y=560)
    j_entry=Entry(window)
    j_entry.place(x=150,y=440)
    k_entry=Entry(window)
    k_entry.place(x=150,y=480)
    m=StringVar(window)
    m.set("           SELECT THE TRAIN")
    l=OptionMenu(window,m,"SHALIMAR EXPRESS","LAHORE EXPRESS","TEEZ GAM","AWAM EXPRESS","RAWALPINDI EXPRESS")
    l.pack()
    l.place(x=80,y=248)
    def save_info():
        try:
            sql = "INSERT INTO customer5(first_name, last_name,mobile,customer_id,cnic_number,date_of_journey,way_of_payment,amount_of_payment,train,no_of_ticket,location) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),f_entry.get(),g_entry.get(),h_entry.get(),i_entry.get(),m.get(),j_entry.get(),k_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window,text=e)
            p.place(x=80,y=600)
            p.pack()
    q=Button(window,text="SUMBIT",width="25",fg="white",bg="blue",command=save_info)
    q.pack()
    q.place(x=70,y=610)
    def sql1():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM customer5"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="FIRST NAME")
        tv.heading(2,text="LAST NAME")
        tv.heading(3,text="MOBILE")
        tv.heading(4,text="CUSTOMER ID")
        tv.heading(5,text="CNIC NUMBER")
        tv.heading(6,text="DATE OF JOURNEY")
        tv.heading(7,text="WAY OF PAYMENT")
        tv.heading(8,text="AMOUNT OF PAYMENT")
        tv.heading(9,text="TRAIN")
        tv.heading(10,text="NUMBER OF TICKET")
        tv.heading(11,text="LOCATION")
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window,text="     VIEW    ",command=sql1,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)




buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
b=Button(root,text="CUSTOMER",command=call_me1,font=buttonFont)
b.pack()
b.place(x=100,y=100)

def call_me2():
    window1=Tk()
    window1.geometry("1340x680+0+0")
    window1.title("EMPLOYEE FORM")
    bemp=Label(window1,text="FIRST NAME")
    bemp.place(x=10,y=120)
    cemp=Label(window1,text="LAST NAME")
    cemp.place(x=10,y=160)
    demp=Label(window1,text="MOBILE NUMBER")
    demp.place(x=10,y=200)
    eemp=Label(window1,text="STATION ID")
    eemp.place(x=10,y=320)
    femp=Label(window1,text="EMPLOYEE ID")
    femp.place(x=10,y=360)
    gemp=Label(window1,text="SALARY")
    gemp.place(x=10,y=400)
    hemp=Label(window1,text="FATHER NAME")
    hemp.place(x=10,y=520)
    iemp=Label(window1,text="DATE OF BIRTH")
    iemp.place(x=10,y=560)
    jemp=Label(window1,text="JOINING DATE")
    jemp.place(x=10,y=440)
    kemp=Label(window1,text="ADDRESS")
    kemp.place(x=10,y=480)
    bemp_entry=Entry(window1)
    bemp_entry.place(x=150,y=120)
    cemp_entry=Entry(window1)
    cemp_entry.place(x=150,y=160)
    demp_entry=Entry(window1)
    demp_entry.place(x=150,y=200)
    eemp_entry=Entry(window1)
    eemp_entry.place(x=150,y=320)
    femp_entry=Entry(window1)
    femp_entry.place(x=150,y=360)
    gemp_entry=Entry(window1)
    gemp_entry.place(x=150,y=400)
    hemp_entry=Entry(window1)
    hemp_entry.place(x=150,y=520)
    iemp_entry=Entry(window1)
    iemp_entry.place(x=150,y=560)
    jemp_entry=Entry(window1)
    jemp_entry.place(x=150,y=440)
    kemp_entry=Entry(window1)
    kemp_entry.place(x=150,y=480)




    memp=StringVar(window1)
    memp.set("           SELECT THE DEPARTMENT")
    lemp=OptionMenu(window1,memp,"ACCOUNTS","MANUFACTURING","SALES","REPAIRING","FINANCIAL")
    lemp.pack()
    lemp.place(x=80,y=248)

#mycursor.execute("create table employee (first_name VARCHAR(20),last_name VARCHAR(20),mobile varchar(20),department varchar(20),email varchar(35),employee_id varchar(15),salary int,joining_date date,address VARCHAR(30),father_name varchar(25),date_of_birth date,primary key(employee_id))")

    def save_info1():
        try:
            sql = "INSERT INTO employee1(first_name, last_name,mobile,department,station_id,employee_id,salary,joining_date,address,father_name,date_of_birth) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (bemp_entry.get(),cemp_entry.get(),demp_entry.get(),memp.get(),eemp_entry.get(),femp_entry.get(),gemp_entry.get(),jemp_entry.get(),kemp_entry.get(),hemp_entry.get(),iemp_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window1,text=e)
            p.place(x=80,y=600)
            p.pack()

    q=Button(window1,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info1)
    q.pack()
    q.place(x=70,y=610)
    def sql3():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM employee1"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="FIRST NAME")
        tv.heading(2,text="LAST NAME")
        tv.heading(3,text="MOBILE")
        tv.heading(4,text="DEPARTMENT")
        tv.heading(5,text="STATION ID")
        tv.heading(6,text="EMPLOYEE ID")
        tv.heading(7,text="SALARY")
        tv.heading(8,text="JOINING DATE")
        tv.heading(9,text="ADDRESS")
        tv.heading(10,text="FATHER NAME")
        tv.heading(11,text="DATE OF BIRTH")
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window1,text="     VIEW    ",command=sql3,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)



buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
c=Button(root,text="EMPLOYEE",command=call_me2,font=buttonFont)
c.pack()
c.place(x=100,y=220)

def call_me3():
    window2=Tk()
    window2.geometry("1340x680+0+0")
    window2.title("TRAIN FORM")
    
    btra=Label(window2,text="TRAIN NAME")
    btra.place(x=10,y=120)
    ctra=Label(window2,text="TRAIN ID")
    ctra.place(x=10,y=160)
    dtra=Label(window2,text="SHIFT")
    dtra.place(x=10,y=200)
    etra=Label(window2,text="TIMING")
    etra.place(x=10,y=320)
    ftra=Label(window2,text="CAPACITY")
    ftra.place(x=10,y=360)
    gtra=Label(window2,text="STATION ID")
    gtra.place(x=10,y=400)
    htra=Label(window2,text="NEXT JOURNEY")
    htra.place(x=10,y=520)
    itra=Label(window2,text="RECENT JOURNEY")
    itra.place(x=10,y=560)
    jtra=Label(window2,text="NUMBER OF STATIONS")
    jtra.place(x=10,y=440)
    ktra=Label(window2,text="FAULT")
    ktra.place(x=10,y=480)

    btra_entry=Entry(window2)
    btra_entry.place(x=150,y=120)
    ctra_entry=Entry(window2)
    ctra_entry.place(x=150,y=160)
    dtra_entry=Entry(window2)
    dtra_entry.place(x=150,y=200)
    etra_entry=Entry(window2)
    etra_entry.place(x=150,y=320)
    ftra_entry=Entry(window2)
    ftra_entry.place(x=150,y=360)
    gtra_entry=Entry(window2)
    gtra_entry.place(x=150,y=400)
    htra_entry=Entry(window2)
    htra_entry.place(x=150,y=520)
    itra_entry=Entry(window2)
    itra_entry.place(x=150,y=560)
    jtra_entry=Entry(window2)
    jtra_entry.place(x=150,y=440)
    ktra_entry=Entry(window2)
    ktra_entry.place(x=150,y=480)


    mtra=StringVar(window2)
    mtra.set("           SELECT THE ROUTE OF TRAIN")
    ltra=OptionMenu(window2,mtra,"KARACHI TO LAHORE","LAHORE TO PINDI","PINDI TO MULTAN","MULTAN TO QUETTA","QUETTA TO FAISLABAD")
    ltra.pack()
    ltra.place(x=80,y=248)

    def save_info2():
        try:
            sql = "INSERT INTO train(train_name,train_id,shift,route,timing,capacity,station_id,number_of_station,fault,next_journey,recent_journey) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (btra_entry.get(),ctra_entry.get(),dtra_entry.get(),mtra.get(),etra_entry.get(),ftra_entry.get(),gtra_entry.get(),jtra_entry.get(),ktra_entry.get(),htra_entry.get(),itra_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window2,text=e)
            p.place(x=80,y=600)
            p.pack()

    q=Button(window2,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info2)
    q.pack()
    q.place(x=70,y=610)

    def sql4():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM train"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="TRAIN NAME")
        tv.heading(2,text="TRAIN ID")
        tv.heading(3,text="SHIFT")
        tv.heading(4,text="ROUTE")
        tv.heading(5,text="TIMING")
        tv.heading(6,text="CAPACITY")
        tv.heading(7,text="STATION ID")
        tv.heading(8,text="NUMBER OF STATION")
        tv.heading(9,text="FAULT")
        tv.heading(10,text="NEXT JOURNEY")
        tv.heading(11,text="RECENT JOURNEY")
        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window2,text="     VIEW    ",command=sql4,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)





buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
d=Button(root,text="    TRAIN     ",command=call_me3,font=buttonFont)
d.pack()
d.place(x=100,y=340)

def call_me4():
    window4=Tk()
    window4.geometry("1340x680+0+0")
    window4.title("INVENTORY FORM")
            
    b=Label(window4,text="INVENTORY NAME")
    b.place(x=10,y=120)
    c=Label(window4,text="INVENTORY ID")
    c.place(x=10,y=160)
    d=Label(window4,text="STATION ID")
    d.place(x=10,y=200)
    e=Label(window4,text="NUMBER OF MATERIAL")
    e.place(x=10,y=320)
    f=Label(window4,text="ITEM ID")
    f.place(x=10,y=360)

    g=Label(window4,text="MODIFIED DATE")
    g.place(x=10,y=400)


    b_entry=Entry(window4)
    b_entry.place(x=170,y=120)
    c_entry=Entry(window4)
    c_entry.place(x=170,y=160)
    d_entry=Entry(window4)
    d_entry.place(x=170,y=200)
    e_entry=Entry(window4)
    e_entry.place(x=170,y=320)
    f_entry=Entry(window4)
    f_entry.place(x=170,y=360)
    g_entry=Entry(window4)
    g_entry.place(x=170,y=400)


    k=StringVar(window4)
    k.set("           PRODUCT NEEDED")
    j=OptionMenu(window4,k,"STEEL","CONTAINER","FIRE EXTINGUISHERS","CHAIN","NONE")
    j.pack()
    j.place(x=80,y=250)
#mycursor.execute("create table inventory (inventory_name,inventory_id ,station_id,product_needed ,no_of_material ,item_id,modified_date date
    def save_info():
        try:
            sql = "INSERT INTO inventory1 (inventory_name,inventory_id,station_id,product_needed,no_of_material,item_id,modified_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),d_entry.get(),k.get(),e_entry.get(),f_entry.get(),g_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window4,text=e)
            p.place(x=80,y=600)
            p.pack()
   
    q=Button(window4,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)

    def sql5():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM inventory1"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6,7),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="INVENTORY NAME")
        tv.heading(2,text="INVENTORY ID")
        tv.heading(3,text="STATION ID")
        tv.heading(4,text="PRODUCT NEEDED")
        tv.heading(5,text="NUMBER OF MATERIAL")
        tv.heading(6,text="ITEM ID")
        tv.heading(7,text="MODIFIED DATE")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window4,text="     VIEW    ",command=sql5,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)


    
    


buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
e=Button(root,text="INVENTORY",command=call_me4,font=buttonFont)
e.pack()
e.place(x=100,y=460)

def call_me5():
    window5=Tk()
    window5.geometry("1340x680+0+0")
    window5.title("TICKET FORM")
    b=Label(window5,text="TICKET ID")
    b.place(x=10,y=120)
    c=Label(window5,text="TRAIN ID")
    c.place(x=10,y=160)
    d=Label(window5,text="ISSUE DATE")
    d.place(x=10,y=200)
    k=StringVar(window5)

    k=StringVar(window5)
    k.set("           SELECT THE ROUTE")
    j=OptionMenu(window5,k,"KARACHI TO LAHORE","LAHORE TO KARACHI","ISLAMABAD TO SUKKUR","LARKANA TO MULTAN","MULTAN TO FAISLABAD","SUKKUR TO HYDERABAD")
    j.pack()
    j.place(x=80,y=240)
    f=Label(window5,text="PAYMENT")
    f.place(x=10,y=300)
    x=Label(window5,text="TICKET CATEGORY")
    x.place(x=10,y=340)
    y=Label(window5,text="TIMING")
    y.place(x=10,y=380)


    b_entry=Entry(window5)
    b_entry.place(x=150,y=120)
    c_entry=Entry(window5)
    c_entry.place(x=150,y=160)
    d_entry=Entry(window5)
    d_entry.place(x=150,y=200)

    f_entry=Entry(window5)
    f_entry.place(x=150,y=300)
    x_entry=Entry(window5)
    x_entry.place(x=150,y=340)
    y_entry=Entry(window5)
    y_entry.place(x=150,y=380)
 


#ticket_id,train_id ,issue_date,route ,payment,ticket_category ,timing 
    def save_info():
        sql = "INSERT INTO ticket (ticket_id, train_id,issue_date,route,payment,ticket_category,timing) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),k.get(),f_entry.get(),x_entry.get(),y_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    q=Button(window5,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)

    def sql5():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM ticket"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="TICKET ID")
        tv.heading(2,text="TRAIN ID")
        tv.heading(3,text="ISSUE DATE")
        tv.heading(4,text="ROUTE")
        tv.heading(5,text="TICKET CATEGORY")
        tv.heading(6,text="TIMING")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window5,text="     VIEW    ",command=sql5,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)

buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
f=Button(root,text="        TICKET       ",command=call_me5,font=buttonFont)
f.pack()
f.place(x=800,y=100)

def call_me6():
    window6=Tk()
    window6.geometry("1340x680+0+0")
    window6.title("PAYMENT FORM")
    b=Label(window6,text="PAYMENT ID")
    b.place(x=10,y=120)
    c=Label(window6,text="PAYMENT DATE")
    c.place(x=10,y=160)
    d=Label(window6,text="TAX")
    d.place(x=10,y=200)
    e=Label(window6,text="CUSTOMER ID")
    e.place(x=10,y=240)
    f=Label(window6,text="RECEIVING DATE")
    f.place(x=10,y=280)
    g=Label(window6,text="WAY OF PAYMENT")
    g.place(x=10,y=320)

    b_entry=Entry(window6)
    b_entry.place(x=170,y=120)
    c_entry=Entry(window6)
    c_entry.place(x=170,y=160)
    d_entry=Entry(window6)
    d_entry.place(x=170,y=200)
    e_entry=Entry(window6)
    e_entry.place(x=170,y=240)
    f_entry=Entry(window6)
    f_entry.place(x=170,y=280)
    g_entry=Entry(window6)
    g_entry.place(x=170,y=320)
#payment_id,payment_date,tax,customer_id,receiving_date,way_of_payment

    def save_info():
        sql = "INSERT INTO payment1 (payment_id,payment_date,tax,customer_id,receiving_date,way_of_payment) VALUES (%s, %s,%s,%s,%s,%s)"
        val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),f_entry.get(),g_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    q=Button(window6,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)

    def sql6():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM payment1"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="PAYMENT ID")
        tv.heading(2,text="PAYMENT DATE")
        tv.heading(3,text="TAX")
        tv.heading(4,text="CUSTOMER ID")
        tv.heading(5,text="RECEIVING DATE")
        tv.heading(6,text="WAY OF PAYMENT")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window6,text="     VIEW    ",command=sql6,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)


buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
g=Button(root,text="     PAYMENT      ",command=call_me6,font=buttonFont)
g.pack()
g.place(x=800,y=220)


def call_me7():
    window7=Tk()
    window7.geometry("1340x680+0+0")
    window7.title("STATION FORM")
        
    b=Label(window7,text="STATION NAME")
    b.place(x=10,y=120)
    c=Label(window7,text="STATION ID")
    c.place(x=10,y=160)
    d=Label(window7,text="LOCATION")
    d.place(x=10,y=200)
    e=Label(window7,text="NUMBER OF RAILWAY TRACK")
    e.place(x=10,y=320)
    f=Label(window7,text="NUMBER OF TRAIN")
    f.place(x=10,y=360)

    g=Label(window7,text="MANAGER NAME")
    g.place(x=10,y=400)


    b_entry=Entry(window7)
    b_entry.place(x=200,y=120)
    c_entry=Entry(window7)
    c_entry.place(x=200,y=160)
    d_entry=Entry(window7)
    d_entry.place(x=200,y=200)
    e_entry=Entry(window7)
    e_entry.place(x=200,y=320)
    f_entry=Entry(window7)
    f_entry.place(x=200,y=360)
    g_entry=Entry(window7)
    g_entry.place(x=200,y=400)


    k=StringVar(window7)
    k.set("           CITY")
    j=OptionMenu(window7,k,"KARACHI","LAHORE","MULTAN","QUETTA","HYDERABAD","SUKKUR","LARKANA","ISLAMABAD")
    j.pack()
    j.place(x=80,y=250)
    def save_info():
        try:
            sql = "INSERT INTO station (station_name, station_id,location,number_of_track,number_of_train,manager_name,city) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),d_entry.get(),e_entry.get(),f_entry.get(),g_entry.get(),k.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window7,text=e)
            p.place(x=80,y=600)
            p.pack()
   
    q=Button(window7,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)

    def sql7():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM station"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6,7),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="STATION NAME")
        tv.heading(2,text="STATION ID")
        tv.heading(3,text="LOCATION")
        tv.heading(4,text="NUMBER OF TRACK")
        tv.heading(5,text="NUMBER OF TRAIN")
        tv.heading(6,text="MANAGER NAME")
        tv.heading(7,text="CITY")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window7,text="     VIEW    ",command=sql7,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)


buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
h=Button(root,text="      STATION       ",command=call_me7,font=buttonFont)
h.pack()
h.place(x=800,y=340)

def call_me8():
    window8=Tk()
    window8.geometry("1340x680+0+0")
    window8.title("NEW SCHEDULE")
        
    b=Label(window8,text="TRAIN NAME")
    b.place(x=10,y=120)
    c=Label(window8,text="TRAIN ID")
    c.place(x=10,y=160)
    e=Label(window8,text="PASSENGER CAPACITY")
    e.place(x=10,y=200)
    f=Label(window8,text="JOURNEY DATE")
    f.place(x=10,y=240)

    g=Label(window8,text="TIMING")
    g.place(x=10,y=280)


    b_entry=Entry(window8)
    b_entry.place(x=200,y=120)
    c_entry=Entry(window8)
    c_entry.place(x=200,y=160)
    e_entry=Entry(window8)
    e_entry.place(x=200,y=200)
    f_entry=Entry(window8)
    f_entry.place(x=200,y=240)
    g_entry=Entry(window8)
    g_entry.place(x=200,y=280)
    k=StringVar(window8)
    k.set("           SELECT THE ROUTE")
    j=OptionMenu(window8,k,"KARACHI TO LAHORE","LAHORE TO KARACHI","ISLAMABAD TO SUKKUR","LARKANA TO MULTAN","MULTAN TO FAISLABAD","SUKKUR TO HYDERABAD")
    j.pack()
    j.place(x=80,y=320)

#train_name,train_id,route,passenger_capacity ,journey_date,timing
    def save_info():
        try:
            sql = "INSERT INTO newschedule (train_name,train_id,route,passenger_capacity ,journey_date,timing) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (b_entry.get(),c_entry.get(),k.get(),e_entry.get(),f_entry.get(),g_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            p=Label(window7,text=e)
            p.place(x=80,y=600)
            p.pack()
   
    q=Button(window8,text="SUMBIT",fg="white",bg="blue",width="25",command=save_info)
    q.pack()
    q.place(x=70,y=610)


    def sql8():
        sql_a=Tk()
        sql_a.title("VIEW")
        sql_a.geometry("1340x680+0+0")
        
        import mysql.connector
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="hashamsql",
            database="railwaystation"
            )
        print(mydb)
        cursor=mydb.cursor()
        import tkinter as tk
        from tkinter import ttk
        sql="SELECT * FROM newschedule"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frn=Frame(sql_a)
        frn.pack(side=tk.LEFT,padx=0)
        tv=ttk.Treeview(frn,columns=(1,2,3,4,5,6),show="headings",height="26")
        tv.pack()
        tv.heading(1,text="TRAIN NAME")
        tv.heading(2,text="TRAIN ID")
        tv.heading(3,text="ROUTE")
        tv.heading(4,text="PASSENGER CAPACITY")
        tv.heading(5,text="JOURNEY DATE")
        tv.heading(6,text="TIMING")

        for i in rows:
            tv.insert("",'end',values=i)
        hor_scroll=ttk.Scrollbar(frn,orient="horizontal",command=tv.xview)
        hor_scroll.pack(side=BOTTOM,fill=X)
        tv.config(xscrollcommand=hor_scroll)
        
    buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
    bbb=Button(window8,text="     VIEW    ",command=sql8,font=buttonFont)
    bbb.pack()
    bbb.place(x=500,y=100)

buttonFont = font.Font(family='Helvetica', size=26, weight='bold')
i=Button(root,text="NEW SCHEDULE",command=call_me8,font=buttonFont)
i.pack()
i.place(x=800,y=460)

mainloop()
