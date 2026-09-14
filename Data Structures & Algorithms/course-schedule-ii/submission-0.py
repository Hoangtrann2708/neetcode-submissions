class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}
        ##hashmap : { 0: {}, 1: {}, 2: {} }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        ## 0: {1}, 1: {2}, 2: {}
        output = []
        circle, visit = set(),set()
        def dfs(crs):
            if crs in circle: ## Neu node hien tai da o trong chu trinh ma t dang di tuc la ta gap circle => return False
                return False
            if crs in visit: ## visit la set de xem crs da duoc hoc chua , neu crs o trong visit => Tuc la da duoc hoc => return True => ( vi du course A da duoc hoc , mà A LÀ preq của B => return True => để quay về B VỀ ĐÁNH DẤU LÀ B CÓ THỂ ĐƯỢC HỌC VÀ ĐƯỢC ADD VÀO CIRCLE ĐỂ TIẾP TỤC DUYỆT B CÒN CẦN PREQ NÀO KHÁC K )
                return True
            circle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):  ## 
                    return False
## Ta chỉ đến được dòng này khi Node hiện tại ko có prequesite nào 
            circle.remove(crs)## circle bỏ node hiện tại để quay về node gọi nó
            visit.add(crs) ## visit add node nay vi no da duoc hoc xong roi 
            output.append(crs) ## output add node nay vi day la node dau tien ko can prequesite
            return True ## return True => cho node nay vi da hoc xong
        for c in range(numCourses):
            if not(dfs(c)):
                return []
        return output


            

            




        