import pysnooper
import random
import logging
import threading
import time
from typing import List


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

class Solution:

    # @pysnooper.snoop(thread_info=True)
    @pysnooper.snoop(thread_info=True)
    def binary_search(self, nums: List[int], target:int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left)
            midnum = nums[mid]

            if midnum == target:
                format = "%(asctime)s: %(message)s"
                logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

                # logging.info("Main    : before creating thread")
                x = threading.Thread(target=thread_function, args=(1,))
                # logging.info("Main    : before running thread")
                x.start()
                # logging.info("Main    : wait for the thread to finish")
                # x.join()
                # logging.info("Main    : all done")
                x.join()
                return mid
            elif midnum < target:

                left = mid + 1
            else:
                right = mid - 1
        return -1


Solution().binary_search([1,2,3,4,5], 2)
