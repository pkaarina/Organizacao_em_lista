#Código para uso organizacional, listar informações e facilitar a vida.

item_para_casa = []
valor = []
comodo = []
valor_total = 0

resposta = "S"

while resposta == "S":      
    item_para_casa.append (input ("\nItem para casa: "))
    valor.append (float (input ("Valor: ")))
    comodo.append (input ("Cômodo: "))
    resposta = input ("\nDigite \"S\" para adicionar mais um item para casa: ").upper()

for indice in range (0, len (item_para_casa)):
    print ("\nItem para casa..: ", (indice+1))
    print ("Nome...........: ", item_para_casa [indice])
    print ("Valor..........: ", valor [indice])
    print ("Cômodo...: ", comodo [indice])
    valor_total = valor_total + valor[indice] 

print ("\nTotal de itens adicionados: ", len(item_para_casa)) 
print ("O valor total para despesa é de: R$", valor_total)

print ("\nObrigada :D")
