# Snake - AI Body Motion Sense

## Visão Geral

Este projeto utiliza inteligência artificial para detectar movimentos corporais e controlar o jogo clássico Snake. Através do uso de modelos de aprendizado de máquina, como o PoseNet e o Teachable Machine, o jogador pode controlar a direção da cobra no jogo usando apenas movimentos do corpo.

## Funcionalidades

- **Controle por Movimento**: Use movimentos corporais para controlar a direção da cobra no jogo.
- **Detecção de Poses em Tempo Real**: A webcam capta os movimentos do jogador e os converte em comandos de direção.
- **Jogo Snake**: Experimente o jogo Snake clássico com uma nova forma de interação.

## Tecnologias Utilizadas

- **HTML/CSS/JavaScript**: Estruturação e estilização da interface do jogo.
- **TensorFlow.js**: Biblioteca utilizada para a inferência dos modelos de aprendizado de máquina.
- **Teachable Machine Pose**: API para detecção e classificação de poses corporais.
- **PoseNet**: Modelo pré-treinado para estimativa de poses humanas.

## Como Executar o Projeto

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/snake-ai-body-motion-sense.git
   cd snake-ai-body-motion-sense

  Instale as Dependências:
Este projeto utiliza apenas bibliotecas carregadas via CDN, então não há dependências para instalar.

Inicie o Projeto:
Basta abrir o arquivo index.html no seu navegador preferido. O jogo iniciará, e você poderá controlar a cobra com seus movimentos corporais.

Estrutura do Projeto
index.html: Estrutura principal do jogo.
styles.css: Estilos CSS aplicados ao jogo.
script.js: Lógica do jogo Snake e integração com a IA.
model.json e metadata.json: Arquivos do modelo de detecção de poses.
Como Jogar
Acesse o Jogo: Abra o arquivo index.html em seu navegador.
Posicione-se na Frente da Webcam: A webcam capturará seus movimentos.
Controle a Cobra: Movimente seu corpo para cima, baixo, esquerda ou direita para controlar a direção da cobra.
Contribuição
Sinta-se à vontade para contribuir com este projeto! Para sugestões, problemas ou melhorias, abra uma issue ou envie um pull request.
