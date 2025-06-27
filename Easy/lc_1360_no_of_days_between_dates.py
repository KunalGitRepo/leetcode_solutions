import time, datetime
from typing import List, Optional


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.datetime.timestamp(datetime.datetime.strptime(date1, "%Y-%m-%d"))
        d2 = datetime.datetime.timestamp(datetime.datetime.strptime(date2, "%Y-%m-%d"))
        if d1 > d2:
            d2, d1 = d1, d2
        return int((d2 - d1) / (3600 * 24))


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    a_start = '2019-06-29'
    a_end = '2019-06-30'
    a_start = '2020-01-15'
    a_end = '2019-12-31'
    ret_val = sol_obj.daysBetweenDates(date1=a_start, date2=a_end)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
