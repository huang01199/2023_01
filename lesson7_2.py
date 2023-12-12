import pyinputplus as pyip
import random

while(True):
    min = 1
    max = 100
   
    c = 0
    a = random.randint(min,max)
   
    print("==========猜數字遊戲============")
    
    while True:
        c=c+1

        b = pyip.inputInt(f"猜數字範圍{min}~{max}:")#pyip.inputInt()是隨機輸出數字的函數
        print(b)
        
        if b == a:
            print(f"猜對了,答案是:{a}")
            print(f"您猜了{c}次")
            break
        elif b > a:
            print("再小一點")
            max = b - 1
        elif b < a:
            print("再大一點")
            min = b + 1
        
        print(f"您已經猜了{c}次")
        
        print("=================")
    
    d=pyip.inputYesNo("請問還要繼續嗎?(y,n)")
    if(d=="no"):
        break
        

print("遊戲結束")