class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        window = {}
        L = len(s1)
        if len(s1)>len(s2):
            return False
        for i in range (L):
            target[s1[i]] = 1+ target.get(s1[i],0)
            window[s2[i]] = 1+ window.get(s2[i],0)
        if target == window:
            return True
        for i in range(L,len(s2)):
            enter = s2[i]
            window[enter]= 1+ window.get(enter,0)
            leave = s2[i-L]
            window[leave]-=1
            if window[leave]== 0:
                del window[leave]
            
            if window == target:
                return True
        return False







         ##flow:
      ##  1: Ta cần bt số lg elements có trong s1 , coi đó là 1 cụm rồi bắt đầu duyệt s2 theo cụm ( cụm 1 có 3 thì cụm 2 cũng duyệt 3 cái 1.  3 cái 1 ).
       ## Ex: S1: abc -> 3 
       ##     S2: jgakgabckk => 3 jga, move window (r+1)-> gak(False)-> akg(false) -> kga -> gab -> abc -> True 
       ## 2. tạo 2 hashmap => TARGET, WINDOW, rồi dùng loop 1 count từng elements
      ##  Initialize , count từng elements của s1 => TARGET = {1:a,1:b,1:c}
       ##             count 3 chữ cái đầu của s2=>> Window = 1:j. 1:g, 1:a }
       ## 3. Loop2 : moving windows ( duyệt từ elemnts thứ 4 của s2 => )
        ##loop2 ( L-> S2)
       ## TẠO 2 VARIABLE : ENTER VS LEAVE ( ENTER = I), LEAVE (I-L)
        ##ENTER THÌ WINDOW[ENTER]+= 1 
        

        