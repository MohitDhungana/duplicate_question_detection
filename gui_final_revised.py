from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from tensorflow.python.keras.models import load_model
import tensorflow.python.keras.backend as K
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import re
import numpy as np
import pandas as pd
import json
import csv

# from essentials import *

# list of questions
filelist=[]
filelist1=[]

ques_list_for_search = []
original_questions = []
target_questions = []

####################################################################################################

# gets a whole question inside text variable on which  preprocessing is done and then the question is splitted into word indices and returned

def compare_questions(q1):

    for i in range(0, len(filelist)):
        with open(filelist[i], 'r') as g:
            header = next(g)
            csvr = csv.reader(g)

            for q2 in csvr:

                # <call function to compare and pass question1 and row as question2>
                is_duplicate, percent = result_prediction(
                    word_indexer(q1), word_indexer(q2))
                if percent > 40:
                    # print("duplicates found:")
                    # print(q1[0])
                    # print(q2[0])
                    # print(" ")
                    if q2[0] not in original_questions:
                        original_questions.append(q2[0])

                    if q1[0] not in target_questions:
                        target_questions.append(q1[0])
                    # print(is_duplicate)
                    # flag = 1
        # if flag == 0:
        #     print('no duplicates found')

    # return two lists here for target and original
    # print(type(q2[0]))
    return original_questions, target_questions


def text_to_word_list(text):
    text = str(text)
    text = text.lower()

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)

    text = text.split()

    return text


