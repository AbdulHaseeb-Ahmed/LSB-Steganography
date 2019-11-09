from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successful", fg="green", font=("Calibri", 11)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x500")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please Enter Details Below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def saved():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Saved")
    screen7.geometry("200x200")
    Label(screen7, text="Saved").pack()

def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()

def create_notes():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Info")
    screen6.geometry("400x400")
    Label(screen6, text="Please enter a filename for the note below").pack()
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    Entry(screen6, text=raw_filename).pack()
    Label(screen6, text="Please enter the notes for the file below").pack()
    Entry(screen6, text=raw_notes).pack()
    Button(screen6, text="Save", command=save).pack()

def view_notes1():
    global screen9
    filename1= raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen9 = Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("400x400")
    Label(screen9, text=data1).pack()
    data.close()

def view_notes():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Info")
    screen8.geometry("250x250")
    all_files = os.listdir()
    Label(screen8, text="Please use one of the filenames below").pack()
    Label(screen8, text=all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen8, textvariable=raw_filename1).pack()
    Button(screen8, command=view_notes1, text="OK").pack()

def delete_notes1():
    global screen11
    filename2 = raw_filename2.get()
    os.remove(filename2)
    screen11 = Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("400x400")
    Label(screen11, text=filename2 + " has been removed!").pack()

def delete_notes():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Info")
    screen10.geometry("250x250")
    all_files = os.listdir()
    Label(screen10, text="Please use one of the filenames below").pack()
    Label(screen10, text=all_files).pack()
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen10, textvariable=raw_filename2).pack()
    Button(screen10, command=delete_notes1, text="OK").pack()

def session():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Dashboard")
    screen3.geometry("500x500")
    Label(screen3, text="Welcome to the Dashboard").pack()
    Button(screen3, text="Create Note", command=create_notes).pack()
    Button(screen3, text="View Note", command=view_notes).pack()
    Button(screen3, text="Delete Note", command=delete_notes).pack()
    Button(screen3, text="Quit", command=delete2).pack()

def login_success():
    session()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Invalid Password")
    screen4.geometry("200x100")
    Label(screen4, text="Password is Incorrect").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Invalid User")
    screen5.geometry("200x100")
    Label(screen5, text="Username Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x500")
    Label(screen2, text="Please Enter Details Below to Login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username * ").pack()
    global username_entry1
    global password_entry1
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()



def main_Screen():
    global screen
    screen = tk.Tk()
    screen.geometry("500x500")
    screen.title("Notes 1.0")
    Label(text= "Notes 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()

main_Screen()



















'''
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.app"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()

def runApps():
    for app in apps:
        os.system('open %s' % app)

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="#263D42", bg="white", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="#263D42", bg="white", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

'''