n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[0], end = " ")
lst.sort(reverse = True)
print(lst[0])
