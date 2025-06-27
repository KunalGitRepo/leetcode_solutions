import time
from typing import List, Optional


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        alice_arrive_day = int(arriveAlice.split('-')[1])
        alice_arrive_month = int(arriveAlice.split('-')[0])
        alice_leave_day = int(leaveAlice.split('-')[1])
        alice_leave_month = int(leaveAlice.split('-')[0])
        bob_arrive_day = int(arriveBob.split('-')[1])
        bob_arrive_month = int(arriveBob.split('-')[0])
        bob_leave_day = int(leaveBob.split('-')[1])
        bob_leave_month = int(leaveBob.split('-')[0])

        if alice_arrive_month != bob_arrive_month:
            if alice_arrive_month < bob_arrive_month:
                start = arriveBob
            else:
                start = arriveAlice
        else:
            if alice_arrive_day != bob_arrive_day:
                if alice_arrive_day < bob_arrive_day:
                    start = arriveBob
                else:
                    start = arriveAlice
            else:
                start = arriveAlice

        if alice_leave_month != bob_leave_month:
            if alice_leave_month > bob_leave_month:
                end = leaveBob
            else:
                end = leaveAlice
        else:
            if alice_leave_day != bob_leave_day:
                if alice_leave_day > bob_leave_day:
                    end = leaveBob
                else:
                    end = leaveAlice
            else:
                end = leaveBob

        start_day = int(start.split('-')[1])
        start_month = int(start.split('-')[0])
        end_day = int(end.split('-')[1])
        end_month = int(end.split('-')[0])

        if start_month != end_month:
            if start_month < end_month:
                days_in_start = days_dict[start_month] - start_day + 1
                days_in_end = min(days_dict[end_month], end_day)
                months = end_month - start_month - 1
                days_in_between = 0
                if months > 0:
                    for i in range(start_month+1, end_month):
                        days_in_between += days_dict[i]
                return days_in_start + days_in_end + days_in_between
            else:
                return 0
        else:
            if start_day != end_day:
                if start_day < end_day:
                    return end_day - start_day + 1
                else:
                    return 0
            else:
                return 1


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    a_start = '08-15'
    a_end = '08-18'
    b_start = '08-16'
    b_end = '08-19'

    ret_val = sol_obj.countDaysTogether(arriveAlice=a_start, leaveAlice=a_end, arriveBob=b_start, leaveBob=b_end)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
