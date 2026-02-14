import tkinter as tk
import sqlite3
conn=sqlite3.connect(r"C:\Users\puriya\OneDrive\Desktop\form.db")
cur=conn.cursor()
cur.execute("""create table if not exists user(
    code text primary key,
    name text,
    family text,
    network text, 
    programming text, 
    age text)""")



# def
def cs():
    dsp2=tk.Label(root,fg="red",bg="silver",height=8,width=25,font=("b nazanin",14,"bold"))
    dsp2.place(x=300,y=400)

def ckst(i,o,p):
    global a
    global b
    global c
    if i==1:
        a='وب'
    else:
        a="-"
    if o==1:
        b="برنامه نویسی"
    else:
        b="-"
    if p==1:
        c="شبکه"
    else:
        c="-"
    return(i,o,p)

def imp():
    x=field11.get()
    y=field22.get()
    z=field33.get()
    q=ckst(x,y,z)
    d=age.get()
    cs()
    dsp2=tk.Label(root,text=f"کد ملی: {kodemeli.get()}\nنام: {firstname.get()}\nنام خانوادگی: {lastname.get()}\nرشته تحصیلی: {a} {b} {c}\nسن: {d}",fg="red",bg="silver",height=8,width=25,font=("b nazanin",14,"bold"))
    dsp2.place(x=300,y=400)
    t1=[kodemeli.get(),firstname.get(),lastname.get(),a,b,c,d]
    cur.execute("insert into user values(?,?,?,?,?,?,?)",t1)
    conn.commit()

def dell():
    cs()
    y=[]
    cur.execute("select * from user")
    for i in cur.fetchall():
        y.append(i[0])
    if kodemeli.get() in y:
        kodemeli.get()=[kodemeli.get()]
        cur.execute("delete from user where code=?",kodemeli.get())
        dsp2=tk.Label(root,text="اطلاعات با موفقیت حذف شد",fg="green",bg="silver",font=("b nazanin",14,"bold"))
        dsp2.place(x=300,y=400)
        conn.commit()
    else:
        dsp2=tk.Label(root,text="چنین کد ملی ای ای وجود ندارد",fg="red",bg="silver",font=("b nazanin",14,"bold"))
        dsp2.place(x=300,y=400)





root=tk.Tk()
root.geometry("640x440")
root.title("register form")
root.configure(bg="black",highlightcolor="blue",highlightthickness=4)


# kodemeli
kodemeli_text=tk.Label(root,text=":کد ملی",font=("b nazanin",14,"bold"),bg="black",fg="purple")
kodemeli_text.grid(row=0,column=0)
kodemeli=tk.StringVar()
kodemeli_entry=tk.Entry(root,textvariable=kodemeli,width=50,font=("b nazanin",12,"bold"))
kodemeli_entry.grid(row=0,column=1)


# firstname and lastname
firstname_text=tk.Label(root,text=":نام",font=("b nazanin",14,"bold"),bg="black",fg="purple")
firstname_text.grid(row=1,column=0)
firstname=tk.StringVar()
firstname_entry=tk.Entry(root,textvariable=firstname,width=50,font=("b nazanin",12,"bold"))
firstname_entry.grid(row=1,column=1)

lastname_text=tk.Label(root,text=": نام خانوادگی",font=("b nazanin",14,"bold"),bg="black",fg="purple")
lastname_text.grid(row=2,column=0)
lastname=tk.StringVar()
lastname_entry=tk.Entry(root,textvariable=lastname,width=50,font=("b nazanin",12,"bold"))
lastname_entry.grid(row=2,column=1)


# field of study
field_text=tk.Label(root,text="رشته تحصیلی",font=("b nazanin",14,"bold"),bg="black",fg="yellow")
field_text.grid(row=3,column=0)
field11=tk.IntVar()
field22=tk.IntVar()
field33=tk.IntVar()
field1=tk.Checkbutton(root,text="وب",variable=field11,font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field1.grid(row=4,column=0)
field2=tk.Checkbutton(root,text="برنامه نویسی",variable=field22,font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field2.grid(row=4,column=1)
field3=tk.Checkbutton(root,text="شبکه",variable=field33,font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field3.grid(row=4,column=2)


# age
age_text=tk.Label(root,text="سن",font=("b nazanin",14,"bold"),bg="black",fg="yellow")
age_text.grid(row=5,column=0)
age=tk.StringVar()
age.set("20<=age<=30")
age1=tk.Radiobutton(root,text="20<=age<=30",variable=age,value="20<=age<=30",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
age1.grid(row=6,column=0)
age2=tk.Radiobutton(root,text="30<=age<=40",variable=age,value="30<=age<=40",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
age2.grid(row=6,column=1)
age3=tk.Radiobutton(root,text="40<=age<=50",variable=age,value="40<=age<=50",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
age3.grid(row=6,column=2)


# buttons
sabt=tk.Button(root,text="ثبت",font=("b nazanin",16,"bold"),bg="green",fg="black",command=imp)
sabt.place(x=50,y=300)
hazf=tk.Button(root,text="حذف",font=("b nazanin",16,"bold"),bg="red",fg="black",command=dell)
hazf.place(x=150,y=300)



root.mainloop()