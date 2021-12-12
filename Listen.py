liste = [1, 2, 3, 4, 5]

# BY INDEX
a = liste[0] # 1

b = liste.remove(4) # [1, 2, 3, 5]


# BY VALUE
c = liste.index(2) # 3

d = liste.pop(1) #[2, 3, 4, 5]


######################

e = liste.count(4) # 1

g = liste.copy() # [1, 2, 3, 4, 5]

liste.append(10) # [1, 2, 3, 4, 5, 10]
liste.extend([7, 8, 9]) # [1, 2, 3, 4, 5, 7, 8, 9]

liste.sort()
liste.reverse()
liste.clear()