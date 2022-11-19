# criar uma variavel que armazena doações
doacao_d = 0.0
doacao_v = 0.0
din = float(input())
dinheiro = din
doacao_d += dinheiro
while True:
    din = float(input())
    if din == -1:
        break
    vic_coin = (din * 2.5)
    doacao_d += dinheiro
    doacao_v += vic_coin
print(f'VC$ {doacao_d:.2F}')
print(f'RS$ {doacao_v:.2F}')
