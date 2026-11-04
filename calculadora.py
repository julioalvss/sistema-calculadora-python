print("Bem vindo à calculadora!")
input("Pressione Enter para continuar...")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
set = input("Escolha a operação desejada:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n")

if set == "1":
    resultado = n1 + n2
    print(f"O resultado da adição é: {resultado}")
elif set == "2":
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")
elif set == "3":
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")
elif set == "4":
    resultado = n1 / n2
    print(f"O resultado da divisão é: {resultado}")
else:
    print("Operação inválida. Por favor, escolha uma opção válida.")