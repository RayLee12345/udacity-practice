def charge(km):
    
    if km < 20 or km == 20:
        return "免費"
    elif km > 20 and km < 200 or km == 200:
        b = 1.2*(a-20)
        return str(b)+"元"
    else:
        b = 0.8*(a-200) + 216
        return str(b)+"元"



print(charge(int(input("輸入:"))))
