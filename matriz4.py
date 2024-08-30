from random import randint

#variáveis globais
categoria = ['Eletrônico', 'Roupa', 'Alimento']
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril']
venda = [[0 for _ in range(len(mes))] for _ in range(len(categoria))]

#função para entrada dos dados das vendas
def ler_dados():
    for i in range(len(categoria)):
        for j in range(len(mes)):
            venda[i][j] = randint(0, 15)
            
# função para imprimir os dados das vendas
def imprimir():
    print("Dados das vendas:")
    for i in range(len(categoria)):
        for j in range(len(mes)):
            print(venda[i][j], end="\t") 
        print()           
        
# função para somar o total de vendas por categoria
def total_de_vendas_por_categoria():
    print("\n####Total por categoria####")
    for i in range(len(categoria)):
        print(f'{categoria[i]} = {sum(venda[i])}')
        
# função para identificar o mês com o maior total de vendas
def melhor_mes():
    maior = 0
    mes_maior_venda = ""
    for j in range(len(mes)):
        total = 0
        for i in range(len(categoria)):
            total = total + venda[i][j]
        if(total > maior):
            maior = total 
            mes_maior_venda = mes[j]
        print(f"### mês com maior total de vendas --> {mes_maior_venda}")

# função para calcular  a média de vendas mensais por categoria
def media_por_categoria():
    print()
    for i in range(len(categoria)):
        print(f"{categoria[i]} = {sum(venda[i])/len(venda[i])}")

# função principal
def main():
    ler_dados()
    imprimir()
    total_de_vendas_por_categoria()
    melhor_mes()
    
#chamada da função principal
if __name__ == '__main__':
    main()