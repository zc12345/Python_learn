#/usr/bin/python2
#coding=utf-8
import sys,os,hashlib,time,base64

class rc4:
    '''
    RC4算法的python实现
    '''
    def __init__(self,public_key = None,ckey_lenth = 16):
        self.ckey_lenth = ckey_lenth#IV长度
        self.public_key = public_key or 'none_public_key'
        key = hashlib.md5(self.public_key).hexdigest()
        self.keya = hashlib.md5(key[0:16]).hexdigest()
        self.keyb = hashlib.md5(key[16:32]).hexdigest()
        self.keyc = ''
        self.result = ''
    
    def encode(self,string):
        self.keyc = hashlib.md5(str(time.time())).hexdigest()[32 - self.ckey_lenth:32]
        string = '0000000000' + hashlib.md5(string + self.keyb).hexdigest()[0:16] + string#增加的字符串用于下面验证完整性和时间戳
        self.result = ''
        self.docrypt(string)
        return self.keyc + base64.b64encode(self.result)#IV+密文
        
    def decode(self,string):
        self.keyc = string[0:self.ckey_lenth]
        string = base64.b64decode(string[self.ckey_lenth:])
        self.result = ''
        self.docrypt(string)
        result = self.result
        if (result[0:10] == '0000000000' or int(result[0:10]) - int(time.time()) > 0) and result[10:26] == hashlib.md5(result[26:] + self.keyb).hexdigest()[0:16]:#result[0:10]完整性检验;result[10:26]时间戳检验
            return result[26:]
        else:
            return None
        
    def docrypt(self,string):
        string_lenth = len(string)
        result = ''
        box = list(range(256))
        randkey = []
        
        cryptkey = self.keya + hashlib.md5(self.keya + self.keyc).hexdigest()
        key_lenth = len(cryptkey)
        #1. init S-box
        for i in xrange(255):
            randkey.append(ord(cryptkey[i % key_lenth]))
        #2. shuffle S-box
        for i in xrange(255):
            j = 0
            j = (j + box[i] + randkey[i]) % 256
            box[i], box[j] = box[j],box[i]#swap
        #3. make sure every element swapped at least once
        a = j = 0
        for i in xrange(string_lenth):
            a = (a + 1) % 256
            j = (j + box[a]) % 256
            box[a], box[j] = box[j], box[a]#swap
            self.result += chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))
        return self.result

if __name__=="__main__":
    
    key = 'helloworld'
    rc = rc4(key)
    plaintext = 'stuid:1234567890 stuname:ssh'
    ciphertext = rc.encode(plaintext)
    decodetext = rc.decode(ciphertext)
    print 'ciphertext:'+ciphertext
    print 'plaintext:'+decodetext
