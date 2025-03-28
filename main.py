import cv2
import os

class Main:
    def __init__ (self):
        try:
            arquivos = [arquivo for arquivo in os.listdir('imagens') if os.path.isfile(os.path.join('imagens', arquivo))]
            tam =  len(arquivos)
        except FileNotFoundError:
            print("Pasta não encontrada.")

        for i in range(tam):
            self.detectar_rosto(f"imagens/imagem{i+1}.jpg")

    def detectar_rosto(self, imagem_path):
        print("Fazendo a detecção")
        face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
        imagem = cv2.imread(imagem_path)

        
        if imagem is None:
            print("Erro ao carregar a imagem! Verifique o caminho do arquivo.")
            return None

        escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        
        if escala_cinza is None:
            print("Erro ao carregar a imagem! Verifique o caminho do arquivo.")
            return None

        faces = face_cascade.detectMultiScale(escala_cinza) # Adicione os parâmetros scaleFactor e minNeighbors

        print(faces)
        for (x, y, w, h) in faces:
            
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 0, 0), 2) # Desenha retângulos ao redor dos rostos
            cv2.imshow("Faces", imagem) # Exibe a imagem atualizada
            cv2.waitKey(0) # Espera por uma tecla ser pressionada

        cv2.destroyAllWindows() # Fecha todas as janelas após a detecção

if __name__ == '__main__':
    Main()