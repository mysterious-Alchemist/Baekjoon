h = int(input()) #점의 개수
lst = [] #점의 좌표 리스트
for i in range(h): #점의 개수만큼 반복해서 리스트에 점의 좌표 저장
    tmp = list(map(int, input().split(" ")))
    lst.append(tmp)
    
a = [] #100 x 100 좌표평면 생성
for i in range(100):
    row = []
    for j in range(100):
        row.append(0)
    a.append(row)
    
#100 x 100 좌표평면에 각 점을 대입시키고 점을 기준으로 10 x 10 범위를 "aa"라는 값으로 변경
for i in lst:
   for j in range(i[1], i[1]+10):
    #    print(f"j = {j}")
       for k in range(i[0], i[0]+10):
        #    print(f"k = {k}")
           a[j][k] = "aa"
            
#"aa"의 개수를 담을 sum1 변수 선언
sum1 = 0
for i in a:
    sum1 = sum1 + i.count("aa")
print(sum1) 