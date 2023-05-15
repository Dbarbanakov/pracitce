def leap_year_check(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print(leap_year_check(2000))
print(leap_year_check(1996))
print(leap_year_check(1900))
