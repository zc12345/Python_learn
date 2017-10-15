# get history records
def get_history():        
    print("历史得分记录")
    with open("score.txt","r") as file_history:
        i = 0 #记录天数
        for line in file_history:
            print("第%d天" % (i),line)
            i = i + 1

    print("="*50)