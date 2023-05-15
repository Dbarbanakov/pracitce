def fib(n):
    if n in (1, 2):
        return n - 1

    return fib(n - 1) + fib(n - 2)


print(fib(5))
print(fib(6))
print(fib(7))


def fib_nums(n):
    nums = [0, 1]

    for i in range(1, n - 1):
        nums.append(nums[i - 1] + nums[i])

    for j in range(n):
        print(f"{j+1} - {nums[j]}")

    print(nums)


fib_nums(10)
