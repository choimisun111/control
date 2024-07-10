# 1. 사용자로부터 값을 입력
num = input("점수를 입력하세요.")
# 2. 사용자로부터 입력받은 값을 숫자형으로 데이터 타입을 변환
print("데이터 타입 변환 전:",num, type(num))
num = int(num)
# 3. 변환된 ㅏㅄ을각 조건에 따라 학점으로 출력
if 81<= num <= 100 :
        print("A")
elif 61 <= num <= 80 :
        print("B")