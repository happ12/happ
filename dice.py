lst = []

def dice(level):
    if level > n:
        print(lst)
        return

    for i in range(1,7):
        lst.append(i)
        dice(level+1)
        lst.pop()

n=int(input())
dice(1)