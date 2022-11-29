try:
    from tkinter import *
except ImportError:
    print("Can't import modules")



mainBlue = "#04386b"
secBlue = "#11589e"




# DEFS

def close(win):
    win.destroy()

def popup(info: str):

    # SET UP POPUP WINDOW

    popup_win = Tk()
    popup_win.geometry("300x150")
    popup_win.iconbitmap("logo.ico")
    popup_win.title("BibloApp")
    popup_win.resizable(False, False)

    # LABELS

    popup_label = Label(popup_win, text=info)
    popup_label.pack(pady=25)

    # BUTTONS

    exit_button = Button(popup_win, text="Ok", width=5, command=lambda: (close(popup_win)))
    exit_button.place(x=225, y=100)

def appScreen(username, studentID):

    appS = Tk()
    appS.geometry("800x600")
    appS.iconbitmap("logo.ico")
    appS.title("BibloApp")
    appS.config(background="#04386b")
    appS.resizable(False, False)




    # LABELS 

    welcome_label = Label(appS, text=f"Welcome, {username}!", font=("JetBrains Mono", 20), bg=mainBlue, fg="white")
    welcome_label.grid(row=1, column=1, padx=5, pady=5, sticky=E)

    

    # BUTTONS
    
    rent_button = Button(appS, text="Rent", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
    rent_button.grid(row=5, column=1, padx=5, pady=15, sticky=E)

def login():

    # SET UP REGISTER WINDOW
    
    logW = Tk()
    logW.geometry("400x500")
    logW.iconbitmap("logo.ico")
    logW.title("BibloApp")
    logW.config(background="#04386b")
    logW.resizable(False, False)

    # Widgets

    header = Label(logW, text="Login")
    header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
    header.pack(pady=25)

    
    # STUDENTID

    label_studentID = Label(logW, text="StudentID:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
    label_studentID.pack(pady=5)

    studentID_entry = Entry(logW, fg="white", bg=secBlue, width=15, font=("Arial", 25))
    studentID_entry.pack(pady=5)


    # PASSWORD

    label_password = Label(logW, text="Password:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
    label_password.pack(pady=5)

    password_entry = Entry(logW, fg="white", bg=secBlue, width=15, font=("Arial", 25), show="*")    
    password_entry.pack(pady=5)


    def loginUser():

        print("logging in user...")

        # get info

        studentID_var = studentID_entry.get() # [0]  - users.txt
        password_var = password_entry.get() # [2]

        f = open("users.txt", "r")
        for i in f.readlines():
            i = i.split(":")
            if i[0] == studentID_var: 
                if i[2].strip("\n") == password_var:
                    logW.destroy()
                    main.destroy()
                    appScreen(i[1], studentID_var)
                    f.close()
                    break
        else:
            popup("Wrong Student ID or Password")
        


        


       
    submit_button = Button(logW, text="Login", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
    submit_button.config(command=loginUser)
    submit_button.pack(pady=25)

def register():

    # SET UP REGISTER WINDOW
    
    regW = Tk()
    regW.geometry("400x500")
    regW.iconbitmap("logo.ico")
    regW.title("BibloApp")
    regW.config(background="#04386b")
    regW.resizable(False, False)

    # Widgets

    header = Label(regW, text="Register")
    header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
    header.pack(pady=25)


    # USERNAME

    label_username = Label(regW, text="Username:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
    label_username.pack(pady=5)

    username_entry = Entry(regW, fg="white", bg=secBlue, width=15, font=("Arial", 25))
    username_entry.pack(pady=5)

    
    # STUDENTID

    label_studentID = Label(regW, text="StudentID:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
    label_studentID.pack(pady=5)

    studentID_entry = Entry(regW, fg="white", bg=secBlue, width=15, font=("Arial", 25))
    studentID_entry.pack(pady=5)


    # PASSWORD

    label_password = Label(regW, text="Password:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
    label_password.pack(pady=5)

    password_entry = Entry(regW, fg="white", bg=secBlue, width=15, font=("Arial", 25), show="*")    
    password_entry.pack(pady=5)


    # SUBMIT

    def registerUser():

        print("registering user...")

        # get info

        username_var = username_entry.get()
        studentID_var = studentID_entry.get()
        password_var = password_entry.get()

        # check if studentID already exists

        f = open("users.txt", "r")
        for i in f.readlines():
            if i.split(":")[0] == studentID_var:
                popup("StudentID allerede i bruk")
                f.close()
                break
        else:
            # if it doesn't, make a new user with new info
            f = open("users.txt", "a")
            f.write(f"\n{studentID_var}:{username_var}:{password_var}")
            popup("Registration complete! You can now close this window.")
            f.close()


       
    submit_button = Button(regW, text="Register", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
    submit_button.config(command=registerUser)
    submit_button.pack(pady=25)


# set up main window

main = Tk()
main.geometry("800x600")
main.iconbitmap("logo.ico")
main.title("BibloApp")
main.config(background="#04386b")
main.resizable(False, False)


# MAIN WINDOW HEADERS

header = Label(main, text="BibloApp")
header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
header.pack(pady=50)



# MAIN WINDOW BUTTONS

button_login = Button(text="Login", font=('JetBrains mono', 25), bg="#11589e", fg="white", relief="flat", width="15", command=login)
button_login.place(x=245, y=250)

button_register = Button(text="Register", font=('JetBrains mono', 25), bg="#11589e", fg="white", relief="flat", width="15", command=register)
button_register.place(x=245, y=350)






main.mainloop()