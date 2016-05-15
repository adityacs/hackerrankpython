a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
sum = int(raw_input())
num = [[x,y,z] for x in range(a+1) for y in range(b+1) for z in range(c+1) if x+y+z != sum]
print num