import queue
import threading
import time

"""
1. Створити по 2 об'єкти на черги та процеси, які б демонстрували їх функціональне призначення."""

def getTime():
    return time.strftime('%T', time.localtime())


qu = queue.Queue()


def Client():
    print(f'C - I am client. I sent transaction to server...')
    print(f'C oi! I need little time to do something ...')
    time.sleep(3)
    trs = list([10,100,20,20000,1,2,3,500,-1])
    for tr in trs:
        qu.put(tr)
        print(f'{getTime()} C Send tr {tr}')
    print(f'{getTime()} C Clint: End work! Go home! :-)')


def Server():
    print(f'S - I am server. I watch queue and process it...')
    while True:
        sum = qu.get()
        if sum < 0.01 or sum == 'q':
            print(f'{getTime()} S Quit received. Goodbye!')
            exit(0)
        elif sum > 1000:
            print(f'{getTime()} S Transaction {sum} too big. Reject it!')
            time.sleep(2)
        else:
            print(f'{getTime()} S Transaction {sum} ok. Approve it (authorize)!')


# ----------------------------

print(f"Hi, I am process. I starts at {getTime()}.")

t1 = threading.Thread(target=Server)
t2 = threading.Thread(target=Client)

t1.start()
t2.start()

t1.join()
t2.join()

print(f'I was kapellmeister. Bye!')
