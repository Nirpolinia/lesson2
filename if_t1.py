age = input("Enter your age ")
def occupation(x):
   if x < 7:
      y = 'kindergarten'
   elif x < 17:
      y = 'school'
   elif x < 22:
      y = 'university'
   else:
      y = 'work'
   return(y)
res = occupation(int(age))
print(res)