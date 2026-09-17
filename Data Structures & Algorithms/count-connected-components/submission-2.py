class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = []
        for i in range (n):
            par.append(i)
        rank = [1]*n
        def find (n1):## bắt đầu đi duyệt các node ( find là đi tìm par của node đó )
            ret= n1 ## initially thì node nào cũng sẽ có par là chính node đó
            while ret != par[ret]: ## ban đầu par [0] vs par[1] là 2 par riêng nhưng sau khi connect vào thì par [0] sẽ có 0 và 1 và khi lần tiếp theo xét [1,2] thì lúc này par 1 đã là 0 , ret vẫn tiếp có trách nghiệm là lưu par [1] là 1 nhưng khi vào while ret != par[ret] ( 1 != 0=> True => Gán lại ret = par[ret]= 0 để sau này khi so sánh par [1] vs par 2 thì ta lại tiếp tục ghép 2 vào par 0 và được par 0 =0,1,2)
                ret = par[ret]
            return ret
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2: ## Chung par => res - 0
                return 0
            if rank[p1]>rank[p2]:
                par[p1] = p2
                rank[p1] += rank[p2]
            else:
                par[p2]= p1
                rank[p1]+= rank[p2]
            return 1
        ret = n
        for n1, n2 in edges:
            ret -= union(n1,n2) ## nếu chung 1 union - 0 nếu ko chung union return 1 xong sau đó -1
        return ret







        
        