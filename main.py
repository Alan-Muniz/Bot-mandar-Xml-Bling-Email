import pyautogui as pyag
import pyperclip
import time
pyag.alert("Vai Começar, aperte OK,e não mexa em nada até que o software acabe seu trabalho!")
time.sleep(8)

#entrar no google chrome
pyag.PAUSE = 1.5

pyag.press("win")
pyag.write("chrome")
pyag.press("enter")
time.sleep(3)
pyag.hotkey("win","up")
#abrir nova aba
pyag.hotkey("ctrl","t")

#entrar no erp
pyperclip.copy("https://www.bling.com.br/login?r=https%3A%2F%2Fwww.bling.com.br%2Fdashboard")
pyag.hotkey("ctrl","v")
pyag.press("enter")
time.sleep(10)
pyag.hotkey("ctrl","a")
time.sleep(4)
pyag.write("realvariedades")
time.sleep(4)
pyag.click(x=589, y=582)
time.sleep(3)
pyag.press("enter")
time.sleep(5)
#baixar xml das notas
pyag.click(x=276, y=120)
time.sleep(5)
pyag.click(x=320, y=376)
time.sleep(3)
pyag.click(x=24, y=268)
time.sleep(3)
pyag.click(x=1480, y=458)
time.sleep(5)
pyag.click(x=754, y=632)
time.sleep(5)

#abrir email
pyag.hotkey("ctrl","t")
time.sleep(5)
pyag.click(x=1394, y=133)
time.sleep(5)

#compor email
time.sleep(10)
pyag.click(x=89, y=195)
time.sleep(5)
pyag.write("alanenvil@hotmail.com")
pyag.press("tab")
pyag.press("tab")
pyag.write("xml das notas empresa AUERICA ALVES FERREIRA MUNIZ-ME")
pyag.press("tab")
time.sleep(5)
pyperclip.copy("Bom dia segue em anexo o xml das notas da empresa: AUERICA ALVES FERREIRA MUNIZ-ME ")
pyag.hotkey("ctrl","v")
time.sleep(5)
#colocando anexo e enviando o email
pyag.click(x=1119, y=829)
time.sleep(5)
pyag.click(x=307, y=171)
time.sleep(2)
pyag.press("enter")
time.sleep(15)
pyag.hotkey("ctrl","enter")