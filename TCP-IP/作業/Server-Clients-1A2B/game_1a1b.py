# 用String讀
s1 = list(input("請play1輸入題目："))
s2 = list(input("請play2輸入題目："))

# 判斷輸入 是否為四個字/是否為數字
while len(s1)!=4 :
    print("play1輸入格式錯誤 , 請重新輸入...")
    s1 = list(input("請play1重新輸入題目："))
while len(s1)==4 :
        i = 0
        while i != 4 : 
            if ord(s1[i]) >= 48 | ord(s1[i]) <= 57 :
                i = i + 1
                continue
            else :
                print("play1輸入格式錯誤 , 請重新輸入...")
                s1 = list(input("請play1入重新題目："))
                i = 0
        break

while len(s2)!=4:
    print("play2輸入格式錯誤 , 請重新輸入...")
    s2 = list(input("請play2重新輸入題目："))
while len(s2) <= 4 :
    j = 0
    while j != 4 : 
        if ord(s2[j]) >= 48 | ord(s2[j]) <= 57 :
            j = j + 1
            continue
        else :
            print("play2輸入格式錯誤 , 請重新輸入...")
            s2 = list(input("請play2輸入重新題目："))
            j = 0
    break

#開始遊戲

A1 = 0
B1 = 0
A2 = 0
B2 = 0

while A1!=4 and A2!= 4:
    A1 = 0
    B1 = 0
    A2 = 0
    B2 = 0
    guess1 = list(input("請play1輸入答案："))
    guess2 = list(input("請play2輸入答案："))
   
    while len(guess1)!=4 :
        print("play1輸入格式錯誤 , 請重新輸入...")
        guess1 = list(input("請play1重新輸入答案："))
    for i in range (4):
        for j in range (4):
            if s2[i] == guess1[j] :
                if i == j :
                    A1 = A1 + 1
                    guess1[j] = 'o'
                    break
                else:
                    B1 = B1 + 1
                    guess1[j] = 'x'
                    break
    
    while len(guess2)!=4:
        print("play2輸入格式錯誤 , 請重新輸入...")    
        guess2 = list(input("請play2重新輸入答案："))                
    for i in range (4):
        for j in range (4):
            if s1[i] == guess2[j] :
                if i == j :
                    A2 = A2 + 1
                    guess1[j] = 'o'
                    break
                else:
                    B2 = B2 + 1
                    guess1[j] = 'x'
                    break
    print("play1:", A1, "A", B1, "B")
    print("play2:", A2, "A", B2, "B")
    

if(A1 == 4|A2==4):
    print("win win")
elif(A1 == 4):
    print("play1 win!")
elif(A2 == 4):
    print("play2 win!")