
from time import sleep

vc = float(input('Digite o valor auferido em sentença: '))
hc = float(input('Digite a porcentagen dos  honorários contratuais: ')) #honorários contratuais
ha = (vc*hc)/100

print('Processando...')
sleep(2)

print('o valor recebido foi {:.2f}'.format(vc))
print('O valor devido para o cliente é de R$ {:.2f}'.format(vc-ha))
print('o valor devido para o advogado é de R$ {:.2f}'.format(ha))
