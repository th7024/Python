def is_odd(N):   
    if N % 2==0:  
       print( N , "은 짝수 입니다.")
    else:   
        print( N , "은 홀수 입니다.")

num = int(input("숫자를 입력하세요 :"))
is_odd(num)

