def abc(a,b): #최대 공약수 찾는 함수
    if(b>a):  #큰 값을 a로 고정하기 위한 조건문
        a, b = b, a #큰 값을 a로 변경
    c = 1 #변수 c 임의 생성
    while(c != 0): #나머지가 0이 될 때까지 반복
        #유클리드 호제법을 알고리즘으로 구현
        c = a % b 
        a, b = b, a
        b = c
    return a

def solution(denum1, num1, denum2, num2):
    n = num1 * num2 
    d = (denum1 * num2) +  (denum2 * num1)
    answer = []
    c = abc(n,d)
    answer.append(d/c)
    answer.append(n/c)
    return answer