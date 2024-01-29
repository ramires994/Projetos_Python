print('Bem vindo a Urna, selecione seu candidato conforme a instrução abaixo:')
print('1 - Candidato 1')
print('2 - Candidato 2')
print('3 - Candidato 3')
print('9 - Voto nulo')

escolha = int(input('Informe o número de seu candidato ou 0 para sair: '))

c1 = 0
c2 = 0
c3 = 0
cont = 0

while (escolha != 0):
     if(escolha == 1):
          c1 += 1
     
     elif(escolha == 2):
          c2 +=1

     elif(escolha == 3):
          c3 +=1
     elif(escolha == 9):
          cont +=1
     else:
          print('Por favor escolha um numero válido de 1 a 3.')
          
     escolha = int(input('Informe o número de seu candidato ou 0 para sair: '))


print(f"o Candidato 1 teve {c1} votos")
print(f"o Candidato 2 teve {c2} votos")
print(f"o Candidato 3 teve {c3} votos")
print(f"Obtivemos {cont} votos nulos")

if(c1 > c2 and c1> c3):
     print('O Candidato 1 venceu!')
elif(c2> c1 and c2 > c3):
     print('O Candidato 2 venceu!')
elif(c3 >c2 and c3> c1):
     print('O Candidato 3 venceu!')
else:
     print('Empate!')