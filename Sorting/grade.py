'''

학생 이름과 성적이 제시됨
성적 낮은 순으로 학생의 이름을 출력

입력 예시:
2
홍길동 92
임찬오 29

'''

n = int(input())

data = list()

def setting(data):
   return data[1]

def sort_fx(data, n):
   for i in range(n):
      input_ = input().split()
      data.append((input_[0], int(input_[1])))

   return(sorted(data, key = setting))

def count_sort(data):
   

result = sort_fx(data, n)
print(result)