length, width = 18, 7


def find_perimeter(l, w):
    return (l * 2) + (w * 2)


def find_area(l, w):
    return l * w


perimeter = find_perimeter(length, width)
area = find_area(length, width)
print("The perimeter is: {}".format(perimeter))
print("The area is: {}".format(area))
