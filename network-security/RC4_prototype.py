#/usr/bin/python2
#coding=utf-8
import hashlib, base64

def rc4(text, key = 'default-key', mode = "encode"):
    key = hashlib.md5(key).hexdigest()
    if mode == "decode":
        text = base64.b64decode(text)
    result = ''
    key_len = len(key)
    #1. init S-box
    box = list(range(256))#put 0-255 into S-box
    j = 0
    for i in range(256):#shuffle elements in S-box according to key
        j = (j + box[i] + ord(key[i%key_len]))%256
        box[i],box[j] = box[j],box[i]#swap elements
    #2. make sure all elements in S-box swapped at least once
    i = j = 0
    for element in text:
        i = (i+1)%256
        j = (j+box[i])%256
        box[i],box[j] = box[j],box[i]
        k = chr(ord(element) ^ box[(box[i]+box[j])%256])
        result += k
    if mode == "encode":
        result = base64.b64encode(result)
    return result

if __name__ == "__main__":
    
    key = "helloworld"
    text = "helloworld!\nstuID:1234567890 stuName:zc12345"
    ciphertext = rc4(text,key,'encode')
    print "==========ciphertext===========\n"+ciphertext
    plaintext = rc4(ciphertext,key,'decode')
    print "==========plaintext============\n"+plaintext
