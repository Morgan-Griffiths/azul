from multiprocessing import Pool, Manager,Value,Lock
import time
import random

def chrome_login_wait(args):
    wait_time, stop_flag,pid,lock = args
    # calls function to login to chrome
    time.sleep(wait_time)
    with lock:
        if stop_flag.value == True:
            return 'stop'
    # click button
    # check result
    result = random.randint(0, 1)
    print('result',pid, result)
    if result:
        return 'stop'
    return 'success'


if __name__ == "__main__":
    N = 5

    wait_times = list(range(1, 5))

    with Manager() as manager:
        stop_flag = manager.Value('i', False)
        lock = manager.Lock()
        with Pool(processes=N) as pool:
            results = []
            for result in pool.imap_unordered(chrome_login_wait, [(wait, stop_flag,i,lock) for i,wait in enumerate(wait_times)]):
                if result == 'stop':
                    with lock:
                        stop_flag.value = True
                results.append(result)

    # Check if any process returned 'stop'
    print(results)
