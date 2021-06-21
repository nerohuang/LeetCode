class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        loopCount = 0;
        while loopCount < len(students) and students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0);
                sandwiches.pop(0);
                loopCount = 0;
            else:
                students.append(students.pop(0));
                loopCount += 1;
        
        return len(students)

# 思路
# 模拟，没什么好说的