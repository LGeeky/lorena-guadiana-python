list1 = ["Python", "Java", "C++", "Ruby", "SQL"]
list2 = ["Python", "R", "SQL", "Matlab", "PHP"]

set1 = set(list1)
set2 = set(list2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)