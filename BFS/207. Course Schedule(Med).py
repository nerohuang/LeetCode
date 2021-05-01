def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)
        no_pre_courses = [n for n in range(numCourses) if not courses[n]]
        count = 0
        while no_pre_courses:
            no_pre = no_pre_courses.pop()
            count+=1
            for course in pres[no_pre]:
                courses[course].remove(no_pre)
                if not courses[course]:
                    no_pre_courses.append(course)
        return count == numCourses

# 思路：
# 可以用bfs，dfs还有有向图（不懂）；
# 思路是建立两个set分别存一个科目所需要的prerequest
# 另一个是prerequest上完之后可以上的科目。
# 然后找到所有不需要prerequest就能上的课noPreCourse
# 然后while直到noPreCourse为空（全部上过）
# 在while过程中
# 先pop出一个noPre的课，然后上课数量count + 1表示
# 上了一节课。
# 然后开始遍历pre[noPre]，位的就是看看哪些课需要这个
# noPre为基础，然后在那个courses的set里面去掉那个
# noPre，因为已经上了。
# 当如果那个course所需要prerequest都去掉了
# 那么当然他也变成了noPre，放进了noPre的list里面
# 直到noPre的list为空，那就是上了多少课。
# 如果count不等于课的数目，那表示还有课没法上，false
# 反之true