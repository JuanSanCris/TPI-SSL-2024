import ply.lex as lex
import re
""" with open('archivo_ejemplo.json') as archivo_empresas:
    datos = archivo_empresas.read() """
    
reservadas = ["VERSION","FIRMA_DIGITAL", "EMPRESAS", #"List_empresas" 
          "NOMBRE_EMPRE","FUNDACION","INGRESOS_ANUALES","PYME",
          "DIRECCION","CALLE","CIUDAD","PAIS","DEPARTAMENTOS","SUB_DPTOS",#"Lista_Dpto",#"Lista_Sub", "Sub_Dpto",
          "JEFE","EMPLEADOS", #"Lista_Empleados",
          "NOMBRE","EDAD","CARGO","SALARIO","ACTIVO","FECHA_CONTRATACION","PROYECTOS",#"Lista_Proyectos",
          "ESTADO","FEC_INICIO","FEC_FIN"]

simbolos = ["TEXTO", "ASIGNACION", "COMA","APERT_LISTA","CIERRE_LISTA","APERT_BLOQUE","CIERRE_BLOQUE","NUMERO","BOOLEANO",
          "FECHA","FECHA_PRUEBA"]

tokens = simbolos + reservadas

t_VERSION = r'"version"'
t_FIRMA_DIGITAL = r'"firma_digital"'
t_EMPRESAS = r'"empresas"'
t_NOMBRE_EMPRE = r'"nombre_empresa"'
t_FUNDACION = r'"fundacion"'
t_INGRESOS_ANUALES = r'"ingresos_anuales"'
t_PYME = r'"pyme":'
t_DIRECCION = r'"direccion"'
t_CALLE = r'"calle"'
t_CIUDAD = r'"ciudad"'
t_PAIS = r'"pais"'
t_DEPARTAMENTOS = r'"departamentos"'
t_SUB_DPTOS = r'"subdepartamentos"'
t_JEFE = r'"jefe"'
t_EMPLEADOS = r'"empleados"'
t_NOMBRE = r'"nombre"'
t_EDAD = r'"edad"'
t_CARGO = r'"cargo"'
t_SALARIO = r'"salario"'
t_ACTIVO = r'"activo"'
t_FECHA_CONTRATACION = r'"fecha_contratacion"'
t_PROYECTOS = r'"proyectos"'
t_ESTADO = r'"estado"'
t_FEC_INICIO = r'"fecha_inicio"'
t_FEC_FIN = r'"fecha_fin"'
t_ASIGNACION = r':'
t_COMA = r','
t_APERT_LISTA = r'[[]'
t_CIERRE_LISTA = r'[]]'
t_APERT_BLOQUE = r'[{]'
t_CIERRE_BLOQUE = r'[}]'
t_NUMERO = r'[\d]+'
t_BOOLEANO = r'(true|false)'
#t_FECHA = r'["](19[0-9][0-9]|20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])["]'


def t_FECHA(t):
    r'["](\d{4})-(\d{2})-(\d{2})["]' #"1899-12-26"
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
    r'["][\w\s]+["]'
    if t.value.upper().strip('"') in reservadas:
        t.type = t.value.upper().strip('"')
    return t


lexer = lex.lex()


#data = '"empresas": [ {\n"nombre_empresa": "MC Donals", "fundacion": 2025, "direccion": { "calle": "Calle Falsa 123", "ciudad": "Springfield", "pais": "USA"},}'

data = '"empresas" :  [{\n"nombre": "string",\n"version": "integer", "fecha_contratacion": "1999-12-31" }]'

#data = '"fecha_contratacion": "2001-04-30"'


#data = '"empresas": ['

lexer.input(data)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
