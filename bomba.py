class Bomba_combustivel():
	def __init__(self):
		self.type_gasoline   = 'Etanol'
		self.valor_litro     = 4.00
		self.quantidade_Comb = 1000

	def abastecerPorValor(self, valor):
		litros = valor / self.valor_litro
		if self.quantidade_Comb < litros:
			print('ERROR: Quantidade insuficiente')
			return
		self.quantidade_Comb -= litros
		print(f'Tipo de gasolina: {self.type_gasoline} ')
		print(f'Valor: {valor} ')
		print(f'Litros Colocados: {litros}L ')
		print(f'Litros Restantes: {self.quantidade_Comb} ')
		print('')

	def abastecerPorLitro(self, litro):
		valor_final = litro * self.valor_litro
		if self.quantidade_Comb < litro:
			print('ERROR: Quantidade insuficiente')
			return
		self.quantidade_Comb -= litro
		print(f'Tipo da gasolina: {self.type_gasoline} ')
		print(f'Litros: {litro}L')
		print(f'valor final: {valor_final}R$ ')
		print(f'Litros Restantes: {self.quantidade_Comb} ')
		print('')

	def alterarValor(self, nValor):
		self.valor_litro = nValor
		print(f'Valor Atualizado: {self.valor_litro}R$ ')

	def alterarCombustivel(self, nCobustivel):
		self.type_gasoline = nCobustivel
		print(f'Tipo de combustivel aterado: {nCobustivel}')

	def alterarQuantidadeCombustivel(self, nQuantidade):
		print(f'Quantidade atual: {self.quantidade_Comb}L ')
		self.quantidade_Comb += nQuantidade
		print(f'Quantidade Atualizada: {self.quantidade_Comb}L ')

def menu01():
	print(''' 
	Menu principal
[ 1 ] Abastecer por Litro    [ 1 ]
[ 2 ] Abastecer por dinheiro [ 2 ]
[ 3 ] Configuraçao           [ 3 ] ''')

def menu02():
	print(''' 
		  CONFIGURAÇAO
[ 1 ] Alterar valor da gasolina      [ 1 ]
[ 2 ] Alterar tipo de combustivel 	 [ 2 ]
[ 3 ] Alterar quantidade Combustivel [ 3 ]  ''')

'''
bomba = Bomba_combustivel()
bomba.alterarValor(2)
bomba.alterarCombustivel('Ditivada')
bomba.alterarCombustivel(10)

print(bomba.valor_litro)
bomba.alterarValor(2)
bomba.abastecerPorLitro(10)
bomba.abastecerPorValor(40)
'''
bomba = Bomba_combustivel()
while True:
	menu01()
	op = int(input(': '))
	if op == 1:
		litros = float(input('Quantos Litros: '))
		bomba.abastecerPorLitro(litros)
	elif op == 2:
		preco = float(input('Valor: '))
		bomba.abastecerPorValor(preco)
	elif op == 3:
		menu02()
		op2 = int(input(': '))
		if op2 == 1:
			new_Valor = float(input('Novo Preço da gasolina: '))
			bomba.alterarValor(new_Valor)
		elif op2 == 2:
			tipo_gasosa = str(input('tipo de gasolina: '))
			bomba.alterarCombustivel(tipo_gasosa)
		elif op2 == 3:
			quantidade = float(input('Atualizar quantidade da gasolina: '))
			bomba.alterarQuantidadeCombustivel(quantidade)
		else:
			print('ERROR: essa opçao nao existe! ')
	else:
		print('ERROR: essa opçao nao existe! ')