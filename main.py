import socket

if __name__ == "__main__":

    s = socket.socket()
    host = socket.gethostname()
    port = 13377
    s.bind((host,port))
    #figure out how to make this always.
    s.listen(15)
    
    while True:
        #when you accept a connection print out "hello there", then close
        c, addr = s.accept()
        data = "hello there"
        c.send(data.encode())
        #add code to read some data from client
        #add data to save that data to a database
        #close the connection
        c.close()
