# process : 실행 중인 프로그램을 의미한, 자신만의 메모리를 확보하고 공유하지 않음.
# thread : light weight process라고도 함. 하나의 process 내에는 한 개의 thread가 존재함
# process 내에 여러 개의 thread를 운영하여 여러 개의 작업을 '동시에 하는 것처럼' 느끼게 할 수 있다.
# multi thread로 multi tasking이 가능하다.


import threading, time

def run(id):
    for i in range(1, 51):
        print('id:{} --> {}'.format(id, i))
        time.sleep(0.2)
        
        
# thread를 사용하지 않은 경우
# run(1)
# run(2)


# thread를 사용한 경우 --> 스레드의 갯수는 메인스레드를 포함해야한다
# threading.Thread(target=수행함수명)
th1 = threading.Thread(target=run, args=('일',))
th2 = threading.Thread(target=run, args=('이',))
th3 = threading.Thread(target=run, args=('삼',))
th1.start()
th2.start()
th3.start()
th1.join()
th2.join() # join() - 스레드를 생성한 스레드를 진행하지않고, 일단 대기하고 다른스레드의 종료를 기다려주는 것
th3.join()
print('프로그램 종료')







