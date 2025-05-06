# not working
# from collections import deque

# class Solution:
#     def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
#         q = deque(tickets)
#         current_required_index = k
#         value = 0
#         seconds = 0
#         while q[current_required_index] > 0:
#             value = q.popleft() - 1
#             if value > 0:
#                 q.append(value)
#             current_required_index = current_required_index - 1 if current_required_index > 0 else len(q) - 1

#             if current_required_index == -1 or q[current_required_index] == 0:
#                 break
#             seconds += 1
            
#         return seconds

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        seconds = 0
        for i in range(len(tickets)):
            if i <= k:
                seconds += min(tickets[i], tickets[k])
            else:
                seconds += min(tickets[i], tickets[k] - 1)
        return seconds



s = Solution()
print(s.timeRequiredToBuy([2,3,2], 2))