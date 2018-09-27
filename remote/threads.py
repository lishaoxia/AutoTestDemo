from time import sleep,ctime
import threading

#音乐播放器
def music(name,loop):
    for i in range(loop):
        print("I was listening to %s! %s" %(name,ctime()))
        sleep(2)


#视频播放器
def movie(name,loop):
    for i in range(loop):
        print("I was at the  %s! %s" %(name,ctime()))
        sleep(5)

'''单线程
if __name__ == '__main__':
    music('一生何求',2)
    movie('精武门',2)
    print('all end:',ctime())
'''
#创建线程组
threads = []

#创建线程t1，并添加到线程组
t1 = threading.Thread(target=music,args=('一生何求',2))
threads.append(t1)

#创建线程t2，并添加到线程组
t2 = threading.Thread(target=movie,args=('精武门',2))
threads.append(t2)

if __name__ == '__main__':
    #启动线程
    for t in  threads:
        t.start()
    #守护线程，上面的循环结束后，所有的线程都启动了，但线程运行时间不确定，所以需要等待终止
    for t in threads:
        t.join()
    print('all end:',ctime())





















