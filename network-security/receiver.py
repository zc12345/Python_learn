#/usr/bin/python2
#coding=utf-8

from Crypto import Random
from Crypto.Hash import SHA
from Secure_comm import Secure_comm
import socket, time, threading

def tcp_server(host, port, sender, receiver):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))#绑定IP地址
    s.listen(5)#监听端口，指定最大连接数
    print 'Waiting for connections......'
    while True:
        sock, addr = s.accept()#接受一个新连接
        t = threading.Thread(target = tcplink, args = (sock, addr, sender, receiver))#创建新线程处理TCP连接
        t.start()

def tcplink(sock, addr, sender, receiver):
    print 'Accept new connection from %s :%s......' % addr
    sock.send('Got it!')
    buffer = []
    while True:
        d = sock.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = ''.join(buffer)
    result = data_process(sender,receiver,data)
    sock.send(str(result))
    sock.close()
    print 'Connection from %s :%s closed~' % addr

def data_process(sender, receiver, data):
    data = data.strip()# 去除可能存在的多余空格和换行
    sec = Secure_comm(sender,receiver)
    try:
        cipher_msg, cipher_key, sign_msg = data.split(':::')# 用规定的三个冒号分割开 AES加密后的消息，RSA加密后的key，消息签名
        key = sec.rsa_decrypt(cipher_key)# 先RSA解密得到AES加密用的key
        msg = sec.aes_decrypt(cipher_msg, key)# 再用key解密AES加密后的消息
        verify_result = sec.verify_sign(msg, sign_msg)# 验证解密得到的消息是否符合签名
    except Exception:# 解密失败
        result = 'Failed to encrypt~'# 给客户端返回fail
        return False
    print 'AES key:', key
    #try:
    #    # 修正windows系统下可能存在的中文传输乱码
    #    msg = msg.decode('gb2312').encode('utf8')
    #except UnicodeDecodeError:
    #    pass
    print 'Message:', msg
    print 'Verify:', verify_result
    result = [msg, key, verify_result]
    return True

if __name__ == '__main__':
    sender = 'A'
    receiver = 'B'
    host = 'admin1'
    port = 23333 
    tcp_server(host, port, sender, receiver)
