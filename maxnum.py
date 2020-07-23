def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))