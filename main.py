'Informação de massa dos módulos da espaçonave'
massa_dos_modulos = [88062, 147838, 73346, 80732, 89182, 86798, 145656, 53825, 79515, 78250, 143033, 53680, 89366, 123255, 74974, 65373, 107733, 118266, 50726, 87810, 104355, 85331, 109624, 54282, 107472, 119291, 128702, 81132, 94609, 105929, 63918, 113360, 66932, 145080, 132130, 63858, 104334, 140635, 67642, 111552,93446, 59263, 133164, 119788, 97327, 77379, 144054, 110747, 89394, 123533, 86026, 124422, 108855, 125000, 99270, 55789, 146945, 103156, 141044, 94238, 136833, 54370, 69178, 142349, 72239, 149992, 50901, 112759, 105467, 90841, 55693, 52532, 92343, 134889, 143351, 123359, 134972, 59986, 85415, 136521, 81581, 131078, 131201, 56194, 142135, 69982, 140667, 110013, 67772, 108135, 
92591, 87200, 78189, 73407, 145395, 131869, 143480, 82068, 82423,110819]

'Use essas variaveis para dar a resposta nas partes 1 e 2'
combustivel1 = 0
combustivel2 = 0

'Parte 1 - Seu código vai aqui \/ ----------------------'

for x in massa_dos_modulos:
  num = (x / 3) - 2
  num = int(num)
  combustivel1 += num

'Parte 2 - Seu código vai aqui \/ ----------------------'


for x in massa_dos_modulos:
  num = (x / 3) - 2
  num = int(num)
  combustivel2 += num
  # print(num)
  while num > 3:
    num = (num / 3) - 2
    num = int(num)
    # print(num)
    combustivel2 += num
  
  


'------------------------------------------------------'

print(f'Para a parte 1 é necessário de combustível: {combustivel1}')
print(f'Para a parte 2 é necessário de combustível: {combustivel2}')