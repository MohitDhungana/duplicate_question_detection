from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from tkinter import filedialog
#WINDOW FOR DETECTION TWO ENTERED QUESTION
def open_window1():
    top = Toplevel()
    top.title("Duplicate Question Detection")
    top.minsize(width=800,height=150)
    top.maxsize(width=800,height=150)
    def get_que(event):
        # Get the value stored in the entries
        q1 = First_que.get()
        q2 = Second_que.get()
        if(q1==q2):
            tkinter.messagebox.showinfo('your result is','your que is duplicate');
        else:
            tkinter.messagebox.showinfo('your result is','your que is not duplicate');
        # Delete the value in the entry
        First_que.delete(0, "end")
        Second_que.delete(0, "end")


    Label(top, text="First Question").grid(row=0, sticky=W, padx=10)
    First_que=Entry(top,width=100)
    First_que.grid(row=0, column=1, sticky=E, pady=10)
 
    Label(top, text="Second Question").grid(row=1, sticky=W, padx=10)
    Second_que=Entry(top,width=100)
    Second_que.grid(row=1, column=1, sticky=E, pady=10)
 
    equalButton=Button(top, text="Submit")
    equalButton.grid(row=3)
    equalButton.bind("<Button-1>", get_que)
    Button1=Button(top, text="  close  ",command=top.destroy)
    Button1.grid(row=3,column=1,sticky=E, pady=10)
    Button1.bind
    

#DATABASE WINDOW
def open_window2():
    top = Toplevel()
    top.title("Duplicate Question Detection With DB")
    top.minsize(width=800,height=150)
    top.maxsize(width=800,height=150)

    def get_que(event):
        # Get the value stored in the entries
        que1= First_que.get()
        count=0
    #database Connection
        try:
            connection = mysql.connector.connect(host='localhost',
                             database='major',
                             user='root',
                             password='')
            cursor = connection.cursor(prepared=True)
            sql_select_Query = "select * from questions"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("Total number of rows in table is - ", cursor.rowcount)
            for row in records:
                if(que1.upper()==row[1].upper()):
                    count+=1

            if(count>0):
                tkinter.messagebox.showinfo('your result is','your que is duplicate');
            else:
                tkinter.messagebox.showinfo('your result is','your que is not duplicate');
                result=cursor.execute ("""INSERT INTO questions (question) VALUES("%s")"""% (que1))
            # print "Number of rows inserted: %d" % cursor.rowcount
                connection.commit()
            print ("Record inserted successfully into python_users table")
            # Delete the value in the entry
            First_que.delete(0, "end")
        except mysql.connector.Error as error :
            print("Failed inserting record into python_users table {}".format(error))
        finally:
        #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("connection is closed")

 
    Label(top, text="First Question").grid(row=0, sticky=W, padx=10)
    First_que=Entry(top,width=100)
    First_que.grid(row=0, column=1, sticky=E, pady=10)
 
    equalButton=Button(top, text="Submit")
    equalButton.grid(row=3)
    equalButton.bind("<Button-1>", get_que)

    Button1=Button(top, text="  close  ",command=top.destroy)
    Button1.grid(row=3,column=1,sticky=E, pady=10)
    Button1.bind

 #CSV FILE WINDOW
def open_window3():
    top = Toplevel()
    top.title("compare with csv file")
    top.minsize(width=800,height=150)
    top.maxsize(width=800,height=150)
    Button1=Button(top, text="  close  ",command=top.destroy)
    Button1.grid(row=3,column=1,sticky=E, pady=10)   
    Button1.bind
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("csv files","*.csv"),("all files","*.*")) )
        # self.label = ttk.Label(text = "")
        # self.label.grid(column = 1, row = 2)
        # self.label.configure(text = self.filename)
        print(self.filename)

    Button2=Button(top, text="  UPLOAD CSV FILE  ")
    Button2.grid(row=3,column=2,sticky=E, pady=10)   
    Button2.bind("<Button-1>", fileDialog)


#MAIN FRONT WINDOW
root = Tk()
root.title("Duplicate Question Detection")
button = Button(root, text="DETECT WITH TWO QUESTIONS", command=open_window1)
button.pack()
button2 = Button(root, text=" DETECT WITH DATABASE QUESTIONS", command=open_window2)
button2.pack()
button3 = Button(root, text="  DETECT WITH CSV FILE  ", command=open_window3)
button3.pack()
button4 = Button(root, text="  exit  ", command=root.destroy)
button4.pack()
root.minsize(width=800,height=150)
root.maxsize(width=800,height=150)
root.mainloop()
