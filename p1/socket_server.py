import socket
from datetime import datetime

with open('./server_log.txt', 'w') as logFile:
    # Specify the IP address and port number
    # (use "127.0.0.1" for localhost on local machine)
    # Create a socket and bind the socket to the address
    # TODO start
    HOST, PORT =
    # TODO end

    while True:
        # Listen to any request
        # TODO start
        # TODO end

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()

        while True:
            try:
                # Accept a new request
                # TODO start
                Client, Addr =
                # TODO end

                while True:
                    Client.send(b"Please input a question for calculation")
                    # Recieve the data from the client, and send the answer back to the client
                    # Ask if the client want to terminate the process
                    # Terminate the process or continue
                    # TODO start
                    # TODO end
            except ValueError:
                continue
        break
    logFile.close()
    # Close the socket
    # TODO start
    # TODO end
