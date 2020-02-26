
from Postgress import DataBaseManager
from ServerWebSocket import ServerWebSocket

def main():
    print("Starting...")

    db_manager = DataBaseManager("EMPLOYEE")
    #db_manager.drop_table()
    #db_manager.create_table()

    db_manager.print_table()
    server_web_socket = ServerWebSocket(db_manager)
    server_web_socket.start()

    print("Finished...")

if __name__ == "__main__":
    main()