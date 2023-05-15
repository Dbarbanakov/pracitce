def area_circle(r):
    return r**2 * 3.14


def area_triangle1(base, height):
    return base * height / 2


def area_triangle2(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5


print(area_circle(5))

print(area_triangle1(2, 5))
print(area_triangle2(4, 4, 2))
