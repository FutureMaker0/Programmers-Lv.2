from collections import defaultdict 

# clothes 갯수 + 종류중복제외 적용한 상태에서 나올 수 있는 조합의 갯수(종류 기준)
def solution(clothes):
    answer = 1
    
    dictlist = defaultdict(list)
    for clothe in clothes:
        clothe_name, clothe_kind = clothe[0], clothe[1]
        dictlist[clothe_kind].append(clothe_name)
    print(dictlist)
    
    
    for elem in dictlist.values():
        # print(elem)
        answer *= len(elem) + 1
        
    return answer - 1


'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''


    
'''
def solution(clothes):
    answer = 1
    closetDic = {}
    
    for i in clothes:
        if i[1] in closetDic:
            closetDic[i[1]].append(i[0]) # 있을 때는 그냥 있는 리스트에 추가하는 것
        else:
            closetDic[i[1]] = [i[0]] # 맨 처음에는 없으니까 리스트를 하나 만들고 넣어주는 것
    print(closetDic)
            
    for i in closetDic.values():
        print(i)
        answer *= (len(i)+1)
        # 3*2
        
        # yello_hat, green_turban, 0
        # blue_sunglasses, 0
        # 6개에서 어디든 최소 1개는 입어야 하므로 아예 안 입는 0*0을 하나 뺴준다.
        
    return answer-1 # 6-1
'''
    
