import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, TclError

import csv
from db_conn import DB, DB_CONN
from data_access import DAO

global genres
genres = []

def login(user_entry, pass_entry):
    username = user_entry.get()
    password = pass_entry.get()

    if username and password:
        print("user: "+username)
        print("pass: "+password)
        signed = DAO.checkUser(username, password)
        if signed == True:
            messagebox.showinfo("Information", "Login succesfull")
        else: messagebox.showinfo("Information", "Login failed")
    else: pass

    return username, password

def signin_UI(container):
    toplevel = tk.Toplevel(container)

    username = tk.StringVar()
    password = tk.StringVar()

    ttk.Label(toplevel, text="Username:").grid(column=0, row=0, sticky=tk.W)
    user_entry = tk.Entry (toplevel, textvariable= username)
    user_entry.grid(column=1, row=0, sticky=tk.W)

    ttk.Label(toplevel, text="Password:").grid(column=0, row=1, sticky=tk.W)
    pass_entry = tk.Entry (toplevel, textvariable= password, show= "*")
    pass_entry.grid(column=1, row=1, sticky=tk.W)


    ttk.Button(toplevel, text="Login", command=lambda: login(user_entry, pass_entry)).grid(column=1, row=2)
    return toplevel, user_entry, pass_entry

def editBook(container): #edit khi ấn thẳng vào book trên bảng result
    pass

def allBook(container) -> None: #khum write duoc
    list_books = DAO.getData()
    print(list_books)
    dataWrite(list_books)
    create_result_frame(container)

def clear_checkboxes(container):
    for widget in container.winfo_children():
        if isinstance(widget, tk.Checkbutton):
            widget.deselect()

def fileClear():
    with open("book.csv", "w") as file:
        file.truncate(0)

def dataRead():
    with open("book.csv", "r", encoding="UTF-8") as file:
        content = csv.reader(file)
    return content

def addBook(title_entry, author_entry):
    genres_str = ', '.join(map(str, genres))
    title = title_entry.get()
    author = author_entry.get()

    print(title)
    print(author)
    DAO.addData_book(title, author, genres_str)

def addBook_UI(container):
    toplevel = tk.Toplevel(container)

    toplevel.columnconfigure(0, weight=1)

    title = tk.StringVar()
    author = tk.StringVar()

    ttk.Label(toplevel, text="Book title:").grid(column=0, row=0, sticky=tk.W)
    title_entry = tk.Entry(toplevel, width=30, textvariable=title)
    title_entry.grid(column=1, row=0)
    
    ttk.Label(toplevel, text="Genre:").grid(column=0, row=1)
    genreMenu(toplevel)
    
    ttk.Label(toplevel, text="Author:").grid(column=0, row=7)
    author_entry = tk.Entry(toplevel, width=30, textvariable=author)
    author_entry.grid(column=1, row=7)

    ttk.Button(toplevel, text="Add", command=lambda: addBook(title_entry, author_entry)).grid(column=1, row=8)

