class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) ->List[int]:
        par = []## tạo list par [1,2,3,4] 
        for i in range (len(edges)+1):
            par.append(i)
            ## Bài này list bắt đầu từ 1 => ta cần len edges +1 , ta vẫn có index 0 nhưng bài này k dùng đến
        rank = [1]*(len(edges)+1)
        def find(n1):
            ret = n1
            while ret != par[ret]:
                ret = par[ret]
            return ret
        def union(n1,n2):
            p1,p2= find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1] > rank[p2]: ## if the elements in p1 >p2 
                par[p2] = p1 ## change the elements's par of p2 to p1 not par[p1]  bởi vì ta đang cần thay đổi mọi elements trong par 2 thành par 1 chứ k phải par của par 1 , p1 là parent của node 1, còn par[p1] là parent của par 1
                rank[p1]+= rank[p2]
            else:
                par[p1]= p2
                rank[p2]+=rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        