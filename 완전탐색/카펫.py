def solution(brown, yellow):
    total = brown + yellow
    # print(total)
    
    hubos = []
    for i in range(3, total):
        divided = total // i
        if total % i == 0:
            hubos.append([i, divided])
    # print(hubos)
    
    for hubo in hubos:
        test = (hubo[0]-2) * (hubo[1]-2)
        if hubo[0] >= hubo[1] and test == yellow:
            return hubo
     
