n = int(input())
dic1 = {}
lst1 = list(map(int, input().split()))

for i in range(len(lst1)):
    dic1[lst1[i]] = i

m = int(input())
# dic2 = {}
lst2 = list(map(int, input().split()))

# for j in range(len(lst2)):
#     dic2[lst1[j]] = j

for i in range(len(lst2)):
    if lst2[i] in dic1:
        print(1)
    else:
        print(0)