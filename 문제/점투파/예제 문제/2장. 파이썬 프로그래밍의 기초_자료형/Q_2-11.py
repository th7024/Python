a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     # a 리스트를 집합자료형으로 변환
b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
print(b)          # [1,2,3,4,5] 출력
# 리스트 자료형이 집합 자료형으로 변환되면서 중복된 값들은 사라지게 된다. 이와 같은 성질을 사용하면 리스트 내에 중 복된 값을 쉽게 제거할 수 있다.