import pyautogui
import time
import threading
import tkinter as tk

# Variáveis globais
clicando = False
cliques = 0
inicio_tempo = None

def iniciar():
    global clicando, cliques, inicio_tempo
    clicando = True
    cliques = 0
    inicio_tempo = time.time()
    atualizar_interface()
    loop_clicks()

def parar():
    global clicando
    clicando = False

def atualizar_interface():
    """Atualiza as informações na interface."""
    tempo_rodado = time.time() - inicio_tempo if inicio_tempo else 0
    tempo_formatado = time.strftime('%H:%M:%S', time.gmtime(tempo_rodado))
    
    tempo_label.config(text=f"Tempo Rodado: {tempo_formatado}")
    cliques_label.config(text=f"Cliques: {cliques}")
    
    if clicando:
        root.after(1000, atualizar_interface)  # Atualiza a cada 1 segundo

def loop_clicks():
    """Loop de cliques automáticos."""
    global cliques
    while clicando:
        item_pos = pyautogui.locateCenterOnScreen(r'D:\projetos_python_vscode\Bot-auto-clique\item.png', confidence=0.8)
        if item_pos:
            pyautogui.moveTo(item_pos)
            pyautogui.click()
            cliques += 1
        time.sleep(2)

def start_thread():
    """Inicia a thread para o loop de cliques."""
    threading.Thread(target=loop_clicks, daemon=True).start()

# Criar a janela principal
root = tk.Tk()
root.title("Bot de Clique Automático")

# Label para mostrar o tempo
tempo_label = tk.Label(root, text="Tempo Rodado: 00:00:00", font=("Arial", 14))
tempo_label.pack(pady=10)

# Label para mostrar o número de cliques
cliques_label = tk.Label(root, text="Cliques: 0", font=("Arial", 14))
cliques_label.pack(pady=10)

# Botão para iniciar o processo
iniciar_btn = tk.Button(root, text="Iniciar", font=("Arial", 14), command=lambda: [iniciar(), start_thread()])
iniciar_btn.pack(pady=10)

# Botão para parar o processo
parar_btn = tk.Button(root, text="Parar", font=("Arial", 14), command=parar)
parar_btn.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
