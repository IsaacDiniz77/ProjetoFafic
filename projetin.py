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
            tipo = str(input(" Diga qual o tipo : A - ADM ou C - Cliente "))

            if tipo != 'A' or 'C':
                print('Tipo Invalido.')
            else:
                break

    p = ([nome,email,usuario,senha,tipo])
    perfis.append(p)


    print("-"*50)

    if opcao1 == 2 :
        print("-"*50)

        usuario = input ( "Digite seu usuario : ")    
        senha = input("Digite sua senha : ") 

        for p in perfis : 
            
            if p [2] == usuario and p [3] == senha:
                
                if p [4] == A:
                    print('Perfil ADM')

                elif p [4] == C:
                    print('Perfil CLIENTE')

                else:
                    print('Perfil Invalido!')

                
