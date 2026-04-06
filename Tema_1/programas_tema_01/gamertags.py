def cabecera():
    '''Muestra la cabecera de la aplicacion'''
    titulo= r""" ______     ______     __    __     ______     ______     ______   ______     ______     ______    
/\  ___\   /\  __ \   /\ "-./  \   /\  ___\   /\  == \   /\__  _\ /\  __ \   /\  ___\   /\  ___\   
\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   \ \  __<   \/_/\ \/ \ \  __ \  \ \ \__ \  \ \___  \  
 \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\    \ \_\  \ \_\ \_\  \ \_____\  \/\_____\ 
  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/   \/_/ /_/     \/_/   \/_/\/_/   \/_____/   \/_____/ 
                                   🎮   ¡Crea tu identidad gamer!  🕹️                                                                     
                                                                                                   """
    print(titulo)
#cabecera()

def crear_tag_basico(nombre):
    """
    Crea un gamertag basico usando las primeras 4 letras del nombre.

    Parametro:
    nombre(str): El nombre del usuario

    Retorna:
    str: Gamertag basico
    """
    tag = nombre[0:4]
    return tag
#tag_basico=crear_tag_basico("Maria")
#print(tag_basico)

def crear_tag_invertido(nombre):
    '''
    Crea un gamertag invirtiendo el nombre completo
    Parametro:
    str: el nombre del usuario

    Retorna
    str: Gamertag(nombre) invertido
    '''
    #straig
    tag= nombre[::-1]
    return tag
#tag_invertido= crear_tag_invertido('Maria')
#print(tag_invertido)

def crear_tag_intercalado(nombre, apellido):
    '''
    Crea un gamertag intercalando el nombre completo y apellido
    Parametro:
    str: el nombre del usuario
    str: apellido del usuario

    Retorna
    str: Gamertag(nombre) intercalado
    '''
    #l1 = nombre[0]
    #l2= apellido[0]
    #l3= nombre[2:-1]
    #l4= apellido[2:-1]
    #print(l1,l2,l3,l4)
    nombre1= nombre[0]
    apellido1= apellido[0]
    nombre2=nombre[1:]
    apellido2=apellido[1:]
    print("3.TAG INTERCALADO: ",nombre1,apellido1,nombre2,apellido2,sep="")
    
#crear_tag_intercalado()

def crear_tag_elite(nombre):
    
    inicio=nombre[:2]
    final= nombre[-2:]
    #pass
    print("4.TAG ELITE: ",inicio,final,sep="")
#crear_tag_elite()

def crear_tag_con_numero(nombre,numero):
    print("5.TAG CON NUMERO: ",nombre[:5],numero,sep="")

def mostrar_estadisticas(nombre):
    """
    Muestra estadisticas del nombre proporcionado
    
    Parametro
    nombre(str): el nombre a analizar

    Retorna
    None(Imprime directamente)
    """
    longitud_nombre=len(nombre)
    print("\n Estadisticas de tu nombre:")
    print("\n Nombre completo:",nombre)
    print("\n Longitud del nombre:" ,longitud_nombre)
    print("\n Primera letra : ",nombre[0])
    print("\n Ultima letra : ",nombre[-1])

def generar_opciones(nombre,apellido,numero):
    """
    Genera y muestra todas las opciones de gamertags

    Parametros:
    nombre (str): Nombre del usuario
    apellido(str):Apellido usuario
    numero(str): NUmero fav
    """
    print("\n====================================================")
    print("TUS OPCIONES DE GAMERTAG:")
    print("\n====================================================")

    tag_basico=crear_tag_basico(nombre)
    print("1.TAG BASICO: ",tag_basico)
    print("2.TAG INVERTIDO: ",crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre,apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre,numero)
    print("\n====================================================")

#=================================================================
#APLICACION PRINCIPAL
#=================================================================
#Llamar a ña funcion cabecera
cabecera()

#Solicitar datos al usuario
nombre = input("\n Introduce tu nombre: ")
apellido = input("\n Introduce tu apellido: ")
numero = input("\n Introduce tu numero favorito: ")

#mostrar estadisticas del nombre

mostrar_estadisticas(nombre)
generar_opciones(nombre,apellido,numero)

print("\n ¡Elige tu favorito y conquista el mundo gamer! 🏁😎\n")
