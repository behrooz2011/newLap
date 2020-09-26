# import multiprocessing
# import time

# def worker():
#     """worker function"""
#     print 'Worker'
#     return

# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         print("multi running: ",i)
#         p = multiprocessing.Process(target=worker)
#         jobs.append(p)
#         p.start()

import multiprocessing

def worker(num):
    """thread worker function"""
    print('Worker:', num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
