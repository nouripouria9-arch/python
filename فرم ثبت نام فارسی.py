import tkinter as tk
from tkinter.filedialog import asksaveasfile
master=tk.Tk()
master.geometry("1000x500")
master.title("فرم ثبت نام")
master.configure(bg="black",highlightcolor="blue",highlightthickness=4)

# formheading
formheading=tk.Label(master,text="فرم ارزیابی",font=("b nazanin",20,"bold"),padx=10,pady=10,bg="black",fg="green",width=800,height=3)
formheading.pack()

# firstname and lastname
firstname_text=tk.Label(master,text=":نام",font=("b nazanin",14,"bold"),bg="black",fg="purple")
firstname_text.place(x=1300,y=100)
firstname=tk.StringVar()
firstname_entry=tk.Entry(master,textvariable=firstname,width=50,font=("b nazanin",12,"bold"))
firstname_entry.place(x=950,y=100)
lastname_text=tk.Label(master,text=": نام خانوادگی",font=("b nazanin",14,"bold"),bg="black",fg="purple")
lastname_text.place(x=1260,y=150)
lastname=tk.StringVar()
lastname_entry=tk.Entry(master,textvariable=lastname,width=50,font=("b nazanin",12,"bold"))
lastname_entry.place(x=950,y=150)

# tahsilat
tahsilat_text=tk.Label(master,text="تحصیلات",font=("b nazanin",14,"bold"),bg="black",fg="orange")
tahsilat_text.place(x=1260,y=200)
tahsilat=tk.StringVar()
tahsilat1=tk.Radiobutton(master,text="دیپلم",variable=tahsilat,value="diplom",font=("b nazanin",14,"bold"),fg="black",bg="purple")
tahsilat1.place(x=1260,y=235)
tahsilat2=tk.Radiobutton(master,text="فوق دیپلم",variable=tahsilat,value="foghdiplom",font=("b nazanin",14,"bold"),fg="black",bg="purple")
tahsilat2.place(x=1100,y=235)
tahsilat3=tk.Radiobutton(master,text="لیسانس",variable=tahsilat,value="lisans",font=("b nazanin",14,"bold"),fg="black",bg="purple")
tahsilat3.place(x=1000,y=235)
tahsilat4=tk.Radiobutton(master,text="فوق لیسانس",variable=tahsilat,value="foghdlisans",font=("b nazanin",14,"bold"),fg="black",bg="purple")
tahsilat4.place(x=880,y=235)
tahsilat5=tk.Radiobutton(master,text="دکتری",variable=tahsilat,value="doctora",font=("b nazanin",14,"bold"),fg="black",bg="purple")
tahsilat5.place(x=750,y=235)

# jensiat
jensiat_text=tk.Label(master,text="جنسیت",font=("b nazanin",14,"bold"),bg="black",fg="violet")
jensiat_text.place(x=1260,y=280)
jensiat=tk.StringVar()
jensiat1=tk.Radiobutton(master,text="خانم",variable=jensiat,value="khanom",font=("b nazanin",14,"bold"),fg="black",bg="pink")
jensiat1.place(x=1260,y=315)
jensiat2=tk.Radiobutton(master,text="آقا",variable=jensiat,value="agha",font=("b nazanin",14,"bold"),fg="black",bg="blue")
jensiat2.place(x=1100,y=315)

# field of study
field_text=tk.Label(master,text="رشته تحصیلی",font=("b nazanin",14,"bold"),bg="black",fg="yellow")
field_text.place(x=1250,y=360)
field11=tk.StringVar()
field22=tk.StringVar()
field33=tk.StringVar()
field44=tk.StringVar()
field1=tk.Checkbutton(master,text="مهارت های پایه",variable=field11,onvalue="basic of computer",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field1.place(x=1210,y=395)
field2=tk.Checkbutton(master,text="وب",variable=field22,onvalue="web",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field2.place(x=1100,y=395)
field3=tk.Checkbutton(master,text="برنامه نویسی",variable=field33,onvalue="programming",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field3.place(x=950,y=395)
field4=tk.Checkbutton(master,text="شبکه",variable=field44,onvalue="network",font=("b nazanin",14,"bold"),fg="black",bg="cyan")
field4.place(x=800,y=395)

# address
address_text=tk.Label(master,text=":آدرس",font=("b nazanin",14,"bold"),bg="black",fg="khaki")
address_text.place(x=1300,y=460)
address_entry=tk.Text(master,font=("b nazanin",12,"bold"),width=50,height=4)
address_entry.place(x=950,y=460)

# phone number
phone_text=tk.Label(master,text=":شماره تماس",font=("b nazanin",14,"bold"),bg="black",fg="lightgreen")
phone_text.place(x=1230,y=600)
phone=tk.StringVar()
phone_entry=tk.Entry(master,textvariable=phone,width=50,font=("b nazanin",14,"bold"))
phone_entry.place(x=860,y=600)


# buttons
sabt=tk.Button(master,text="ثبت",font=("b nazanin",16,"bold"),bg="green",fg="black",command=lambda:register())
sabt.place(x=500,y=600)
hazf=tk.Button(master,text="حذف",font=("b nazanin",16,"bold"),bg="red",fg="black",command=lambda:hazf())
hazf.place(x=700,y=600)

# def
def register():
    file=asksaveasfile()
    file.write(firstname_entry.get()+"\n")
    file.write(lastname_entry.get()+"\n")
    file.write(tahsilat.get()+"\n")
    file.write(jensiat.get()+"\n")
    file.write(field1.get()+"\n")
    file.write(field2.get()+"\n")
    file.write(field3.get()+"\n")
    file.write(field4.get()+"\n")
    file.write(address_entry.get("1.0",tk.END)+"\n")
    file.write(phone.get()+"\n")


def hazf():
    firstname_entry.delete(0,tk.END)
    lastname_entry.delete(0,tk.END)
    tahsilat.set(" ")
    jensiat.set(" ")
    field1.set(0)
    field2.set(0)
    field3.set(0)
    field4.set(0)
    address_entry.delete("1.0",tk.END)
    phone_entry.delete(0,tk.END)


master.mainloop()