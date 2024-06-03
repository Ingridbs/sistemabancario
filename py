class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saques = 3
        self.saques_hoje = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_hoje >= self.limite_saques:
            print("Limite diário de saques atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_hoje += 1
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque deve ser positivo.")

    def mostrar_extrato(self):
        print("\nExtrato de transações:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    def resetar_saques_diarios(self):
        self.saques_hoje = 0

def main():
    banco = Banco()
    
    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            banco.sacar(valor)
        elif opcao == '3':
            banco.mostrar_extrato()
        elif opcao == '4':
            print("Saindo do sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
