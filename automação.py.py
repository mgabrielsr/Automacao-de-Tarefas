# importar bibliotecas
import pyautogui as pa
import pandas as pd
import time

# tabela com produtos
tabela = pd.read_csv("produtos.csv")

# pyautogui.PAUSE = () -> Altera velocidade dos comandos
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever texto
# pyautogui.press -> pressionar uma tecla
# pyautogui.hotkey -> apertar um conjunto de teclas  (ctrl C, ctrl V, alt tab)

pa.PAUSE = (0.8)

pa.press("win")
pa.write("Chrome")
pa.press("enter")

time.sleep(1)

pa.click(x=551, y=313)
pa.click(x=743, y=28)
link = "https://forms.gle/VNkJynJhBSTmmwdv6"
pa.write(link)
pa.press("enter")

time.sleep(2)

for linha in tabela.index:
    
    codigo = str(tabela.loc[linha, "codigo"])

    pa.click(x=407, y=432)
    pa.write(str(tabela.loc[linha, "codigo"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
    
        pa.write(obs)
    pa.press("tab")
    pa.press("enter")

    time.sleep(2)

    pa.click(x=409, y=240)