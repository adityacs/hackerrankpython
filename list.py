n = int(raw_input())
list1 = [int(x) for x in raw_input().split()]
list2 = sorted(list(set(list1)))
print list2[-2]
