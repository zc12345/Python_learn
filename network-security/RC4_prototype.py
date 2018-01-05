#/usr/bin/python2
#coding=utf-8

def rc4(text, key, mode = "encode"):
    key_len = len(key)
    #1. init S-box
    box = range(256)#put 0-255 into S-box
    j = 0
    for i in range(256):#shuffle elements in S-box according to key
        j = (j + box[i] + ord(key[i%key_len]))%256
        box[i],box[j] = box[j],box[i]#swap elements
    #2. make sure all elements in S-box swapped at least once
    i= j = 0
    result = ''
    for element in text:
        i = (i+1)%256
        j = (j+box[i])%256
        box[i],box[j] = box[j],box[i]
        k = chr(ord(element) ^ box[(box[i]+box[j])%256])
        result += k
    return result

if __name__ == "__main__":
    
    key = "hello"
    text = "helloworld"
    ciphertext = rc4(key, text)
    print ciphertext
    plaintext = rc4(key, ciphertext)
    print plaintext
