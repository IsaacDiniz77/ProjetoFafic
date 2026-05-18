#fazenda sertao 
#Douglas Alencar Pereira Vieira e Francisco Isaac Diniz Vidal P1 

perfis = [["douglas","douglas@fazenda.com","douglas123","douglas123","A"],["douglas","douglascliente@fazenda.com","douglas123cliente","douglas123cliente","C"]]
rebanho = []
produtos = []
agendamentos = []
historico_compras = []


while True: 
    print("\n\nFazenda Sertao\n\n")
    print("-"*50)
    print('1- Criar uma conta ')
    print('2- Fazer login ')
    print("0- fechar programa ")
    print("-"*50)
    opcao1 = int(input("Digite a Opcão: "))

    if opcao1 == 0 : 
        break

    if opcao1 == 1 :
        print("-"*50)

        while True:
            nome = input(" Digite o seu nome completo : ")
            if len(nome) < 4:
                print('Nome invalido.')
            else:
                break

        while True:
            email = input(" Digite seu email : ")
            if '@' not in email:
                print('Email invalido.')
            else:
                break

        while True:
            usuario = input("Digite seu novo usuario : ")
            if len(usuario) < 4:
                print('Usuario Invalido.')
            else:
                ja_existe = False
                for pf in perfis:
                    if pf[2] == usuario:
                        ja_existe = True
                if ja_existe:
                    print('Usuario ja cadastrado.')
                else:
                    break

        while True:
            senha = input("Digite sua Nova senha : ")
            if len(senha) < 8:
                print('Senha com menos de oito caracteres.')
            else:
                break

        while True:
            tipo = input(" Diga qual o tipo : A = ADM ou C = Cliente: ").upper()
            if tipo == 'A' or tipo == 'C':
                p = [nome, email, usuario, senha, tipo]
                perfis.append(p)
                print('Conta criada com sucesso!')
                break
            else:
                print('Tipo Invalido.')

    print("-"*50)

    if opcao1 == 2 :
        print("-"*50)

        while True:
            usuario = input("Digite seu usuario : ")
            if len(usuario) < 4:
                print('Usuario Invalido.')
            else:
                break

        while True:
            senha = input("Digite sua senha : ")
            if len(senha) < 8:
                print('Senha Errada.')
            else:
                break

        for p in perfis :

            if p[2] == usuario and p[3] == senha:

                if p[4] == 'A':

                    while True:
                        print("\n\nFazenda Sertao\n\n")
                        print("\n\nPainel ADM\n\n")
                        print("-"*50)
                        print('1- Gerenciar Rebanho')
                        print('2- Gerenciar Producao e Derivados')
                        print('3- Lista de Estoque')
                        print('4- Remover Cliente do Painel')
                        print('5- Silagem')
                        print("0- Logout ")
                        print("-"*50)
                        opcao1 = int(input("Digite a Opcão: "))

                        if opcao1 == 0:
                            break

                        if opcao1 == 1:

                            while True:
                                print("\n\nGerenciar Rebanho\n\n")
                                print("-"*50)
                                print('1- Cadastrar Animal')
                                print('2- Buscar Animal')
                                print('3- Atualizar Status')
                                print('4- Remover Animal')
                                print('5- Listar Rebanho')
                                print('0- Voltar')
                                print("-"*50)
                                opcao_rebanho = int(input("Digite a Opcão: "))

                                if opcao_rebanho == 0:
                                    break

                                if opcao_rebanho == 1:
                                    print("-"*50)
                                    while True:
                                        animal = input('Tipo (BL-Bovino de Leite / C-Caprino / O-Ovino / SL-Suino): ').upper()
                                        if animal == 'BL':
                                            nome_tipo = 'Bovino de Leite'
                                            break
                                        elif animal == 'C':
                                            nome_tipo = 'Caprino'
                                            break
                                        elif animal == 'O':
                                            nome_tipo = 'Ovino'
                                            break
                                        elif animal == 'SL':
                                            nome_tipo = 'Suino/Leitao'
                                            break
                                        else:
                                            print('Tipo invalido.')

                                    while True:
                                        identificacao = input('Brinco do animal (ex: 001): ')
                                        brinco_existe = False
                                        for a in rebanho:
                                            if a[1] == identificacao:
                                                brinco_existe = True
                                        if brinco_existe:
                                            print('Brinco ja cadastrado. Digite outro.')
                                        else:
                                            break

                                    while True:
                                        status_cod = input('Status (V-Vender / L-Lactacao / E-Engorda): ').upper()
                                        if status_cod == 'V':
                                            status = 'Para Venda'
                                            break
                                        elif status_cod == 'L':
                                            status = 'Em Lactacao'
                                            break
                                        elif status_cod == 'E':
                                            status = 'Para Engorda'
                                            break
                                        else:
                                            print('Status invalido.')

                                    rebanho.append([nome_tipo, identificacao, status])
                                    print('Animal cadastrado com sucesso!')

                                if opcao_rebanho == 2:
                                    print("-"*50)
                                    brinco_busca = input('Brinco do animal: ')
                                    encontrado = False
                                    for a in rebanho:
                                        if a[1] == brinco_busca:
                                            print('Tipo: ' + a[0] + ' | Brinco: ' + a[1] + ' | Status: ' + a[2])
                                            encontrado = True
                                    if encontrado == False:
                                        print('Animal nao encontrado.')
                                    print("-"*50)

                                if opcao_rebanho == 3:
                                    print("-"*50)
                                    if len(rebanho) == 0:
                                        print('Nenhum animal cadastrado.')
                                    else:
                                        for i in range(len(rebanho)):
                                            a = rebanho[i]
                                            print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                                        print("-"*50)
                                        while True:
                                            idx_str = input('Numero do animal para atualizar: ')
                                            if idx_str.isdigit():
                                                idx_at = int(idx_str) - 1
                                                if 0 <= idx_at < len(rebanho):
                                                    break
                                            print('Numero invalido.')
                                        while True:
                                            novo_status_cod = input('Novo status (V-Vender / L-Lactacao / E-Engorda): ').upper()
                                            if novo_status_cod == 'V':
                                                rebanho[idx_at][2] = 'Para Venda'
                                                break
                                            elif novo_status_cod == 'L':
                                                rebanho[idx_at][2] = 'Em Lactacao'
                                                break
                                            elif novo_status_cod == 'E':
                                                rebanho[idx_at][2] = 'Para Engorda'
                                                break
                                            else:
                                                print('Status invalido.')
                                        print('Animal atualizado com sucesso!')

                                if opcao_rebanho == 4:
                                    print("-"*50)
                                    if len(rebanho) == 0:
                                        print('Nenhum animal cadastrado.')
                                    else:
                                        for i in range(len(rebanho)):
                                            a = rebanho[i]
                                            print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                                        print("-"*50)
                                        while True:
                                            idx_str = input('Numero do animal para remover: ')
                                            if idx_str.isdigit():
                                                idx_rm = int(idx_str) - 1
                                                if 0 <= idx_rm < len(rebanho):
                                                    break
                                            print('Numero invalido.')
                                        a_removido = rebanho.pop(idx_rm)
                                        print('Animal ' + a_removido[0] + ' brinco ' + a_removido[1] + ' removido!')

                                if opcao_rebanho == 5:
                                    print("-"*50)
                                    if len(rebanho) == 0:
                                        print('Nenhum animal cadastrado.')
                                    else:
                                        for i in range(len(rebanho)):
                                            a = rebanho[i]
                                            print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                                    print("-"*50)

                        if opcao1 == 2:
                            while True:
                                print("\n\nGerenciar Producao e Derivados\n\n")
                                print("-"*50)
                                print('1- Registrar Producao Diaria de Leite e Fabricar Queijo')
                                print('2- Alterar Produto no Estoque')
                                print('0- Voltar')
                                print("-"*50)
                                opcao_prod = int(input("Digite a Opcão: "))

                                if opcao_prod == 0:
                                    break

                                if opcao_prod == 1:
                                    print("-"*50)

                                    while True:
                                        data = input('Data da ordenha (dd/mm/aaaa): ')
                                        dataFormada = data.split('/')
                                        if len(dataFormada) == 3 and dataFormada[0].isdigit() and dataFormada[1].isdigit() and dataFormada[2].isdigit():
                                            break
                                        print('Data invalida.')

                                    litros_dia = int(input('Litros de leite ordenhados no dia: '))
                                    litros_restantes = litros_dia

                                    print("-"*50)
                                    print('Producao registrada: ' + str(litros_dia) + 'L em ' + data)
                                    fab = input('Deseja fabricar queijo com esse leite? (S/N): ').upper()

                                    if fab == 'S':
                                        while litros_restantes > 0:
                                            print("-"*50)
                                            print('Litros disponiveis: ' + str(litros_restantes) + 'L')
                                            print('QC  - Queijo Coalho    (8L = 1kg)')
                                            print('QM  - Queijo Mussarela (4L = 1kg)')
                                            print('QMT - Queijo Manteiga  (6L = 1kg)')
                                            print('0   - Parar fabricacao')
                                            print("-"*50)

                                            while True:
                                                tipo_queijo = input('Tipo de queijo: ').upper()
                                                if tipo_queijo == 'QC':
                                                    nome_queijo = 'Queijo Coalho'
                                                    litros_por_kg = 8
                                                    break
                                                elif tipo_queijo == 'QM':
                                                    nome_queijo = 'Queijo Mussarela'
                                                    litros_por_kg = 4
                                                    break
                                                elif tipo_queijo == 'QMT':
                                                    nome_queijo = 'Queijo Manteiga'
                                                    litros_por_kg = 6
                                                    break
                                                elif tipo_queijo == '0':
                                                    break
                                                else:
                                                    print('Tipo invalido.')

                                            if tipo_queijo == '0':
                                                break

                                            kg_produzido = litros_restantes // litros_por_kg
                                            litros_usados = kg_produzido * litros_por_kg
                                            litros_restantes = litros_restantes - litros_usados

                                            print("-"*50)
                                            print('Kg produzido  : ' + str(kg_produzido) + 'kg de ' + nome_queijo)
                                            print('Litros usados : ' + str(litros_usados) + 'L')
                                            print('Litros restam : ' + str(litros_restantes) + 'L')
                                            print("-"*50)

                                            if kg_produzido > 0:
                                                valorptd = float(input('Valor de venda por kg: R$ '))
                                                produtos.append([nome_queijo, kg_produzido, valorptd])
                                                print(str(kg_produzido) + 'kg de ' + nome_queijo + ' adicionado ao estoque!')
                                            else:
                                                print('Litros insuficientes para 1kg de ' + nome_queijo + '.')
                                                break

                                        print("-"*50)
                                        print('Fabricacao encerrada. Litros restantes: ' + str(litros_restantes) + 'L')

                                if opcao_prod == 2:
                                    print("-"*50)
                                    if len(produtos) == 0:
                                        print('Nenhum produto cadastrado.')
                                    else:
                                        for i in range(len(produtos)):
                                            p = produtos[i]
                                            print(str(i+1) + '- ' + p[0] + ' | ' + str(p[1]) + 'kg | R$ ' + str(p[2]) + '/kg')
                                        print("-"*50)
                                        while True:
                                            idx_str = input('Numero do produto a alterar: ')
                                            if idx_str.isdigit():
                                                idx_alt = int(idx_str) - 1
                                                if 0 <= idx_alt < len(produtos):
                                                    break
                                            print('Numero invalido.')
                                        nova_qtd = int(input('Nova quantidade kg: '))
                                        novo_valor = float(input('Novo valor R$: '))
                                        produtos[idx_alt][1] = nova_qtd
                                        produtos[idx_alt][2] = novo_valor
                                        print('Produto atualizado com sucesso!')

                        if opcao1 == 3:
                            print("-"*50)
                            print('\n[ Rebanho ]')
                            if len(rebanho) == 0:
                                print('Nenhum animal cadastrado.')
                            else:
                                for i in range(len(rebanho)):
                                    a = rebanho[i]
                                    print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                            print("-"*50)
                            print('\n[ Produtos e Derivados ]')
                            if len(produtos) == 0:
                                print('Nenhum produto cadastrado.')
                            else:
                                for i in range(len(produtos)):
                                    p = produtos[i]
                                    print(str(i+1) + '- ' + p[0] + ' | ' + str(p[1]) + 'kg | R$ ' + str(p[2]) + '/kg')
                            print("-"*50)

                        if opcao1 == 4:
                            print("-"*50)
                            clientes_idx = []
                            for i in range(len(perfis)):
                                if perfis[i][4] == 'C':
                                    clientes_idx.append(i)
                            if len(clientes_idx) == 0:
                                print('Nenhum cliente cadastrado.')
                            else:
                                for j in range(len(clientes_idx)):
                                    c = perfis[clientes_idx[j]]
                                    print(str(j+1) + '- ' + c[0] + ' | Usuario: ' + c[2])
                                print("-"*50)
                                while True:
                                    idx_str = input('Numero do cliente a remover: ')
                                    if idx_str.isdigit():
                                        escolha = int(idx_str) - 1
                                        if 0 <= escolha < len(clientes_idx):
                                            break
                                    print('Numero invalido.')
                                removido = perfis.pop(clientes_idx[escolha])
                                print('Cliente ' + removido[0] + ' removido com sucesso!')

                        if opcao1 == 5:
                            print("-"*50)
                            while True:
                                data = input('Data: (dd/mm/aaaa) ')
                                dataFormada = data.split('/')
                                if len(dataFormada) == 3 and dataFormada[0].isdigit() and dataFormada[1].isdigit() and dataFormada[2].isdigit():
                                    break
                                print('Data invalida.')
                            kg_silagem = int(input('Kg de silagem consumida: '))
                            print('Silagem de ' + str(kg_silagem) + 'kg registrada em ' + data + '!')





            elif p [4] == 'C':
                    print('Perfil CLIENTE')

                    while True:
                        print("\n\nFazenda Sertao\n\n")
                        print("\n\nPainel Cliente\n\n")

                        print("-"*50)

                        print('1- Comprar Produtos')
                        print('2- Rebanho')
                        print('3- Silagem')
                        print("0- fechar programa ")

                        print("-"*50)
                        opcao1 = int(input("Digite a Opcão: "))

                        if opcao1 == 0:
                            break
                            
                    
                            
                        

            else:
                print('Perfil Invalido!')


