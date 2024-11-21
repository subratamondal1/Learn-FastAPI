import threading
import time


def summation_of_squares(x):
    sum_squares = 0
    for i in range(x):
        sum_squares += i**2
    print(sum_squares)


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    start = time.time()

    current_threads = []
    for i in range(5):
        t = threading.Thread(target=summation_of_squares, args=((i + 1) * 1000000,))
        t.start()
        current_threads.append(t)

    for t in current_threads:
        t.join()

    end = time.time()
    print(f"Time taken by Summation Squares: {end - start:.4f}")

    start = time.time()

    current_threads = []
    for i in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(i,))
        t.start()
        current_threads.append(t)

    for t in current_threads:
        t.join()

    end = time.time()
    print(f"Time taken by Sleep a Little: {end - start:.4f}")


if __name__ == "__main__":
    main()
