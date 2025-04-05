from view import *
from db_conn import DB

class Main:
    def __init__(self) -> None:
        self.tk = Tk()
        self.tk.title("Library management")
        self.operate()
        self.tk.mainloop()
    def operate(self) -> None:
        try: 
            DB.initializeDB()
        except: pass
        BookView(main=self.tk)
        return None
    
if __name__ == "__main__":
    app = Main()
    