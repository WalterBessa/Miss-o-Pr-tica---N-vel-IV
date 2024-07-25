from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa("João", "12345", "2024-01-01", True)
print("Instancia da classe Pessoa:")
pessoa.imprimir()

pessoa_fisica = PessoaFisica("Ana", "67890", "2024-01-01", True, "1990-01-01", "000.111.222-33", "12345678-9")
print("\nInstancia da classe PessoaFisica:")
pessoa_fisica.imprimir()

pessoa_juridica = PessoaJuridica("Empresa X", "11223", "2024-01-01", True, "2024-01-01", "00.000.000/0001-00")
print("\nInstancia da classe PessoaJuridica:")
pessoa_juridica.imprimir()

try:
    pessoa_fisica.cpf = "000.111.222-3" 
except ValueError as e:
    print(f"\nErro ao definir CPF: {e}")

pessoa_fisica.cpf = "000.111.222-33"

try:
    pessoa_juridica.cnpj = "00.000.000/0001-0"
except ValueError as e:
    print(f"\nErro ao definir CNPJ: {e}")

pessoa_juridica.cnpj = "00.000.000/0001-00" 

print("\nInstancia da classe PessoaFisica após alterações:")
pessoa_fisica.imprimir()
print("\nInstancia da classe PessoaJuridica após alterações:")
pessoa_juridica.imprimir()
