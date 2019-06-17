sum = 0
num = 1
def jiecheng(n):
   for i in range(1,n+1):
       for j in range(1,i+1):
           num=num*j
       sum=sum+num
   return sum
print(jiecheng(3))