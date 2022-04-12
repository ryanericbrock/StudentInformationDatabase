# Introduction
The Student Information Database is a project that I created for CS 4310 (Computer Networks) to demonstrate knowledge on how to create client-server applications using Python. This project demonstrates the foundational knowledge of using sockets to establish a TCP connection between a client and server applicaiton. As such, the functionality is limited to adding, removing, and viewing the students in the database. For simplicity, a .csv file was used to store student information instead of an actual database; the .csv file is pre-loaded with three students for testing purposes.

# Requirements
This project does not require any modules outside of the included Python3 modules.

# Installation
Make sure all files have been downloaded. No additional downloads or installations are required outside of the provided files and Python3. Run the server.py file on your server device and client.py on your client device. Make sure to change the following line of code to include the server address that the server.py file is being hosted on.
> client_socket.connect(('[server address]', port))
