A, B, C = map(int, [3, 3, 3])
D, E, F = map(int, [4, 4, 4])
G, H, I = map(int, [5, 5, 5])
J, K, L = map(int, [6, 6, 6])
M, N, O = map(int, [7, 7, 7])
P, Q, R, S = map(int, [8, 8, 8, 8])
T, U, V = map(int, [9, 9, 9])
W, X, Y, Z = map(int, [10, 10, 10, 10])


n = input()
ans = list(map(eval, n))
print(sum(ans))