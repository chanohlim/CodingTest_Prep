'''

학생 이름과 성적이 제시됨
성적 낮은 순으로 학생의 이름을 출력

'''

n = int(input())

data = list()

def setting(data):
   return data[1]

for i in range(n):
   input_ = input().split()
   data.append((input_[0], int(input_[1])))

result = sorted(data, key = setting)

print(result)