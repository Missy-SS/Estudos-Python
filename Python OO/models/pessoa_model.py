class Pessoa:
    def __init__(this, nome="", idade=0, profissao=""):
        this._nome = nome
        this._idade = idade
        this._profissao = profissao
    
    def __str__(this):
        return f"{this._nome.ljust(25)} | {this._idade} anos | {this._profissao.ljust(25)}"
    

        
    @property
    def saudacao (this):
        if this._profissao:
            return f"Saudações, {this._profissao}"
        else:
            return f"Saudações, {this._nome}"
    
    def aniversario (this):
        this._idade = int(this._idade) + 1

pessoa1 = Pessoa(f"Amy".ljust(25), "29".ljust(25), "Engenheira")
pessoa2 = Pessoa(f"Alice".ljust(25), "50".ljust(25), "Administradora")
pessoa3 = Pessoa(f"Roberta".ljust(25), "18".ljust(25), "Caixa de Mercado")

print("Informações iniciais")
print(f"Nome".ljust(25), "Idade".ljust(32), "Profissão")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após o aniversário")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)