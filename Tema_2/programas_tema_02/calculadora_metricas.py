# ==========================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ========================================


peso_kg=float(input("Ingrese su peso en kg: "))
altura_cm=float(input("Ingrese su altura en cm: "))
edad=int(input("Ingrese su edad: "))

def calcular_imc(peso_kg, altura_m):
  """Calcula el Índice de Masa Corporal (IMC).
	Fórmula: IMC = peso / (altura^2)
	 
	    Parámetros:
	    peso_kg (float): Peso en kilogramos
	    altura_m (float): Altura en metros
	 
	    Retorna:
	    float: El IMC calculado
	    """
  imc = peso_kg / (altura_m ** 2)
  print(f"Tiene sobrepeso({imc:.2f}): return {imc >= 25}" )
  return imc >= 25

calcular_imc(peso_kg, altura_cm/100)
	 
def es_peso_saludable(imc):
	"""
	    Determina si el IMC está en rango saludable (18.5 - 24.9).
	 
	    Parámetro:
	    imc (float): Índice de Masa Corporal
	 
	    Retorna:
	    bool: True si está en rango saludable, False si no
	    """
	    # Operadores de comparación y lógicos
	print(f"Tiene bajo peso({imc:.2f}): return {18.5 <= imc <= 24.9}" )
	return 18.5 <= imc <= 24.9

es_peso_saludable(calcular_imc(peso_kg, altura_cm/100))
	 
def tiene_sobrepeso(imc):
	"""
	    Determina si hay sobrepeso (IMC >= 25).
	    """
	    # TU CÓDIGO AQUÍ
	print(f"Tiene sobrepeso({imc:.2f}): return {imc >= 25}" )
	return imc >= 25
	 
	 
def tiene_bajo_peso(imc):
	"""
	    Determina si hay bajo peso (IMC < 18.5).
	    """
	    # TU CÓDIGO AQUÍ
	print(f"Tiene bajo peso({imc:.2f}): return {imc < 18.5}" )
	return imc < 18.5
	 
	 
def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
	"""
	    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.
	    
	    Parámetros:
	    peso_kg (float): Peso en kg
	    altura_cm (float): Altura en cm
	    edad (int): Edad en años
	    es_hombre (bool): True si es hombre, False si es mujer
	    
	    Retorna:
	    float: Calorías diarias recomendadas
	    """
	    # Operadores aritméticos y booleanos
	    # Fórmula para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad)
	    # Fórmula para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad)
	 
	    # Usa el hecho de que True=1 y False=0
	    # TU CÓDIGO AQUÍ
	calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
	calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
	print(f"Calorías para hombre: {calorias_hombre:.2f}, Calorías para mujer: {calorias_mujer:.2f}")
	return es_hombre * calorias_hombre + (not es_hombre) * calorias_mujer
        #usa el hecho de que true1 y false 0
        #return es_hombre * calorias_hombre + (1 es_hombre) * calorias_mujer
	 
def calcular_agua_diaria(peso_kg):
	"""
	    Calcula litros de agua recomendados al día (35ml por kg de peso).
	    """
	    # TU CÓDIGO AQUÍ
	agua_litros = (peso_kg * 35) / 1000
	print(f"Calcular agua diaria:( {peso_kg}) return {agua_litros:.2f} litros" )
	return agua_litros
	 
def calcular_ritmo_cardiaco_maximo(edad):
	"""
	    Calcula el ritmo cardíaco máximo (220 - edad).
	    """
	    # TU CÓDIGO AQUÍ
	ritmo_cardiaco_max = 220 - edad
	print(f"Calcular ritmo cardíaco máximo:( {edad}) return {ritmo_cardiaco_max} bpm" )
	return ritmo_cardiaco_max

