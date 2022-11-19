doação_d = 0.0
doação_v = 0.0
while True:
    dinheiro = dict()
    din = float(input())
    if din == -1:
        break
    dinheiro['doações'] = din
    vic_coin = din * 2.50
    dinheiro['vic_coin'] = vic_coin
    doação_d += dinheiro['doações']
    doação_v += dinheiro['vic_coin']
print(f'VC$ {doação_d:.2F}')
print(f'RS$ {doação_v:.2F}')