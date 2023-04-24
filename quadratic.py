print("Welcome to Viswadev's quadratic roots calculator. Here you can find the roots of quadratic equation by providing the coefficients. ")
a = int(input("Enter the coefficient of x^2 "))
b = int(input("Enter the coefficient of x^1"))
c = int(input("Enter the coefficient of x^0"))
k = (b**2)-(4*a*c)
D = k**0.5
x1 = (-b + D)/(2*a)
x2 = (-b - D)/(2*a)
print("The roots of equation are:",x1 , x2 )
