N = int(input("Dose enan akeraio arithmo:"))
while N >= 1000000:
  print ("lathos kataxorisi dokimase ksana")
  N = int(input("Dose ksana enan akeraio arithmo:"))

ypoloipo = N
ginomeno = 1
i = 1

while ginomeno != N:
  i = i + 1
  dynami = 0
  while ypoloipo%i == 0:
    ypoloipo = ypoloipo/i
    dynami = dynami + 1
  if dynami > 0:
      print ("(",i , "**" , dynami ,end="" ")")
      ginomeno = ginomeno*i**dynami
       
