#EXERCICIO UM#
valor = [4.00, 4.50, 5.00, 6.00, 4.00, 6.00, 4.50, 0.50]
comidas =[ 'salgado', 'refrigerante', 'suco', 'sorvete', 'cafe', 'capuccino', 'bolo',' dadinho']
# print(valor, comidas, len(valor), len(comidas)) // verifiquei tamanho das listas
pedido = input('NOME DO PEDIDO')
def valor_retornado ():
    n = 1 
    for x in range (n,8):
        if pedido.lower()==comidas[x-1].lower(): #entrada em maiusculo e minusculo
            print('O preço é',valor[x-1])

    
#chamada da função
valor_retornado ()

#EXERCICIO DOIS#
nomes = []
pedidos = []
def nome_e_pedido():
    #peça os nomes e adicione as listas previamente dadas
    for x in range (1,7):
        nome = input('Por favor, forneça seu nome.')
        nome = nome.lower()
        salgado = input('O que vai pedir?')
        salgado = salgado.lower()
        nomes.append(nome)
        pedidos.append(salgado)
    #imprima a lista
    for y in range (1,7):
        print(nomes[y-1],',', pedidos[y-1])
    return salgado
#chamada da função        
salgado = nome_e_pedido ()

preco = []
#EXERCÍCIO TRES#
#TA DANDO TUDO ERRRAAAAAAAADOOOO
def vouchorar():
    for k in range (1,8):
        if salgado.lower() == comidas[k-1].lower():
            preco.append(valor_retornado)
    for h in range (1,7):
        print(nomes[h-1], pedidos[h-1])

    for l in range (1,8):
        if salgado[l-1]:
            for h in range (h-1):
                if salgado==valor[h-1]:
                    preco.append(salgado)
                    
vouchorar()






    
