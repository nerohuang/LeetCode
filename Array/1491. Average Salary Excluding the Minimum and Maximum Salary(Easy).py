class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary));
        salary.remove(max(salary));
        return (sum(salary)/len(salary));

#class Solution:
#    def average(self, salary: List[int]) -> float:
#        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)