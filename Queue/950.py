from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()

        result = [0] * len(deck)

        q = deque(range(len(deck)))

        for i in deck:
            result[q.popleft()] = i

            if q:
                q.append(q.popleft())
        
        return result