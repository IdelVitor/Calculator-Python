def valores():
    
    numero1 = float(input('Me diga um numero: '))
    numero2 = float(input('Me diga o segundo numero para o cálculo:'))
    
    while True:
        operador = input('Me diga o operador que irá utilizar entre cálculo = *, soma = +, subtração = -, divisão = /: ')
        if operador not in ['*', '-', '/', '+']:
            print('Dado inválido, escreva novamente:')
            continue
        return numero1, numero2, operador

def calculo(numero1, numero2, operador):

    while True:
        if operador == '*':
            print(f'{numero1} * {numero2}: {numero1 * numero2}')
            break
        elif operador == '+':
            print(f'{numero1} + {numero2}: {numero1 + numero2}')
            break
        elif operador == '-':
            print(f'{numero1} - {numero2}: {numero1 - numero2}')
            break
        elif operador == '/':
            if numero2 != 0:
                print(f'{numero1} / {numero2} = {numero1 / numero2}')
            else:
                print('Divisão por zero não é permitida.')
            break

def sair():
    
    while True:
        
        sair = input('Se desejar sair, digite "s": ').strip().lower()
        if sair == 's':
            print('Obrigado por utilizar o app') 
            break
        elif sair == 'n':
            print('Você optou por continuar.')
            valores()
        else:
            print('Dado inválido, digite novamente!')


num1, num2, op = valores()
calculo(num1, num2, op)
sair()