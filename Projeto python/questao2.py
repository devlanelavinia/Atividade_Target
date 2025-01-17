# Questão 2: Fibonacci e verificação
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == b or num == 0

# Entrada do número
number = int(input("Informe um número: "))

if is_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} NÃO pertence à sequência de Fibonacci.")
