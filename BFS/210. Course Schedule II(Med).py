class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseOrder = [];
        pres = defaultdict(set);
        courses = defaultdict(set);
        for course, pre in prerequisites:
            pres[pre].add(course);
            courses[course].add(pre);
        noPresList = [n for n in range(numCourses) if not courses[n]];
        courseOrder.extend(noPresList);
        while noPresList:
            noPre = noPresList.pop();
            for course in pres[noPre]:
                courses[course].remove(noPre);
                if not courses[course]:
                    noPresList.append(course);
                    courseOrder.append(course);
        return courseOrder if len(courseOrder) == numCourses else [];

# 思路
# 和上一题一样，差别他要把order列出来
# 那很好办，只要把noPre的课程另外建立一个数组然后塞进去就完事了
