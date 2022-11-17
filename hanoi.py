def hanoi(n, _from, _to, _aux):
    if n==1:
        print(_from,'->',_to)
        return
    hanoi(n-1, _from, _aux, _to)
    print(_from,'->',_to)
    hanoi(n-1, _aux, _to, _from)

hanoi(5,1,3,2)