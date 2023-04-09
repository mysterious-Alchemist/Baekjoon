lst = list(map(int, input().split()))
a_lst = [1, 2, 3, 4, 5, 6, 7, 8]
d_lst = [8, 7, 6, 5, 4, 3, 2, 1]

if (lst == a_lst):
    print("ascending")
elif(lst == d_lst):
    print("descending")
else:
    print("mixed")