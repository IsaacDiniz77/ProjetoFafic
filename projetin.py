# #fazenda sertao 
# #Douglas Alencar Pereira Vieira e Francisco Isaac Diniz Vidal P1 

# cliente = []
# adm = []


# while True: 
#     print("\n\nFazenda Sertao\n\n")

#     print("-"*50)

#     print('1-Criar uma conta ')
#     print('2- Fazer login ')
#     print("0- fechar programa ")

#     print("-"*50)
#     opcao1 = int(input("Digite a Opcao "))

#     if opcao1 == 0 : 
#         break

#     if opcao1 == 1 :
#         print("-"*50)

#         nome = input ( " Digite o seu nome completo : ")
#         email = input ( " Digite seu email : ")
#         usuario = input ( "Digite seu novo usuario : ")
#         senha = ("Digite sua Nova senha : ")
        
 
#         print("-"*50)

contatos = []

while True:
    print ("Bem vindo ao brasicont app ")
    print ("1- Criar contato  ")
    print ("2- Buscar contato por nome ")
    print ("3- listar contatos ")
    print ("4- alterar contato ")
    print ("5- Apagar contato ")
    print ("6- Buscar contato por numero ")
    print ("0- sair ")
    opcao = int(input("Digite a opcao : "))
    if opcao == 0 :
        break
    elif opcao == 1 :
        nome = input("digite o nome do contato : ")
        celular = int(input("digite o numero do celular :"))
        email = input("digite email : ")
        contatos.append([nome,celular,email])

    elif opcao == 2 : 
        print("-" * 50  )
        nome = input("Digite o nome do contato : ")
        for c in contatos : 
            if c [0] == nome :
                print(c[0],"-", c[1],"-", c[2]) 
                
        print("-" * 50  )
        
    elif opcao == 3 :

        print("-" * 50  )
        for c in contatos: 
            print(c[0],"-", c[1],"-", c[2])
        
        print("-" * 50  )

    
    elif opcao == 4 :
        print("-" * 50  )
        print ("Para alterar informe o dado abaixo ")
        celular = input(" Digite o celular do contato ")
        
        for posicao in range(len(contatos)):

            if contatos [posicao][1] == celular :

                nome = input("digite o novo nome: ")
                celular = input (" digite o novo celular :")
                email = input("digite o novo email :")
                contatos[posicao]= [nome,celular,email]

                print("\n\ncontato alterado com sucesso!\n\n")

        print("-" * 50  )
    elif opcao == 5 :
        print("-" * 50  )
        print ( "para apagar informe o dado abaixo")
        celular = input("digite o celular do contato que deseja apagar ")
        
        for posicao in range(len(contatos)):
            if contatos [posicao][1] == celular :
                contatos.pop(posicao)
                print (" contato removido com sucesso ")
                break
        print("-" * 50  )
    elif opcao == 6 : 

        print("-" * 50  )
        celular = input("Digite o numero do contato : ")
        for c in contatos : 
            if c [1] == celular :

                print(c[0],"-", c[1],"-", c[2])

        print("-" * 50  )