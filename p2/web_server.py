from socket import *

# Note: After finishing the program, try to type http://HOST:PORT/index.html in your browser for test

ServerSocket = socket(AF_INET, SOCK_STREAM)
# Create a socket and bind the socket to the address
# TODO start
# TODO end

while True:
    print('Ready to serve...')

    # Establish the connection
    # TODO start
    ConnectionSocket, Addr =
    # TODO end

    try:
        # Receive a HTTP request from the client
        # TODO start
        RecvMessage =
        # TODO end

        if RecvMessage == "":
            RecvMessage = "/ /"

        FileName = RecvMessage.split()[1]
        print(FileName)
        f = open(FileName[1:])

        # Read data from the file that the client requested
        # Split the data into lines for further transmission
        # TODO start
        DataInFile =
        # TODO end

        # Send one HTTP header line into socket
        # Send HTTP Status to the client
        # TODO start
        # TODO end

        # Send the Content Type to the client
        # TODO start
        # TODO end

        # Send the content of the requested file to the client
        for i in range(0, len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode())
        ConnectionSocket.send("\r\n".encode())

        ConnectionSocket.close()
    except IOError:
        # Send the response message if the file is not found
        # TODO start
        # TODO end

        # Close client socket
        # TODO start
        # TODO end

