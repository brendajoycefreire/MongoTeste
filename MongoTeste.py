import sys

def check_virtualenv():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("O ambiente virtual está ativado.")
        print(f"Diretório do ambiente virtual: {sys.prefix}")
    else:
        print("O ambiente virtual NÃO está ativado.")
        print(f"Usando a instalação do Python em: {sys.prefix}")

check_virtualenv()
