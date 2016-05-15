n = int(raw_input())
list_students_grades = [[raw_input(), float(raw_input())] for _ in range(n)]
grades1 = sorted(list(set([grades for name, grades in list_students_grades])))
print("\n".join([x for x,y in sorted(list_students_grades) if y == grades1[1]]))


