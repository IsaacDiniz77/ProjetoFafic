#fazenda sertao 
#Douglas Alencar Pereira Vieira e Francisco Isaac Diniz Vidal P1 
#funcoes 
def criarconta ():  
        
    while True:
        nome = input(" Digite o seu nome completo : ")
        if len(nome) < 4:
            print('Nome invalido.')
        else:
            break

    while True:
        email = input(" Digite seu email : ")
        if '@gmail.com' not in email and '@hotmail.com' not in email and '@outlook.com' not in email:
            print('Email invalido.')
        else:
            break

    while True:
        usuario = input("Digite seu novo usuario : ")
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
            p = [nome, email, usuario, senha, tipo]
            perfis.append(p)
            print('Conta criada com sucesso!')
            break
        else:
            print('Tipo Invalido.') 


def fazerloguin ():

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

                return 'A'
            
            if p[4] == 'C': 
                
                return "C"
    return None

perfis = [["douglas","douglas@fazenda.com","douglas123","douglas123","A"],["douglas","douglascliente@fazenda.com","douglas123cliente","douglas123cliente","C"]]
rebanho = []
produtos = []
agendamentos = []
historico_compras = []
aval = []

while True: 
    print("\n\nFazenda Sertao\n\n")
    print("-"*50)
    print('1- Criar uma conta ')
    print('2- Fazer login ')
    print("0- fechar programa ")
    print("-"*50)
    opcao1 = int(input("Digite a Opcao: "))

    if opcao1 == 0 : 
        break

    if opcao1 == 1 :
        criarconta()

    if opcao1 == 2 :

        verificacaoAdmouCliente = fazerloguin()
        
        while  verificacaoAdmouCliente == 'A':
            print("\n\nFazenda Sertao\n\n")
            print("\n\nPainel ADM\n\n")
            print("-"*50)
            print('1- Gerenciar Rebanho\n' \
                  '2- Gerenciar Producao e Derivados\n' \
                  '3- Lista de Estoque\n'
                  '4- Remover Cliente do Painel\n'
                  '5- Silagem\n'
                  '0- Sair Painel ADM \n'
                  )
            print("-"*50)
            opcao1 = int(input("Digite a Opcao: "))

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
                    print('0- Voltar para aba principal')
                    print("-"*50)
                    opcao_rebanho = int(input("Digite a Opcao: "))

                    if opcao_rebanho == 0:
                        break

                    if opcao_rebanho == 1:
                      
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
                            brincoexiste = False
                            for a in rebanho:
                                if a[1] == identificacao:
                                    brincoexiste = True
                            if brincoexiste:
                                print('Brinco ja cadastrado. Digite outro.')
                            else:
                                break

                        while True:
                            status = input('Status (V-Vender / L-Lactacao / E-Engorda): ').upper()
                            if status == 'V':
                                status = 'Para Venda'
                                break
                            elif status == 'L':
                                status = 'Em Lactacao'
                                break
                            elif status == 'E':
                                status = 'Para Engorda'
                                break
                            else:
                                print('Status invalido.')

                        rebanho.append([nome_tipo, identificacao, status])
                        print('Animal cadastrado com sucesso!')


                    if opcao_rebanho == 2:
                        
                        brincobusca = input('Brinco do animal: ')
                        encontrado = False
                        for a in rebanho:
                            if a[1] == brincobusca:
                                print('Tipo: ' + a[0] + ' | Brinco: ' + a[1] + ' | Status: ' + a[2])
                                encontrado = True
                        if encontrado == False:
                            print('Animal nao encontrado.')
                     


                    if opcao_rebanho == 3:
                       
                        if len(rebanho) == 0:
                            print('Nenhum animal cadastrado.')
                        else:
                            for i in range(len(rebanho)):
                                a = rebanho[i]
                                print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                           
                            while True:
                                numeroanimal = input('Numero do animal para atualizar: ')
                                numerovalido = False
                                for i in range(len(rebanho)):
                                    if numeroanimal == str(i+1):
                                        numerovalido = True
                                        numeroatt = i
                                if numerovalido:
                                    break
                                else:
                                    print('Numero invalido.')
                            while True:
                                novostatus = input('Novo status (V-Vender / L-Lactacao / E-Engorda): ').upper()
                                if novostatus == 'V':
                                    rebanho[numeroatt][2] = 'Para Venda'
                                    break
                                elif novostatus == 'L':
                                    rebanho[numeroatt][2] = 'Em Lactacao'
                                    break
                                elif novostatus == 'E':
                                    rebanho[numeroatt][2] = 'Para Engorda'
                                    break
                                else:
                                    print('Status invalido.')
                            print('Animal atualizado com sucesso!')


                    if opcao_rebanho == 4:
                        
                        if len(rebanho) == 0:
                            print('Nenhum animal cadastrado.')
                        else:
                            for i in range(len(rebanho)):
                                a = rebanho[i]
                                print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                            
                            while True:
                                numeroremover = input('Numero do animal para remover: ')
                                numerovalido = False
                                for i in range(len(rebanho)):
                                    if numeroremover == str(i+1):
                                        numerovalido = True
                                        numeroatt = i
                                if numerovalido:
                                    break
                                else:
                                    print('Numero invalido.')
                            animalremovido = rebanho.pop(numeroatt)
                            print('Animal ' + animalremovido[0] + ' brinco ' + animalremovido[1] + ' removido!')


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
                    opcaoprod = int(input("Digite a Opcao: "))

                    if opcaoprod == 0:
                        break

                    
                    if opcaoprod == 1:
                        print("-"*50)

                        while True:
                            data = input('Data da ordenha (dd/mm/aaaa): ')
                            dataFormada = data.split('/')
                            datavalida = False
                            if len(dataFormada) == 3:
                                validodia = True
                                validomes = True
                                validoano = True
                                for c in dataFormada[0]:
                                    if c < '0' or c > '9':
                                        validodia = False
                                for c in dataFormada[1]:
                                    if c < '0' or c > '9':
                                        validomes = False
                                for c in dataFormada[2]:
                                    if c < '0' or c > '9':
                                        validoano = False
                                if validodia and validomes and validoano:
                                    datavalida = True
                            if datavalida:
                                break
                            else:
                                print('Data invalida.')

                        litrosdia = int(input('Litros de leite ordenhados no dia: '))
                        litrosrestantes = litrosdia

                        print("-"*50)
                        print('Producao registrada: ' + str(litrosdia) + 'L em ' + data)
                        fab = input('Deseja fabricar queijo com esse leite? (S/N): ').upper()

                        if fab == 'S':
                            while litrosrestantes > 0:
                                print("-"*50)
                                print('Litros disponiveis: ' + str(litrosrestantes) + 'L')
                                print('QC  - Queijo Coalho    (8L = 1kg)')
                                print('QM  - Queijo Mussarela (4L = 1kg)')
                                print('QMT - Queijo Manteiga  (6L = 1kg)')
                                print('0   - Parar fabricacao')
                                print("-"*50)

                                while True:
                                    tipoqueijo = input('Tipo de queijo: ').upper()
                                    if tipoqueijo == 'QC':
                                        nomequeijo = 'Queijo Coalho'
                                        litrosporkg = 8
                                        break
                                    elif tipoqueijo == 'QM':
                                        nomequeijo = 'Queijo Mussarela'
                                        litrosporkg = 4
                                        break
                                    elif tipoqueijo == 'QMT':
                                        nomequeijo = 'Queijo Manteiga'
                                        litrosporkg = 6
                                        break
                                    elif tipoqueijo == '0':
                                        break
                                    else:
                                        print('Tipo invalido.')

                                if tipoqueijo == '0':
                                    break

                                kgproduzido = litrosrestantes // litrosporkg
                                litrosusados = kgproduzido * litrosporkg
                                litrosrestantes = litrosrestantes - litrosusados

                                print("-"*50)
                                print('Kg produzido  : ' + str(kgproduzido) + 'kg de ' + nomequeijo)
                                print('Litros usados : ' + str(litrosusados) + 'L')
                                print('Litros restam : ' + str(litrosrestantes) + 'L')
                                print("-"*50)

                                if kgproduzido > 0:
                                    valorptd = float(input('Valor de venda por kg: R$ '))
                                    produtos.append([nomequeijo, kgproduzido, valorptd])
                                    print(str(kgproduzido) + 'kg de ' + nomequeijo + ' adicionado ao estoque!')
                                else:
                                    print('Litros insuficientes para 1kg de ' + nomequeijo + '.')
                                    break

                            print("-"*50)
                            print('Fabricacao encerrada. Litros restantes: ' + str(litrosrestantes) + 'L')


                    if opcaoprod == 2:
                        print("-"*50)
                        if len(produtos) == 0:
                            print('Nenhum produto cadastrado.')
                        else:
                            for i in range(len(produtos)):
                                pr = produtos[i]

                                print(str(i+1) + '- ' + pr[0] + ' | ' + str(pr[1]) + 'kg | R$ ' + str(pr[2]) + '/kg')
                            print("-"*50)
                            while True:
                                produtoalterar = input('Numero do produto a alterar: ')
                                ptdvalido = False
                                for i in range(len(produtos)):
                                    if produtoalterar == str(i+1):
                                        ptdvalido = True
                                        ptdatt = i
                                if ptdvalido:
                                    break
                                else:
                                    print('Numero invalido.')
                            novaqtd = int(input('Nova quantidade kg: '))
                            novovalor = float(input('Novo valor R$: '))
                            produtos[ptdatt][1] = novaqtd
                            produtos[ptdatt][2] = novovalor
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
                        pr = produtos[i]
                        print(str(i+1) + '- ' + pr[0] + ' | ' + str(pr[1]) + 'kg | R$ ' + str(pr[2]) + '/kg')
                print("-"*50)


            if opcao1 == 4:
                print("-"*50)
                clientes = []
                for i in range(len(perfis)):
                    if perfis[i][4] == 'C':
                        clientes.append(i)
                if len(clientes) == 0:
                    print('Nenhum cliente cadastrado.')
                else:
                    for j in range(len(clientes)):
                        c = perfis[clientes[j]]
                        print(str(j+1) + '- ' + c[0] + ' | Usuario: ' + c[2])
                    print("-"*50)
                    while True:
                        numerocliente = input('Numero do cliente a remover: ')
                        clientevalido = False
                        for j in range(len(clientes)):
                            if numerocliente == str(j+1):
                                clientevalido = True
                                escolha = j
                        if clientevalido:
                            break
                        else:
                            print('Numero invalido.')
                    removido = perfis.pop(clientes[escolha])
                    print('Cliente ' + removido[0] + ' removido com sucesso!')


            if opcao1 == 5:
                print("-"*50)
                while True:
                    data = input('Data: (dd/mm/aaaa) ')
                    dataFormada = data.split('/')
                    datavalida = False
                    if len(dataFormada) == 3:
                        validodia = True
                        validomes = True
                        validoano = True
                        for c in dataFormada[0]:
                            if c < '0' or c > '9':
                                validodia = False
                        for c in dataFormada[1]:
                            if c < '0' or c > '9':
                                validomes = False
                        for c in dataFormada[2]:
                            if c < '0' or c > '9':
                                validoano = False
                        if validodia and validomes and validoano:
                            datavalida = True
                    if datavalida:
                        break
                    else:
                        print('Data invalida.')
                kgsilagem = int(input('Kg de silagem consumida: '))
                print('Silagem de ' + str(kgsilagem) + 'kg registrada em ' + data + '!')
        
        while verificacaoAdmouCliente == 'C' :
            print("-"*50)
            print("\n\nPainel Cliente\n\n")
            print('1- Comprar Produtos\n' \
                  '2- Ver Rebanho\n' \
                  '3- Historico de Compras\n' \
                  '4- Agendar Retirada/Transporte\n' \
                  '5- Avaliar Produto\n' \
                  '0- Sair Painel ADM \n' \
                  )
            
            opcao1 = int(input("Digite a Opcao: "))
            print("-"*50)
            if opcao1 == 0:
                break


            if opcao1 == 1:
                print("-"*50)
                if len(produtos) == 0:
                    print('Nenhum produto disponivel no estoque.')
                else:
                    print('\n[ Produtos Disponiveis ]\n')
                    for i in range(len(produtos)):
                        pr = produtos[i]
                        print(str(i+1) + '- ' + pr[0] + ' | ' + str(pr[1]) + 'kg disponivel | R$ ' + str(pr[2]) + '/kg')
                    print("-"*50)

                    while True:
                        numeroptd = input('Numero do produto que deseja comprar (0 para cancelar): ')
                        if numeroptd == '0':
                            break
                        ptdvalido = False
                        for i in range(len(produtos)):
                            if numeroptd == str(i+1):
                                ptdvalido = True
                                ptdcompra = i
                        if ptdvalido:
                            ptdescolhido = produtos[ptdcompra]
                            print('Produto: ' + ptdescolhido[0])
                            print('Disponivel: ' + str(ptdescolhido[1]) + 'kg')
                            print('Preco: R$ ' + str(ptdescolhido[2]) + '/kg')
                            print("-"*50)

                            while True:
                                qtdptd = input('Quantidade em kg que deseja comprar: ')
                                qtdvalida = True
                                if len(qtdptd) == 0:
                                    qtdvalida = False
                                else:
                                    for c in qtdptd:
                                        if c < '0' or c > '9':
                                            qtdvalida = False
                                if qtdvalida and int(qtdptd) > 0:
                                    qtdcompra = int(qtdptd)
                                    if qtdcompra <= ptdescolhido[1]:
                                        break
                                    else:
                                        print('Quantidade indisponivel. Estoque: ' + str(ptdescolhido[1]) + 'kg.')
                                else:
                                    print('Quantidade invalida.')

                            total = qtdcompra * ptdescolhido[2]
                            produtos[ptdcompra][1] = ptdescolhido[1] - qtdcompra

                            historico_compras.append([nome_cliente, ptdescolhido[0], qtdcompra, total])

                            print("-"*50)
                            print('Compra realizada com sucesso!')
                            print('Produto : ' + ptdescolhido[0])
                            print('Qtd     : ' + str(qtdcompra) + 'kg')
                            print('Total   : R$ ' + str(total))
                            print("-"*50)

                            continuar = input('Deseja comprar mais algum produto? (S/N): ').upper()
                            if continuar != 'S':
                                break
                            else:
                                print("\n[ Produtos Disponiveis ]\n")
                                for i in range(len(produtos)):
                                    pr = produtos[i]
                                    print(str(i+1) + '- ' + pr[0] + ' | ' + str(pr[1]) + 'kg disponivel | R$ ' + str(pr[2]) + '/kg')
                                print("-"*50)
                        else:
                            print('Numero invalido.')


            if opcao1 == 2:
                print("-"*50)
                print('\n[ Rebanho da Fazenda ]\n')
                if len(rebanho) == 0:
                    print('Nenhum animal cadastrado no rebanho.')
                else:
                    for i in range(len(rebanho)):
                        a = rebanho[i]
                        print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1] + ' | ' + a[2])
                print("-"*50)


            if opcao1 == 3:
                print("-"*50)
                print('\n[ Seu Historico de Compras ]\n')
                temcompra = False
                for hc in historico_compras:
                    if hc[0] == nome_cliente:
                        print('Produto: ' + hc[1] + ' | Qtd: ' + str(hc[2]) + 'kg | Total: R$ ' + str(hc[3]))
                        temcompra = True
                if temcompra == False:
                    print('Nenhuma compra realizada ainda.')
                print("-"*50)

            if opcao1 == 4:
                print("-"*50)
                print('\n[ Agendar Retirada/Transporte ]\n')

                
                compras_cliente = []
                for hc in historico_compras:
                    if hc[0] == nome_cliente:
                        compras_cliente.append(hc)

                if len(compras_cliente) == 0:
                    print('Voce nao possui compras para agendar retirada.')
                    print('Realize uma compra primeiro.')
                    print("-"*50)
                else:
                    print('O que deseja agendar para retirada:')
                    print('1- Leite / Queijo (produto comprado)')
                    print('2- Animal do Rebanho')
                    print("-"*50)

                    while True:
                        tipoagend = input('Escolha o tipo (1 ou 2): ')
                        if tipoagend == '1' or tipoagend == '2':
                            break
                        else:
                            print('Opcao invalida.')

                    if tipoagend == '1':
                        print("\n[ Suas Compras ]\n")
                        for i in range(len(compras_cliente)):
                            hc = compras_cliente[i]
                            print(str(i+1) + '- ' + hc[1] + ' | ' + str(hc[2]) + 'kg | R$ ' + str(hc[3]))
                        print("-"*50)
                        while True:
                            numcompra = input('Numero da compra para agendar retirada: ')
                            compravalida = False
                            for i in range(len(compras_cliente)):
                                if numcompra == str(i+1):
                                    compravalida = True
                                    compra = i
                            if compravalida:
                                break
                            else:
                                print('Numero invalido.')
                        itemagendado = compras_cliente[compra][1] + ' (' + str(compras_cliente[compra][2]) + 'kg)'

                    else:
                        print("\n[ Animais Para Venda ]\n")
                        animaisvenda = []
                        for a in rebanho:
                            if a[2] == 'Para Venda':
                                animaisvenda.append(a)
                        if len(animaisvenda) == 0:
                            print('Nenhum animal disponivel para venda no momento.')
                            print("-"*50)
                            continue
                        for i in range(len(animaisvenda)):
                            a = animaisvenda[i]
                            print(str(i+1) + '- ' + a[0] + ' | Brinco: ' + a[1])
                        print("-"*50)
                        while True:
                            numanimal = input('Numero do animal para agendar retirada: ')
                            animalvalido = False
                            for i in range(len(animaisvenda)):
                                if numanimal == str(i+1):
                                    animalvalido = True
                                    animal = i
                            if animalvalido:
                                break
                            else:
                                print('Numero invalido.')
                        itemagendado = animaisvenda[animal][0] + ' Brinco ' + animaisvenda[animal][1]

                    
                    while True:
                        dataagend = input('Data para retirada (dd/mm/aaaa): ')
                        dataFormada = dataagend.split('/')
                        datavalida = False
                        if len(dataFormada) == 3:
                            validodia = True
                            validomes = True
                            validoano = True
                            for c in dataFormada[0]:
                                if c < '0' or c > '9':
                                    validodia = False
                            for c in dataFormada[1]:
                                if c < '0' or c > '9':
                                    validomes = False
                            for c in dataFormada[2]:
                                if c < '0' or c > '9':
                                    validoano = False
                            if validodia and validomes and validoano:
                                datavalida = True
                        if datavalida:
                            break
                        else:
                            print('Data invalida.')

                    
                    while True:
                        horarioagend = input('Horario preferido (ex: 08:00 / 14:30): ')
                        horarioFormado = horarioagend.split(':')
                        horariovalido = False
                        if len(horarioFormado) == 2:
                            validohora = True
                            validomin = True
                            for c in horarioFormado[0]:
                                if c < '0' or c > '9':
                                    validohora = False
                            for c in horarioFormado[1]:
                                if c < '0' or c > '9':
                                    validomin = False
                            if validohora and validomin:
                                hora = int(horarioFormado[0])
                                minuto = int(horarioFormado[1])
                                if 0 <= hora <= 23 and 0 <= minuto <= 59:
                                    horariovalido = True
                        if horariovalido:
                            break
                        else:
                            print('Horario invalido. Use o formato hh:mm (ex: 08:00).')

                    agendamentos.append([nome_cliente, dataagend, horarioagend, itemagendado, 'Pendente'])

                    print("-"*50)
                    print('Agendamento realizado com sucesso!')
                    print('Cliente : ' + nome_cliente)
                    print('Item    : ' + itemagendado)
                    print('Data    : ' + dataagend)
                    print('Horario : ' + horarioagend)
                    print('Status  : Pendente')
                    print('O caminhao da fazenda passara para buscar o pedido.')
                    print("-"*50)

                    print('\n[ Seus Agendamentos ]\n')
                    temag = False
                    for ag in agendamentos:
                        if ag[0] == nome_cliente:
                            print('Item: ' + ag[3] + ' | Data: ' + ag[1] + ' | Horario: ' + ag[2] + ' | Status: ' + ag[4])
                            temag = True
                    if not temag:
                        print('Nenhum agendamento ainda.')
                    print("-"*50)
                    
                    
            if opcao1 == 5:
                print("-"*50)
                        
                print('\n[ Avaliar Produto ]\n')

                
                compras_cliente = []
                for hc in historico_compras:
                    if hc[0] == nome_cliente:
                        compras_cliente.append(hc)

                if len(compras_cliente) == 0:
                    print('Voce ainda nao realizou nenhuma compra para avaliar.')
                    print("-"*50)
                else:
                    print('Selecione o produto que deseja avaliar:')
                    for i in range(len(compras_cliente)):
                        hc = compras_cliente[i]
                        print(str(i+1) + '- ' + hc[1] + ' | ' + str(hc[2]) + 'kg | R$ ' + str(hc[3]))
                    print("-"*50)

                    while True:
                        numavaliacao = input('Numero do produto a avaliar: ')
                        avaliacaovalida = False
                        for i in range(len(compras_cliente)):
                            if numavaliacao == str(i+1):
                                avaliacaovalida = True
                                avali = i
                        if avaliacaovalida:
                            break
                        else:
                            print('Numero invalido.')

                    produtoavaliado = compras_cliente[avali][1]

                    
                    while True:
                        nota = input('Nota de 1 a 5 (1-Pessimo / 5-Excelente): ')
                        notavalida = nota in ['1', '2', '3', '4', '5']
                        if notavalida:
                            nota = int(nota)
                            break
                        else:
                            print('Nota invalida. Digite um numero de 1 a 5.')

                    comentario = input('Deixe um comentario (opcional, Enter para pular): ')
                    if len(comentario) == 0:
                        comentario = 'Sem comentario.'

                    aval.append([nome_cliente, produtoavaliado, nota, comentario])
                    
                    print("-"*50)
                    print('Avaliacao registrada com sucesso!')
                    print('Produto   : ' + produtoavaliado)
                    print('Nota      : ' + str(nota) + '/5')
                    print('Comentario: ' + comentario)
                    print("-"*50)

                    
                    totalnotas = 0
                    qtdnotas = 0
                    for av in aval:
                        if av[1] == produtoavaliado:
                            totalnotas = totalnotas + av[2]
                            qtdnotas = qtdnotas + 1
                    media = totalnotas / qtdnotas
                    print('Media de avaliacoes do ' + produtoavaliado + ': ' + str(round(media, 1)) + '/5')
                    print("-"*50)

  

                            