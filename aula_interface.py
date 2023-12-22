import requests
from tkinter import *
import datetime as dt

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    hora = dt.datetime.now()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f''' 
    Cotação correspondente às : {hora}
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}'''

    texto_cotacao["text"] = texto

janela = Tk()
janela.title('Cotação das moedas')

texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas")
texto_orientacao.grid(column=0, row=0, padx=15, pady=10)

botao = Button(janela, text="Clique aqui", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx= 10, pady=15)

texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=0, row=2)
janela.mainloop()
