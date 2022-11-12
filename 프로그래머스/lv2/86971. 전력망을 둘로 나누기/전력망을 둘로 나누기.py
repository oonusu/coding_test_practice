from collections import defaultdict
def solution(n, wires):
    w_map = defaultdict(list)
    res = float('inf')

    for i, j in wires:
        w_map[i].append(j)
        w_map[j].append(i)

    def dfs(x, visited):
        visited.add(x)
        for v in w_map[x]:
            if v not in visited:
                visited = dfs(v, visited)
        return visited

    for i in w_map:
        for j in w_map[i]:
            temp = set()
            temp.add(i)
            record = dfs(j, temp)
            diff = abs((n - (len(record) - 1)) - (len(record) - 1))
            res = min(res, diff)

    return res