# Execute o programa e digite seu nome quando solicitado no console. Você verá que o programa para e aguarda a
# entrada do usuário ao usar a função input().

# Além disso, observe que podemos deixar um espaço no prompt usado na função input para facilitar a digitação
# do nome do usuário, pois teremos um espaço em branco entre o ponto de interrogação e início do texto do usuário.

name = input("Hello! What is your name: ")
print(f"Nice to meet you, {name}")

age = input("How old are you? ")
bot_age = 3
age_difference = int(age) - bot_age

print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

color = input("What's your favorite color? ")

print(f"Oh, {color} is a beautiful color!")
