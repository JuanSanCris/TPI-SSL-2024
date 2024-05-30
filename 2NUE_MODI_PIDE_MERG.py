import ply.lex as lex
import json 
import tkinter as tk
from tkinter import filedialog


# Lista de palabras reservadas
reserved = {
    '"version"': 'VERSION',
    '"firma_digital"': 'FIRMA_DIGITAL',
    '"empresas"': 'EMPRESAS',   #"List_empresas"
    '"nombre_empresa"': 'NOMBRE_EMPRE',
    '"fundacion"': 'FUNDACION',
    '"ingresos_anuales"': 'INGRESOS_ANUALES',
    '"pyme"': 'PYME',
    '"direccion"': 'DIRECCION',
    '"calle"': 'CALLE',
    '"ciudad"': 'CIUDAD',
    '"pais"': 'PAIS',
    '"departamentos"': 'DEPARTAMENTOS',
    '"sub_departamentos"': 'SUB_DPTOS',      #"Lista_Dpto",#"Lista_Sub", "Sub_Dpto",
    '"jefe"': 'JEFE',
    '"empleados"': 'EMPLEADOS', #"Lista_Empleados",
    '"nombre"': 'NOMBRE',
    '"edad"': 'EDAD',
    '"cargo"': 'CARGO',
    '"salario"': 'SALARIO',
    '"activo"': 'ACTIVO',
    '"fecha_contratacion"': 'FECHA_CONTRATACION',
    '"proyectos"': 'PROYECTOS',
    '"estado"': 'ESTADO',
    '"fecha_inicio"': 'FEC_INICIO',
    '"fecha_fin"': 'FEC_FIN',
}

# Lista de tokens
tokens = [
    'TEXTO',
    'ASIGNACION',
    'COMA',
    'APERT_LISTA',
    'CIERRE_LISTA',
    'APERT_BLOQUE',
    'CIERRE_BLOQUE',
    'NUMERO',
    'BOOLEANO',
    'FECHA',
    'FECHA_PRUEBA',
    'FLOTANTE'
] + list(reserved.values())


t_ASIGNACION = r':'
t_COMA = r','
t_APERT_LISTA = r'[[]'
t_CIERRE_LISTA = r'[]]'
t_APERT_BLOQUE = r'[{]'
t_CIERRE_BLOQUE = r'[}]'
t_NUMERO = r'[\d]+'
t_BOOLEANO = r'(true|false)'




# Expresiones regulares para tokens simples
#t_PLUS = r'\+'


def t_FECHA(t):
    r'["](\d{4})-(\d{2})-(\d{2})["]' #"1899-12-26"
    year = int(t.value[1:5])  # Extrae y convierte el año a un entero
    month = int(t.value[6:8])
    day = int(t.value[9:11])
    if not ((1900 <= year <= 2099) and (1 <= month <= 12) and (1 <= day <= 31)):
        print('Error en fecha')
    else:
        return t    


# Expresión regular para las cadenas con comillas que no sean la palabra reservada
def t_TEXTO(t):
    r'\"([^\\\n]|(\\.))*?\"'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.value = t.value[1:-1]  # Remueve las comillas si no es una palabra reservada
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'


# Manejar errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)


def t_ignore_tab(t):
    r'\t'

def t_ignora_espacios(t):
    r'\s'

def t_nueva_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Construir el lexer
lexer = lex.lex()

# Datos de prueba
#data = '"empresas": [ {\n"nombre_empresa": "MC Donals", "fundacion": 2025, "direccion": { "calle": "Calle Falsa 123", "ciudad": "Springfield", "pais": "USA"},}'

def leer_texto():
    print("Ingresa texto. Presiona Control + z (Ctrl + z) para finalizar.")

    texto = ""
    while True:
        try:
            # Leer una línea de entrada del usuario
            linea = input()
            texto += linea + '\n'  # Agregar la línea al texto completo
        except EOFError:
            print("\nFinalizando la lectura (Control + z detectado).")
            break

    return texto

if __name__ == "__main__":
    texto_ingresado = leer_texto()


#data = '"fecha_contratacion": "2001-04-30"'

# Alimentar al lexer con los datos
lexer.input(texto_ingresado)

# Imprimir los tokens generados
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)