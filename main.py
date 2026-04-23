import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

torneira_aberta = False
tempo_inicio = 0
TEMPO_ABERTA = 20

# 🔥 DETECÇÃO DE JOINHA SIMPLES E EFICAZ
def is_joinha(hand):
    # Polegar (dedo que fica em pé)
    thumb_tip = hand.landmark[4]
    thumb_ip = hand.landmark[3]  # Articulação do meio do polegar
    
    # Indicador
    index_tip = hand.landmark[8]
    index_pip = hand.landmark[6]
    
    # Dedo médio
    middle_tip = hand.landmark[12]
    middle_pip = hand.landmark[10]
    
    # Dedo anelar
    ring_tip = hand.landmark[16]
    ring_pip = hand.landmark[14]
    
    # Mindinho
    pinky_tip = hand.landmark[20]
    pinky_pip = hand.landmark[18]
    
    # CONDICÃO 1: Polegar deve estar esticado para CIMA
    # O polegar em joinha fica com a ponta acima da articulação média
    polegar_esticado = thumb_tip.y < thumb_ip.y - 0.02
    
    # CONDIÇÃO 2: Os outros 4 dedos devem estar FECHADOS (dobrados)
    # Dedo fechado = ponta do dedo está abaixo da articulação média
    indicador_fechado = index_tip.y > index_pip.y
    medio_fechado = middle_tip.y > middle_pip.y
    anelar_fechado = ring_tip.y > ring_pip.y
    mindinho_fechado = pinky_tip.y > pinky_pip.y
    
    # RESULTADO: Polegar pra cima E todos os outros dedos fechados
    return polegar_esticado and indicador_fechado and medio_fechado and anelar_fechado and mindinho_fechado

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Processamento para detecção
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = hands.process(frame_rgb)

    zona_y = int(h * 0.6)

    # Verifica se tem mão na zona e se é joinha
    if not torneira_aberta and resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:
            
            # Desenha os pontos da mão (opcional)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Pega a posição da mão
            y_vals = [lm.y for lm in hand_landmarks.landmark]
            y_centro = sum(y_vals) / len(y_vals)
            
            # Verifica se está na zona da pia
            if y_centro > 0.6:  # Dentro da zona azul
                
                # Verifica se é joinha
                if is_joinha(hand_landmarks):
                    torneira_aberta = True
                    tempo_inicio = time.time()
                    print("✅ JOINHA DETECTADO! Torneira aberta")
                    cv2.putText(frame, "JOINHA DETECTADO!", (10, 100),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "FACA O GESTO DE JOINHA", (10, 100),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Timer para fechar a torneira
    if torneira_aberta:
        tempo_passado = time.time() - tempo_inicio
        if tempo_passado >= TEMPO_ABERTA:
            torneira_aberta = False
            print("⏰ Torneira fechada")
        else:
            # Mostra tempo restante
            tempo_restante = int(TEMPO_ABERTA - tempo_passado)
            cv2.putText(frame, f"Tempo: {tempo_restante}s", (10, 150),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    # Status da torneira
    status = "ABERTA" if torneira_aberta else "FECHADA"
    cor = (0, 255, 0) if torneira_aberta else (0, 0, 255)
    
    cv2.putText(frame, f"Torneira: {status}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2)

    # Desenha a zona da pia
    cv2.rectangle(frame, (0, zona_y), (w, h), (255, 0, 0), 2)
    cv2.putText(frame, "ZONA DA PIA", (10, zona_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Instrução
    cv2.putText(frame, "Faça JOINHA dentro da zona azul", (10, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Torneira Inteligente - Joinha", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()