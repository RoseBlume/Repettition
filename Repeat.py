from Repeat import R
#Example of use
c = 0
for i in range(len(R.repeat(5))):
    c += 1
    c = str(c)
    print("Count is " + c)
    c = int(c)
