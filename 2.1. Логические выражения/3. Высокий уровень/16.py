X, Y = 3, 1

# ((x, y), radius)
C1 = ((0, 0), 1)
C2 = ((2, 0), 2)

def is_in_circle(x: float, y: float, c: set):
    return (x-c[0][0])**2 + (y-c[0][1])**2 <= c[1]**2

out = is_in_circle(X, Y, C2)
print(out)
