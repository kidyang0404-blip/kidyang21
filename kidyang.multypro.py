import time
import multiprocessing

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n"% i)

if __name__ == "__main__":
    print("Start")
    start = time.time()

    processes = []

    for i in range(5):
        p = multiprocessing.Process(target = long_task)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print("End")

    print("걸린 시간:%.2f초"
                 % (end - start))
