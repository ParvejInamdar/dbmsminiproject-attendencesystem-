import pymysql
from tkinter import *
from tkinter import messagebox
import subprocess as s

connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
cursor = connection.cursor()
student = """CREATE TABLE IF NOT EXISTS Student1(ID INT(20) PRIMARY KEY,NAME  CHAR(20) NOT NULL,CITY CHAR(10),CONTACT CHAR(10),MARKS INT(20))"""
cursor.execute(student)
connection.close()

connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
cursor = connection.cursor()
teach = """CREATE TABLE IF NOT EXISTS teacher(tID INT(20) PRIMARY KEY,tNAME  CHAR(20) NOT NULL,tSUBJECT CHAR(10),DEPARTMENT CHAR(20))"""
cursor.execute(teach)
connection.close()

connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
cursor = connection.cursor()
Department = """CREATE TABLE IF NOT EXISTS department(TEACHER_NAME CHAR(20) NOT NULL,DEPARTMENT_NAME CHAR(20) NOT NULL,tID INT,ID INT,Foreign key(tID) references teacher(tID),Foreign key(ID) references Student1(ID))"""
cursor.execute(Department)
connection.close()
def search():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		if(ID.get()):
			sql="select * from Student1 where ID='%s'"%ID.get()
			cursor.execute(sql)
			r=cursor.fetchone()
			fopen=open('id.txt','w')
			for i in r:
				fopen.write(str(i)+'\n')
			fopen.close()
			connection.close()
			import subprocess as s
			pn='notepad.exe'	
			fname='id.txt'
			s.Popen([pn,fname])
		elif(NAME.get()):
			sql="select * from Student1 where NAME='%s'"%NAME.get()
			cursor.execute(sql)
			r=cursor.fetchall()
			fopen=open('name.txt','w')
			for i in r:
				fopen.write(str(i)+'\n')
			fopen.close()
			connection.close()
			import subprocess as s
			pn='notepad.exe'	
			fname='name.txt'
			s.Popen([pn,fname])
		elif(CITY.get()):
			sql="select * from Student1 where CITY='%s'"%CITY.get()
			cursor.execute(sql)
			r=cursor.fetchall()
			fopen=open('city.txt','w')
			for i in r:
				fopen.write(str(i)+'\n')
			fopen.close()
			connection.close()
			import subprocess as s
			pn='notepad.exe'	
			fname='city.txt'
			s.Popen([pn,fname])
		elif(CONTACT.get()):
			sql="select * from Student1 where CONTACT='%s'"%CONTACT.get()
			cursor.execute(sql)
			r=cursor.fetchall()
			fopen=open('contact.txt','w')
			for i in r:
				fopen.write(str(i)+'\n')
			fopen.close()
			connection.close()
			import subprocess as s
			pn='notepad.exe'	
			fname='contact.txt'
			s.Popen([pn,fname])
		else:
			sql="select * from Student1 where MARKS='%s'"%MARKS.get()
			cursor.execute(sql)
			r=cursor.fetchall()
			fopen=open('marks.txt','w')
			for i in r:
				fopen.write(str(i)+'\n')
			fopen.close()
			connection.close()
			import subprocess as s
			pn='notepad.exe'	
			fname='marks.txt'
			s.Popen([pn,fname])
		connection.close()
			
def clear():
		ID.set('')
		NAME.set('')
		CITY.set('')
		CONTACT.set('')
		MARKS.set('')

def insert():
			connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
			cursor = connection.cursor()
			s=len(CONTACT.get())
			if(s!=10):
				messagebox.showinfo("ERROR!!!.","Number is invalid")
			else:
				sql="insert into Student1 values('%s','%s','%s','%s','%s')"%(ID.get(),NAME.get(),CITY.get(),CONTACT.get(),MARKS.get())
				cursor.execute(sql)
				connection.commit()
				messagebox.showinfo("Suceesfully Inserted.")
				connection.close()
			connection.close()

def update():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="update Student1 set NAME='%s',CITY='%s',CONTACT='%s',MARKS='%s' where ID='%s'"%(NAME.get(),CITY.get(),CONTACT.get(),MARKS.get(),ID.get())
		cursor.execute(sql)
		sql1="update Student1 set NAME='%s',CITY='%s',CONTACT='%s',MARKS='%s' where CITY='%s'"%(NAME.get(),CITY.get(),CONTACT.get(),MARKS.get(),ID.CITY())
		cursor.execute(sql1)
		connection.commit()
		connection.close()
		messagebox.showinfo("Suceesfully Updated")

