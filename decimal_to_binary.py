def dectobin(n):
    binary_reverse = ""

    while n > 0:
        if n % 2 == 0:
            n = n / 2
            binary_reverse += "0"
        else:
            n = (n - 1) / 2
            binary_reverse += "1"

    binary = "0b"
    for x in reversed(binary_reverse):
        binary += x

    return binary


print(dectobin(128))
print(bin(128))

print(dectobin(127))
print(bin(127))
