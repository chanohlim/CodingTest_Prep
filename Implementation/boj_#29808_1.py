'''

국어 점수가 영어 점수보다 높다면, 두 점수의 차에 인문관의 건물 번호 508을 곱해준다. 아니라면, 두 점수의 차에 국제관의 건물 번호 108을 곱해준다.
수학 점수가 탐구 점수보다 높다면, 두 점수의 차에 제1공학관의 건물 번호 212를 곱해준다. 아니라면, 두 점수의 차에 ITBT관의 건물 번호 305을 곱해준다.
위에서 계산한 두 값을 더한 뒤, 한양대학교의 우편번호 04763 (=4763)을 곱하면 학번이 나온다.

a = | 국어 - 영어 |
b = | 수학 - 탐구 |


수학 > 탐구 : a x 212
수학 < 탐구 : a x 305
국어 > 영어 : b x 508
국어 < 영어 : b x 108

'''

student_id = int(input())
result_list = set() # 중복 제거

if student_id % 4763 != 0: # 학번이 4763으로 안나누어지면 바로 종료
    print(0)
    exit()

n = student_id // 4763 # 만약 학번이 4763으로 나눠지면 나누기


for a in range(201): # a = |수학 - 탐구|, 이 차는 항상 0에서 200 사이이므로.
    i = 305 * a # 수학 < 탐구
    if i > n: # i가 n보다 커지면 성립이 안됨. i + 다른 정수 = n 이기 때문.
        break

    m = n - i # m = |국어 - 영어| * 212 or 305

    if m % 108 == 0: # 국어 < 영어
        b = m // 108
        if 0 <= b <= 200:
            result_list.add((b, a))

    if m % 508 == 0: # 국어 > 영어
        b = m // 508
        if 0 <= b <= 200:
            result_list.add((b, a))


for a in range(201):
    i = 212 * a # 수학 > 탐구
    if i > n:
        break

    m = n - i

    if m % 108 == 0:
        b = m // 108
        if 0 <= b <= 200:
            result_list.add((b, a))

    if m % 508 == 0:
        b = m // 508
        if 0 <= b <= 200:
            result_list.add((b, a))


result_list = sorted(result_list, key=lambda x: (x[0], x[1]))

print(len(result_list))
for b, a in result_list:
    print(b, a)