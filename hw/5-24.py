PI = 3.141592653589793
E = 3
e0 = 8.85*(10**-12)
e = 1

r1 = int(input("r1: "))
q_max = E/(4*PI*e0*e*(r1**2))
f_min = E*r1
print("r1 >")
print("q_max", q_max)
print("f_min", f_min)

r2 = int(input("r2: "))
q_max = E/(4*PI*e0*e*(r2**2))
f_min = E*r2
print("r2 >")
print("q_max", q_max)
print("f_min", f_min)

r3 = int(input("r3: "))
q_max = E/(4*PI*e0*e*(r3**2))
f_min = E*r3
print("r3 >")
print("q_max", q_max)
print("f_min", f_min)
