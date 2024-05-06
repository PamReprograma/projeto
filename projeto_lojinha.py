


dataset = [ 
    {'ano_receita': 2022, 'mes_receita': '1', 'faturamento': 49179, 'despesas': 6295},
    {'ano_receita': 2022, 'mes_receita': '2', 'faturamento': 12018, 'despesas': 43329},
    {'ano_receita': 2022, 'mes_receita': '3', 'faturamento': 23524, 'despesas': 49376},
    {'ano_receita': 2022, 'mes_receita': '4', 'faturamento': 29615, 'despesas': 16973},
    {'ano_receita': 2022, 'mes_receita': '5', 'faturamento': 26527, 'despesas': 43742},
    {'ano_receita': 2022, 'mes_receita': '6', 'faturamento': 48400, 'despesas': 11447},
    {'ano_receita': 2022, 'mes_receita': '7', 'faturamento': 27219, 'despesas': 25593},
    {'ano_receita': 2022, 'mes_receita': '8', 'faturamento': 46787, 'despesas': 19018},
    {'ano_receita': 2022, 'mes_receita': '9', 'faturamento': 32306, 'despesas': 13522},
    {'ano_receita': 2022, 'mes_receita': '10', 'faturamento': 27106, 'despesas': 15969},
    {'ano_receita': 2022, 'mes_receita': '11', 'faturamento': 15255, 'despesas': 20105},
    {'ano_receita': 2022, 'mes_receita': '12', 'faturamento': 23864, 'despesas': 32509},
    {'ano_receita': 2023, 'mes_receita': '1', 'faturamento': 47240, 'despesas': 55776},
    {'ano_receita': 2023, 'mes_receita': '2', 'faturamento': 42771, 'despesas': 36819},
    {'ano_receita': 2023, 'mes_receita': '3', 'faturamento': 18008, 'despesas': 35853},
    {'ano_receita': 2023, 'mes_receita': '4', 'faturamento': 21857, 'despesas': 6940},
    {'ano_receita': 2023, 'mes_receita': '5', 'faturamento': 29735, 'despesas': 59626},
    {'ano_receita': 2023, 'mes_receita': '6', 'faturamento': 33704, 'despesas': 30072},
    {'ano_receita': 2023, 'mes_receita': '7', 'faturamento': 26515, 'despesas': 12129},
    {'ano_receita': 2023, 'mes_receita': '8', 'faturamento': 18149, 'despesas': 21663},
    {'ano_receita': 2023, 'mes_receita': '9', 'faturamento': 46176, 'despesas': 12564},
    {'ano_receita': 2023, 'mes_receita': '10', 'faturamento': 24649, 'despesas': 58127},
    {'ano_receita': 2023, 'mes_receita': '11', 'faturamento': 44484, 'despesas': 5304},
    {'ano_receita': 2023, 'mes_receita': '12', 'faturamento': 30840, 'despesas': 5055},
    {'ano_receita': 2024, 'mes_receita': '1', 'faturamento': 28726, 'despesas': 25133},
    {'ano_receita': 2024, 'mes_receita': '2', 'faturamento': 34962, 'despesas': 26537},
    {'ano_receita': 2024, 'mes_receita': '3', 'faturamento': 49424, 'despesas': 29649},
    {'ano_receita': 2024, 'mes_receita': '4', 'faturamento': 42698, 'despesas': 54170},
    {'ano_receita': 2024, 'mes_receita': '5', 'faturamento': 37237, 'despesas': 48453},
    {'ano_receita': 2024, 'mes_receita': '6', 'faturamento': 30665, 'despesas': 8782},
    {'ano_receita': 2024, 'mes_receita': '7', 'faturamento': 39597, 'despesas': 12261},
    {'ano_receita': 2024, 'mes_receita': '8', 'faturamento': 49326, 'despesas': 18862},
    {'ano_receita': 2024, 'mes_receita': '9', 'faturamento': 19043, 'despesas': 48517},
    {'ano_receita': 2024, 'mes_receita': '10', 'faturamento': 24464, 'despesas': 24215},
    {'ano_receita': 2024, 'mes_receita': '11', 'faturamento': 11635, 'despesas': 8190},
    {'ano_receita': 2024, 'mes_receita': '12', 'faturamento': 39303, 'despesas': 14418}
]
def menu():

    print("----- LOJINHA DA PAMELLA ------\n\n")
    opt_usuario = int(input("Escolha a opção que você deseja:\n\n[1] Adicionar novos registros\n\n[2] Calcular receita\n\n"))

    if opt_usuario == 1:
        novo_registro()
    elif opt_usuario == 2:
        calculo_receita()
    else:
        print("Opção Inválida, por favor Ctrl + c e escolha novamente.")



