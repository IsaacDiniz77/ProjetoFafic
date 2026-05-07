#fazenda sertao 
#Douglas Alencar Pereira Vieira e Francisco Isaac Diniz Vidal P1 

perfis = [["douglas","douglas123","douglas123","douglas123","ADM"],["douglas","douglas123cliente","douglas123cliente","douglas123cliente","Cliente"]]



while True: 
    print("\n\nFazenda Sertao\n\n")

    print("-"*50)

    print('1- Criar uma conta ')
    print('2- Fazer login ')
    print("0- fechar programa ")

    print("-"*50)
    opcao1 = int(input("Digite a Opcão: "))

    if opcao1 != 1 or 2 or 0  :

        print ("Opçao invalida ! " * 3 )

    if opcao1 == 0 : 
        break

    if opcao1 == 1 :
        print("-"*50)

        while True:
            nome = input( " Digite o seu nome completo : ")

            if len(nome) < 4:
                print('Nome invalido.')
            else:
                break

        while True:
            email = input( " Digite seu email : ")

            if '@' not in email:
                print('Email invalido.')
            else:
                break

        while True:
            usuario = input ( "Digite seu novo usuario : ")

            if len(usuario) < 4:
                print('Usuario Invalido.')
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

                p = [nome,email,usuario,senha,tipo]
                perfis.append(p)
                break
            else:
                print('Tipo Invalido.')
               


    print("-"*50)

    if opcao1 == 2 :
        print("-"*50)
        while True:
            usuario = input ( "Digite seu usuario : ")
            
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
            
            if p [2] == usuario and p [3] == senha:
                
                if p [4] == 'A':

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
                        opcao1 = int(input("Digite a Opcão: "))

                    if opcao1 == 0:
                        break

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