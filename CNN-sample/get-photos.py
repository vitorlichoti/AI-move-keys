import cv2
import os

# Criar diretórios para armazenar as imagens
os.makedirs('data/direita', exist_ok=True)
os.makedirs('data/esquerda', exist_ok=True)

# Inicializar a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mostrar o frame na tela
    cv2.imshow('Frame', frame)

    # Capturar imagens pressionando as teclas 'd' e 'e'
    key = cv2.waitKey(1)
    if key == ord('d'):
        cv2.imwrite(f'data/direita/{len(os.listdir("data/direita"))}.jpg', frame)
    elif key == ord('e'):
        cv2.imwrite(f'data/esquerda/{len(os.listdir("data/esquerda"))}.jpg', frame)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
