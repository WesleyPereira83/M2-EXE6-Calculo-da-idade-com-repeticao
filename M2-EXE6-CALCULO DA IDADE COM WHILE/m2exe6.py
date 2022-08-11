#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. 
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
#no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e 
# continuará perguntando até que um valor correto seja preenchido.

ok = False

while (ok==False):

    try:
        nome = str(input('Insira seu nome completo:\n\n'))
        print(' ')
        ano = int(input('Digite seu ano de nascimento com 4 dígitos:\n\n'))
        idade = 2022 - ano

  
        if ano >= 1922 and ano<= 2021:
            print(' ')
            print(f'Avaliação => Ano de {ano} validado!' )
            print(' ')
            print(f'{nome} você completou ou completará:', idade, 'ano(s) de idade.' )  
            break
        
        else:
            print(f'Avaliação => Ano inválido!' )
            print(' ')     
      
    except (ValueError):
            print(' ')  
            print('Tipo de dados não corresponde ou não é válido.')
            print(' ')
  