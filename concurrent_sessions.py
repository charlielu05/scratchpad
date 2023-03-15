# Find the maximum number of concurrent sessions in the following data with the first value representing start time and last value end time. The input is not necessarily sorted. 
# Input: (2,5), (3,6), (8,10),(10,12),(9,20) 
# Output: 3 (from 8 to 20) 
# Input: (2,5), (3,6), (8,10),(9,12),(12,20) 
# Output: 2 (from 8 to 12 or 2 to 6)

# filter entries that are overlapped
# if number of overlap is > half of entries, use that as max

from functools import partial
from typing import List

def overlapped(session_b, session_a):
    # we compare against a
    if session_b[0] <= session_a[1] and session_b[1] >= session_a[0]:
        return True
    else: 
        return False

def overlap_loop(sessions:List[tuple[int,int]])->int:
    count_list = []

    while len(sessions) != 0:
        comparison_session = sessions[0]
        overlap_filter = partial(overlapped, session_a=comparison_session) 
        overlapped_iterator = filter(overlap_filter, sessions)
        overlapped_list = list(overlapped_iterator)
        overlapped_count = len(overlapped_list)
        count_list.append(overlapped_count)
        sessions = list(set(sessions) - set(overlapped_list))

    return count_list

if __name__ == "__main__":
    test_case_session_a = (2,5)
    test_case_session_b = (3,6)

    overlap_filter = partial(overlapped, session_a=test_case_session_a)

    assert overlap_filter(session_b=test_case_session_b) == True
    assert overlap_filter(session_b=(7,9)) == False

    test_case_sessions = [(2,5), (3,6), (8,10),(10,12),(9,20)]

    overlapped_iterator = filter(overlap_filter, test_case_sessions) 

    none_overlapped = list(set(test_case_sessions) - set(overlapped_iterator))

    #print(none_overlapped)
    print(max(overlap_loop(test_case_sessions)))

    test_case_sessions_b = [(2,5), (3,6), (8,10),(9,12),(12,20)]
    print(max(overlap_loop(test_case_sessions_b)))