def novo_registro():
    print("Você escolheu a opção novo registro, por favor digite os dado conforme solicitado abaixo:\n\n")

    ano = int(input("Digite o ano (Ex: 2024): "))
    mes = int(input("Digite o mês (Ex: 12): "))
    faturamento = int(input("Digite o faturamento correspondente (Ex: 23568): "))
    despesas = int(input("Digite as despesas correspondente (Ex: 25568): "))

    new_regitro = {"ano_receita": ano,"mes_receita": mes,"faturamento": faturamento, "despesas": despesas} 
    dataset.append(new_regitro)

    print(dataset)



def calculo_receita():

    print("Você escolheu a opção calculo da receita, por favor digite os dado conforme solicitado abaixo:\n\n")
    mes_receita = input("Digite o mês que voce deseja saber a receita:\n\n")
    
    valor_total = 0

    for i in dataset:
        mes_dicionario = i.get("mes_receita")
        if mes_dicionario == mes_receita :
            receita = i.get("faturamento") - i.get("despesas")
            valor_total += receita

    print("O valor da receita total do mês",mes_receita, "é ", valor_total, "reais\n\n")

    opt2 = input("Você deseja saber o mês com maior fatuamento e mês com maior despesa?\n\n[1] SIM\n\n[2]NÃO\n\n")

    valor_maior_despesa_mes = 0
    maior_despesa_mes = ""

    valor_maior_despesa_ano = 0
    maior_despesa_ano = ""

    valor_maior_faturamento_mes = 0
    maior_faturamento_mes = ""

    valor_maior_faturamento_ano = 0
    maior_faturamento_ano = ""

    if opt2 == "1":

        for i in dataset:
            despesas_mes = i.get("despesas")
            if despesas_mes > valor_maior_despesa_mes:
                valor_maior_despesa_mes = despesas_mes
                maior_despesa_mes = i.get("mes_receita")
        for i in dataset:
            despesas_ano = i.get("despesas")
            if despesas_ano > valor_maior_despesa_ano:
                valor_maior_despesa_ano = despesas_ano
                maior_despesa_ano = i.get("ano_receita")

         

        print("----DESPESAS----\n\nO mes com maior despesa foi: ", maior_despesa_mes, "e o valor: ", valor_maior_despesa_mes,"reais.")
        print("O ano com maior despesa foi: ", maior_despesa_ano, "e o valor: ", valor_maior_despesa_ano,"reais.\n\n")

        for i in dataset:
            faturamento_mes = i.get("faturamento")
            if faturamento_mes > valor_maior_faturamento_mes:
                valor_maior_faturamento_mes = faturamento_mes
                maior_faturamento_mes = i.get("mes_receita")

        for i in dataset:
            faturamento_ano = i.get("faturamento")
            if faturamento_ano > valor_maior_faturamento_ano:
                valor_maior_faturamento_ano = faturamento_ano
                maior_faturamento_ano = i.get("ano_receita")

        print("----FATURAMENTO----\n\nO mês com maior faturamento foi:", maior_faturamento_mes, "e o valor:", valor_maior_faturamento_mes,"reais.")
        print("O ano com maior faturamento foi:", maior_faturamento_ano, "e o valor:", valor_maior_faturamento_ano,"reais.\n\n")

    else:
        exit()
            
menu()