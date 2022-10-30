import socket
from datetime import datetime
import math

def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))
    
def ceil(n):
    return int(-1 * n // 1 * -1)

def floor(n):
    return int(n // 1)

def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .0001: # example threshold
            return guess
        last_guess= guess

def perm(n, k):
    result = fact(n) / fact(n-k)
    return result


def calculate(s):
    if '*' in s:
        s = s.split('*')
        return float(s[0])*float(s[1])
    elif '/' in s:
        s = s.split('/')
        return float(s[0])/float(s[1])
    elif '+' in s:
        s = s.split('+')
        return float(s[0])+float(s[1])
    elif '-' in s:
        s = s.split('-')
        return float(s[0])-float(s[1])
    elif '!' in s:
        s = s.split('!')
        return fact(int(s[0]))
    elif 'ceil' in s:
        s = s.split()
        return ceil(float(s[1]))
    elif 'floor' in s:
        s = s.split()
        return floor(float(s[1]))
    elif 'sqrt' in s:
        s = s.split()
        return sqrt(float(s[1]))
    elif 'perm' in s:
        s = s.split()
        n = int(s[1])
        k = int(s[2])
        print(n, k)
        return perm(n, k)


with open('./server_log.txt', 'w') as logFile:
    # Specify the IP address and port number
    # (use "127.0.0.1" for localhost on local machine)
    # Create a socket and bind the socket to the address
    # TODO start
    HOST, PORT = "127.0.0.1", 4047
    # HOST, PORT = "140.112.42.104", 7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    # TODO end

    while True:
        # Listen to any request
        # TODO start
        s.listen(0)
        # TODO end

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()

        while True:
            try:
                # Accept a new request
                # TODO start
                Client, Addr = s.accept()
                # TODO end

                while True:
                    Client.send(b"Received the message from server: Please input a question for calculation")
                    # Recieve the data from the client, and send the answer back to the client
                    # Ask if the client want to terminate the process
                    # Terminate the process or continue
                    # TODO start
                    message = Client.recv(4096).decode()
                    Client.send(("Question: " + message + "\n").encode())
                    # logFile.write("Question: " + message + "\n")
                    result = calculate(message)
                    Client.send(("Answer: " + str(result) + "\n").encode())
                    Client.send("Do you wish to continue? (Y/N)".encode())
                    message = Client.recv(4096).decode()
                    Client.send((message + "\n").encode())
                    logFile.write(message + "\n")
                    if(message == 'N'):
                        Client.close()
                        break    
                break
                # TODO end
            except ValueError:
                continue
        break
    logFile.close()
    # Close the socket
    # TODO start
    s.close()
    # TODO end
