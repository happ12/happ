from stack import *

st = getStack()

for item in range(1,5):
    push(st, item)

while not isEmpty(st):
    item = pop(st)
    print(item)