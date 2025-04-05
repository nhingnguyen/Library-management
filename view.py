import tkinter as tk
from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from tkinter import messagebox
import csv
from book_controller import BookController, Menu
from data_access import DAO
login = False

class UI:
    f_tree: Frame
    tree: Treeview
    
    button_frame: Frame
    btn_add: Button
    btn_search: Button
    btn_edit: Button
    btn_del: Button
    btn_refresh: Button
    btn_login: Button


    search: Button
    add: Button
    edit: Button
    delbokk: Button
    signin_button: Button

    add_UI: Toplevel
    search_UI: Toplevel
    toplevel: Toplevel
    login_ui: Toplevel

    title_label: Label
    author_label: Label
    genre_label: Label

    title_entry: Entry
    author_entry: Entry

class BookView:
    ui: UI
    tree: Treeview
    main: Tk
    def __init__(self, main: Tk) -> None:
        self.main = main
        self.ui = UI()
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=1)
        self.createView()
        return None
    
    def login_UI(self) -> Entry:
        self.ui.login_ui = tk.Toplevel(self.main)

        username = tk.StringVar()
        password = tk.StringVar()

        Label(self.ui.login_ui, text="Username:").grid(column=0, row=0, sticky=tk.W)
        user_entry = tk.Entry (self.ui.login_ui, textvariable= username)
        user_entry.grid(column=1, row=0, sticky=tk.W)

        Label(self.ui.login_ui, text="Password:").grid(column=0, row=1, sticky=tk.W)
        pass_entry = tk.Entry (self.ui.login_ui, textvariable= password, show= "*")
        pass_entry.grid(column=1, row=1, sticky=tk.W)


        def signin(username, password) -> bool:
            global login
            login = DAO.checkUser(username, password)
            if login == True:
                messagebox.showinfo("Information", "Login successful")
                self.ui.btn_login.config(state="disabled")
                self.ui.btn_add.config(state="active")
            else:
                messagebox.showinfo("Information", "Login failed") 
            return login
        self.ui.signin_button = Button(self.ui.login_ui, text="Login", command=lambda: [signin(user_entry.get(), pass_entry.get()), Menu.closeToplevel(self.ui.login_ui),self.tableView(login)])
        self.ui.signin_button.grid(column=1, row=2)
        print(login)
        return user_entry, pass_entry
    
    def createView(self) -> None:
        self.buttonElements()
        self.tableView(login)
        return None
    
    def tableView(self, login) -> None:
        self.ui.f_tree = Frame(self.main)
        self.ui.f_tree.grid(column=0, row=1, sticky="nsew")

        self.ui.tree = Treeview(self.ui.f_tree, columns=("ID", "Title", "Author", "Genre"), show="headings")
        self.ui.tree.pack(side="left", fill="both", expand=True)

        self.ui.tree.heading("ID", text="ID")
        self.ui.tree.heading("Title", text="Title")
        self.ui.tree.heading("Author", text="Author")
        self.ui.tree.heading("Genre", text="Genre")

        scrollbar = Scrollbar(self.ui.f_tree, orient="vertical", command=self.ui.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.ui.tree.configure(yscrollcommand=scrollbar.set)

        with open("book.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.ui.tree.insert("", "end", values=row)
        if login == True:
            self.ui.tree.bind("<Double-1>", self.doubleClick)
        else: pass
        return None
    
    def buttonElements(self) -> None:
        self.ui.button_frame = Frame(self.main)
        self.ui.button_frame.grid(column=0, row=0, sticky="nsew")

        self.ui.btn_search = Button(self.ui.button_frame, text="Search book", command=lambda :self.search_UI()) 
        self.ui.btn_add =    Button(self.ui.button_frame, text="Add book", command=lambda :self.add_UI())
        self.ui.btn_add.config(state="disabled")          
        self.ui.btn_login =  Button(self.ui.button_frame, text="Login", command=lambda: self.login_UI())          
        self.ui.btn_refresh= Button(self.ui.button_frame, text="Refresh", command=lambda: [BookController.refresh(), self.tableView(login)])

        self.ui.btn_search. pack(side="left", expand=True, fill=BOTH)
        self.ui.btn_add.    pack(side="left", expand=True, fill=BOTH)
        self.ui.btn_login.  pack(side="left", expand=True, fill=BOTH)
        self.ui.btn_refresh.pack(side="right", expand=True, fill=BOTH)
        return None
    
    def genreMenu(self,container) -> None:
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

        button = Checkbutton(container, text="Horror", variable=check, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check, 0))
        button1 = Checkbutton(container, text="Fiction", variable=check1, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check1, 1))
        button2 = Checkbutton(container, text="Novel", variable=check2, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check2, 2))
        button3 = Checkbutton(container, text="Romance", variable=check3, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check3, 3))
        button4 = Checkbutton(container, text="Drama", variable=check4, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check4, 4))
        button5 = Checkbutton(container, text="History", variable=check5, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check5, 5))
        button6 = Checkbutton(container, text="Art & Photography", variable=check6, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check6, 6))
        button7 = Checkbutton(container, text="Guide", variable=check7, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check7, 7))
        button8 = Checkbutton(container, text="Non-fiction", variable=check8, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check8, 8))
        button9= Checkbutton(container, text="Food & Drinks", variable=check9, onvalue=1, offvalue=0, command=lambda: BookController.checkGenre(check9, 9))

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
        return None

    def search_UI(self) -> Entry:
        self.ui.search_UI = Toplevel(self.main)

        self.title = StringVar()
        self.author = StringVar()

        self.ui.title_label = Label(self.ui.search_UI, text="Book title:"). grid(column=0, row=0)
        self.ui.title_entry = Entry(self.ui.search_UI, width=30, textvariable=self.title)
        self.ui.title_entry.grid(column=1, row=0)

        self.ui.author_label = Label(self.ui.search_UI, text="Author:").    grid(column=0, row=1)
        self.ui.author_entry = Entry(self.ui.search_UI, width=30, textvariable=self.author)
        self.ui.author_entry.grid(column=1, row=1)

        self.ui.genre_label = Label(self.ui.search_UI, text="Genre:").      grid(column=0, row=2)
        self.genreMenu(self.ui.search_UI)

        self.ui.search = Button(self.ui.search_UI, text="Search", command=lambda: [BookController.searchBook(self.ui.title_entry, self.ui.author_entry), Menu.closeToplevel(self.ui.search_UI), self.tableView(login)])
        self.ui.search.grid(column=1, row=7)
        Menu.listClear()
        return self.ui.title_entry, self.ui.author_entry
    
    def add_UI(self) -> Entry:
        self.ui.add_UI = Toplevel(self.main)

        title = StringVar()
        author = StringVar()

        self.ui.title_label = Label(self.ui.add_UI, text="Book title:").             grid(column=0, row=0)
        self.ui.title_entry = Entry(self.ui.add_UI, width=30, textvariable=title)
        self.ui.title_entry.grid(column=1, row=0)

        self.ui.author_label = Label(self.ui.add_UI, text="Author:").                grid(column=0, row=1)
        self.ui.author_entry = Entry(self.ui.add_UI, width=30, textvariable=author)
        self.ui.author_entry.grid(column=1, row=1)

        self.ui.genre_label = Label(self.ui.add_UI, text="Genre:").                  grid(column=0, row=2)      
        self.genreMenu(self.ui.add_UI)

        self.ui.add = Button(self.ui.add_UI, text="Add", command=lambda: [BookController.addBook(self.ui.title_entry, self.ui.author_entry), Menu.closeToplevel(self.ui.add_UI), self.tableView(login)])
        self.ui.add.grid(column=1, row=7)
        Menu.listClear()
        return self.ui.title_entry, self.ui.author_entry

    def doubleClick(self, event) -> None: #edit-del
        item = self.ui.tree.focus()
        values = self.ui.tree.item(item, "values")
        print(item)
        print(values)

        #row data
        self.ui.toplevel = Toplevel(self.main)
        self.ui.toplevel.columnconfigure(0, weight=1)
        self.ui.toplevel.columnconfigure(1, weight=3)

        varlist = []

        Label(self.ui.toplevel, text="ID:").    grid(column=0, row=0)
        Label(self.ui.toplevel, text="Title:"). grid(column=0, row=1)
        Label(self.ui.toplevel, text="Author:").grid(column=0, row=2)
        Label(self.ui.toplevel, text="Genre:"). grid(column=0, row=3)

        for i, value in enumerate(values):
            entry_var = StringVar(value=value)
            entry = Entry(self.ui.toplevel, width=30, textvariable=entry_var)
            entry.grid(column=1, row=i)
            if i == 0:
                entry.config(state="readonly")
            varlist.append(entry_var)

        Button(self.ui.toplevel, text="Edit", command=lambda: [BookController.editBook(values, varlist), Menu.closeToplevel(self.ui.toplevel),BookController.refresh()]).grid(column=1, row=4)
        Button(self.ui.toplevel, text="Delete", command=lambda:[BookController.delBook(values),Menu.closeToplevel(self.ui.toplevel),BookController.refresh()]).grid(column=1, row=4, sticky=E)
        return None
