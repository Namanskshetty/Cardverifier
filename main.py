import re
reg="^[0-9]+$"
print("Welcome to credit card or debit card verifier (offline)")
card=str(input("Enter your 16 digit number without spaces: "))
go=re.search(reg,card)
if len(card)>16 or len(card)<16:
  print("Length provied error")
elif go==None:
  print("Enter the digits only")
else:
  cardno = []
  for i in card:
    cardno.append(int(i))
  for i in range(len(cardno)):
    if (i % 2) != 0:
      cardno[i-1]=cardno[i-1]*2
  for i in range(len(cardno)):
    if cardno[i]>9:
      bo=str(cardno[i])
      res=[]
      for j in bo:
        res.append(int(j))
      cardno[i]=sum(res)
  if sum(cardno)%10==0:
    print("The card checks out")
  else:
    print("card not found")
