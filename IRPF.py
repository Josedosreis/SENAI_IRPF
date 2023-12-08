while True:

    # Apresentação
    print(f'\n\t\t\t ------ Imposto de Renda ------ \n')

    # Entrada
    sl_bruto = float(input('Informe o salário: '))
    dp = int(input('Informe o numero de dependentes: '))

    desconto_dp = (189.59 * dp)
    sl_base = (sl_bruto - desconto_dp)

    # Processamento
    if sl_base < 1903.98:
        aliquota = 0.0
        imp_bruto = (sl_base * aliquota) - 0.0
    elif sl_base <= 2826.65:
        aliquota = 0.075
        imp_bruto = (sl_base * aliquota) - 142.80
    elif sl_base <= 3751.05:
        aliquota = 0.15
        imp_bruto = (sl_base * aliquota) - 354.80
    elif sl_base <= 4664.8:
        aliquota = 0.225
        imp_bruto = (sl_base * aliquota) - 636.13
    else:
        aliquota = 0.227
        imp_bruto = (sl_base * aliquota) - 869.36

    ir_devido = imp_bruto
    sl_liquido = (sl_bruto - ir_devido)
    aliq_efetiva = (ir_devido / sl_bruto)

    print('\n\t --- Saídas de Dados --- \n')

    # Saída
    print('Salário Bruto: __________________________________________________ R$: {:.2f}'.format(sl_bruto))
    print('Núm. Dependencia: __________________________________________________ {}'.format(dp))
    print('Salário Base: __________________________________________________ R$: {:.2f}'.format (sl_base))
    print('Aliquota: __________________________________________________ {:.2f}%'.format(aliquota*100))
    print('IR Devido: __________________________________________________ R$: {:.2f}'.format(ir_devido))
    print('Salário Liquido: __________________________________________________ R$: {:.2f}'.format(sl_liquido))
    print('Aliquota Efetiva: __________________________________________________ {:.2f}%'.format(aliq_efetiva*100))
    
    print('\n ---- Selecione a opção desejada')
    
    print('1. Calcular outro imposto de renda: ')
    print('2. Fechar: ')
    
    op = int(input(''))
        
    if op == 1:
        print('---- Carregando... ----- ')
    elif op == 2:
        print('---- Finalizando... ----- ')
        break
    else:
        print(' ---- Opção invalida!! ----- ')
        break
            
            
    
          
