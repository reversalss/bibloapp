try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    print("Can't import modules")


# COLORS

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

    welcome_label = Label(appS, text=f"Welcome, {username}!", font=("JetBrains Mono", 25), bg=mainBlue, fg="white")
    welcome_label.pack(pady=60)


    def bookrent():


        renB = Tk()
        renB.geometry("400x500")
        renB.iconbitmap("logo.ico")
        renB.title("BibloApp")
        renB.config(background="#04386b")
        renB.resizable(False, False)

        # Widgets

        header = Label(renB, text="Rent")
        header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
        header.pack(pady=25)


        books = []

        f = open("books.txt", "r")
        for i in f.readlines():
            i = i.split("|")
            books.append(f"{i[0]}: {i[1]}")
        
        book_combobox = ttk.Combobox(renB)
        book_combobox.config(values=books)
        book_combobox.config(background=secBlue, foreground="white", width=50)
        book_combobox['state'] = 'readonly'
        book_combobox.pack(pady=(50,0))

        def rentbook():

            book = book_combobox.get()
            book = book.split(":") 
            book = f"{book[0].strip()}|{book[1].strip()}" # <ISBN>: <NAME> -> <ISBN>|<NAME>
            print(f"renting book for studentID: {studentID}")

            # remove book
            with open("rented.txt", "a") as f:
                f.write(f"{book}|{studentID}")
                popup("Book successfully rented!\nYou may now close this window.")


            with open("books.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i.strip("\n") != book:
                        f.write(i)
                f.truncate()

        submit_button = Button(renB, text="Rent Book", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
        submit_button.config(command=rentbook)
        submit_button.pack(pady=25)
        
    def bookreturn():

        retB = Tk()
        retB.geometry("400x500")
        retB.iconbitmap("logo.ico")
        retB.title("BibloApp")
        retB.config(background="#04386b")
        retB.resizable(False, False)

        # Widgets

        header = Label(retB, text="Return")
        header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
        header.pack(pady=25)


        books = []

        f = open("rented.txt", "r")
        for i in f.readlines():
            i = i.split("|")
            if i[2].strip() == studentID:
                books.append(f"{i[0]}: {i[1]}")
        
        book_combobox = ttk.Combobox(retB)
        book_combobox.config(values=books)
        book_combobox.config(background=secBlue, foreground="white", width=50)
        book_combobox['state'] = 'readonly'
        book_combobox.pack(pady=(50,0))

        def returnbook():

            book = book_combobox.get()
            book = book.split(":") 
            book = f"{book[0].strip()}|{book[1].strip()}" # <ISBN>: <NAME> -> <ISBN>|<NAME>
            print(f"renting book for studentID: {studentID}")

            # remove book
            with open("books.txt", "a") as f:
                f.write(f"\n{book}")
                popup("Book successfully returned!\nYou may now close this window.")


            with open("rented.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i.strip("\n") != f"{book}|{studentID}":
                        f.write(i)
                f.truncate()

        submit_button = Button(retB, text="Add Book", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
        submit_button.config(command=returnbook)
        submit_button.pack(pady=25)






    # BUTTONS

    rent_button = Button(appS, text="Rent Book", font=('JetBrains mono', 22), bg="#11589e", fg="white", relief="flat", width="15", command=bookrent)
    rent_button.pack(pady=(40, 0))

    return_button = Button(appS, text="Return Book", font=('JetBrains mono', 22), bg="#11589e", fg="white", relief="flat", width="15", command=bookreturn)
    return_button.pack(pady=(15, 0))


    def bookadd():

        addB = Tk()
        addB.geometry("400x500")
        addB.iconbitmap("logo.ico")
        addB.title("BibloApp")
        addB.config(background="#04386b")
        addB.resizable(False, False)

        # Widgets

        header = Label(addB, text="Add Book")
        header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
        header.pack(pady=25)


        # bookname

        label_bookname = Label(addB, text="Book Name:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
        label_bookname.pack(pady=5)

        bookname_entry = Entry(addB, fg="white", bg=secBlue, width=15, font=("Arial", 25))
        bookname_entry.pack(pady=5)


        # ISBN

        label_ISBN = Label(addB, text="ISBN:", bg=mainBlue, fg="white", font=("JetBrains Mono", 10))
        label_ISBN.pack(pady=5)

        ISBN_entry = Entry(addB, fg="white", bg=secBlue, width=15, font=("Arial", 25))
        ISBN_entry.pack(pady=5)



        # SUBMIT

        def addbook():

            print("adding book")

            # get info

            bookname_var = bookname_entry.get()
            ISBN_var = ISBN_entry.get()

            try:
                ISBN_var = int(ISBN_entry) 
            except: popup("ISBN can only be a number")
            else:
            
                if len(bookname_var) == 0 or len(ISBN_var) == 0:
                    popup("One of the fields are empty!\n please fill all fields")
                else:
                    # check if ISBN already exists

                    f = open("books.txt", "r")
                    for i in f.readlines():
                        if i.split("|")[0] == ISBN_var:
                            popup("ISBN allerede lagt til")
                            f.close()
                            break
                    else:
                        # if it doesn't, make a new book with new info
                        f = open("books.txt", "a")
                        f.write(f"{ISBN_var}|{bookname_var}\n")
                        popup("Adding book complete! You can now close this window.")
                        f.close()

                
        submit_button = Button(addB, text="Add Book", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
        submit_button.config(command=addbook)
        submit_button.pack(pady=25)


    ###########################################

    def bookremove():

        remB = Tk()
        remB.geometry("400x500")
        remB.iconbitmap("logo.ico")
        remB.title("BibloApp")
        remB.config(background="#04386b")
        remB.resizable(False, False)

        # Widgets

        header = Label(remB, text="Remove")
        header.config(font=('Akira Expanded', 40), bg="#04386b", fg="white")
        header.pack(pady=25)


        books = []

        f = open("books.txt", "r")
        for i in f.readlines():
            if len(i) != "":
                i = i.split("|")
                books.append(f"{i[0]}: {i[1]}")
            
        
        book_combobox = ttk.Combobox(remB)
        book_combobox.config(values=books)
        book_combobox.config(background=secBlue, foreground="white", width=50)
        book_combobox['state'] = 'readonly'
        book_combobox.pack(pady=(50,0))


        def removebook():

            book = book_combobox.get()
            book = book.split(":") 
            book = f"{book[0].strip()}|{book[1].strip()}" # <ISBN>: <NAME> -> <ISBN>|<NAME>
            print(f"removing {book}")

            with open("books.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i.strip("\n") != book:
                        f.write(i)
                f.truncate()
                popup("Book Removed!")

            

            

                        


        submit_button = Button(remB, text="Remove Book", font=('JetBrains mono', 15), bg="#11589e", fg="white", relief="flat", width="15")
        submit_button.config(command=removebook)
        submit_button.pack(pady=25)


    ###########################################



    if int(studentID) == 1:
        add_book = Button(appS, text="Add Book", font=('JetBrains mono', 22), bg="#11589e", fg="white", relief="flat", width="15", command=bookadd)
        add_book.pack(pady=(50, 0))

    if int(studentID) == 1:
        add_book = Button(appS, text="Remove Book", font=('JetBrains mono', 22), bg="#11589e", fg="white", relief="flat", width="15", command=bookremove)
        add_book.pack(pady=(15, 0))



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
                    appScreen(i[1], i[0])
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