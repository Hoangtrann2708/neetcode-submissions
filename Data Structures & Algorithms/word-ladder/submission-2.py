class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList: ## duyet tung tu co trong list
            for j in range (len(word)): ## tao ra cac pattern cho tung word
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word) ## voi moi pattern thi tu do chinh la 1 value 
            ##
        visit = set([beginWord])
        q= collections.deque([beginWord])
        ret = 1
        while q:
            ## qlen = len(q)
            for i in range (len(q)):
                word = q.popleft()
                if word == endWord:
                    return ret
                for j in range (len(word)):
                    pattern = word[:j] + "*"+ word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
                    adj[pattern] = []
            ret+=1
        return 0


                




        

        













        ## Bài có 2 giai đoạn 
        #1 Dựng adj 
        #2 BFS










        ##  1Dựng adj 
        ## Naive : lấy 1 từ so sánh n-1 từ còn lại => n^2 và nếu tất cả từ đều có m chữ => n^2*m
        ## ví dụ cat: có 3 chữ => so sánh với bat ( cũng 3 chữ)
        ##=> c vs b (same), a vs a, t vs t
        #Tiếp túc cat vs bag => ta lại phải so sánh c vs b, a vs a, t vs g
        

        #Khôn => vẫn loops chạy qua n từ trong list nhưng với mỗi từ ta sẽ viết nó theo m khuôn
       # ví dụ hot => m = 3 => 3 khuôn (*ot, h*t, ho*) 
        # => Ta cần loop qua từng vị trí trong từ đó ( for j )
       # j =0 => ta biết khuôn đó *ot 
       # bây giờ tạo khuôn đó lại tốn m => word[:j] + * + word[:j+1]


        