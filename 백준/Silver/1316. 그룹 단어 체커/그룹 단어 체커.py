n = int(input()) #단어 개수 숫자 
lst = [] #단어를 담을 리스트

#단어를 리스트에 담는 과정
for i in range(n): 
    word = input()
    lst.append(word)
    
sum_lst = [] #그룹단어가 아닌 경우 숫자를 1 추가하는 리스트
for w in lst: #리스트 안에 있는 단어를 반복
    #print(f"w {w}")
    #se = set([]) 
    for i in range(len(w)-1): #단어의 길이 -1만큼 반복(w[i+1]까지 고려하려면 단어의 길이 -1을 해주어야 함)
        if w[i] != w[i+1]: #지금 글자와 다음 글자가 다르다면
            if w[i] in w[i+1:]: #지금 글자가 나중에 다시 나온다면
                sum_lst.append(1) #그룹단어가 아니기 때문에 1을 추가하고 
                break #반복문을 탈출
print(n-sum(sum_lst)) #전체 단어 개수에서 그룹단어가 아닌 것의 개수를 뺌