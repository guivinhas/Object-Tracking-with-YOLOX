# YOLO Object Tracking with Roboflow
Este projeto foi desenvolvido com o objetivo de aprender e explorar o rastreamento de objetos em vídeos utilizando técnicas avançadas de Visão Computacional. Utilizando a API do Roboflow para detecção de objetos, o código aplica o YOLO para realizar o rastreamento de jogadores, bola e juízes em um vídeo de futebol.
![image](https://github.com/user-attachments/assets/c895dd72-8401-47ae-a752-0d7acb50a530)

# Tecnologias Utilizadas
OpenCV: Usado para processamento de vídeo e exibição dos resultados em tempo real.
Roboflow API: Plataforma para treinamento e deployment de modelos de detecção de objetos. Utilizamos a API para carregar e rodar o modelo de detecção de futebol.
YOLO (You Only Look Once): Um modelo de detecção de objetos em tempo real. O YOLO é eficiente e rápido, adequado para aplicações que exigem processamento em tempo real, como rastreamento de objetos em vídeos.
Como Funciona
O vídeo de entrada é analisado frame a frame. Para cada frame, o modelo de detecção de objetos (YOLO) identifica jogadores, a bola e juízes no vídeo e desenha caixas delimitadoras ao redor deles. Durante o processamento do vídeo, o código também permite interação com a reprodução, como pausa, reinício e controle de progresso.

# Funcionalidades
Detecção de Objetos: Utiliza a API Roboflow para detectar jogadores, bola e juízes em vídeos de futebol.
Desenho de Caixas Delimitadoras: As caixas de rastreamento são desenhadas ao redor dos objetos detectados, com rótulos e confiança da previsão.
Controle de Vídeo: Permite controlar a reprodução do vídeo (pausar, reiniciar e controle de progresso).
# Como Rodar o Projeto
Pré-requisitos
Python 3.x
OpenCV (pip install opencv-python)
Roboflow SDK (pip install roboflow)
Modelo treinado no Roboflow para detecção de futebol (substitua API_KEY e MODEL_ID pelos valores apropriados).
# Passos
Instalar as dependências:

bash
Copiar
Editar
pip install opencv-python roboflow
Baixar o vídeo: Adicione o vídeo que será processado no mesmo diretório do script. A variável video_path no código está configurada para "videoplayback1.mp4", mas você pode ajustá-la conforme necessário.

# Executar o script:

bash
Copiar
Editar
python tracker.py
O vídeo será processado e as caixas delimitadoras serão desenhadas sobre os objetos detectados. Use as teclas para interagir com a reprodução:

p: Pausar/Continuar
r: Reiniciar o vídeo
q: Sair do programa

# Aprendizados
Durante o desenvolvimento deste projeto, aprendi:

Integração com API de Detecção de Objetos: Como utilizar o Roboflow para carregar e executar modelos de detecção de objetos em vídeos.
Processamento de Vídeo com OpenCV: Como ler e manipular vídeos frame a frame, além de desenhar caixas delimitadoras e adicionar rótulos.
Aplicação Prática de YOLO: Como aplicar o modelo YOLO para detecção de objetos em tempo real, com foco no rastreamento de jogadores e outros elementos em vídeos de futebol.

Este foi um projeto desafiador, mas extremamente recompensador. Ele me proporcionou uma compreensão mais profunda de como as técnicas de Visão Computacional podem ser aplicadas em problemas do mundo real, como análise de esportes e monitoramento de atividades.
