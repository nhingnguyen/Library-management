import tkinter as tk
from tkinter import messagebox
import csv
from data_access import DAO
from db_conn import DB_CONN



global genres
genres = []
class BookController:
    def checkGenre(checked, input_genre) -> list:
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

    def addBook(title_entry, author_entry) -> None:
        genres_str = ', '.join(map(str, genres))
        title = title_entry.get()
        author = author_entry.get()
        print(title)
        print(author)
        try:
            if len(genres) > 1:
                messagebox.showerror("Error", "Please choose only 1 genre")
            else:
                DAO.addData_book(title, author, genres_str)
        except:
            messagebox.showerror("Error", "Cannot add book")

        return None
    
    def searchBook(title_entry, author_entry) -> None: 
        title =  title_entry.get()
        author = author_entry.get()
        books = []

        print(f"{title}\n{author}")
        records = DAO.getRecords()
        if title == '' and author == '' and genres == []:
            messagebox.showinfo("Information", "Can't find book")
        else:
            for record in records:
                if title != '' and author != '' and genres != []:
                    for genre in genres:
                        if title in record[1] and author in record[2] and genre in record[3]:
                            print(record)
                            books.append(record)
                elif title != '' and author != ''and genres == []:
                    if title in record[1] and author in record[2]:
                        print(record)
                        books.append(record)
                elif title != '' and author == ''and genres != []:
                    for genre in genres:
                        if title in record[1] and genre in record[3]:
                            print(record)
                            books.append(record)
                elif title == '' and author != ''and genres != []:
                    for genre in genres:
                        if author in record[2] and genre in record[3]:
                            print(record)
                            books.append(record)      
                elif title != '' and author == ''and genres == []:
                    if title in record[1]:
                        print(record)
                        books.append(record)
                elif title == '' and author != ''and genres == []:
                    if author in record[2]:
                        print(record)
                        books.append(record)    
                elif title == '' and author == ''and genres != []:
                    for genre in genres:
                        if genre in record[3]:
                            print(record)
                            books.append(record)  
        Menu.fileClear()
        Menu.fileWrite(books)
        genres.clear()
        return None

    def editBook(values, varlist) -> None:
        DAO.editBook(values, varlist)
        return None
    
    def delBook(values) -> None:
        DAO.delData_book(values)
        return None

    def refresh() -> None:
        records = DAO.getRecords()       
        Menu.fileClear()
        Menu.fileWrite(records)
        return None
    
class Menu:
    def fileRead():
        with open("book.csv", "r", encoding="UTF-8") as file:
            content = csv.reader(file)
        return content
    def fileClear():
        with open("book.csv", "w") as file:
            file.truncate(0)
        return None
    def fileWrite(records):
        with open('book.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return None
    def listClear():
        genres.clear()
        return None
    def checkboxClear(container):
        for widget in container.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.deselect()
        return None
    def closeToplevel(toplevel):
        toplevel.destroy()
        return None