while True:
    print("\n\nFazenda Sertao\n\n")
    print("\n\nPainel ADM\n\n")

    print("-"*50)

    print('1- Inserir Produto')
    print('2- Alterar Produtos Do Estoque')
    print('3- Gerenciar Rebanho')
    print('4- Retirar Cliente do Painel')
    print('5- Lista de Estoque')
    print('6- Silagem')
    print("0- fechar programa ")

    print("-"*50)

                




data = input('Data: (dd/mm/aaaa)')         
dataFormada = data.split('/')
dia = dataFormada [0]
mes = dataFormada [1]
ano = dataFormada [2]


        
        
        













# contatos = []

# while True:
#     print ("Bem vindo ao brasicont app ")
#     print ("1- Criar contato  ")
#     print ("2- Buscar contato por nome ")
#     print ("3- listar contatos ")
#     print ("4- alterar contato ")
#     print ("5- Apagar contato ")
#     print ("6- Buscar contato por numero ")
#     print ("0- sair ")
#     opcao = int(input("Digite a opcao : "))
#     if opcao == 0 :
#         break
#     elif opcao == 1 :
#         nome = input("digite o nome do contato : ")
#         celular = int(input("digite o numero do celular :"))
#         email = input("digite email : ")
#         contatos.append([nome,celular,email])

