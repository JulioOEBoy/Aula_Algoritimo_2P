a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
print("O valor de delta é:", delta)

x_vertice = -b / (2*a)
y_vertice = a * x_vertice**2 + b * x_vertice + c
print(f"O vértice da parábola está em ({x_vertice}, {y_vertice})")