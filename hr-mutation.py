string = raw_input()
pos = [x for x in raw_input().split()]
print pos
po = int(pos[0])
string = string[:po] + pos[1] + string[po+1:]
print string
