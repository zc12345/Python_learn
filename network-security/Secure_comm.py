#/usr/bin/python2
#coding=utf-8

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, DES
from RC4_prototype import rc4
import base64, hashlib

class Secure_comm:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.iv = '\x00'*16

    def gen_key(self, name):
        random_generator = Random.new().read
        key = RSA.generate(2048, random_generator)
        private = key.exportKey()
        public = key.publickey().exportKey()
        keylist = [private, public]
        with open(name + '-private.pem', 'w') as file:
            file.write(private)
        with open(name + '-public.pem', 'w') as file:
            file.write(public)
        return keylist

    def sign(self,msg):
        '''
        param msg: message
        return: SHA1 signature
        '''
        with open(self.sender + '-private.pem') as file:
            key = file.read()
            rsa_key = RSA.importKey(key)
            signer = Signature_pkcs.new(rsa_key)
            digest = SHA.new()
            digest.update(msg)
            sign = signer.sign(digest)
            signature = base64.b64encode(sign)
        return signature

    def verify_sign(self, msg, signature):
        '''
        param msg: msg to be verified
        param signature: SHA1 signature(base64 encoded)
        return: true/false
        '''
        with open(self.sender + '-public.pem') as file:
            key = file.read()
            rsa_key = RSA.importKey(key)
            verifier = Signature_pkcs.new(rsa_key)
            digest = SHA.new()
            digest.update(msg)
            is_verified = verifier.verify(digest,base64.b64decode(signature))
        return is_verified

    def rsa_encrypt(self, plaintext):
        with open(self.sender + '-public.pem') as file:
            key = file.read()
            rsa_key = RSA.importKey(key)
            cipher = Cipher_pkcs.new(rsa_key)
            ciphertext = base64.b64encode(cipher.encrypt(plaintext))
        return ciphertext

    def rsa_decrypt(self, ciphertext):
        with open(self.sender + '-private.pem') as file:
            key = file.read()
            rsa_key = RSA.importKey(key)
            cipher = Cipher_pkcs.new(rsa_key)
            plaintext = cipher.decrypt(base64.b64decode(ciphertext), Random.new().read)
        return plaintext

    def aes_encrypt(self, plaintext, key = ('0'*32)):
        if len(key)<32 :
            key += '\x00'*(32-len(key))
        pad = 16 - len(plaintext)%16
        plaintext += chr(pad) * pad #加入保证消息长度为16*n
        if len(key) == 16 or len(key) == 24 or len(key) == 32:
            aes = AES.new(key, AES.MODE_CBC, self.iv)
            ciphertext = base64.b64encode(aes.encrypt(plaintext))
            return ciphertext
        else:
            print "Error: key length error"
            return None

    def aes_decrypt(self, ciphertext, key = ('0'*32)):
        if len(key)<32 :
            key += '\x00'*(32-len(key))
        ciphertext = base64.b64decode(ciphertext)
        if len(key) == 16 or len(key) == 24 or len(key) == 32:
            aes = AES.new(key, AES.MODE_CBC, self.iv)
            plaintext = aes.decrypt(ciphertext)
            return plaintext[:-ord(plaintext[-1])]#移除padding
        else:
            print "Error: key length error"
            return None

    def des_encrypt(self, plaintext, key = ('0'*8)):
        if len(key)<8 :
            key += '\x00'*(8-len(key))
        pad = 8 - len(plaintext)%8
        plaintext += chr(pad) * pad #加入保证消息长度为8*n
        key = key[0:8] #保证密钥长度为8
        des = DES.new(key, DES.MODE_ECB)
        ciphertext = base64.b64encode(des.encrypt(plaintext))
        return ciphertext

    def des_decrypt(self, ciphertext, key = ('0'*8)):
        if len(key)<8 :
            key += '\x00'*(8-len(key))
        key = key[0:8] #保证密钥长度为8
        ciphertext = base64.b64decode(ciphertext)
        des = DES.new(key, DES.MODE_ECB)
        plaintext = des.decrypt(ciphertext)
        return plaintext[:-ord(plaintext[-1])]#移除padding


if __name__ == "__main__":
    sender = 'A'
    receiver = 'B'
    key = "helloworld"
    msg = "stuID=1234567890--stuName=zc12345"
    sec = Secure_comm(sender, receiver)
    #key_sender = sec.gen_key(sender)
    #key_receiver = sec.gen_key(receiver)
    sign = sec.sign(msg)
    #print sign
    verify = sec.verify_sign(msg,sign)
    #print verify
    ciphertext = sec.des_encrypt(msg, key)
    print ciphertext
    plaintext = sec.des_decrypt(ciphertext, key)
    print plaintext
    
