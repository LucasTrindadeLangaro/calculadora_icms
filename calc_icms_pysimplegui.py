from PySimpleGUI import *

layout = [
    [Text('Valor total do produto'), InputText()],
    [Text('Aliquota do ICMS'), InputText()],
    [Text('Redução da Base de calculo'), InputText()],
    [Button('Calcular'), Button('Cancelar')],
    [Text('Base ICMS: ')],
    [Text('Aliq ICMS: ')],
    [Text('Valor ICMS: ')]
]

janela = Window("Titulo da janela", layout)


while True:
    #evento = todo clique que vc faz dentro da tela
    #valores
    evento, valores = janela.read()
    if evento == WIN_CLOSED:
        break

janela.close()