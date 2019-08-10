from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
filelist=[]
filelist1=[]
texts=['hello','hi','good morning','good afternoon','good night']
#WINDOW FOR DETECTION TWO ENTERED QUESTION
def open_window1():
    top = Toplevel()
    top.title("Duplicate Question Detection")
    # top.minsize(width=800,height=150)
    # top.maxsize(width=800,height=150)
    top.geometry('1350x750+0+0')
    top.config(bg='powder blue')
    top.attributes('-fullscreen',True)
    lblTitle = Label(top,  text = 'Detect with two questions', font = ('arial',30,'bold'), bg='powder blue',
                              fg = 'brown')
    lblTitle.grid(row=0, columnspan = 2, pady = 40)
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


    Label(top, text="First Question").grid(row=4,sticky=W, padx=10)
    First_que=Entry(top,width=120)
    First_que.grid(row=4, column=1, sticky=E, pady=10)
 
    Label(top, text="Second Question").grid(row=5,sticky=W, padx=10)
    Second_que=Entry(top,width=120)
    Second_que.grid(row=5, column=1, sticky=E, pady=10)
 
    equalButton=Button(top, text="Submit")
    equalButton.grid(row=6)
    equalButton.bind("<Button-1>", get_que)
    Button1=Button(top, text="  close  ",command=top.destroy)
    Button1.grid(row=6,column=1,sticky=E, pady=10)
    Button1.bind

def onequewindow(param):
    param.destroy
    top = Toplevel()
    top.title("Duplicate Question Detection With existing questions")
    top.geometry('1350x750+0+0')
    top.config(bg='powder blue')
    Button1=Button(top, text="  Close  ",command=top.destroy,fg='red')  
    Button1.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=20)
    Button1.bind
    lblTitle1 = Label(top,  text = 'Your Question already exists!!!!!', font = ('arial',15,'bold'), bg='powder blue',
                              fg = 'purple')
    lblTitle1.place(x=500,y=100)
    lblTitle1 = Label(top,  text = 'Similar questions are :', font = ('arial',15,'bold'), bg='powder blue',
                              fg = 'purple')
    lblTitle1.place(x=500,y=150)
    List=Listbox(top, width=50, height=20, font=("Times", 12),fg= 'red')
    for i in range(len(texts)):
        List.insert(i+1,'   '+texts[i])
    List.place(x=500,y=200)
    List.bind()
    
    

#DATABASE WINDOW
def open_window2():
    top = Toplevel()
    top.title("Duplicate Question Detection With DB")
    top.geometry('1350x750+0+0')
    top.config(bg='powder blue')
    top.attributes('-fullscreen',True)
    lblTitle = Label(top,  text = 'Detect with Existing questions', font = ('arial',30,'bold'), bg='powder blue',
                              fg = 'brown')
    lblTitle.grid(row=0, columnspan = 2, pady = 40)

    def get_que(event):
        # Get the value stored in the entries
        que1= First_que.get()
        print(que1)
 
    Label(top, text="First Question").grid(row=5, sticky=W, padx=10)
    First_que=Entry(top,width=120)
    First_que.grid(row=5, column=1, sticky=E, pady=10)
 
    equalButton=Button(top, text="Submit",command=lambda: onequewindow(top))
    equalButton.grid(row=6)
    equalButton.bind("<Button-1>")

    Button1=Button(top, text="  close  ",command=top.destroy)
    Button1.grid(row=6,column=1,sticky=E, pady=10)
    Button1.bind
def comp(param):
    param.destroy
    top = Toplevel()
    top.title("Duplicate Question Detection With Existing Questions")
    top.geometry('1350x750+0+0')
    top.config(bg='powder blue')
    Button1=Button(top, text="  Close  ",command=top.destroy,fg='red')  
    Button1.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=30)
    Button1.bind
    lblTitle = Label(top,  text = 'Your result is :' , font = ('arial',30,'bold'), bg='powder blue',
                              fg = 'purple')
    lblTitle.place(x=50,y=100)
    lblTitle1 = Label(top,  text = 'Original File' , font = ('arial',15,'bold'), bg='powder blue',
                              fg = 'black')
    lblTitle1.place(x=50,y=170)
    List1=Listbox(top, width=50, height=20, font=("Times", 16, "bold"),fg= 'purple')
    for i in range(len(texts)):
        List1.insert(i+1,'  '+texts[i])
    # scrollbar = Scrollbar(top, orient="vertical")
    # scrollbar.config(command=List1.yview)
    # scrollbar.bind()
    # List1.config(yscrollcommand=scrollbar.set)
    List1.place(x=50,y=200)
    List1.bind()
    lblTitle2 = Label(top,  text = 'Target File' , font = ('arial',15,'bold'), bg='powder blue',
                              fg = 'black')
    lblTitle2.place(x=700,y=170)
    List2=Listbox(top, width=50, height=20, font=("Times", 16, "bold"),fg= 'red')
    for i in range(len(texts)):
        List2.insert(i+1,'  '+texts[i])
    List2.place(x=700,y=200)
    List2.bind()


 #CSV FILE WINDOW
