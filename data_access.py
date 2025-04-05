import hashlib
from db_conn import DB_CONN
from dataclasses import dataclass
from tkinter import messagebox


@dataclass
class Book: #Books table
    id: int
    name: str
    author: str
    genre: str

@dataclass
class Student:
    id: int
    name: str
    username: str
    password: str

class DAO:
    @staticmethod
    def addData_book(name: str, author: str, genre: str) -> None:
        try: 
            query = "INSERT INTO book (name, author, genre) VALUES (?, ?, ?)"
            info = (name, author, genre)
            cursor = DB_CONN.cursor()
            cursor.execute(query, info)
            DB_CONN.commit()
            cursor.close()
            added = True
        except:
            added = False
            print("Error while inserting data.")
        if added == True:
            messagebox.showinfo("Information", "Add book successfull")
        return added        
    
    @staticmethod
    def addData_student(name: str, username: str, password: str) -> None:
        try: 
            query = "INSERT INTO student (name, username, password) VALUES (?, ?, ?)"
            info = (name, username, password)
            cursor = DB_CONN.cursor()
            cursor.execute(query, info)
            DB_CONN.commit()
            cursor.close()
        except:
            print("Error while inserting data.")
        return None  
    
    @staticmethod
    def getRecords() -> list:
        cursor =DB_CONN.cursor()
        query = "SELECT * FROM book"
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records
    
    @staticmethod
    def delData_book(values: tuple) -> None:
        book_id = values[0]
        try:
            cursor = DB_CONN.cursor()
            query = "DELETE FROM book WHERE id = ?"
            info = (book_id,)
            cursor.execute(query, info)
            DB_CONN.commit()
            cursor.close()
            messagebox.showinfo("Information", "Book deleted")
        except:
            messagebox.showerror("Error", "Cannot delete book")
        return None
    
    @staticmethod
    def editBook(values: tuple, varlist: list) -> None:
        update_values = [entry_var.get() for entry_var in varlist]
        book_id = values[0]
        title = update_values[1]
        author = update_values[2]
        genre = update_values[3]

        cursor = DB_CONN.cursor()
        query = "UPDATE book SET"
        info = []

        if title != values[1]:
            query += " name = ?,"
            info.append(title)
        if author != values[2]:
            query += " author = ?,"
            info.append(author)
        if genre != values[3]:
            query += " genre = ?,"
            info.append(genre)

        query = query.rstrip(",") + " WHERE id = ?"
        info.append(book_id)

        print(query)
        print(info)   
        try:
            cursor.execute(query, info)
            DB_CONN.commit()
            cursor.close()
            messagebox.showinfo("Information", "Book edited")
        except:
            messagebox.showerror("Error", "Cannot edit book")
        return None

    @staticmethod
    def checkUser(username: str, password: str) -> bool:
        global user_id
        query = "SELECT * FROM student"
        cursor = DB_CONN.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        DB_CONN.commit()
        cursor.close()

        login = False
        user_id = ''
        en_pass = hashlib.md5(password.encode()).hexdigest()
        print(en_pass)

        for record in records:
            print(record)
            if username == record[2] and en_pass == record[3]:
                login = True
                print(record[2])
                #user_id = record[0]
        return login
    
    @staticmethod
    def addUser(username: str, password: str) -> None:
        try:    
            en_pass = hashlib.md5(password.encode()).hexdigest()            
            query = "INSERT INTO student (name, password) VALUES (?, ?)"
            info = (username, en_pass)
            cursor = DB_CONN.cursor()
            cursor.execute(query, info)
            DB_CONN.commit()
            cursor.close()
        except:
            print("Error while inserting user.")
        return None