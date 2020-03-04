
from Postgress import DataBaseManager
from ServerWebSocket import ServerWebSocket
from Postgis import DataBaseManagerWithGeo

USE_POSTGRESS = 0
DROP_TABLE = 0
CREATE_TABLE = 0

def main():
    print("Starting...")

    if USE_POSTGRESS:
        db_manager = DataBaseManager("EMPLOYEE")
    else:
        db_manager = DataBaseManagerWithGeo("EMPLOYEE")

    if DROP_TABLE:
        db_manager.drop_table()

    if CREATE_TABLE:
        db_manager.create_table()


    #db_manager.add_emloyee("a", "a", 30, "M", 1000, "0 0, 10 10, 50 10, 0 0")
    #db_manager.add_emloyee("b", "b", 30, "M", 500,  "10 10, 10 20, 30 20, 30 30, 10 10")
    db_manager.print_table()

    #server_web_socket = ServerWebSocket(db_manager)
    #server_web_socket.start()


    print("Finished...")
    db_manager.close_db()

if __name__ == "__main__":
    main()