def open_window3():
    top = Toplevel()
    top.title("Duplicate Question Detection")
    top.geometry('1350x750+0+0')
    top.config(bg='powder blue')
    top.attributes('-fullscreen',True)
    lblTitle = Label(top,  text = 'Upload a CSV File to compare', font = ('arial',30,'bold'), bg='powder blue',
                              fg = 'brown')
    lblTitle.grid(row=0, columnspan = 2, pady = 40)
    lblTitle.place(x=450,y=40)
    Button1=Button(top, text="  Close  ",command=top.destroy,fg='red')  
    Button1.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=200)
    Button1.bind
    Button2=Button(top, text="  UPLOAD ORIGINAL FILE  ",fg='blue')
    Button2.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=100)
    Button2.bind("<Button-1>", fileDialog)
    Button2=Button(top, text="  UPLOAD TARGET FILE  ",fg='blue')
    Button2.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=150)
    Button2.bind("<Button-1>", fileDialog1)
    if(len(filelist)>0):
        lblTitle1= Label(top,  text = 'Original Files Uploaded', font = ('arial',15,'bold'), bg='powder blue',
                              fg = 'purple')
        lblTitle1.grid(row=0, columnspan = 2, pady = 40)
        lblTitle1.place(x=450,y=250)
        j=0
        for i in range(len(filelist)):
            exec('Label%d=Label(top,text="%s")\nLabel%d.place(x=450, y=280+j)' % (i,filelist[i],i))
            j+=20
    if(len(filelist1)>0):
        lblTitle1= Label(top,  text = 'Target Files Uploaded', font = ('arial',15,'bold'), bg='powder blue',
                              fg = 'purple')
        lblTitle1.grid(row=0, columnspan = 2, pady = 40)
        lblTitle1.place(x=450,y=350)
        j=0
        for i in range(len(filelist1)):
            exec('Label%d=Label(top,text="%s")\nLabel%d.place(x=450, y=380+j)' % (i,filelist1[i],i))
            j+=20
    if(len(filelist1)>0 and len(filelist)>0 ):
        Button3=Button(top, text="  COMPARE ",fg='blue',command=lambda: comp(top))
        Button3.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=450)
        Button3.bind("<Button-1>")

def fileDialog(self):
    self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("csv files","*.csv"),("all files","*.*")) )
    filelist.append(self.filename)
    open_window3()
def fileDialog1(self):
    self.filename1 = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("csv files","*.csv"),("all files","*.*")) )
    filelist1.append(self.filename1)
    open_window3()



root = Tk()
root.title("Duplicate Question Detection")
lblTitle = Label(root,  text = ' Duplicate Question Detection', font = ('arial',40,'bold'), bg='powder blue',
                              fg = 'brown')
lblTitle.pack()
lblTitle.place(x=370,y=40)
button = Button(root, text="DETECT WITH TWO QUESTIONS", command=open_window1,fg="purple")
button.pack()
button.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=150)
button2 = Button(root, text=" DETECT WITH EXISTING QUESTIONS", command=open_window2,fg="purple")
button2.pack()
button2.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=200)
button3 = Button(root, text="  COMPARE CSV FILES ", command=open_window3,fg="purple")
button3.pack()
button3.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=250)
button4 = Button(root, text="  Exit ", command=root.destroy,fg="red")
button4.pack()
button4.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=300)
root.geometry('1350x750+0+0')
root.config(bg='powder blue')
root.attributes('-fullscreen',True)
# root.minsize(width=800,height=150)
# root.maxsize(width=800,height=150)
root.mainloop()
