import cv2
import time
from inference_sdk import InferenceHTTPClient

# Configurações do Roboflow
API_KEY = "0HYBwl9ki5IOLdcdQnkF"  # Substitua pela sua chave de API
MODEL_ID = "football-players-detection-3zvbc/1"  # Substitua pelo seu model_id

# Cores para cada classe (em formato BGR)
COLORS = {
    "player": (0, 255, 0),  # Verde para jogadores
    "ball": (0, 0, 255),    # Vermelho para a bola
    "referee": (255, 0, 0)  # Azul para juízes
}

# Inicializa o cliente do Roboflow
client = InferenceHTTPClient(
    api_url="http://localhost:9001",  # URL do servidor de inferência local
    api_key=API_KEY
)

# Função para desenhar caixas delimitadoras com estilo
def draw_boxes(frame, detections):
    for detection in detections:
        x = detection["x"]
        y = detection["y"]
        width = detection["width"]
        height = detection["height"]
        label = detection["class"]
        confidence = detection["confidence"]

        # Converte as coordenadas para inteiros
        x1 = int(x - width / 2)
        y1 = int(y - height / 2)
        x2 = int(x + width / 2)
        y2 = int(y + height / 2)

        # Cor da caixa com base na classe
        color = COLORS.get(label, (0, 255, 0))  # Verde padrão se a classe não for mapeada

        # Desenha a caixa delimitadora
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # Fundo semi-transparente para o rótulo
        label_text = f"{label} {confidence:.2f}"
        (label_width, label_height), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(frame, (x1, y1 - label_height - 10), (x1 + label_width, y1), color, -1)

        # Desenha o rótulo
        cv2.putText(frame, label_text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# Função para processar o vídeo
def process_video(video_path):
    global cap, paused, frame_count, start_time

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Cria uma janela redimensionável
    cv2.namedWindow("YOLO Object Tracking", cv2.WINDOW_NORMAL)

    # Obtém o número total de frames no vídeo
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Cria uma barra de progresso (linha do tempo)
    cv2.createTrackbar("Progresso", "YOLO Object Tracking", 0, total_frames, on_trackbar)

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break

            # Atualiza a posição da barra de progresso
            cv2.setTrackbarPos("Progresso", "YOLO Object Tracking", frame_count)

            # Executa a inferência no frame atual
            result = client.infer(frame, model_id=MODEL_ID)

            # Desenha as caixas delimitadoras
            draw_boxes(frame, result["predictions"])

            # Exibe o frame
            cv2.imshow("YOLO Object Tracking", frame)

        # Controles de teclado
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Pressione 'q' para sair
            break
        elif key == ord('p'):  # Pressione 'p' para pausar/continuar
            paused = not paused
        elif key == ord('r'):  # Pressione 'r' para reiniciar o vídeo
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frame_count = 0

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "videoplayback1.mp4"  # Substitua pelo nome do seu vídeo
    process_video(video_path)