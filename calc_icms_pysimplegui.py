from PySimpleGUI import *

layout = [
    [Text('Valor total do produto'), InputText(key='vlr_prod')],
    [Text('Aliquota do ICMS'), InputText(key='aliq')],
    [Text('Redução da Base de calculo', visible=False, key='input_texto_reducao'), InputText(key='reducao_base', visible=False)],
    [Button('Calcular'), Button('Calcular com Redução'), Button('Cancelar')],
    [Text('Base ICMS: ' ,key='texto_base_icms')],
    [Text('Redução de Base: ',visible=False, key='texto_reducao')],
    [Text('Aliq ICMS: ' ,key='texto_aliq_icms')],
    [Text('Valor ICMS: ',key='texto_valor_icms')]
]

janela = Window("Calculadora de ICMS", layout)


while True:
    #evento = todo clique que vc faz dentro da tela
    #valores

    evento, valores = janela.read()

    if evento == WIN_CLOSED or evento == 'Cancelar':
        break

    if evento == 'Calcular com Redução':
        janela['input_texto_reducao'].update(visible=True)
        janela['reducao_base'].update(visible=True)

    if evento == 'Calcular':

        if janela['reducao_base'].visible and float(valores['reducao_base']) > 0:
            if float(valores['reducao_base']) == 0:
                break
            percent_reduc = float(valores['reducao_base'])/100
            calc_base_icms = float(valores['vlr_prod'])*percent_reduc
            base_icms = float(valores['vlr_prod'])-calc_base_icms
            print(base_icms)
            vlr_icms = base_icms*(float(valores['aliq'])/100)

            janela['texto_base_icms'].update(f'Base ICMS: R$ {base_icms}')
            janela['texto_reducao'].update(visible=True)
            janela['texto_reducao'].update(f'Redução de Base: {valores["reducao_base"]}%')
            janela['texto_aliq_icms'].update(f'Aliq ICMS: {valores["aliq"]}%')
            
            formatado_icms = f'Valor ICMS: R$ {vlr_icms:_.2f}'
            formatado_icms = formatado_icms.replace('.',',').replace('_','.')
            janela['texto_valor_icms'].update(formatado_icms)
        
        else:
            vlr_icms  = float(valores['vlr_prod'])*(float(valores['aliq'])/100)

            janela['texto_base_icms'].update(f'Base ICMS: R$ {valores["vlr_prod"]}')
            janela['texto_aliq_icms'].update(f'Aliq ICMS: {valores["aliq"]}%')

            formatado_icms = f'Valor ICMS: R$ {vlr_icms:_.2f}'
            formatado_icms = formatado_icms.replace('.',',').replace('_','.')
            janela['texto_valor_icms'].update(formatado_icms)
            print(vlr_icms)

janela.close()