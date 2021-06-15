from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
from tkinter.scrolledtext import*
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def f1():
	Register.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	Register.withdraw()

def f3():
	user1 = entry_1.get()
	password1 = entry_2.get()
	#user = "student"
	#password  = "student123"
	#if (user == user1):
	#	if(password == password1):
	#		showinfo("success","Login successful")
	#		Attend.deiconify()
	#		root.withdraw()
	con=None
	try:
			con = connect("report.db")
			cur = con.cursor()
			sql = "select * from students"
			cur.execute(sql)
			data = cur.fetchall()
			if len(user1)== 0 :
				showerror("error","User is empty")
				return
			elif len(password1) == 0:
				showerror("error","Password is empty")
				return
			for d  in data :
				if user1==str(d[0]) and password1==str(d[1]) :
					showinfo("success","Login successful")
					Attend.deiconify()
					root.withdraw()
					return
			showwarning("Error","Invalid Login Credentials!!")

	except exception as e:
			showerror("Issue",e)
	finally:
			if con is not None:
				con.close()
			entry_1.delete(0,END)
			entry_2.delete(0,END)
def f4():
	root.deiconify()
	Attend.withdraw()
def f5():
	View.deiconify()
	root.withdraw()
	con = None
	try:
			con = connect("report.db")
			cur = con.cursor()
			sql = "select * from record"
			cur.execute(sql)
			data = cur.fetchall()
			msg = ""
			for d  in data :
				msg = msg + "Ent No = " + str(d[0]) + " Rno = " + str(d[1])+"Status ="+str(d[2])+"\n"
			st.insert(INSERT,msg)
	except exception as e:
			showerror("Issue",e)
	finally:
			if con is not None:
					con.close()
def f6():
	Attend.deiconify()
	View.withdraw()
def f7():
	con = None
	try:
		con = connect("report.db")
		cur = con.cursor()
		sql = "insert into students values ('%s' ,'%s' ,'%s' ,'%s')"
		user = regisentry_user.get( )
		password = regisentry_pass.get( )
		first = regisentry_first.get( )
		last = regisentry_last.get( )
		if len(user) == 0:
			showerror("error","Entry box is empty")
			return
		if not first.isalpha():
			showerror("Mistake","name should contain alphabets only")
			return
		cur.execute(sql%(user,password,first,last))
		con.commit()
		showinfo("Success","Row inserted")
	except exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
		regisentry_user.delete(0,END)
		regisentry_pass.delete(0,END)
		regisentry_first.delete(0,END)
		regisentry_last.delete(0,END)
		regisentry_user.focus()
def f8():
	con = None
	try:
		con = connect("report.db")
		cur = con.cursor()
		sql = "insert into record values('%d','%d','%s')"
		Ent = int(Attendentry_1.get())
		rno = int(Attendentry_2.get())
		status = Attendentry_3.get()
		cur.execute(sql%(Ent,rno,status))
		con.commit()
		showinfo("success","data inserted")
	except Exception as e:
		con.rollback()
		showerror("Issue","Primary key cannot be null ! ")
	finally:
		if con is not None:
			con.close()
		Attendentry_1.delete(0,END)
		Attendentry_2.delete(0,END)
		Attendentry_3.delete(0,END)
		Attendentry_1.focus()
def f9():
	con = None
	student_list =[]
	status_list = []
	try:
		con = connect("report.db")
		cur = con.cursor()
		sql = "select * from record"
		cur.execute(sql)
		table = cur.fetchall()
		for Ent,rno,status in table:
			student_list.append(rno)
			status_list.append(status)
		plt.title("Class Attendance!")
		plt.bar(status_list,student_list,linewidth = 5,width = 0.65,alpha = 0.45)
		plt.xlabel("Status")
		plt.ylabel("Rno")
		plt.show()

	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()
def on_close():
	if askokcancel("Quit","Do you want to exit ?"):
		root.destroy()

root = Tk()
root.title("Online Attendance System")
root.geometry("700x550+500+100")
root.configure(background= "light pink")