def delete():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="delete from Student1 where ID='%s'"%(ID.get())
		cursor.execute(sql)
		connection.commit()
		connection.close()
		messagebox.showinfo("Suceesfully Deleted.")
		
def display():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="select * from Student1"
		cursor.execute(sql)
		r=cursor.fetchall()
		fopen=open('records.txt','w')
		for i in r:
			fopen.write(str(i)+'\n')
		fopen.close()
		connection.close()
		pn='notepad.exe'	
		fname='records.txt'
		s.Popen([pn,fname])
	
def view():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql1="drop view IF EXISTS v2"
		cursor.execute(sql1)
		sql="create view v2 as select NAME,CITY,SUBJECT from Student1"
		cursor.execute(sql)
		sql1="select * from v2"
		cursor.execute(sql1)
		r=cursor.fetchall()
		fopen=open('view.txt','w')
		for i in r:
			fopen.write(str(i)+'\n')
		fopen.close()
		connection.close()
		pn='notepad.exe'	
		fname='view.txt'
		s.Popen([pn,fname])
window=Tk()
window.title('Databse Operation')
	
ptitle=Label(window,text='CRUD Operations')
ptitle.grid(row=0,column=0,columnspan=2)
	
ID=StringVar()
NAME=StringVar()
CITY=StringVar()
CONTACT=StringVar()
MARKS=StringVar()
l1=Label(window,text='ID')
e1=Entry(window,text=ID)
	
l2=Label(window,text='NAME')
e2=Entry(window,text=NAME)
	
l3=Label(window,text='CITY')
e3=Entry(window,text=CITY)
	
l4=Label(window,text='CONTACT')
e4=Entry(window,text=CONTACT)
	
l13=Label(window,text='MARKS')
e13=Entry(window,text=MARKS)
	
b1=Button(window,text='Insert',command=insert)
b2=Button(window,text='Delete',command=delete)
b3=Button(window,text='Update',command=update)
b4=Button(window,text='Search',command=search)
b5=Button(window,text='Clear',command=clear)
b6=Button(window,text='Display',command=display)
b7=Button(window,text='View',command=view)
	
l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
	
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
	
l3.grid(row=3,column=0)
e3.grid(row=3,column=1)
	
l4.grid(row=4,column=0)
e4.grid(row=4,column=1)
	
l13.grid(row=5,column=0)
e13.grid(row=5,column=1)
	
b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
b3.grid(row=7,column=0)
b4.grid(row=7,column=1)
b5.grid(row=8,column=0)
b6.grid(row=8,column=1)
b7.grid(row=9,column=0)
	
window.mainloop()



def tdelete():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="delete from teacher where tID='%s'"%(tID.get())
		cursor.execute(sql)
		connection.commit()
		connection.close()
		messagebox.showinfo("Suceesfully Deleted.")
		
def tinsert():
		connection1 = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection1.cursor()
		sql1="insert into teacher values('%s','%s','%s','%s')"%(tID.get(),tNAME.get(),tSUBJECT.get(),DEPARTMENT.get())
		cursor.execute(sql1)
		connection1.commit()
		connection1.close()
		messagebox.showinfo("Suceesfully Inserted.","Insertion sucessfully")
	
def tsearch():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="select * from teacher where tID='%s'"%tID.get()
		cursor.execute(sql)
		r=cursor.fetchone()
		tNAME.set(r[1])
		tSUBJECT.set(r[2])
		DEPARTMENT.set(r[3])
		connection.close()

def tupdate():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="update teacher set tNAME='%s',tSUBJECT='%s',DEPARTMENT='%s' where tID='%s'"%(tNAME.get(),tSUBJECT.get(),DEPARTMENT.get(),tID.get())
		cursor.execute(sql)
		connection.commit()
		connection.close()
		messagebox.showinfo("Suceesfully Updated")

top=Tk()
top.title("teachers information")
tID=StringVar()
tNAME=StringVar()
tSUBJECT=StringVar()
DEPARTMENT=StringVar()	
			
