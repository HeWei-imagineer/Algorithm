#关于递归函数问题:
def move_one(num,init,des):
    print('move '+str(num)+' from '+init+' to '+des)
    print('---------------------------------')
def hanoi(num,init,temp,des):
    if num==1:
        move_one(num,init,des)
    else:
        hanoi(num-1,init,des,temp)
        move_one(num,init,des)
        hanoi(num-1,temp,init,des)

# 一件很难的事，我可以完成其中一小步，剩下的交给第二个人做。
# 第二个人接到任务时，想我可以完成其中一小步，剩下的交给第三个人做。...
# 直到任务最后被分解成简单的一小步。