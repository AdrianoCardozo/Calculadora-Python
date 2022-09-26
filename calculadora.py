mensagem = "Insira a operação matemática que deseja."
mensagem += "\n+ para adição"
mensagem += "\n- para subtração"
mensagem += "\n* para multiplicação"
mensagem += "\n/ para divisão: "

operacao = input (mensagem)

num_1 = int (input("Entre o primeiro número: "))
num_2 = int (input("Entre o segundo número: "))

if operacao == '+':
    print(f"Operação: {num_1} {operacao} {num_2} = {num_1 + num_2} ")
   
elif operacao == '-':
    print(f"Operação: {num_1} {operacao} {num_2} = {num_1 - num_2} ")

elif operacao == '*':
    print(f"Operação: {num_1} {operacao} {num_2} = {num_1 * num_2} ")
   
elif operacao == '/':
    print(f"Operação: {num_1} {operacao} {num_2} = {num_1 / num_2} ")

else:
    print("Somente operações matemáticas, tente novamente")