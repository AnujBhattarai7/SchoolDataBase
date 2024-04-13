import Backend

if __name__ == "__main__":
    Backend.Init()
    
    print("Hello")

    Backend.Add("STUDENT", Backend.Student(1, "Anuj", 98088888, 1))
    print(Backend.Get("STUDENT", "ID, Name", "WHERE ID = 1"))
    print(Backend.Get("sqlite_master", "name", "WHERE type = 'table'"))

    Backend.Clear()

    Backend.ShutDown()