# write test questions to .csv file
def write_to_csv(question1, question2, is_duplicate, percent):
    with open('prediction_test_questions.csv', mode='a', newline="") as question_file:
        question_writer = csv.writer(question_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        question_writer.writerow(
            [question1, question2, is_duplicate, str(percent)])


# manhattan distance calculation function
def manhattan_distance(left, right):
    return K.exp(-K.sum(K.abs(left-right), axis=1, keepdims=True))


# function to predict result from two supplied questions
# that returns is_duplicate result and percentage
def result_prediction(q1, q2):
    # preprocessing for prediction
    question_list = [q1, q2]
    question_list = pad_sequences(question_list, maxlen=50)

    # convert to numpy array to feed to model
    que1 = np.asarray(question_list[0])
    que2 = np.asarray(question_list[1])

    # predict sample questions on saved model using above numpy array
    pred = new_model.predict([[que1], [que2]])

    # Prediction threshold
    if pred >= 0.5:
        # print("Duplicate -> ", str(pred[0][0]*100) + ' %')
        # tkinter.messagebox.showinfo('your result is', 'your que is duplicate ')
        return 1, pred[0][0]*100
    else:
        # print("Not Duplicate -> ", str(pred[0][0]*100) + ' %')
        # tkinter.messagebox.showinfo(
        #     'your result is', 'your que is not duplicate ')
        return 0, pred[0][0]*100


# function to index tokenized words using training vocabulary dictionary
def word_indexer(question):
    ques_index = []

    for word in text_to_word_list(question):
        if word in vocab_dictionary:
            ques_index.append(vocab_dictionary[word])
    return ques_index


# load trained model
model_path = 'model_for_gui.h5'
new_model = load_model(model_path)


# import vocabulary dictionary and parse it in python
dict_path = 'vocabulary_dictionary.json'


# read dictionary file
with open(dict_path, 'r') as my_file:
    data = my_file.read()


# parse dictionary
vocab_dictionary = json.loads(data)






################################ 1 starts here ########################################################


#WINDOW FOR DETECTION TWO ENTERED QUESTION 1
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
        question1 = First_que.get()
        question2 = Second_que.get()

        # Get the value stored in the entries
        q1 = word_indexer(First_que.get())
        q2 = word_indexer(Second_que.get())
    
        # get result and percentage from prediction
        is_duplicate, percent = result_prediction(q1, q2)

        if percent>=50:
            tkinter.messagebox.showinfo(
            'your result is', 'Your question is duplicate')
        else:
            tkinter.messagebox.showinfo(
            'your result is', 'Your question is not duplicate ')
        # if(q1==q2):
        #     tkinter.messagebox.showinfo('your result is','your que is duplicate')
        # else:
        #     tkinter.messagebox.showinfo('your result is','your que is not duplicate')

        # write final result to csv file
        write_to_csv(question1, question2, is_duplicate, percent)

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

################################ 2 starts here ########################################################    

def onequewindow(param):
    param.destroy
    top = Toplevel()
    top.title("Duplicate Question Detection With existing questions")
    top.geometry('1350x750+0+0')
    top.config(bg='powder blue')
    Button1=Button(top, text="  Close  ",command=top.destroy,fg='red')  
    Button1.place(bordermode=OUTSIDE, height=45, width=220, x=570,y=20)
    Button1.bind
    
    if not ques_list_for_search:
        lblTitle1 = Label(top,  text = 'Your Question does not match!!!!!', font = ('arial',15,'bold'), bg='powder blue',
                                fg = 'purple')
        lblTitle1.place(x=500,y=100)
    
    else:
        lblTitle1 = Label(top,  text = 'Your Question already exists!!!!!', font = ('arial',15,'bold'), bg='powder blue',
                                fg = 'purple')
        lblTitle1.place(x=500,y=100)
        lblTitle1 = Label(top,  text = 'Similar questions are :', font = ('arial',15,'bold'), bg='powder blue',
                                fg = 'purple')
        lblTitle1.place(x=500,y=150)
        List=Listbox(top, width=50, height=20, font=("Times", 12),fg= 'red')
        for i in range(len(ques_list_for_search)):
            List.insert(i+1,'   '+ques_list_for_search[i])
        List.place(x=500,y=200)
        List.bind()
        ques_list_for_search.clear()
    

#SEARCH QUESTION WINDOW
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
        question1= First_que.get()

        # Get the value stored in the entries
        q1 = word_indexer(First_que.get())

        # Delete the value in the entry
        First_que.delete(0, "end")
        # print(que1)
        
        with open('prediction_test_questions.csv', 'r') as f:
            # remove head row
            header = next(f)
            csvr = csv.reader(f)
            flag = 0
            # loop through each row
            # print(f"Checking with: {question1}")
            for row in csvr:
                # loop through first two cols(both question cols)
                for i in range(0, 2):
                    # print(row[i])
                    q2 = row[i]
                    is_duplicate, percent = result_prediction(
                        q1, word_indexer(q2))
    
                    if is_duplicate == 1:
                        # print(f"duplicate found-> {row[i]}")
                        ques_list_for_search.append(row[i])
                        flag = 1
            # if flag == 0:
                # print('no duplicates found')
    Label(top, text="First Question").grid(row=5, sticky=W, padx=10)
    First_que=Entry(top,width=120)
    First_que.grid(row=5, column=1, sticky=E, pady=10)
 
    equalButton=Button(top, text="Submit",command=lambda: onequewindow(top))
    equalButton.grid(row=6)
    equalButton.bind("<Button-1>",get_que)

    Button1=Button(top, text="  close  ",command=top.destroy)
    Button1.grid(row=6,column=1,sticky=E, pady=10)
    Button1.bind

################################ 3 starts here ########################################################

def comp(param):
    param.destroy
    top = Toplevel()
    # comparision starts here
    for i in range(0, len(filelist1)):
        with open(filelist1[i], 'r') as f:
            # remove head row
            header = next(f)
            csvr = csv.reader(f)
    
            # loops through each row
            for row in csvr:
                # <call compare function here and pass row as parameter to compare>
                original_questions, target_questions = compare_questions(row)
                # print(shape(original_questions))
                # print(len(original_questions))
                # print(row)
                # print(" ")
    
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
    for i in range(len(original_questions)):
        List1.insert(i+1,'  '+original_questions[i])
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
    for i in range(len(target_questions)):
        List2.insert(i+1,'  '+target_questions[i])
    List2.place(x=700,y=200)
    List2.bind()
    # print(original_questions)
    original_questions.clear()
    # print(target_questions)
    target_questions.clear()
    filelist.clear()
    filelist1.clear()



#CSV FILE WINDOW 3
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
# print(filelist)
# print(filelist1)