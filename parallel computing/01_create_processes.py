import multiprocessing
import time


def do_work():
    """CPU BOUND TASK"""
    print("Starting work...")
    i = 0
    for _ in range(100000000):
        i += 1
    print("Finished work!\n")


if __name__ == "__main__":
    try:
        multiprocessing.set_start_method("spawn")
    except RuntimeError:
        pass  # The start method has already been set, so we ignore the error

    start = time.time()
    for i in range(1, 6):
        print(i)
        p = multiprocessing.Process(target=do_work, args=())
        p.start()

    end = time.time()
    print(f"Time taken by thread {i}: {end - start:.4f}")
