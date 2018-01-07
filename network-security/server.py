#/usr/bin/python2
#coding=utf-8
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from Secure_comm import Secure_comm

sender = 'A'
receiver = 'B'
sec = Secure_comm(sender,receiver)

class MyProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        print 'Connection made from', self.transport.client
        # self.transport.client is client
        # self.transport.write(s) send s to client

    def dataReceived(self, data): # 当收到消息时触发此函数
        print 'Message from', self.transport.client, ':'
        data = data.strip()# 去除可能存在的多余空格和换行
        #sec = Secure_comm(sender,receiver)
        try:
            cipher_msg, cipher_key, sign_msg = data.split(':::')# 用规定的三个冒号分割开 AES加密后的消息，RSA加密后的key，消息签名
            key = sec.rsa_decrypt(cipher_key)# 先RSA解密得到AES加密用的key
            msg = sec.aes_decrypt(cipher_msg, key)# 再用key解密AES加密后的消息
            verify_result = Utils.verify_sign(msg, sign_msg)# 验证解密得到的消息是否符合签名
        except Exception:# 解密失败
            self.transport.write('fail')# 给客户端返回fail
            return
        print 'AES key:', key
        try:
            # 修正windows系统下可能存在的中文传输乱码
            msg = msg.decode('gb2312').encode('utf8')
        except UnicodeDecodeError:
            pass
        print 'Message:', msg
        print 'Verify:', verify_result
        if verify_result:# 如果签名认证通过给客户端返回success
            self.transport.write('success')
        else:# 否则返回fail
            self.transport.write('fail')

    def connectionLost(self, reason):
        print 'Lost connection of', self.transport.client

class MyFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        """
        Called when new client connect
        """
        return MyProtocol(self)


def main():
    factory = MyFactory()
    reactor.listenTCP(23333, factory)
    reactor.run()


if __name__ == '__main__':
    main()
