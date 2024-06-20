# A ordem das instruções é importante. Após coletarmos a entrada e armazena-la em uma variável,
# podemos reutiliza-la. Coloque as linhas na ordem correta para usar a saída coletada na instrução de saída.
print("Whats is your name?")
name_input = input()
# Saída
print(f"Hi, {name_input}!")

# Também podemos adicionar um prompt adicional à função input. O prompt será exibido no console.
user_input = input("Enter your name: ")

# Se inserirmos um prompt adicional, o usuário começará a digitar na mesma linha em que o prompt é exibido no console.
# É por isso que é útil adicionar um espaço em branco no final do prompt usando a função input.
print(f"Thanks, {user_input}")

# podemos usar a função input quantas vezes quisermos.
user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
print(user_input_1)
print(user_input_2)

# A entrada é sempre do tipo string. Se quisermos usá-lo como um número, precisamos convertê-lo previamente para um
# número inteiro ou ponto flutuante.

user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
number1 = int(user_input_1)
number2 = int(user_input_2)
result = number1 + number2
print(f"The sum is {result}")

# Qual será a saída, assumindo uma entrada de 10?
age_string = input("Enter your age: ")

if int(age_string) < 21:
    print("Under 21")
else:
    print("21 or older.")

# Peça o nome do usuário e armazene-o na variável user_name.
user_name = input("Enter your name: ")

# Adicione os símbolos para coletar corretamente uma entrada de string do usuário.
user_input = input("Enter something: ")

# Use a função input para armazenar a entrada do usuário na variavel User_name.
user_name = input("Enter your name: ")

# Obtenha um valor do usuário e armazene-o na variável job.
job = input("Enter your job title:")
print(job)
