def midterm(level):
    if level > n:
        print(lst)
        return

    for i in range(1, n+1):
        if visited[i] == False:
            lst.append(i)
            visited[i] = True
            midterm(level+1)
            lst.pop()
            visited[i] = False

n = int(input())
lst = []
visited = [False for _ in range(n+1)]
midterm(1)