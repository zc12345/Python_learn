#/usr/bin/python2
#coding=utf-8

import socket, time, threading

def tcp_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))#绑定IP地址
    s.listen(5)#监听端口，指定最大连接数
    print 'Waiting for connections......'
    while True:
        sock, addr = s.accept()#接受一个新连接
        t = threading.Thread(target = tcplink, args = (sock, addr))#创建新线程处理TCP连接
        t.start()

def tcplink(sock, addr):
    print 'Accept new connection from %s :%s......' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s~'%data)
    sock.close()
    print 'Connection from %s :%s closed~' % addr

if __name__ == "__main__":
    #host = '127.0,0.1'
    host = socket.gethostname()
    print host
    port = 9999
    tcp_server(host,port)
