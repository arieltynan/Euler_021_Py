# Euler Problem 021
# Completed 19 January 2021

n = 9999 #less than 10000
sumdivs = [] #sums of each numbers divisors
for i in range(0,n+1): #list of numbers 1-9,999
    div = [] #list of divisors
    for j in range(1,i): #finding divisors
        if (i % j == 0):
            div.append(j) 
    i = i + 1
    sumdivs.append(sum(div))     #sum of divisors of a number
for i in range(0,2*n):
    sumdivs.append(0)
amisum = 0 #sum of amicable numbers
i = 0
while i < n:
    #compare index to divisor sum 
    if i == sumdivs[sumdivs[i]] and i != sumdivs[i]:
        amisum = amisum + i
    i = i + 1
print(amisum)

