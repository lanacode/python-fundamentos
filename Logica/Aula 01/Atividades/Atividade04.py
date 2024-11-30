salarioMensal = input('Digite seu salario bruto: ')
horasTrabalhadas = input('Digite quantas horas você trabalha por semana: ')

salarioMensal = int(salarioMensal)
horasTrabalhadas = int(horasTrabalhadas)

horasTrabalhadasPorMes = horasTrabalhadas*4

salarioPorHora = horasTrabalhadasPorMes/salarioMensal

print(f'você recebe R${salarioPorHora} por hora')
