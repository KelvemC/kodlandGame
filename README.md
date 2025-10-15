# Platformer Zombie Adventure

Um jogo simples de plataforma desenvolvido em Python usando PgZero, onde um herói precisa coletar itens enquanto evita zumbis. O objetivo é sobreviver e coletar todos os itens em um ambiente cheio de perigos!

## Requisitos
- Python 3.6 ou superior
- Biblioteca PgZero (`pip install pgzero`)

## Como Jogar
1. Clone ou baixe este repositório.
2. Certifique-se de ter o PgZero instalado (veja "Instalação" abaixo).
3. Navegue até a pasta do projeto no terminal.
4. Execute o jogo com: `pgzrun meu_jogo.py`.
5. Use as teclas:
   - **Setas esquerda/direita**: Mover o herói.
   - **Espaço**: Pular.
   - **Mouse**: Clique em "Start" no menu para começar ou "Quit" para sair.
6. Coletar todos os itens vence; tocar em zumbis reduz vidas. Perca todas as vidas para game over.

## Instalação
1. Instale o Python em [python.org](https://www.python.org/downloads/).
2. Atualize o pip: `python -m pip install --upgrade pip`.
3. Instale o PgZero: `pip install pgzero`.
4. Verifique com `pgzrun --version`.

## Estrutura do Projeto
meu_projeto/
├── meu_jogo.py          # Código principal do jogo
├── images/              # Sprites (herói, zumbis, itens, botões)
├── sounds/              # Efeitos sonoros (pulo, coleta, hit)
└── music/               # Música de fundo


## Assets
- **Sprites**: 
  - Herói e zumbis baseados em packs da Kenney [](https://kenney.nl/assets).
  - Exemplos: `hero_idle.png`, `zombie_walk1.png`, `item.png`.
  - Agradecimentos à comunidade Kenney por assets gratuitos!
- **Sons**: Efeitos como `jump.wav`, `collect.wav`, `hit.wav` (fonte: Kenney).
- **Música**: `background_music.ogg` (fonte: Kenney).

## Contribuições
- Sprites de zumbis e pessoas foram adicionados para enriquecer o tema. Ajuste os nomes no código (`meu_jogo.py`) se necessário (ex.: `Actor('zombie_walk1')`).
- Sinta-se à vontade para adicionar mais assets ou melhorar o código!

## Licença
Este projeto usa assets CC0 da Kenney. O código é original e pode ser usado/modificado livremente.

## Contato
Para dúvidas ou ajuda, consulte este README ou peça suporte ao criador do código! kelvemcif@gmail.com