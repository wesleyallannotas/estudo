num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
if num1 > num2:
    print('O \033[1;33mPRIMEIRO\033[m valor e maior')
elif num2 > num1:
    print('O \033[1;33mSEGUNDO\033[m valor e maior')
else:
    print('Nao existe valor maior, os dois sao \033[1;31mIGUAIS\033[m')
