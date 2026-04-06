palabra_adivinar="azucar"
def adivinar_palabra(letra_prueba,palabra_intento):
    letra_en_palabra=letra_prueba in palabra_adivinar
    print(f"¿La letra de prueba se encuentra en la palabra?{letra_en_palabra}")
    comparacion=palabra_intento==palabra_adivinar
    resultado_adivinanza=len(palabra_adivinar)==len(palabra_intento)
    resultado=comparacion and resultado_adivinanza
    print(f"El jugador gana:{resultado}")
adivinar_palabra("z","azúcar")
 