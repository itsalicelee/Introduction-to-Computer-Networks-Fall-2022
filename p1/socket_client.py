import socket
import time

with open('./client_log.txt', 'w') as logFile:
    logFile.write("The Client is running..\n")
    logFile.flush()

    # Configure the server IP with its corrosponding port number
    # Specify the TCP connection type and make connection to the server
    # TODO start
    HOST, PORT =
    # TODO end

    Testcase = open('./p1_testcase', 'r')
    TestcaseContents = Testcase.readlines()
    Testcase.close()

    # Write the information of HOST and PORT to the client_log.txt
    # TODO start
    # TODO end

    # Read test cases from p1_testcase
    # You can change the test case or create other test cases on your own
    for PreprossingLine in TestcaseContents:
        Line = PreprossingLine.strip()

        # For connection stability
        time.sleep(3)

        # Client sent the request to the server and receive the response from the server
        # TODO start
        # TODO end


    # Close the socket
    # TODO start
    # TODO end
logFile.close()
