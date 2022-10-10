print("Enter the range to generate Armstrong numbers:")
n=input()   
print("The Armstrong Numbers are:")
for num in range(int(n)):
  temp=num
  sum=0
  while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
#commend added for "more changes" assignment
  if sum==num:
    print (num)
