from bisect import bisect_left
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import lru_cache
from heapq import heappop
from heapq import heappush
from math import ceil
from pprint import pprint
from typing import List
from typing import Optional
import pysnooper
import random
import sys


import pysnooper
from typing import List

def binary_search(nums: List[int], target:int) -> int:
    left, right = 0, len(nums) -1
    while left <= right:
        mid = left + (right - left)
        midnum = nums[mid]

        if midnum == target:
            return mid
        elif midnum < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sys.gettrace()
l = [1,2,3,5,7,9]
tmp = binary_search(l, 7)
print(tmp)

sys.settrace(binary_search)
# python3 -m trace -t temp.py 

