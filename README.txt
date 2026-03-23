# AI Backing Track Generator

Um script de automação em Python que faz o download de áudio do YouTube na melhor qualidade e utiliza Inteligência Artificial (Demucs/PyTorch) para separar os instrumentos musicais em trilhas independentes (Stems).

O objetivo principal é criar *backing tracks* limpas para prática instrumental, isolando vocais, bateria, baixo e outros instrumentos.

## Tecnologias Utilizadas
Python 3: Linguagem base da automação.
Demucs (Meta AI): Modelo de Machine Learning baseado em PyTorch para separação de fontes de áudio de alta fidelidade.
yt-dlp: Ferramenta de extração e roteamento de mídia do YouTube.
FFmpeg: Motor de processamento e conversão para o formato lossless (`.wav`).
Torchcodec:* Otimização de tensores de áudio processados pela IA.

## Arquitetura e Decisões de Design (KISS)
O projeto foi refatorado para seguir o princípio **KISS (Keep It Simple, Stupid)**. Integrações iniciais com APIs instáveis (como a do Spotify, sujeita a pesados *Rate Limits* e bloqueios de chave de desenvolvedor) foram removidas. O fluxo atual foca em estabilidade absoluta: extração direta via `yt-dlp` e processamento imediato pelo motor de IA local, sem depender de autenticações externas ou servidores de terceiros.

## Instalação e Uso

1. Clone este repositório:
`git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git`

2. Crie e ative um ambiente virtual:
`python -m venv .venv`
`# No Windows:`
`.venv\Scripts\activate`

3. Instale as dependências:
`pip install -r requirements.txt`

4. Execute o programa:
`python main.py`