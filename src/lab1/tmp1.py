def triangle_shape(height):
    triangle = ""
    for i in range(height):
        for j in range(height - i):
            triangle += " "
        for j in range(2 * i + 1):
            triangle += "x"
        for j in range(height - i):
            triangle += " "
        triangle += "\n"
    return triangle


print(triangle_shape(5))
