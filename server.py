# Import statements
import socket
import csv

# Reserve port 8080
port = 8080

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created!")

# Bind pocket to port
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', port))
print("Socket bound to port", port)

# Listen for incoming connections
server.listen()
print("Socket is listening!")

# Run server until interrupted
while True:
    # Accept connection with client
    conn, addr = server.accept()
    print("Got connection from", addr)

    # Send acknowledgement to client
    conn.send("Connected to server!".encode())

    # Run connection until client ends it
    while True:
        # Default server message
        server_message = ""

        # Receive message
        client_message = conn.recv(1024).decode()
        client_message_list = client_message.split("-")

        # Handle client message
        if client_message_list[0] == "end":
            print(str(addr) + " has disconnected")
        elif client_message_list[0] == "add":
            row = client_message_list[1:]
            with open('students.csv', 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(row)
            server_message = " | ".join(row) + "  added!\n"
        elif client_message_list[0] == "display":
            # Read students from csv file to list of tuples
            with open('students.csv') as file:
                csv_reader = csv.reader(file)
                rows = [tuple(row) for row in csv_reader]

            # Check method client chose for displaying students
            if client_message_list[1] == "id":
                for row in rows:
                    if row[0] == client_message_list[2]:
                        server_message = " | ".join(row) + "\n"
            elif client_message_list[1] == "score":
                server_message = ""
                for row in rows:
                    if int(row[3]) > int(client_message_list[2]):
                        server_message += " | ".join(row) + "\n"
            else:
                server_message = ""
                for row in rows:
                    server_message += " | ".join(row) + "\n"

            # Check if any students found
            if server_message == "":
                server_message = "No matching students found!\n"
        elif client_message_list[0] == "delete":
            rows = []
            with open('students.csv', 'r') as file:
                csv_reader = csv.reader(file)
                rows = [tuple(row) for row in csv_reader]
                for row in rows:
                    if row[0] == client_message_list[1]:
                        rows.remove(row)
            with open('students.csv', 'w') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)
            server_message = "Student removed!\n"
        else:
            break
    
        # Send server response:
        try:        
            conn.send(server_message.encode())
        except:
            conn.send("ERROR!\n")

    # Close connection
    conn.close()
