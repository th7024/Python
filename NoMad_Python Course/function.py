def say_hello(who):  
    print("hello", who)

say_hello("Yoo") #함수에 인자를 넘겨줌

def Plus(a, b):   
    print(a+b)
def minus(a,b=1):  
    print(a-b)

minus(3) #b의 값을 default로 줬음 , b를 입력안해도 함수가 실행 가능
Plus(2,5)    

#return이 있는 경우와 없는 경우
def p_plus(a, b):   
    print(a+b)

def r_plus(a,b):    
    return a+b
p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)


# 인자로 함수 전달하기
def say_hello(name, age):   
    return f"Hello {name} you are {age} years old" #f 를 스트링 앞에 쓰면 인자를 쓸 수 있음
hello = say_hello("Yoo", "23")
print(hello)