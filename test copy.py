import concurrent.futures
import time


def do1(seconds):
    time.sleep(seconds)
    return str(seconds)


if __name__ == '__main__':
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        arr=list(range(5))
        f=executor.map(do1,arr)
        for result in f:
            print(result)

    finish = time.perf_counter()
    print(f'{finish - start} second')
