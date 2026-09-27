class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] *(amount+1) 
            # [amount +1] la cac gia tri cua toan bo cua list con (amount+1 ) la so luong ptu trong array
        dp[0]=0
        for i in range (1,amount+1):## try from dp[1] to dp amount
            for c in coins : ## try every coins 
                if i -c >=0:# nếu amount đó có thể dùng đc coin c thì mới vào được điều kiện 
                # ví dụ amount = 1 thì ta sẽ ko thể dùng coin 3 được nên ko vào điều kiện
                    dp[i]= min(dp[i],1 + dp[i-c])
        return dp[amount] if dp[amount]!= amount+1 else -1
                
""" For this problems we use DP BOTTOM-UP
EXAMPLE : COINS {1,3,4,5} AMOUNT 7
Question: ASKING HOW COULD EXCHANGE 7 with the min coins
7 = 1+1+1+1+1+1+1 => 7 coins
7 = 3+3+1= 3 coins
7 = 4+3 = 2 coins
7 = 5+1+1 = 3 coins 
so the best options is 2 
BUT WE USE DP BOTTOM -UP SO INSTEAD OF AKSING THE AMOUNT IS 7 WE WILL START AT THE AMOUNT IS 0 FIRST
WE ASSUME DP(7) IS THE NUMBER OF MIN COINS TO EXCHANGE THE AMOUNT 7 
=> WE START AT AMOUNT 0 FIRST SO => DP(0)
với giá trị là 0 thì đương nhiên là 0 cần coin nào luôn 
-> DP [0] = 0
-> TIẾP ĐẾN DP[1] CÓ BN ĐỒNG COIN TẠO NÊN AMOUNT 1
 => CÓ MỖI ĐỒNG 1 => VẬY LÀ SẼ LÀ ĐỒNG 1 ĐÓ + VỚI DP[0]


 VÍ DỤ VỚI DP5 THÌ TA SẼ HỎI LÀ SỐ ĐỒNG ÍT NHẤT ĐỂ TẠO NÊN AMOUNT 5 LÀ BAO NHIÊU
 VẬY ĐỂ TẠO NÊN AMOUNT 5 TA CÓ NHỮNG CÁCH SAU

 1. 1,1,1,1,1 => KẾT THÚC CỦA DÃY LÀ 1 => 1+ DP(4)
 2. 1+1+3 => KẾT THÚC CỦA DÃY LÀ 3 => 1+ DP(2)
 3. 1+4 => KẾT THÚC LÀ 4 => 1+ DP(1)
 4. 5=> KẾT THÚC LÀ 5 => 1+DP(0)

 TA NHẬN THẤY TRONG TỪNG NÀY CÁCH TA SẼ CHỌN CÁCH TỐN ÍT COINS NHẤT 
 VÀ MỖI LẦN TÍNH DP[I] TA SẼ LUÔN DÙNG CÁC DP TRƯỚC ĐÓ
 DP[I] SẼ LUÔN KẾT THÚC 1 TRONG CÁC SỐ 1,3,4,5 NÊN
 1+ Ở ĐÂY ĐẠI DIỆN CHO VIỆC TA SẼ DÙNG THÊM 1 COIN VÀ COIN ĐÓ CÓ THỂ LÀ 1 OR 3 OR 4 OR 5 VÀ VÌ TA SẼ COIN ĐÓ CÓ GIÁ TRỊ LÀ C  NÊN PHẦN CÒN LẠI LÀ I -C
 DP [I] = C+ DP[I-C]
 """

