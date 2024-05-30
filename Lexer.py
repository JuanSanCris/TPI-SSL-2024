import ply.lex as lex
import re
""" with open('archivo_ejemplo.json') as archivo_empresas:
    data = archivo_empresas.read() """
    
reservadas = ["VERSION","FIRMA_DIGITAL", "EMPRESAS", #"List_empresas" 
          "NOMBRE_EMPRESA","FUNDACION","INGRESOS_ANUALES","PYME",
          "DIRECCION","CALLE","CIUDAD","PAIS","DEPARTAMENTOS","SUBDEPARTAMENTOS",#"Lista_Dpto",#"Lista_Sub", "Sub_Dpto",
          "JEFE","EMPLEADOS", #"Lista_Empleados",
          "NOMBRE","EDAD","CARGO","SALARIO","ACTIVO","FECHA_CONTRATACION","PROYECTOS",#"Lista_Proyectos",
          "ESTADO","FEC_INICIO","FEC_FIN", "LINK"]

simbolos = ["TEXTO", "ASIGNACION", "COMA","APERT_LISTA","CIERRE_LISTA","APERT_BLOQUE","CIERRE_BLOQUE","NUMERO", "FLOTANTE", "BOOLEANO",
          "FECHA","FECHA_PRUEBA", "ERROR", "VACIO"]

tokens = simbolos + reservadas

t_VERSION = r'"version":'
t_FIRMA_DIGITAL = r'"firma_digital":'
t_EMPRESAS = r'"empresas":'
t_NOMBRE_EMPRESA = r'"nombre_empresa":'
t_FUNDACION = r'"fundacion":'
t_INGRESOS_ANUALES = r'"ingresos_anuales":'
t_PYME = r'"pyme":'
t_DIRECCION = r'"direccion":'
t_CALLE = r'"calle":'
t_CIUDAD = r'"ciudad":'
t_PAIS = r'"pais":'
t_DEPARTAMENTOS = r'"departamentos":'
t_SUBDEPARTAMENTOS = r'"subdepartamentos":'
t_JEFE = r'"jefe":'
t_EMPLEADOS = r'"empleados":'
t_NOMBRE = r'"nombre":'
t_EDAD = r'"edad":'
t_CARGO = r'"cargo":'
t_SALARIO = r'"salario":'
t_ACTIVO = r'"activo":'
t_FECHA_CONTRATACION = r'"fecha_contratacion":'
t_PROYECTOS = r'"proyectos":'
t_ESTADO = r'"estado":'
t_FEC_INICIO = r'"fecha_inicio":'
t_FEC_FIN = r'"fecha_fin":'
t_LINK = r'"link":'
#t_ASIGNACION = r':'
t_COMA = r','
t_APERT_LISTA = r'[[]'
t_CIERRE_LISTA = r'[]]'
t_APERT_BLOQUE = r'[{]'
t_CIERRE_BLOQUE = r'[}]'
t_NUMERO = r'[\d]+'
t_BOOLEANO = r'(true|false)'
t_VACIO = r'(null|[[][ ]*[]]|[{][ ]*[}])'
#t_FECHA = r'["](19[0-9][0-9]|20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])["]'

def t_FLOTANTE(t):
    r'[-+]?(\d*\.\d+|\.\d+)'
    return t


def t_FECHA(t):
    r'["](\d{4})-(\d{2})-(\d{2})["]'
    year = int(t.value[1:5])  # Extrae y convierte el año a un entero
    month = int(t.value[6:8])
    day = int(t.value[9:11])
    if not ((1900 <= year <= 2099) and (1 <= month <= 12) and (1 <= day <= 31)):
        print('Error en fecha')
    else:
        return t    
   
        
#Tokens de salto de linea o especiales que ignoran o muestran error
def t_ignore_tab(t):
    r'\t'

def t_ignora_espacios(t):
    r'\s'

def t_nueva_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Error de caracter '%s'" % t.value[0])
    t.lexer.skip(1)

def t_TEXTO(t): #"fecha_contratacion"
    r'\"([^\\\n]|(\\.))*?\"[:]?'
    if t.value[-1] == ':':
        t.value = t.value.strip(':')   
        if t.value.upper().strip('"') in reservadas:
            t.type = t.value.upper().strip('"')
        else:
            print("Error en linea ", t.lineno)
            t.type = 'ERROR'
    return t



lexer = lex.lex()




#data = '"empre":  [{\n"nombre": { },\n"version": 500.15, "fecha_contratacion": "1999-12-31", "link": "https://www.mcdonalds.com.ar", }]'


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


lexer.input(texto_ingresado)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
