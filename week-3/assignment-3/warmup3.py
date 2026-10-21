print(not True and False)       # not True is False given that False and False is False
print(True or False and False)  # AND runs before or: False and False is False; True or False is True
print(not (5 > 3))              # 5 > 3 is True; not True is False
print(10 == 10 and 4 != 4)      # 10 is equal to 10 is True; 4 is not equal to 4 is False; True and False is False
print(not False or not True)    # not False is True; not True is False; True or False is True