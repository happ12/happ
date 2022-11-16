from module1_nameclash import *
from module1_nameclash import double as db
print(double)
m1_double = double
from module2_nameclash import *
print(double)
print(double(5))

print(m1_double(5))
print(db(5))
print(globals())