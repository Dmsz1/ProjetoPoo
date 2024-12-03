import random


def banco():
    conta = criarconta()
    c = ContaC(conta)
    p = ContaP(conta)
    print("Para efetuar a criação da conta, faça um depósito de ao menos R$: 10,00!")
    
    print("""
            ----------------------
            |     E3 BANK      |
            ----------------------
            | 1 - DEPOSITAR      |
            | 2 - SAIR           |
            ----------------------
            """)
    
    op = int(input("Operação: "))
    if op == 1:
        if c.depositar():
            print("Sua conta foi criada com sucesso!")
            while True:
                print("""
                    ----------------------
                    |     E3 BANK      |
                    ----------------------
                    | 1 - CONTA CORRENTE |
                    | 2 - CONTA POUPANÇA |
                    | 3 - SAIR           |
                    ----------------------
                    """)
                op = int(input("Operação: "))
                if op == 1:
                    while True:
                        print("""
                            ----------------------
                            |     E3 BANK      |
                            |   CONTA CORRENTE   |
                            ----------------------
                            | 1 - DEPOSITAR      |
                            | 2 - SACAR          |
                            | 3 - APLICAR        |
                            | 4 - VOLTAR         |
                            ----------------------
                            """)
                        op = int(input("Operação: "))
                        if op == 1:
                            c.depositar()
                        elif op == 2:
                            c.sacar()
                        elif op == 3:
                            c.aplicar()
                        elif op == 4:
                            break
                        else:
                            print("Operação indisponível!")
                elif op == 2:
                    while True:
                        print("""
                        ----------------------
                        |     E3 BANK      |
                        |   CONTA POUPANÇA   |
                        ----------------------
                        | 1 - RESGATAR       |
                        | 2 - EXTRATO        |
                        | 3 - VOLTAR         |
                        ----------------------
                        """)
                        op = int(input("Operação: "))
                        if op == 1:
                            saldo, aplicado = p.resgatar(c.get_saldo(), c.get_aplicado())
                            c.set_saldo(saldo)
                            c.set_aplicado(aplicado)
                        elif op == 2:
                            p.extrato(c.get_saldo(), c.get_aplicado())
                        elif op == 3:
                            break
                        else:
                            print("Operação indisponível!")
                elif op == 3:
                    print("O programa foi encerrado")
                    break
                else:
                    print("Operação indisponível!")


def criarconta():
    nome = input("Qual o nome do titular: ")
    senha = input("Digite sua senha: ")
    while len(senha) != 4:
        print("A senha deve possuir 4 dígitos")
        senha = input("Digite sua senha: ")
    return nome, senha


class ContaC:
    def __init__(self, conta):
        self.__nome = conta[0]
        self.__n_conta = random.randint(100, 999)
        self.__senha = conta[1]
        self.__saldo = 0
        self.__aplicado = 0

    def set_saldo(self, novosaldo):
        self.__saldo = novosaldo

    def set_aplicado(self, novosaldo):
        self.__aplicado = novosaldo

    def set_senha(self, nova_senha):
        self.__senha = nova_senha

    def get_saldo(self):
        return self.__saldo

    def get_senha(self):
        return self.__senha

    def get_nome(self):
        return self.__nome

    def get_n_conta(self):
        return self.__n_conta

    def get_aplicado(self):
        return self.__aplicado

    def verificar_senha(self):
        contador = 0
        while contador < 3:
            senha = input("Digite sua senha: ")
            if senha == self.get_senha():
                return True
            contador += 1
        print("Senha incorreta. Operação cancelada.")
        return False

    def sacar(self):
        if self.verificar_senha():
            valor = float(input("Valor do saque: "))
            if valor > 0 and valor <= self.__saldo:
                self.__saldo -= valor
                print("Saque efetuado com sucesso!")
            else:
                print("Saldo insuficiente ou valor inválido.")

    def depositar(self):
        if self.verificar_senha():
            valor = float(input("Valor do depósito: "))
            if valor > 10:
                self.__saldo += valor
                print("Depósito efetuado com sucesso!")
                return True
            else:
                print("O valor mínimo para depósito é R$ 10,00.")
        return False

    def aplicar(self):
        if self.verificar_senha():
            valor = float(input("Qual o valor a ser aplicado: "))
            if valor > 0 and valor <= self.__saldo:
                self.__saldo -= valor
                self.__aplicado += valor
                print("Aplicação realizada com sucesso!")
            else:
                print("Saldo insuficiente ou valor inválido.")


class ContaP(ContaC):
    def resgatar(self, saldo, aplicado):
        if self.verificar_senha():
            valor = float(input("Valor a resgatar: "))
            if valor > 0 and valor <= aplicado:
                aplicado -= valor
                saldo += valor
                print("Resgate efetuado com sucesso!")
            else:
                print("Valor inválido ou insuficiente na poupança.")
        return saldo, aplicado

    def extrato(self, saldo, aplicado):
        if self.verificar_senha():
            print(f"""
            ----------------------
            |     E3 BANK      |
            |  EXTRATO BANCÁRIO  |
            ----------------------
             Titular: {self.get_nome()}
             Conta: {self.get_n_conta()}
             Conta Corrente: R$ {saldo:.2f}
             Conta Poupança: R$ {aplicado:.2f}
            """)


banco()
