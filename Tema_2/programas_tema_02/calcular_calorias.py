def calcular_calorias(carbohidratos, proteinas, grasas):
   carbohidratos_cal = carbohidratos * 4
   proteinas_cal= proteinas * 4
   grasas_cal= grasas * 9
   total_calorias = carbohidratos_cal + proteinas_cal + grasas_cal
   return total_calorias

calorias=calcular_calorias(10,40,5)
print(f"Calorías totales: {calorias}")

calorias=calcular_calorias(60,10,7)
print(f"Calorías totales: {calorias}")

calorias=calcular_calorias(10,40,5)
print(f"Calorías totales: {calorias}")

