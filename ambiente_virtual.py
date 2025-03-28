import os

class Ambiente_Virtual():
    def __init__(self):
        self.configurar_ambiente_virtual()
        self.instalar_dependencias()

    def configurar_ambiente_virtual(self):
        """Cria e ativa um ambiente virtual para o projeto."""
        os.system("python3 -m venv .venv")
    def instalar_dependencias(self):
        """Instala dependências no ambiente virtual."""
        os.system("pip install opencv-python")
        print("Dependências instaladas com sucesso!")

if __name__ == '__main__':
    Ambiente_Virtual()
    print("Execute: source .venv/bin/activate")