#     elif opcao == 2 : 
#         print("-" * 50  )
#         nome = input("Digite o nome do contato : ")
#         for c in contatos : 
#             if c [0] == nome :
#                 print(c[0],"-", c[1],"-", c[2]) 
                
#         print("-" * 50  )
        
#     elif opcao == 3 :

#         print("-" * 50  )
#         for c in contatos: 
#             print(c[0],"-", c[1],"-", c[2])
        
#         print("-" * 50  )

    
#     elif opcao == 4 :
#         print("-" * 50  )
#         print ("Para alterar informe o dado abaixo ")
#         celular = input(" Digite o celular do contato ")
        
#         for posicao in range(len(contatos)):

#             if contatos [posicao][1] == celular :

#                 nome = input("digite o novo nome: ")
#                 celular = input (" digite o novo celular :")
#                 email = input("digite o novo email :")
#                 contatos[posicao]= [nome,celular,email]

#                 print("\n\ncontato alterado com sucesso!\n\n")

#         print("-" * 50  )
#     elif opcao == 5 :
#         print("-" * 50  )
#         print ( "para apagar informe o dado abaixo")
#         celular = input("digite o celular do contato que deseja apagar ")
        
#         for posicao in range(len(contatos)):
#             if contatos [posicao][1] == celular :
#                 contatos.pop(posicao)
#                 print (" contato removido com sucesso ")
#                 break
#         print("-" * 50  )
#     elif opcao == 6 : 

#         print("-" * 50  )
#         celular = input("Digite o numero do contato : ")
#         for c in contatos : 
#             if c [1] == celular :

#                 print(c[0],"-", c[1],"-", c[2])

#         print("-" * 50  )
