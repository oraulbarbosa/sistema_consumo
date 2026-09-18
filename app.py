
# Sistema de Consumo de Água

tipo_imovel = input("Digite o tipo de imóvel: ").strip() # .strip retira os espaços em branco.
consumo_mensal = float(input("Digite o consumo mensal de água(m3): "))

if tipo_imovel == "Comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif (tipo_imovel == "Apartamento" or tipo_imovel == "Casa") and consumo_mensal <= 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "Apartamento" or tipo_imovel == "Casa") and consumo_mensal <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")





