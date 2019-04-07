preco = int (input('forneça o preço'))
###############################
while(preco%2)==0: #par
        preco=preco/2
        print('{}'.format(preco)) #por condição
        if(preco%2)!=0: #resto diferente de 0 é impar
            preco =(preco*3+1)/2
            print('{}'.format(preco)) #por condição aqui
