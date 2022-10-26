from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python proxy_server.py server_ip"\n[server_ip : It is the IP address of proxy server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
TCPServerSocket = socket(AF_INET, SOCK_STREAM)
# TODO start
HOST, PORT = "127.0.0.1", 4047
TCPServerSocket.bind((HOST, PORT))
TCPServerSocket.listen(0)
# TODO end

while True:
    # Strat receiving data from the client
    print('Ready to serve...')
    # TODO start
    TCPClientSocket, Addr = TCPServerSocket.accept()
    # TODO end
    print('Received a connection from:', Addr)

    # Receive request from the client
    # TODO start
    RecvMessage = TCPClientSocket.recv(2048).decode('utf-8')
    # TODO end
    print(RecvMessage)

    # Extract the filename from the given message
    if RecvMessage == "":
        RecvMessage = "/ /"
    print(RecvMessage.split()[1])
    Filename = RecvMessage.split()[1].partition("/")[2]
    print(Filename)
    FileExist = "false"
    FileToUse = "/" + Filename
    print(FileToUse)

    try:
        # Check whether the file exist in the cache
        f = open(FileToUse[1:], "r")
        DataInFile = f.readlines()
        FileExist = "true"

        # Proxy Server finds the file (cache hit) and generates a response message
        # Send the file back to the client
        TCPClientSocket.send(("HTTP/1.1 200 OK\r\n").encode('utf-8'))
        TCPClientSocket.send(("Content-Type:text/html\r\n\r\n").encode('utf-8'))
        # TODO start
        for i in range(0, len(DataInFile)):
            TCPClientSocket.send(DataInFile[i].encode('utf-8'))
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
                proxy_ip = sys.argv[1]
                try:
                    proxy_port = sys.argv[2]
                except:
                    proxy_port = 80
                SocketOnProxyServer.connect((proxy_ip, proxy_port))
                SocketOnProxyServer.sendall(RecvMessage.encode('utf-8'))
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
                buffer = b''
                while 1:
                    # receive data from web server
                    data = SocketOnProxyServer.recv(8192)
                    if (len(data) > 0):
                        buffer += data
                    else:
                        break
                # TODO end

                # Create a new copy in the cache for the requested file
                # Also send the response back to client socket and the corresponding file from cache
                TmpFile = open(Filename, "w")
                print("open the file successfully")
                # TODO start
                TCPClientSocket.send(buffer)
                TmpFile.write(buffer)
                TmpFile.close()
                
                # TODO end
            except:
                print("Illegal request")
            SocketOnProxyServer.close()
        else:
            # HTTP response message for file is not found
            # TODO start
            TCPClientSocket.send(("HTTP/1.1 404 Not Found\r\n").encode('utf-8'))
            TCPClientSocket.send(("Content-Type: text/html; charset=utf-8\r\n").encode('utf-8'))
            TCPClientSocket.send(("404 Not Found\r\n").encode('utf-8'))
            
            # TODO end

    # Close the client sockets
    TCPClientSocket.close()
    # break

# Close the server socket
# TODO start
TCPServerSocket.close()
# TODO end
