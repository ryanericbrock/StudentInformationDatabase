# Import socket module
import socket

# Reserve Port 8080
port = 8080

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
# CHANGE TO INCLUDE YOUR SERVER ADDESS
client_socket.connect(('[server address]', port))

# Receive acknowledgement from server
print(client_socket.recv(1024).decode())

# Keep running until client ends program
while True:
    valid_inputs = ["add", "display", "delete", "exit"]

    # Keep asking for user input until valid input given
    while True:
        client_message_list = []
        print("Enter one of the following commands:")
        print('    "add": add student to database')
        print('    "display": display student information')
        print('    "delete": remove student from database')
        print('    "exit": exit the program')
        userSelection = input('Input: ')

        # Check for valid input
        if userSelection in valid_inputs:
            client_message_list.append(userSelection)
            break
        else:
            print("\nInvalid input. Try again!\n")
    
    # Handle client message
    print()
    if client_message_list[0] == "add":
        client_message_list.append(input("Enter Student's ID: "))
        client_message_list.append(input("Enter Student's First Name: "))
        client_message_list.append(input("Enter Student's Last Name: "))
        client_message_list.append(input("Enter Student's Score: "))
    elif client_message_list[0] == "display":
        print("Enter one of the following commands:")
        print('    "id": dispaly student with matching ID')
        print('    "score": display all students above score')
        print('    "all": display all students')
        client_message_list.append(input("Input: "))
        if client_message_list[1] == "id":
            client_message_list.append(input("\nEnter Student's ID to display: "))
        elif client_message_list[1] == "score":
            client_message_list.append(input("\nEnter Score to display: "))
        else:
            client_message_list.append("all")
    elif client_message_list[0] == "delete":
        client_message_list.append(input("Enter Student's ID to remove: "))
    else:
        break

    # Send client message to server
    client_message = "-".join(client_message_list)
    client_socket.send(client_message.encode())

    # Receive and display server response
    print()
    print(client_socket.recv(1024).decode())

# Close connection
client_socket.send("end".encode())
client_socket.close()
