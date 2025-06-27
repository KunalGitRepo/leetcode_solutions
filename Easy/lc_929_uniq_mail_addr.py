import time
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        new_mail_list = set()
        for mail in emails:
            m_list = mail.split('@')
            if len(m_list) <= 1 or len(m_list) > 2:
                continue
            # if m_list[1].count('.') > 1:
            #     continue
            if '+' in m_list[0]:
                name_list = m_list[0].split('+')
                name = name_list[0].replace('.', '')
            else:
                name = m_list[0].replace('.', '')
            mail_id = name + '@' + m_list[1]
            new_mail_list.add(mail_id)
        return len(new_mail_list)


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    n = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    n = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    ret_val = sol_obj.numUniqueEmails(emails=n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
