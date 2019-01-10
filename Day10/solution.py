import time
import subprocess
import threading

def scheduler(f, n):
    """
    Runs the function `f` after at n millisecond intervals
    :param f: The function to run
    :param n: The interval between executions
    :return:
    """
    while True:
        thread = threading.Thread(target=f)
        thread.start()
        time.sleep(n/1000)