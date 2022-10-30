from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python proxy_server.py server_ip"\n[server_ip : It is the IP address of proxy server')
    sys.exit(2)

# Proxy server: 127.0.0.1:5000
# http://127.0.0.1:5000/index.html

# Create a server socket, bind it to a port and start listening
TCPServerSocket = socket(AF_INET, SOCK_STREAM)
# TODO start
# proxy server ip and port
HOST, PORT = sys.argv[1], 8000
print(HOST, PORT)
TCPServerSocket.bind((HOST, PORT))
TCPServerSocket.listen(100)
# TODO end

while True:
    # Strat receiving data from the client
    print('Ready to serve...')
    # TODO start
    TCPClientSocket, Addr = TCPServerSocket.accept()
    # TODO end
    print('Received a connection from:', Addr)

    # Step1: Receive request from the client
    # TODO start
    RecvMessage = TCPClientSocket.recv(4096).decode()
    # TODO end
    

    # Extract the filename from the given message
    if RecvMessage == "":
        RecvMessage = "/ /"
    print("Recv Message: ", RecvMessage.split()[1])
    Filename = RecvMessage.split()[1].partition("/")[2]
    print("Filename:", Filename)
    FileExist = "false"
    FileToUse = "/" + Filename
    print("FileToUse:", FileToUse)

    try:
        # Check whether the file exist in the cache
        f = open(FileToUse[1:], "r")
        DataInFile = f.readlines()
        f.close()
        FileExist = "true"

        # Proxy Server finds the file (cache hit) and generates a response message
        # Send the file back to the client
        TCPClientSocket.send(("HTTP/1.1 200 OK\r\n").encode('utf-8'))
        TCPClientSocket.send(("Content-Type:text/html\r\n\r\n").encode('utf-8'))
        # TODO start
        for i in range(0, len(DataInFile)):
            TCPClientSocket.send(DataInFile[i].encode())
        TCPClientSocket.send("\r\n".encode())
        # TODO end

        print('Read from cache')

    # Error handling if the file is not found in cache
    except IOError:
        if FileExist == "false":
            # Create a socket on the proxy server
            # TODO start
            SocketOnProxyServer = socket(AF_INET, SOCK_STREAM)
            # TODO end
            HostName = Filename.replace("www.", "", 1)
            print("host name is " + HostName)
            try:
                print("try to connect to the web_server")
                # Connect the socket to the web server port
                # TODO: start
                SocketOnProxyServer.connect(("127.0.0.1", 4047))
                # TODO end
                print("connected successfully")

                # Create a temporary file based on this socket
                FileObject = SocketOnProxyServer.makefile('rw', None)
                print("GET " + "http://" + FileToUse + " HTTP/1.1\r\n")
                FileObject.write("GET " + FileToUse + " HTTP/1.1\r\n")
                FileObject.flush()
                print("get the file successfully")

                # Read the response into buffer
                # TODO start
                buffer = FileObject.readlines()
                print("Buffer: ", buffer)
                # TODO end

                # Create a new copy in the cache for the requested file
                # Also send the response back to client socket and the corresponding file from cache
                TmpFile = open(Filename, "w")
                print("open the file successfully")
                # TODO start
                for i in range(len(buffer)):
                    if i <= 1:
                        TCPClientSocket.send(buffer[i].encode())
                    else:
                        TmpFile.write(buffer[i])
                TmpFile.close()
                print("Done")
                # TODO end
            except:
                print("Illegal request")
            
        else:
            # HTTP response message for file is not found
            # TODO start
            print("404 Not Found")
            TCPClientSocket.send(b"HTTP/1.1 404 Not Found\r\n")
            TCPClientSocket.send(b"Content-Type: text/html; charset=utf-8\r\n")
            TCPClientSocket.send(b"404 Not Found\r\n")
            TCPClientSocket.send(b"\r\n")
            
            # TODO end

    # Close the client sockets
    TCPClientSocket.close()
    # break

# Close the server socket
# TODO start
TCPServerSocket.close()
# TODO end