label_1 = Label (root,text = "Login Form",font = ('arial',28),bd = 10,bg ="light blue" )
label_1.pack(pady = 10)
label_2 = Label(root,text = "Username:",font = ('arial',18),bg= "light pink").place(x = 60 ,y=150)
entry_1 = Entry(root,width = 30)

entry_1.place(x = 210,y = 155)

label_3 = Label(root,text = "Password:",font = ('arial',18),bg= "light pink").place(x = 60 ,y=200)
entry_2 = Entry(root,width = 30)
entry_2.place(x = 210,y = 205)
btn_1 = Button(root, text = "Submit",width = 10, font = ('arial',12,'bold'),command = f3).place(x = 250, y =270)
btn_2 = Button(root, text = "Register",width = 10, font = ('arial',12,'bold'),command = f1).place(x = 250,y = 320)

Register = Toplevel(root)
Register.title("Registration")
Register.geometry("700x550+500+100")
Register.configure(background = "light green")

regislabel_user= Label(Register,text = "Enter Username:",font = ('arial',18),bg= "light green").place(x = 270,y=10)
regisentry_user = Entry(Register,width = 30)
regislabel_pass = Label(Register,text = "Enter Password:",font = ('arial',18),bg= "light green").place(x = 270,y=110)
regisentry_pass = Entry(Register,width = 30)
regislabel_first = Label(Register,text = "First Name:",font = ('arial',18),bg= "light green").place(x = 270,y=210)
regisentry_first = Entry(Register,width = 30)
regislabel_last = Label(Register,text = "Last Name:",font = ('arial',18),bg= "light green").place(x = 270,y=310)
regisentry_last = Entry(Register,width = 30)
regisbtn_save = Button(Register, text = "Save",width = 10, font = ('arial',12,'bold'),command = f7).place(x = 300, y =410)
regisbtn_back = Button(Register, text = "Back",width = 10, font = ('arial',12,'bold'),command = f2).place(x = 300,y = 460)
regisentry_user.place(x = 270,y = 60)
regisentry_pass.place(x = 270,y = 160)
regisentry_first.place(x = 270,y = 260)
regisentry_last.place(x = 270,y = 360)
Register.withdraw()

Attend = Toplevel(root)
Attend.title("Online Attendance")
Attend.geometry("700x550+500+100")
Attend.configure(background = "light blue")

Attendlabel_1 = Label(Attend,text = "Ent No:",font = ('arial',18),bg= "light blue").place(x = 200,y=20)
Attendentry_1 = Entry(Attend,width = 30)
Attendentry_1.place(x = 350,y = 20)
Attendlabel_2 = Label(Attend,text = "Roll No:",font = ('arial',18),bg= "light blue").place(x = 200,y = 120)
Attendentry_2 = Entry(Attend,width = 30)
Attendentry_2.place(x = 350,y = 120)
Attendlabel_3 = Label(Attend,text = "Status:",font = ('arial',18),bg= "light blue").place(x = 200,y=220)
Attendentry_3 = Entry(Attend,width = 30)
Attendentry_3.place(x = 350 , y = 220)
Attendbtn_1 = Button(Attend, text = "Submit",width = 10, font = ('arial',12,'bold'),command = f8).place(x = 300, y =300)
Attendbtn_2 = Button(Attend, text = "View",width = 10, font = ('arial',12,'bold'),command = f5).place(x = 300,y = 350)
Attendbtn_3 = Button(Attend, text = "Graph",width = 10, font = ('arial',12,'bold'),command = f9).place(x = 300, y = 400)
Attendbtn_4 = Button(Attend,text = "Back",width = 10, font = ('arial',12,'bold'),command = f4).place(x = 300, y = 450)
Attend.withdraw()

View = Toplevel(root)
View.title("View Student")
View.geometry("700x550+500+100")
View.configure(background = "light green")

st = ScrolledText(View,width = 40,height = 25,font = ('arial',12,'bold'))
stbtn_1 =  Button(View,text = 'Back',font = ('arial',12,'bold'),command = f6)
st.pack(pady = 5)
stbtn_1.pack(pady = 5)
View.withdraw()
root.mainloop()
