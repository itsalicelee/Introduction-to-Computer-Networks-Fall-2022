import socket
import time

with open('./b07303024_p1_client_result.log', 'w') as logFile:
    logFile.write("The Client is running..\n")
    logFile.flush()

    # Configure the server IP with its corrosponding port number
    # Specify the TCP connection type and make connection to the server
    # TODO start
    HOST, PORT = "127.0.0.1", 4047
    # HOST, PORT = "140.112.42.104", 7777
    client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_s.connect((HOST, PORT))
    # TODO end

    Testcase = open('./p1_testcase', 'r')
    TestcaseContents = Testcase.readlines()
    Testcase.close()

    # Write the information of HOST and PORT to the client_log.txt
    # TODO start
    logFile.write("Connect to {}, using port number {}\n".format(HOST, PORT))
    # TODO end

    # Read test cases from p1_testcase
    # You can change the test case or create other test cases on your own
    for PreprossingLine in TestcaseContents:
        
        Line = PreprossingLine.strip()

        # For connection stability
        time.sleep(3)

        # Client sent the request to the server and receive the response from the server
        # TODO start
        client_s.send(Line.encode())
        msg = client_s.recv(1024)
        logFile.write(msg.decode() + "\n")
        # TODO end


    # Close the socket
    # TODO start
    logFile.write("N\n")
    client_s.close()
    # TODO end
logFile.close()
