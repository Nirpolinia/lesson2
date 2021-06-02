age = input("Enter your age ")
def occupation(x):
   if x < 7:
    y = 'kindergarten'
   if (x < 17 and x > 7):
    y = 'school'
   if (x < 22 and x > 17):
    y = 'university'
   if x >= 22:
    y = 'work'
   return(y)
res = occupation(int(age))
print(res)