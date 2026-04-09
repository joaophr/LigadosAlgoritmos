n = 0
somat = 0
for i in range(343):
    somal = 0
    for c in range (i):
        print (n, end= " ")
        somal += n
    somat += somal
    print ("= " + str(somal))
    print ("\n")
    n += 1
print ("Soma total: " + str(somat))
