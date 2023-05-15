# initial deposit
n = 10000

# interest rate in percents
rate = 2 * 0.01

# time period - years
years = 5

for i in range(years):
    n += n * rate

print(int(n))
