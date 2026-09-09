class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap ={} ## đây là hashmap , và trong hashmap nó sẽ kiểu 
                        ## { 0: [1,2,3] , thì cái 1 ,2,3 trong ngoặc vuông đó là list khá giống array , và với list ta dùng append ()
        for i in range (n):
            preMap[i] =[]
        ## xong dòng này ta được { 0:[], 1:[] 2:[] 3:[] 4:[]
        for n1,n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        ## xong loops này ta dc : { 0:[1,2,3], 1:{0,4} ...}

        visit= set() ## track xem hiện tại đang visited đến node nào 
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for adj in preMap[node]:
                if adj == prev:
                    continue
                if not dfs(adj,node): ## đi hết nhánh dưới rồi không phát hiện circle nên vẫn ổn
                ##=> VẬY THÌ K CÓ GÌ KHÔNG ỔN CẢ => KO RETURN FALSE 

                    return False
            return True
        return dfs(0,-1) and len(visit)== n




        