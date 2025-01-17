
# Bot de Clique Automático com Interface Gráfica

Este projeto é um **bot de clique automático** desenvolvido em Python, com uma interface gráfica simples, usando a biblioteca **Tkinter** para gerenciar a interação do usuário e **PyAutoGUI** para realizar cliques automáticos em uma área específica da tela. O bot localiza uma imagem na tela e clica automaticamente nela, com contagem de cliques e tempo de execução.

## Funcionalidades

- **Clique Automático**: O bot localiza uma imagem na tela e clica automaticamente nela a cada 2 segundos.
- **Interface Gráfica**: A interface gráfica exibe o tempo total de execução e o número de cliques realizados.
- **Botões de Controle**: O usuário pode iniciar ou parar o bot através dos botões na interface.
- **Contador de Cliques e Tempo**: A interface mostra o número de cliques realizados e o tempo total de execução.

## Como Usar

1. **Baixar ou Clonar o Repositório**:
   - Faça o download ou clone o repositório para o seu computador.

2. **Instalar Dependências**:
   - Instale as dependências necessárias com o comando:
     ```bash
     pip install -r requirements.txt
     ```

3. **Executar o Bot**:
   - Execute o script Python `bot_auto_clique_gui.py` para iniciar o bot com a interface gráfica:
     ```bash
     python bot_auto_clique_gui.py
     ```

4. **Usar a Interface**:
   - Clique no botão **Iniciar** para começar o processo de cliques automáticos.
   - Clique no botão **Parar** para interromper o processo.
   - A interface mostrará o tempo de execução e a contagem de cliques.

## Observações

- A imagem usada para localizar o item na tela precisa estar disponível no mesmo diretório do script, ou você pode modificar o caminho da imagem no código.
- **Git LFS** é usado para armazenar arquivos grandes como executáveis gerados pela compilação.

