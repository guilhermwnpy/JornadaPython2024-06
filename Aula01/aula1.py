import time
import pyautogui
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

tabela = pd.read_csv("Aula01/produtos.csv")

pyautogui.PAUSE = 1.2

# Entrar no chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
pyautogui.write(link)
pyautogui.press("enter")

# pausa 2 segundos após abrir o site
time.sleep(2)

# entra no campo de email
pyautogui.press("tab")
pyautogui.write("guilherme@gmail.com")

# entra no campo de senha 
pyautogui.press("tab")
pyautogui.write("ssfsddfdssd")

# entra no campo do botão e pressiona
pyautogui.press("tab")
pyautogui.press("enter")

# entra no primeiro campo do formulario de produtos
pyautogui.press("tab")

for linha in tabela.index:
    pyautogui.PAUSE = 0.5
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(0.5)
    for i in range(7):
        pyautogui.hotkey("shift", "tab")
