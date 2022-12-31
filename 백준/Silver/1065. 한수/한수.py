def cold_number(num):
    d = 0
    if num<100:
        c = num
        return print(c)
    elif num>=100:
        for i in range(num, 99 , -1):
           a = i // 100
           b = (i // 10) % 10 
           c = i % 10
           if (a - b) == (b - c):
               d = d + 1
        return print(d + 99) 

num = int(input())
cold_number(num)