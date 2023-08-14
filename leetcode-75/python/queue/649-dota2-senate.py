from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R, D = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))

        return "Radiant" if R else "Dire"
