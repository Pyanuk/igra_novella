#2код
def rectangle_area(width, height):
    return width * height
width = 5
height = 10
area = rectangle_area(width, height)
print(f"Площадь прямоугольника с шириной {width} и высотой {height} равна {area}.")

#3 код
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
result = is_even(2)
print(result)

#4код
def sum_digits(number):
    total = 0
    number_str = str(number)
    for digit in number_str:
        total += int(digit)

    return total
result = sum_digits(125)
print(result)
