from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)

        rounds = 0
        for count in freq.values():
            if count == 1: return -1
            if count % 3 == 0:
                rounds += int(count / 3)
            else:
                rounds += int((count / 3) + 1)

        return rounds


