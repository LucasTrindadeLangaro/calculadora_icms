from PySimpleGUI import *

layout = [
    [Text('Valor total do produto'), InputText(key='vlr_prod')],
    [Text('Aliquota do ICMS'), InputText(key='aliq')],
    #[Text('Redução da Base de calculo'), InputText(key=)],
    [Button('Calcular'), Button('Cancelar')],
    [Text('Base ICMS: ' ,key='texto_base_icms')],
    [Text('Aliq ICMS: ' ,key='texto_aliq_icms')],
    [Text('Valor ICMS: ',key='texto_valor_icms')]
]

janela = Window("Titulo da janela", layout)


while True:
    #evento = todo clique que vc faz dentro da tela
    #valores
    evento, valores = janela.read()
    if evento == WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Calcular':
        vlr_icms  = float(valores['vlr_prod'])*(float(valores['aliq'])/100)
        janela['texto_base_icms'].update(f'Base ICMS: {valores["vlr_prod"]}')
        janela['texto_aliq_icms'].update(f'Aliq ICMS: {valores["aliq"]}')
        janela['texto_valor_icms'].update(f'Valor ICMS: {vlr_icms}')
        print(vlr_icms)

janela.close()