def dataWrite(records) -> None:
    with open('book.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

def search(title_entry, author_entry, container): 
    name =  title_entry.get()
    author = author_entry.get()
    books = []

    print(f"{name}\n{author}")

    cursor =DB_CONN.cursor()
    query = "SELECT * FROM book"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    if name == '' and author == '' and genres == []:
        for record in records:
            books.append(record)
    else:
        for record in records:
            if name != '' and author != '' and genres != []:
                for genre in genres:
                    if name in record[1] and author in record[2] and genre in record[3]:
                        print(record)
                        books.append(record)
            elif name != '' and author != ''and genres == []:
                if name in record[1] and author in record[2]:
                    print(record)
                    books.append(record)
            elif name != '' and author == ''and genres != []:
                for genre in genres:
                    if name in record[1] and genre in record[3]:
                        print(record)
                        books.append(record)
            elif name == '' and author != ''and genres != []:
                for genre in genres:
                    if author in record[2] and genre in record[3]:
                        print(record)
                        books.append(record)      
            elif name != '' and author == ''and genres == []:
                if name in record[1]:
                    print(record)
                    books.append(record)
            elif name == '' and author != ''and genres == []:
                if author in record[2]:
                    print(record)
                    books.append(record)    
            elif name == '' and author == ''and genres != []:
                for genre in genres:
                    if genre in record[3]:
                        print(record)
                        books.append(record)  
             
    dataWrite(books)

    #clean up
    result_frame = create_result_frame(container)
    result_frame.grid(column=0, row=1)
    genres.clear()
    fileClear()
    return records

def checkGenre(checked, input_genre):
    check_values = [
        "Horror",
        "Fiction",
        "Novel",
        "Romance",
        "Drama",
        "History",
        "Art & Photography",
        "Guide",
        "Non-fiction",
        "Food & Drinks",
    ]
    for i, genre in enumerate(check_values):
        if checked.get() == 1 and input_genre == i:
            genres.append(genre)
        if checked.get() == 0 and input_genre == i:
            genres.remove(check_values[i])
    print(genres)
    return genres

def genreMenu(toplevel):
    check = IntVar()
    check1 = IntVar()
    check2 = IntVar()
    check3 = IntVar()
    check4 = IntVar()
    check5 = IntVar()
    check6 = IntVar()
    check7 = IntVar()
    check8 = IntVar()
    check9 = IntVar()

    button = Checkbutton(toplevel, text="Horror", variable=check, onvalue=1, offvalue=0, command=lambda: checkGenre(check, 0))
    button1 = Checkbutton(toplevel, text="Fiction", variable=check1, onvalue=1, offvalue=0, command=lambda: checkGenre(check1, 1))
    button2 = Checkbutton(toplevel, text="Novel", variable=check2, onvalue=1, offvalue=0, command=lambda: checkGenre(check2, 2))
    button3 = Checkbutton(toplevel, text="Romance", variable=check3, onvalue=1, offvalue=0, command=lambda: checkGenre(check3, 3))
    button4 = Checkbutton(toplevel, text="Drama", variable=check4, onvalue=1, offvalue=0, command=lambda: checkGenre(check4, 4))
    button5 = Checkbutton(toplevel, text="History", variable=check5, onvalue=1, offvalue=0, command=lambda: checkGenre(check5, 5))
    button6 = Checkbutton(toplevel, text="Art & Photography", variable=check6, onvalue=1, offvalue=0, command=lambda: checkGenre(check6, 6))
    button7 = Checkbutton(toplevel, text="Guide", variable=check7, onvalue=1, offvalue=0, command=lambda: checkGenre(check7, 7))
    button8 = Checkbutton(toplevel, text="Non-fiction", variable=check8, onvalue=1, offvalue=0, command=lambda: checkGenre(check8, 8))
    button9= Checkbutton(toplevel, text="Food & Drinks", variable=check9, onvalue=1, offvalue=0, command=lambda: checkGenre(check9, 9))
    
    button.grid(column=0, row=2)
    button1.grid(column=0, row=3)
    button2.grid(column=0, row=4)
    button3.grid(column=0, row=5)
    button4.grid(column=0, row=6)
    button5.grid(column=1, row=2)
    button6.grid(column=1, row=3)
    button7.grid(column=1, row=4)
    button8.grid(column=1, row=5)
    button9.grid(column=1, row=6)

def search_UI(container):
    toplevel = tk.Toplevel(container)

    toplevel.columnconfigure(0, weight=1)

    title = tk.StringVar()
    author = tk.StringVar()

    ttk.Label(toplevel, text="Book title:").grid(column=0, row=0, sticky=tk.W)
    title_entry = tk.Entry(toplevel, width=30, textvariable=title)
    title_entry.grid(column=1, row=0)
    
    #Genre frame
    ttk.Label(toplevel, text="Genre:").grid(column=0, row=1)
    genreMenu(toplevel)
    
    ttk.Label(toplevel, text="Author:").grid(column=0, row=7)
    author_entry = tk.Entry(toplevel, width=30, textvariable=author)
    author_entry.grid(column=1, row=7)

    ttk.Button(toplevel, text="Search", command=lambda: search(title_entry, author_entry, container)).grid(column=1, row=8)
    genres.clear()
    clear_checkboxes(toplevel)
    return toplevel, title_entry, author_entry

def create_result_frame(container):
    frame = ttk.Frame(container)
    frame.grid(column=0, row=2)

    tree = ttk.Treeview(frame, columns=("ID", "Title", "Author", "Genre"), show="headings")
    tree.pack(side="left", fill="both", expand=True)

    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Genre", text="Genre")

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")

    tree.configure(yscrollcommand=scrollbar.set)


    with open("book.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            tree.insert("", "end", values=row)
    return frame

def create_button_frame(container): #search, add, del book function
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Search book', command=lambda: search_UI(container)).grid(column=0, row=0)
    ttk.Button(frame, text='Add book',command= lambda: addBook_UI(container)).grid(column=1, row=0)
    ttk.Button(frame, text='Delete book').grid(column=2, row=0)
    #sign in buttonn in user frame

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_user_frame(container): 
    frame = tk.Frame(container, highlightbackground="black", highlightthickness=1)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Sign in', command=lambda: (container)).grid(column=3, row=0)
    return frame

def mainWindow():
    root = tk.Tk()
    root.title('Library manage system')
    root.resizable(0, 0)

    try:
        DB.initializeDB() #execute create tables query from setup.sql
    except: pass

    result_frame = create_result_frame(root)
    result_frame.grid(column=0, row=1)

    button_frame = create_button_frame(root)
    button_frame.grid(column=0, row=0)

    signin_frame = create_user_frame(root)
    signin_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == '__main__':
    app = mainWindow()