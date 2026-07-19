#Crie um assistente financeiro que converse com seu cliente e oriente. # 


transacoes = ['luz', 'água', 'mercado', 'lazer']
preco = [350,100,250,500]
data = ['03/06/26', '25/04/26', '26/06/26', '31/04/06']

#menu de opção  
while True:
    print('Olá eu sou o primeiro Assistente Financeiro')
    print('\n' + '='*30)
    print('1- Visualizar o estrato da conta')
    print('2- Adicionar nova Transação')
    print('3- ver Total de Gastos')
    print('q sair do sistema')
    print('\n'+'='*30)
    opcao=input('Escolha uma opção ').strip().lower()
    if opcao == 'q':
          print('\n Saindo do sistema')
          break
    elif opcao=='1':
         print('\n =1- Visualizar o extrato atual')   
         for i, item, valor, dt in zip(range(len(transacoes)), transacoes, preco, data):
           print(f'ID {i} | {item.capitalize()} | R$ {valor:2f} | Data: {dt}')
    elif opcao=='2':
        print('\n Cadastrar uma nova Transição')
        novo_item=input('Digite o nome do gasto(ex: Luz)')
        novo_preco=float(input('informe o preço'))
        nova_data=input('digite a data(ex 13/06/26)')
        
        transacoes.append(novo_item)
        preco.append(novo_preco)
        data.append(nova_data)    
        print(f"\nSucesso!' {novo_item}' foi adicionado. ")

    elif opcao=='3':
        print('O Total é: ')
        total=sum(preco)
        print()
        print(f'O total acomulado da suas despesas é: R$ {total:.2f}')
    else:
        print('Opção inválida!, por favor, escolha 1, 2, 3 ou q.')
