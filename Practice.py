import numpy as np

# 길이가 4인 배열 생성(인덱스 0부터 시작)
arr1=np.arange(4)
# print(arr1)

# 정수 데이터 타입을 갖는 0으로 채운 배열 생성
arr2=np.zeros((4,4),dtype=int)
# print(arr2)

# 실수 데이터 타입을 갖는 1로 채운 배열 생성
arr3=np.ones((4,4),dtype=float)
# print(arr3)

# 0부터 6까지 랜덤하게 초기화된 3x3 배열 생성
arr4=np.random.randint(0,7,(4,4))
# print(arr4)

# 배열 합치기
arr5=np.concatenate([arr3,arr4])
# print(arr5)

# 배열 형태 바꾸기
arr6=arr1.reshape((2,2))
# print(arr6)
arr7=arr5.reshape(4,8)
# print(arr7)

# 배열 쪼개기
left, right =np.split(arr7,[4],axis=1)
# print(left)
# print('\n')
# print(right)

# 매트릭스에 스칼라 연산
arr8=np.random.randint(1,7,size=4).reshape(2,2)
result_arr=arr8*10
# print(arr8)
# print(result_arr)