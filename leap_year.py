def is_leap(year):
    leap = False
    
    # Write your logic here
    if  year >= 1900 and year <= 10**5:
        if ((year%4 == 0 and year%100 !=0) or year%400 ==0):
            leap =True
        else:
            leap = False
        return leap
    else:
        print ("Year out of range.")
        return leap
year = int(input())
print(is_leap(year))