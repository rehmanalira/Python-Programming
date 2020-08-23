"""
Function Caching :
basically function is used to save the time of a function which one time runs and
when it will re run then it will save the time and it will run the

for this we use @lru_cach which is import from the functools
"""

import time
from functools import lru_cache
@lru_cache(maxsize=4)
def work(n):
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("We are starting...")
    work(3)
    work(2)
    work(2)
    work(1)
    work(4)
    print("We are again starting...")
    work(4)
    work(1)
    work(5)
    print("Here we End...")