sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for sales in sales_data[:]:
  for i in sales:
    scoops_sold = scoops_sold+i
print(scoops_sold)
  #print(scoops_sold)