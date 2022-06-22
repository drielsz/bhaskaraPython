a = float(input("Digite o valor para a: "))
b = float(input("Digite o valor para b: "))
c = float(input("Digite o valor para c: "))

delta = (b**2) - 4 * a * c
raiz_delta = delta ** 0.5
print("Raiz de delta: ", raiz_delta)
if a == 0:
    print("Valor do A:", a)
    print("O valor de A foi igual 0. Sem continuação.")
if delta < 0:
    print("Valor de delta: ", delta)
    print("Sem raiz")
else:
    x1 = (-b + raiz_delta ) / (2 * a)
    x2 = (-b - raiz_delta ) / (2 *a)
    print("Valor de x1:", x1 , "Valor de x2:", x2)