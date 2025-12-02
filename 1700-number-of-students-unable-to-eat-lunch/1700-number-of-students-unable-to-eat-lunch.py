class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for s in students:
            count[s] += 1

        for s in sandwiches:
            if count[s] == 0:
                return sum(count)
            count[s] -= 1 

        return 0
