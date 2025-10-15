pacientes = []
contador = 1
while True:
    print(f'Dados do paciente {contador}')
    paciente = {
        'nome':input('Digite o nome: '),
        'peso':float(input('Digite o peso(kg): ')),
        'sexo':input('Digite o sexo(M-masculino, F-feminino): ').upper(),
        'altura':float(input('Digite a altura(metros): ')),
        'idade':int(input('Digite a idade: '))
    }
    imc = paciente['peso'] / (paciente['altura'] ** 2)

    if paciente['sexo'] == 'M' or paciente['sexo'] == 'Masculino':
        tmb = 9.99 * paciente['peso'] + 6.25 * (paciente['altura'] * 100) - 4.42 * paciente['idade'] - 5
    else:
        tmb = 9.99 * paciente['peso'] + 6.25 * (paciente['altura'] * 100) - 4.42 * paciente['idade'] - 161

    if imc < 18.5:
        condicao = 'Magreza'
        grau = '0'
    elif imc < 24.9:
        grau = '0'
        condicao = 'Normal'
    elif imc < 29.9:
        grau = '1'
        condicao = 'Sobrepeso'
    elif imc < 39.9:
        grau = '2'
        condicao = 'Obesidade'
    elif imc >= 40:
        grau = '3'
        condicao = 'Obesidade grave'

    paciente['imc'] = imc
    paciente['tmb'] = tmb
    paciente['condicao_imc'] = condicao
    paciente['grau'] = grau

    pacientes.append(paciente)
    contador += 1
    continua = input('Quer adicionar mais algum paciente? s ou n: ').lower()
    if continua == 'n':
        break

paciente_maior_imc = pacientes[0]
for paciente in pacientes:
    if paciente['imc'] > paciente_maior_imc['imc']:
        paciente_maior_imc = paciente
paciente_maior_tmb = pacientes[0]
for paciente in pacientes:
    if paciente['tmb'] > paciente_maior_tmb['tmb']:
        paciente_maior_tmb = paciente
paciente_menor_imc = pacientes[0]
for paciente in pacientes:
    if paciente['imc'] < paciente_menor_imc['imc']:
        paciente_menor_imc = paciente
paciente_menor_tmb = pacientes[0]
for paciente in pacientes:
    if paciente['tmb'] < paciente_menor_tmb['tmb']:
        paciente_menor_tmb = paciente

menu = True
while menu == True:
    opcaoMenu = int(input('Opções:\n'
                     '1 - maior IMC\n'
                     '2 - maior TMB\n'
                     '3 - menor IMC\n'
                     '4 - menor TMB\n'
                     '5 - Buscar paciente\n'
                     '6 - Listar pacientes registrados\n'
                     '7 - Sair\n'))

    if opcaoMenu == 1:
        print(f"{paciente_maior_imc['nome']} tem o maior IMC: {paciente_maior_imc['imc']:.2f} classificação {paciente_maior_imc['condicao_imc']} grau {paciente_maior_imc['grau']}")
    elif opcaoMenu == 2:
        print(f"{paciente_maior_tmb['nome']} tem o maior TMB: {paciente_maior_tmb['tmb']:.2f}")
    elif opcaoMenu == 3:
        print(f"{paciente_menor_imc['nome']} tem o menor IMC: {paciente_menor_imc['imc']:.2f} classificação {paciente_menor_imc['condicao_imc']} grau {paciente_menor_imc['grau']}")
    elif opcaoMenu == 4:
        print(f"{paciente_menor_tmb['nome']} tem o menor TMB: {paciente_menor_tmb['tmb']:.2f}")
    elif opcaoMenu == 5:
        busca = input('Qual o nome inteiro do paciente? ')
        encontrado = False
        for paciente in pacientes:
            if paciente['nome'] == busca:
                print(f"{paciente['nome']}:")
                print(f'Idade = {paciente['idade']} anos')
                print(f'Sexo = {paciente["sexo"]}')
                print(f'Peso = {paciente["peso"]:.1f}kg')
                print(f'Altura = {paciente["altura"]}m')
                print(f"IMC = {paciente['imc']:.2f}")
                print(f"TMB = {paciente['tmb']:.2f}")
                print(f"Classificação = {paciente['condicao_imc']}")
                print(f"Grau de obesidade = {paciente['grau']}")
                encontrado = True
                break
        if not encontrado:
            print('Paciente não encontrado.')
    elif opcaoMenu == 6:
        for paciente in pacientes:
            print(f"{paciente['nome']}")
    elif opcaoMenu == 7:
        menu = False
    else:
        print('Opção invalida!')

print('Programa encerrado!')