l8=Label(top,text='Teacher ID')
e8=Entry(top,text=tID)
		
l9=Label(top,text='Teacher NAME')
e9=Entry(top,text=tNAME)
		
l10=Label(top,text='SUBJECT')
e10=Entry(top,text=tSUBJECT)
		
l11=Label(top,text='DEPARTMENT')
e11=Entry(top,text=DEPARTMENT)
	
b9=Button(top,text='Insert',command=tinsert)
b10=Button(top,text='Delete',command=tdelete)
b11=Button(top,text='Search',command=tsearch)
b12=Button(top,text='Update',command=tupdate)
		
l8.grid(row=1,column=0)
e8.grid(row=1,column=1)
		
l9.grid(row=2,column=0)
e9.grid(row=2,column=1)
		
l10.grid(row=3,column=0)
e10.grid(row=3,column=1)
		
l11.grid(row=4,column=0)
e11.grid(row=4,column=1)
		
b9.grid(row=5,column=0)
b10.grid(row=5,column=1)
b11.grid(row=6,column=0)
b12.grid(row=6,column=1)
top.mainloop()	


def dinsert():
		connection1 = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection1.cursor()
		sql="insert into department values('%s','%s','%s','%s')"%(TEACHER_NAME.get(),DEPARTMENT_NAME.get(),tID.get(),ID.get())
		cursor.execute(sql)
		connection1.commit()
		connection1.close()
		messagebox.showinfo("Suceesfully Inserted.","Insertion sucessfully")
	
def ddelete():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="delete from department where ID='%s'"%(ID.get())
		cursor.execute(sql)
		connection.commit()
		connection.close()
		messagebox.showinfo("Suceesfully Deleted.")
	
def dupdate():
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
		cursor = connection.cursor()
		sql="update department set TEACHER_NAME='%s',DEPARTMENT_NAME='%s',ID='%s' where tID='%s'"%(TEACHER_NAME.get(),DEPARTMENT_NAME.get(),ID.get(),tID.get())
		cursor.execute(sql)
		connection.commit()
		connection.close()
		messagebox.showinfo("Suceesfully Updated")

def dsearch():
	connection = pymysql.connect(host="localhost",user="root",passwd="",database="STUDENT" )
	cursor = connection.cursor()
	sql="select student1.NAME,teacher.tID,teacher.tNAME,teacher.DEPARTMENT,teacher.tSUBJECT from department,Student1,teacher where student1.ID=department.ID and teacher.tID=department.tID and department.DEPARTMENT_NAME='%s'"%DEPARTMENT_NAME.get()
	cursor.execute(sql)
	r=cursor.fetchall()
	fopen=open('view.txt','w')
	for i in r:
		fopen.write(str(i)+'\n')
	fopen.close()
	connection.close()
	import subprocess as s
	pn='notepad.exe'	
	fname='view.txt'
	s.Popen([pn,fname])
		

	
top1=Tk()
top1.title("Department information")
TEACHER_NAME=StringVar()
DEPARTMENT_NAME=StringVar()
tID=StringVar()
ID=StringVar()	
	
l12=Label(top1,text='Teacher NAME')
e12=Entry(top1,text=TEACHER_NAME)
		
l13=Label(top1,text='DEPARTMENT')
e13=Entry(top1,text=DEPARTMENT_NAME)
		
l14=Label(top1,text='Teacher ID')
e14=Entry(top1,text=tID)
		
l15=Label(top1,text='Student ID')
e15=Entry(top1,text=ID)
b13=Button(top1,text='Insert',command=dinsert)
b14=Button(top1,text='Delete',command=ddelete)
b15=Button(top1,text='Search',command=dsearch)
b16=Button(top1,text='Update',command=dupdate)
	
l12.grid(row=1,column=0)
e12.grid(row=1,column=1)
		
l13.grid(row=2,column=0)
e13.grid(row=2,column=1)
		
l14.grid(row=3,column=0)
e14.grid(row=3,column=1)
		
l15.grid(row=4,column=0)
e15.grid(row=4,column=1)
	
b13.grid(row=5,column=0)
b14.grid(row=5,column=1)
b15.grid(row=6,column=0)
b16.grid(row=6,column=1)
	
top1.mainloop()