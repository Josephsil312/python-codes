def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))