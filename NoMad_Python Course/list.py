days_list = ["Mon","Tue","Wed","Thur","Fri"]
print(type(days_list))
days_list.append("Sat") #리스트에 값 추가하기
print("Mon" in days_list) #bool 검사하기
print(days_list[3]) #인덱스로 값 찾는거
print(len(days_list)) #리스트 길이 출력

days_str = "Mon,Tue,Wed,Thur,Fri"
print(type(days_str))

#리스트는 mutable 시컨스로서 값이 변함.
#리스트와 딕셔너리를 제외하곤 다 immutable 시컨스임 
 