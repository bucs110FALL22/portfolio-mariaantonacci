##part 1

print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(15%15)
print(10%10)
print(0%10)
print(10/15)

#the result of line 12 is mathematically incorrect

##part 2
rate= input("Please put the current exchange rate from euro to dollar: ")
rate=int(rate)
amount= input("Please put the amount of money you would like to exchange: ")
amount=int(amount)
total= (rate*amount)
result= (total-3)
print(result)