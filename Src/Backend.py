import sqlite3

_Cursor : sqlite3.Cursor = None
_Connection : sqlite3.Connection = None

class Student:
    def __init__(self, ID : int, Name : str, PhoneNumber : int, Class : int) -> None:
        self.ID = ID
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Class = Class

class Teacher:
    def __init__(self, ID : int, Name : str, PhoneNumber : int, Class : int) -> None:
        self.ID = ID
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Class = Class

def _Update_():
    _Connection.commit()

def Execute(Query : str):
    _Cursor.execute(Query)
    _Update_()

def Init() -> bool:
    global _Cursor
    global _Connection

    _Connection = sqlite3.connect('School.db')

    _Cursor = _Connection.cursor()

    Execute("""
                    CREATE TABLE IF NOT EXISTS STUDENT(
                        ID INTEGER PRIMARY KEY NOT NULL,
                        Name TEXT,
                        PhoneNumber INTEGER,
                        Class INTEGER  
                    );
                    """)
    Execute("""
                    CREATE TABLE IF NOT EXISTS TEACHER(
                        ID INTEGER PRIMARY KEY NOT NULL,
                        Name TEXT,
                        PhoneNumber INTEGER,
                        Class INTEGER  
                    );
                    """)

    return not(_Cursor == None and _Connection == None)
    

def Add(Data) -> bool:
        
    if isinstance(Data, Student):
        Table_Name = "STUDENT"
    elif isinstance(Data, Teacher):
        Table_Name = "TEACHER"
    else:
        print("Type: Data error")
        return
        
    Execute(f"""
                    INSERT INTO {Table_Name}(ID, Name, PhoneNumber, Class)
                    VALUES({Data.ID}, "{Data.Name}", {Data.PhoneNumber}, {Data.Class});
                    """)

def Get(Table_Name, Return : str, Condition : str):
    # Execute the SELECT query
    _Cursor.execute(f"""SELECT {Return} FROM {Table_Name} {Condition};""")

    # Fetch all rows from the query
    rows = _Cursor.fetchall()
    RowsList = [list(row) for row in rows]

    return RowsList

def ShutDown() -> bool:
    global _Connection, _Cursor
 
    _Connection.close()
    _Cursor = None
    _Connection = None

    return _Cursor == None and _Connection == None

def Clear():
    Execute("DELETE FROM TEACHER;")
    Execute("DELETE FROM STUDENT;")
    
