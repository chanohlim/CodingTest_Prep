def solution(genres, plays):
    
    answer = []
    data = dict()
    
    for i in range(len(genres)):
        data.setdefault(genres[i], []).append((i, plays[i]))
        
    genres = set(genres)
    order = []
    for genre in genres:
        cnt = 0
        
        data[genre].sort(key=lambda x:-x[1])
        for playcnt in data[genre]:
            cnt += playcnt[1]
            
        order.append((genre, cnt))
        
    
        
    order.sort(key=lambda x:-x[1])
    
    for genre, val in order:
        cnt = 0
        for d in data[genre]:
            answer.append(d[0])
            cnt += 1
            if cnt == 2:
                break

    return answer