import threading
import time

"""
# Without Multi-Threading
def do_work():
""IO BOUND TASK""
    print("Starting work...")
    time.sleep(1)
    print("Finished work!\n")


start = time.time()
for i in range(1, 6):
    print(i)
    do_work()

end = time.time()
print(f"Time taken by thread {i}: {end - start:.4f}")
"""

"""
# With Multi-Threading
def do_work():
    ""IO BOUND TASK""
    print("Starting work...")
    time.sleep(1)
    print("Finished work!\n")


start = time.time()
for i in range(1, 6):
    print(i)
    t = threading.Thread(target=do_work, args=())
    t.start()
end = time.time()
print(f"Time taken by thread {i}: {end - start:.4f}")
"""


def do_work():
    """CPU BOUND TASK"""
    print("Starting work...")
    i = 0
    for _ in range(100000000):
        i += 1
    print("Finished work!\n")


start = time.time()
for i in range(1, 6):
    print(i)
    t = threading.Thread(target=do_work, args=())
    t.start()
end = time.time()
print(f"Time taken by thread {i}: {end - start:.4f}")
