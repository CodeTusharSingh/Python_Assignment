print("---------leap year---------")
yr = int(input("enter the the year you want to check for leap year: "))
if((yr % 4 == 0 and yr % 100 != 0) or (yr % 100 == 0 and yr % 400 == 0)):
    print(yr, "is a leap year ")
else:
    print(yr, "is not a leap year")

# A CODE BY TUSHAR SINGH