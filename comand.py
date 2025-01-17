import pyautogui
import time

# Assinatura
print("Desenvolvido por: Lucas P")
print("Este programa foi feito para automação de cliques.")


# Aguarda alguns segundos antes de iniciar
print("Iniciando em 3 segundos...")
time.sleep(3)

while True:
    item_pos = pyautogui.locateCenterOnScreen('D:\projetos_python_vscode\Bot-auto-clique\item.png', confidence=0.8)

    if item_pos:
        print(f"Item Encontrado em{item_pos}")
        pyautogui.moveTo(item_pos)
        pyautogui.click()
    else:
        print("Item não encontrado")
    time.sleep(2)
