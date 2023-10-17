from PySimpleGUI import *

aliquotas_por_estado = {
'Acre':	17,
'Alagoas':	17,
'Amazonas':	18,
'Amapá':	18,
'Bahia':	18,
'Ceará':	18,
'Distrito Federal':	18,
'Espírito Santo':	17,
'Goiás':	17,
'Maranhão':	18,
'Mato Grosso':	17,
'Mato Grosso do Sul':	17,
'Minas Gerais':	18,
'Pará':	17,
'Paraíba':	18,
'Paraná':	18,
'Pernambuco':	18,
'Piauí':	17,
'Rio Grande do Norte':	18,
'Rio Grande do Sul':	17,
'Rio de Janeiro':	18,
'Rondônia':	17.5,
'Roraima':	17,
'Santa Catarina':	17,
'São Paulo':	18,
'Sergipe':	18,
'Tocantins':	18,
}

layout = [
    [Text('Valor total do produto'), InputText(key='vlr_prod')],
    [Text('Escolha o Estado de origem'), Combo(list(aliquotas_por_estado.keys()), key='estado')],
    [Text('Escolha o Estado de destino'), Combo(list(aliquotas_por_estado.keys()), key='estado')],
    [Text('Redução da Base de cálculo', visible=False, key='input_texto_reducao'), InputText(key='reducao_base', visible=False)],
    [Button('Calcular'), Button('Calcular com Redução'), Button('Cancelar')],
    [Text('Base ICMS: ', key='texto_base_icms')],
    [Text('Redução de Base: ', visible=False, key='texto_reducao')],
    [Text('Aliq ICMS: ', key='texto_aliq_icms')],
    [Text('Valor ICMS: ', key='texto_valor_icms')]
]

janela = Window("Calculadora de ICMS", layout)

while True:
    # evento = todo clique que vc faz dentro da tela
    # valores

    evento, valores = janela.read()

    if evento in (WIN_CLOSED, 'Cancelar'):
        break

    if evento == 'Calcular com Redução':
        janela['input_texto_reducao'].update(visible=True)
        janela['reducao_base'].update(visible=True)

    if evento == 'Calcular':
        if valores['vlr_prod'] == '':
            valores['vlr_prod'] = '0'
        if valores['reducao_base'] == '':
            valores['reducao_base'] = '0'
        
        if janela['reducao_base'].visible and float(valores['reducao_base'].replace(',','.')) > 0:
            valor_input = valores['vlr_prod'].replace(',','.')
            percent_reduc = float(valores['reducao_base'].replace(',','.')) / 100
            base_icms = float(valores['vlr_prod'].replace(',','.')) * (1 - percent_reduc)
            estado_selecionado = valores['estado']
            if estado_selecionado in aliquotas_por_estado:
                aliq_estado = aliquotas_por_estado[estado_selecionado]
            else:
                aliq_estado = 0 
            vlr_icms = base_icms * (aliq_estado / 100)

            janela['texto_base_icms'].update(f'Base ICMS: R$ {base_icms:.2f}')
            janela['texto_reducao'].update(visible=True)
            janela['texto_reducao'].update(f'Redução de Base: {valores["reducao_base"]}%')
            janela['texto_aliq_icms'].update(f'Aliq ICMS: {aliq_estado}%')
            
            formatado_icms = f'Valor ICMS: R$ {vlr_icms:.2f}'
            formatado_icms = formatado_icms.replace('.',',').replace('_','.')
            janela['texto_valor_icms'].update(formatado_icms)
        
        else:
            vlr_icms  = float(valores['vlr_prod'].replace(',','.')) * (aliquotas_por_estado[valores['estado']] / 100)

            janela['texto_base_icms'].update(f'Base ICMS: R$ {valores["vlr_prod"]}')
            janela['texto_aliq_icms'].update(f'Aliq ICMS: {aliquotas_por_estado[valores["estado"]]}%')

            formatado_icms = f'Valor ICMS: R$ {vlr_icms:.2f}'
            formatado_icms = formatado_icms.replace('.',',').replace('_','.')
            janela['texto_valor_icms'].update(formatado_icms)
            print(vlr_icms)

janela.close()
