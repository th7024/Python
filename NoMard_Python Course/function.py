def say_hello(who):  
    print("hello", who)

say_hello("Yoo") #함수에 인자를 넘겨줌

def Plus(a, b):   
    print(a+b)
def minus(a,b=1):  
    print(a-b)

minus(3) #b의 값을 default로 줬음 , b를 입력안해도 함수가 실행 가능
Plus(2,5)    