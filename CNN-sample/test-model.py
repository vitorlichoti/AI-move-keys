import numpy as np
from tensorflow.keras.models import load_model

# Carregar o modelo treinado
model = load_model('motion_detection_model.h5')

# Inicializar a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocessar o frame para ser compatível com o modelo
    img = cv2.resize(frame, (150, 150))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    # Fazer a previsão
    prediction = model.predict(img)
    
    if prediction > 0.5:
        label = 'Braço Direito Levantado'
    else:
        label = 'Braço Esquerdo Levantado'

    # Mostrar o resultado na tela
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
