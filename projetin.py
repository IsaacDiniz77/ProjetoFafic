#fazenda sertao 
#Douglas Alencar Pereira Vieira e Francisco Isaac Diniz Vidal P1 

perfis = [["douglas","douglas123","douglas123","douglas123","ADM"],["douglas","douglas123cliente","douglas123cliente","douglas123cliente","Cliente"]]



while True: 
    print("\n\nFazenda Sertao\n\n")

    print("-"*50)

    print('1-Criar uma conta ')
    print('2- Fazer login ')
    print("0- fechar programa ")

    print("-"*50)
    opcao1 = int(input("Digite a Opcao "))

    if opcao1 == 0 : 
        break

    if opcao1 == 1 :
        print("-"*50)

        nome = input ( " Digite o seu nome completo : ")
        email = input ( " Digite seu email : ")
        usuario = input ( "Digite seu novo usuario : ")
        senha = input("Digite sua Nova senha : ")
        tipo = input (" Diga qual o tipo : ADM ou Cliente ").upper 
        perfis.append([nome,email,usuario,senha,tipo])

        print("-"*50)

    if opcao1 == 2 :
        print("-"*50)

        usuario = input ( "Digite seu usuario : ")    
        senha = input("Digite sua senha : ") 

        for p in perfis : 
            
            if p [2] == usuario and p [3] == senha:
                
                if p [4] == 1:
                    print('Perfil ADM')

                elif p [4] == 2:
                    print('Perfil CLIENTE')

                else:
                    print('Perfil Invalido!')

