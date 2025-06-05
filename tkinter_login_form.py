from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login Form")
window.geometry("340x440")
window.configure(bg='#333333')

frame = Frame(bg='#333333')

def login():
    username = "Tanisha Khaitan"
    password = '1234'
    
    if username_entry.get()=="Tanisha Khaitan" and password_entry.get()=='1234':
        messagebox.showinfo(title = 'Login success',message="Congratulations!! You successfully logged in.")
    else:
        messagebox.showinfo(title='Invalid Data',message="User data is invalid!! try again!!")

#label = Label(window,text='Login')
#label.pack()
#label.grid(row=0, column=0)


#creating widgets
login_label = Label(frame,text='Login', bg='#333333', fg='yellow', font=("arial", 25), underline=True)
username_label = Label(frame,text='Username', bg='#333333', fg='#ffffff',font=("arial", 15))
username_entry = Entry(frame, font=("arial", 15))
password_entry = Entry(frame, show='*', font=("arial", 15)) 
password_label = Label(frame,text='Password',bg='#333333', fg='#ffffff',font=("arial", 15))
login_button = Button(frame,text='Login',bg='yellow',fg='black', font=("arial", 14), command=login)



#placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40) 
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20) 
password_entry.grid(row=2, column=1, pady=20)
password_label.grid(row=2, column=0) 
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()