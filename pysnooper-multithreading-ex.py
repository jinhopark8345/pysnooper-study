import logging
import threading
import time
import concurrent.futures
import pysnooper

# [rest of code]

@pysnooper.snoop(thread_info=True)
def thread_function(name):
    # logging.info("Thread %s: starting", name)
    time.sleep(2)
    # logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    custom_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=custom_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(5))
