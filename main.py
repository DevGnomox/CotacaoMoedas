

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")


class MoedaAgora(App):
    def build(self):
        return GUI

    def on_start(self):

        self.root.ids["valor1"].text = f"Dólar R$ {self.cotacao('USD')}"
        self.root.ids["valor2"].text = f"Euro R$ {self.cotacao('EUR')}"
        self.root.ids["valor3"].text = f"Bitcoin R$ {self.cotacao('BTC')}"
        self.root.ids["valor4"].text = f"Ethereum R$ {self.cotacao('ETH')}"
        self.root.ids["valor5"].text = f"Iene Japonês R$ {self.cotacao('JPY')}"
        self.root.ids["valor6"].text = f"Dólar Canadense R$ {self.cotacao('CAD')}"
        self.root.ids["valor7"].text = f"Dólar Australiano R$ {self.cotacao('AUD')}"
        self.root.ids["valor8"].text = f"Libra Esterlina R$ {self.cotacao('GBP')}"
        self.root.ids["valor9"].text = f"Yuan Chinês R$ {self.cotacao('CNY')}"
        self.root.ids["valor10"].text = f"Dogecoin R$ {self.cotacao('DOGE')}"

        self.root.ids["valor11"].text = f"Dólar R$ {self.cotacaoo('USD')}"
        self.root.ids["valor22"].text = f"Euro R$ {self.cotacaoo('EUR')}"
        self.root.ids["valor33"].text = f"Bitcoin R$ {self.cotacaoo('BTC')}"
        self.root.ids["valor44"].text = f"Ethereum R$ {self.cotacaoo('ETH')}"
        self.root.ids["valor55"].text = f"Iene Japonês R$ {self.cotacaoo('JPY')}"
        self.root.ids["valor66"].text = f"Dólar Canadense R$ {self.cotacaoo('CAD')}"
        self.root.ids["valor77"].text = f"Dólar Australiano R$ {self.cotacaoo('AUD')}"
        self.root.ids["valor88"].text = f"Libra Esterlina R$ {self.cotacaoo('GBP')}"
        self.root.ids["valor99"].text = f"Yuan Chinês R$ {self.cotacaoo('CNY')}"
        self.root.ids["valor100"].text = f"Dogecoin R$ {self.cotacaoo('DOGE')}"

    def cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        valor_moeda = requisicao.json()
        cota = valor_moeda[f"{moeda}BRL"]["bid"]
        return cota

    def cotacaoo(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        valor_moeda = requisicao.json()
        cota = valor_moeda[f"{moeda}BRL"]["pctChange"]
        return cota


MoedaAgora().run()