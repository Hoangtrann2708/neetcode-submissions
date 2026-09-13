class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visit = set()

        def dfs(course):
            if course in visit:        ## gặp lần thứ 2 → đã tạo thành loop
                return False
            if preMap[course] == []:   ## ko còn prerequisite nào → True
                return True

            visit.add(course)
            for pre in preMap[course]:     ## dfs các neighbor của course
                if not dfs(pre):
                    return False
            visit.remove(course)           ## NGOÀI vòng for

            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True