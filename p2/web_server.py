from socket import *

# Note: After finishing the program, try to type http://HOST:PORT/index.html in your browser for test
# http://127.0.0.1:4047/index.html
# http://127.0.0.1:4046/index.html

ServerSocket = socket(AF_INET, SOCK_STREAM)
# Create a socket and bind the socket to the address
# TODO start
HOST = "127.0.0.1"
PORT = 4046
ServerSocket.bind((HOST, PORT))
ServerSocket.listen(0)
# TODO end

while True:
    print('Ready to serve...')

    # Establish the connection
    # TODO start
    ConnectionSocket, Addr = ServerSocket.accept()
    print(str(Addr) + "connected")
    # TODO end

    try:
        # Receive a HTTP request from the client
        # TODO start
        RecvMessage = ConnectionSocket.recv(4096).decode()
        print("RecvMsg: ", RecvMessage)
        # TODO end

        if RecvMessage == "":
            RecvMessage = "/ /"

        FileName = RecvMessage.split()[1]
        print(FileName)
        f = open(FileName[1:])

        # Read data from the file that the client requested
        # Split the data into lines for further transmission
        # TODO start
        DataInFile = f.read()
        # TODO end

        # Send one HTTP header line into socket
        # Send HTTP Status to the client
        # TODO start
        header = b'HTTP/1.1 200 OK\r\n'
        ConnectionSocket.send(header)
        # TODO end

        # Send the Content Type to the client
        # TODO start
        contentType = b'Content-Type: text/html; charset=UTF-8\n\n'
        ConnectionSocket.send(contentType)
        # TODO end

        # Send the content of the requested file to the client
        for i in range(0, len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode())
        ConnectionSocket.send("\r\n".encode())

        ConnectionSocket.close()
    except IOError:
        # Send the response message if the file is not found
        # TODO start
        print("404 Not Found")
        ConnectionSocket.send(b'HTTP/1.1 404 Not Found\r\n')
        ConnectionSocket.send(b'Content-Type: text/html; charset=utf-8\r\n')
        ConnectionSocket.send(b'404 Not Found\r\n')
        # TODO end

        # Close client socket
        # TODO start
        ConnectionSocket.close()
        # TODO end
ServerSocket.close()

