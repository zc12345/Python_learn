#/usr/bin/python2
#coding=utf-8

import socket

def udp_connect(host, port, msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in msg:
        s.sendto(data,(host,port))
        print s.recv(1024)
    s.close()
    result = True
    return result

def tcp_connect(host, port, msg):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建socket
    #AF_INET指定使用IPv4协议，AF_INET6指定IPv6协议；SOCK_STREAM指定使用面向流的TCP协议
    s.connect((host, port))#建立连接
    data = send_recv(s, msg)
    s.close()
    result = save_data(data)
    return result

def send_recv(socket, msg):#发送和接收数据
    #socket.send(msg)#发送数据
    #================send_recv test
    data = socket.recv(1024)
    msg_test = ['hello', 'world', 'Siri']
    for msg_data in msg_test:
        socket.send(msg_data)
        print socket.recv(1024)
    socket.send('exit')
    #================send_recv test
    #================recv data
    #buffer = []#缓存区
    #while True:
    #    d = socket.recv(1024)
    #    if d:
    #        buffer.append(d)
    #    else:
    #        break#一次只接受1kb数据，直到返回空数据，接收完毕
    #data = ''.join(buffer)
    #================recv data
    return data

def save_data(data):
    header, html = data.split('\r\n\r\n',1)
    with open('test.html','wb') as file:
        file.write(html)
    return header

if __name__ == "__main__":
    #host = "www.sina.com.cn"
    #port = 80
    host = 'admin1'
    port = 9999
    #msg = 'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
    msg = 'test'
    result = udp_connect(host,port,msg)
    print result
