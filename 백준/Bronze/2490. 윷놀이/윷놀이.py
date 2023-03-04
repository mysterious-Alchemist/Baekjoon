#백준 2490 윷놀이
dic = {0:"D", 1:"C", 2:"B", 3:"A", 4:"E"}
for i in range(3):
    print(dic[sum(list(map(int,input().split())))])