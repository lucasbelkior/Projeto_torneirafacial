from deepface import DeepFace
import cv2
import time
import os
import serial
from datetime import datetime


# ==========================
# CONFIGURAÇÕES
# ==========================

COM_ARDUINO = "COM3"

TEMPO_TOTAL = 60

TEMPO_ABERTA_INICIO = 8

TEMPO_FECHADA = 42

INTERVALO_RECONHECIMENTO = 2


# ==========================
# ARDUINO
# ==========================

arduino = serial.Serial(
    COM_ARDUINO,
    9600
)

time.sleep(2)


def abrir_torneira():

    arduino.write(b"ABRIR\n")

    print("TORNEIRA ABERTA")



def fechar_torneira():

    arduino.write(b"FECHAR\n")

    print("TORNEIRA FECHADA")




# ==========================
# PASTAS
# ==========================

os.makedirs(
    "videos",
    exist_ok=True
)

os.makedirs(
    "logs",
    exist_ok=True
)



# ==========================
# CAMERA
# ==========================

cap = cv2.VideoCapture(
    0,
    cv2.CAP_DSHOW
)


cap.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    640
)

cap.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    480
)



# ==========================
# VARIÁVEIS
# ==========================

ultimo_teste = 0

funcionario = "Nenhum"

mensagem = "Aguardando..."

gravando = False

inicio = 0

estado = "FECHADA"

video = None




print("Sistema Hospitalar iniciado")



# ==========================
# LOOP
# ==========================

while True:


    ret, frame = cap.read()


    if not ret:

        continue



    agora = time.time()



    # ==========================
    # RECONHECIMENTO
    # ==========================


    if not gravando and agora - ultimo_teste > INTERVALO_RECONHECIMENTO:


        try:


            resultado = DeepFace.find(

                img_path=frame,

                db_path="funcionarios",

                model_name="Facenet",

                detector_backend="opencv",

                enforce_detection=False

            )


            if len(resultado) > 0:


                dados = resultado[0]


                if not dados.empty:


                    caminho = dados.iloc[0]["identity"]


                    funcionario = os.path.basename(

                        os.path.dirname(caminho)

                    )


                    print(
                        "Reconhecido:",
                        funcionario
                    )


                    mensagem = "FUNCIONARIO RECONHECIDO"


                    gravando = True


                    inicio = agora



                    abrir_torneira()


                    estado = "ABERTA"



                    nome_video = (

                        f"videos/{funcionario}_"

                        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"

                    )


                    video = cv2.VideoWriter(

                        nome_video,

                        cv2.VideoWriter_fourcc(*"mp4v"),

                        20,

                        (640,480)

                    )


                    with open(

                        "logs/registros.txt",

                        "a"

                    ) as log:


                        log.write(

                            f"{datetime.now()} - {funcionario}\n"

                        )




        except Exception as erro:


            print(

                "Erro reconhecimento:",

                erro

            )


        ultimo_teste = agora





    # ==========================
    # PROTOCOLO 60 SEGUNDOS
    # ==========================


    tempo_passado = 0



    if gravando:


        tempo_passado = agora - inicio


        video.write(frame)



        if tempo_passado < 8:


            if estado != "ABERTA":

                abrir_torneira()


            estado = "ABERTA"




        elif tempo_passado < 50:


            if estado != "FECHADA":

                fechar_torneira()


            estado = "FECHADA"




        elif tempo_passado < 60:


            if estado != "ABERTA":

                abrir_torneira()


            estado = "ABERTA"




        else:


            fechar_torneira()


            video.release()

            video = None


            gravando = False


            funcionario = "Nenhum"


            mensagem = "Aguardando..."

            estado = "FECHADA"


            print(
                "Processo finalizado"
            )



    restante = int(

        TEMPO_TOTAL - tempo_passado

    )



    # ==========================
    # TELA
    # ==========================


    cv2.putText(

        frame,

        mensagem,

        (20,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (0,255,0),

        2

    )


    cv2.putText(

        frame,

        f"Funcionario: {funcionario}",

        (20,90),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (255,255,0),

        2

    )



    cv2.putText(

        frame,

        f"Torneira: {estado}",

        (20,140),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (0,0,255),

        2

    )



    cv2.putText(

        frame,

        f"Tempo: {max(restante,0)}s",

        (20,190),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (255,255,255),

        2

    )



    cv2.imshow(

        "Sistema Hospitalar",

        frame

    )



    if cv2.waitKey(1) == 27:

        break




cap.release()


if video:

    video.release()


arduino.close()


cv2.destroyAllWindows()