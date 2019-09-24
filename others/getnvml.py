#!/usr/bin/python3
# -*- coding: utf-8 -*- 

from pynvml import *
import datetime
import time
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header  

def get_info():
    nvmlInit()#初始化
    print("Driver: ", nvmlSystemGetDriverVersion())  #显示驱动信息
    
    #查看设备
    deviceCount = nvmlDeviceGetCount()
    while True:
        for i in range(deviceCount):
            handle = nvmlDeviceGetHandleByIndex(i)
            print("GPU", i, ":", nvmlDeviceGetName(handle))
            #查看显存、温度、风扇、电源
            handle = nvmlDeviceGetHandleByIndex(i)
            info = nvmlDeviceGetMemoryInfo(handle)
            memory_util_rate = 100 * info.used / info.total
            gpu_util_rate = nvmlDeviceGetUtilizationRates(handle).gpu
            gpu_io_rate = nvmlDeviceGetUtilizationRates(handle).memory
            print("Memory Used Rate: ",memory_util_rate,'%')
            print("GPU Used Rate: ",gpu_util_rate,'%')
            print("GPU IO Rate: ",gpu_io_rate,'%')
            print("Temperature is %d C"%nvmlDeviceGetTemperature(handle,0))
            print("Power ststus",nvmlDeviceGetPowerState(handle))
            if memory_util_rate < 10 and gpu_util_rate < 10:
                #最后要关闭管理工具
                nvmlShutdown()
                return i, memory_util_rate, gpu_util_rate
        time.sleep(10)

def sendemail(subject_content, msg_content, password):
    #设置smtplib所需的参数
    #下面的发件人，收件人是用于邮件传输的。
    smtpserver = 'smtp.163.com'
    username = '18292885866@163.com'
    sender = '18292885866@163.com'
    receiver = ['18292885866@163.com']
    
    subject=Header(subject_content, 'utf-8').encode()
    
    #构造邮件对象MIMEMultipart对象
    #下面的主题，发件人，收件人，日期是显示在邮件页面上的。
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = '18292885866@163.com <18292885866@163.com>'
    #收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = ";".join(receiver) 
    msg['Date']= datetime.datetime.now().strftime('%Y-%m-%d')
    
    #构造文字内容   
    text = msg_content
    text_plain = MIMEText(text,'plain', 'utf-8')    
    msg.attach(text_plain)  
           
    #发送邮件
    smtp = smtplib.SMTP()    
    smtp.connect('smtp.163.com')
    #我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    #smtp.set_debuglevel(1)  
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()
    print("send sucessfully.")
    
    
if __name__ == "__main__":
    password = getpass.getpass("Please input password:")
    i, memory_util_rate, gpu_util_rate = get_info()
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = nowTime + "\ngpu " + str(i) + ";\nmemory_util_rate: " + str(int(memory_util_rate)) + "%;\ngpu_util_rate: " + str(gpu_util_rate) + "%"
    subject = "GPU is available now."
    sendemail(subject, msg, password)
