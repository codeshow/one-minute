# for item in sequence:

print('*** Strings ***')
palavra = 'Python'
for letra in palavra:
  print(letra)

print('*** Listas ***')
lista = ['Python', 'Java', 'C#']
for linguagem in lista:
  print(linguagem)

print('*** Dicionarios ***')
dicionario = {'linguagem': 'Python', 'versão': 3.12, 'biblioteca': 'pandas'}
for chave in dicionario:
  print(f'{chave}: {dicionario[chave]}')
