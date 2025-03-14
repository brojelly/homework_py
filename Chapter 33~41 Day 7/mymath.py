import math

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

def rectangular_prism_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == "task_8":
    print("삼각형 넓이 (밑변=10, 높이=5):", triangle_area(10, 5))
    print("원의 넓이 (반지름=7):", circle_area(7))
    print("직육면체 넓이 (길이=4, 너비=3, 높이=2):", rectangular_prism_area(4, 3, 2))
