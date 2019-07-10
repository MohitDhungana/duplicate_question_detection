
from tkinter import *
from tkinter import ttk

from tensorflow.python.keras.models import load_model
import tensorflow.python.keras.backend as K
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import json
import re
import numpy as np
import pandas as pd
import csv


# gets a whole question inside text variable on which  preprocessing is done and then the question is splitted into word indices and returned
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
    with open('prediction_test_questions.csv', mode='a') as question_file:
        question_writer = csv.writer(
            question_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        question_writer.writerow([question1, question2, is_duplicate, percent])


# manhattan distance calculation function
def manhattan_distance(left, right):
    return K.exp(-K.sum(K.abs(left-right), axis=1, keepdims=True))


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


# function for tkinter button-click event
def get_que(event):

    print('\n\n\n')
    question1 = First_que.get()
    question2 = Second_que.get()
    print(question1)
    print(question2)

    # Get the value stored in the entries
    q1 = word_indexer(First_que.get())
    q2 = word_indexer(Second_que.get())

    # Delete the value in the entry
    First_que.delete(0, "end")
    Second_que.delete(0, "end")

    # get result and percentage from prediction
    is_duplicate, percent = result_prediction(q1, q2)

    # write final result to csv file
    write_to_csv(question1, question2, is_duplicate, percent)


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
        print("Duplicate -> ", str(pred[0][0]*100) + ' %')
        return 1, str(pred[0][0]*100)
    else:
        print("Not Duplicate -> ", str(pred[0][0]*100) + ' %')
        return 0, str(pred[0][0]*100)


# function to index tokenized words using training vocabulary dictionary
def word_indexer(question):
    ques_index = []

    for word in text_to_word_list(question):
        if word in vocab_dictionary:
            ques_index.append(vocab_dictionary[word])
    return ques_index


# ------------------------GUI STARTS HERE------------------------
root = Tk()
root.title("Duplicate Question Detection")
root.minsize(width=800, height=150)
root.maxsize(width=800, height=150)

# rows start at 0, 1, ...
# columns start at 0, 1, ...
# sticky defines how the widget expands (N, NE, E, SE,
# S, SW, W, NW)
# padx and pady provide padding around the widget above
# and below it

# First label
Label(root, text="First Question").grid(row=0, sticky=W, padx=10)
First_que = Entry(root, width=100)
First_que.grid(row=0, column=1, sticky=E, pady=10)

# Second label
Label(root, text="Second Question").grid(row=1, sticky=W, padx=10)
Second_que = Entry(root, width=100)
Second_que.grid(row=1, column=1, sticky=E, pady=10)

# Button label
equalButton = Button(root, text="Submit")
equalButton.grid(row=3)

# Button click event-> function 'get_que' is called
equalButton.bind("<Button-1>", get_que)

# GUI END
root.mainloop()
