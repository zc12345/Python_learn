#!/usr/bin/env python3
# -*- coding:utf-8 -*-
r'''
This program is just for fun.
'''
# 添加时间戳
from records import get_history
import time
ISOTIMEFORMAT = "%Y-%m-%d %X"
current = time.strftime(ISOTIMEFORMAT,time.localtime())

# 初始化得分情况
score = 0
print("对抗世间无聊！\n 2333333333 \n 加油吧，骚年！")

#1. 学习时间

study_time = int (input('1.1 今天学习了多少分钟？（forest记录和手机使用记录为证）\n'))
if study_time > 960:
    print("少年郎，你是连觉都没睡？")
    study_time = int (input("还不从实招来，究竟学了几分钟？\n"))
elif study_time < 120:
    print("骚年你今天究竟都干了什么？看小说？打游戏？")

recite_words = int (input("1.2 今天背了多少单词？\n"))
codes = int (input("1.3 今天写了多少行代码？\n"))
score = score + study_time/10 + recite_words/5 + codes/10

#2. 其他得分
# 2.1 跑步
steps = int (input("2.1 今天走了多少步？\n"))
run_miles = int (input("2.2 今天跑了多少公里？\n"))
score = score + steps/500 + run_miles*5
# 2.2 作息
breakfeast = int (input("3.1 今天吃早饭了吗？\n1.吃了 0.没吃\n"))
lunch = int (input("3.2 今天在13:00之前吃完午饭了吗？\n1.是 0.否\n"))
supper = int (input("3.3 今天在19:30之前吃完晚饭了吗？\n1.是 0.否\n"))
getup = int (input("3.4 今天在08:00之前起床了吗？\n1.是 0.否\n"))
sleep = int (input("3.5 今天在01:00之前睡觉了吗？\n1.是 0.否\n"))
score = score + (breakfeast + lunch + supper + getup + sleep)*2

my_dict = {"study_time":study_time,"recite_words":recite_words,"codes":codes,
"steps":steps,"run_miles":run_miles,
"breakfeast":breakfeast,"lunch":lunch,"supper":supper,
"getup":getup,"sleep":sleep,"score":score}

print("="*50)
print("今日总得分\t %0.2f"% (score))
print("+"*50) #分割线
# 读取历史记录
get_history()
# 输出到文件中
# w,w+模式表示覆盖写，a+表示追加写
with open("score.txt","a+") as f:
    print("%0.2f\trecord time:%s\tdetails:%s" % (score,current,my_dict),file=f)

stop = input("按Enter键关闭")