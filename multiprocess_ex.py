import multiprocessing
import time


def method(i):
    print(f"Entering {i}")
    time.sleep(i)
    print(f"Exiting {i}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=method, args=[2])
    p1.start()
    p1.join()
