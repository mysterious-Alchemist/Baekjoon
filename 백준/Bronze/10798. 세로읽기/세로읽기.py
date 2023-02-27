#백준 10798 세로읽기
lst = []
for i in range(5):
    lst.append(list(input()))

for j in range(15):
    for i in range(15):
        try:
            print(lst[i][j], end = "")
        except:
            pass