#/usr/bin/python2
#coding=utf-8

import socket
from Secure_comm import Secure_comm

#HOST = '120.78.148.77'
#PORT = 8888

def Sender(sender, receiver, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPv4 & TCP
    msg = raw_input("Message:")
    key = raw_input("AES key:")
    sec = Secure_comm(sender, receiver)
    ciphermsg = sec.aes_encrypt(msg,key)
    cipherkey = sec.rsa_encrypt(key)
    signature = sec.sign(msg)
    text = ciphermsg + ":::" + cipherkey + ":::" + signature
    print "Connecting......"
    print text
    try:
        s.connect((host, port))
        print "Success connected"
        s.send(text)
        print "Sending Messages......\n",text
        data = s.recv(1024)
        print "Received Result:\n",data
    except Exception:
        print "Failed......"
    s.close()

def test(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPv4 & TCP
    print "Connecting......"
    s.connect((host, port))
    print "Success..."

if __name__ == "__main__":
    sender = 'A'
    receiver = 'B'
    host = '120.78.148.77'
    port = 23333
    Sender(sender, receiver, host, port)
    #test(host,port)
