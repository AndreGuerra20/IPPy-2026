# Ficha 10 - Ex 5
# Dicionário com os produtos de uma pastelaria e o respetivo preço. O utilizador vai
# pedindo (produto, quantidade) até escrever "OK". No final imprime-se o talão com IVA 23%.

IVA = 0.23

produtos = {'café': 0.80, 'galão': 1.30, 'pastel de nata': 1.20, 'croissant': 1.50,
            'bola de berlim': 1.60, 'torrada': 1.80, 'sumo natural': 2.50}


def mostrar_produtos(produtos):
    print('=== Produtos disponíveis ===')
    for produto, preco in produtos.items():
        print(f'  {produto:<16} {preco:>6.2f} €')


def fazer_pedido(produtos):
    pedido = []
    produto = input('Produto (OK para terminar): ').lower()
    while produto != 'ok':
        if produto in produtos:
            quantidade = int(input('Quantidade: '))
            pedido.append((produto, quantidade))
        else:
            print('Produto inexistente!')
        produto = input('Produto (OK para terminar): ').lower()
    return pedido


def imprimir_talao(produtos, pedido):
    print()
    print('========== TALÃO ==========')
    total = 0
    for produto, quantidade in pedido:
        preco = quantidade * produtos[produto]
        total += preco
        print(f'{quantidade:>3} - {produto:<16} - {preco:>6.2f} €')
    print('---------------------------')
    print(f'Subtotal:   {total:>8.2f} €')
    print(f'IVA (23%):  {total * IVA:>8.2f} €')
    print(f'Total:      {total * (1 + IVA):>8.2f} €')


mostrar_produtos(produtos)
lista_pedido = fazer_pedido(produtos)
imprimir_talao(produtos, lista_pedido)
