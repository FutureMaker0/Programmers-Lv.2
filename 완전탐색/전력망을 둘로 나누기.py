from collections import deque

def solution(n, wires):
    answer = 10000
    graph = [[] for _ in range(n+1)]
    # print(graph)
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    # print(graph)
    
    for start, end in wires:
        # print(start, end)
        visited = [False for _ in range(n+1)]
        # print(visited)
        
        dq = deque()
        dq.append(start)
        # print(dq)
        
        visited[start] = True
        visited[end] = True
        # print(visited)
        
        result = 1
        while dq:
            node = dq.popleft()
            # print(node)
            for elem in graph[node]:
                # print(elem)
                if not visited[elem]:
                    # print(visited[elem])
                    
                    result += 1
                    visited[elem] = True
                    dq.append(elem)
            
            # print(result)
            # print(visited)
            # print(dq)
            # print(' ')
            
        # print(result)
        # print(visited)
        # print(' ')
        
        min_value = min(result, n-result)
        max_value = n - min_value
        # print(max_value, min_value)
        
        if answer > max_value - min_value:
            answer = max_value - min_value
    
    print(answer)
    return answer
