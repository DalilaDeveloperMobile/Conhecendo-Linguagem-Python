# Funções de Entrada e Saída:

# Entrada
nome = input("Informe o seu nome")
# Result: Informe o seu nome Dalila
idade = input("Informe a sua idade")
# Result: Informe a sua idade 28

# Saída
print(nome, idade) 
# Result: Dalila  28

print(nome, idade, end="...\n")
# Result: Dalila  28...
 
print(nome, idade, sep="#") 
# Result: Dalila# 28

print(nome, idade, sep="#", end="...\n")
# Result: Dalila# 28... 