import ply.lex as lex
import re
""" with open('archivo_ejemplo.json') as archivo_empresas:
    datos = archivo_empresas.read() """

tokens = ["Version","FirmaDigital", "Empresas", #"List_empresas" 
          "Nombre_Empre","Fundacion","Ingresos_Anuales","Pyme",
          "Direccion","Calle","Ciudad","Pais","Departamentos","Sub_Dptos",#"Lista_Dpto",#"Lista_Sub", "Sub_Dpto",
          "Jefe","Empleados", #"Lista_Empleados",
          "Nombre","Edad","Cargo","Salario","Activo","Fec_Contra","Proyectos",#"Lista_Proyectos",
          "Estado","Fec_Inicio","Fec_Fin","Texto","ApertLista","CierreLista","ApertBloque","CierreBloque","Numero","Booleano",
          "Fecha","FechaPrueba", "Asignacion"]

t_Version = r'"version"'
t_FirmaDigital = r'"firma_digital"'
t_Empresas = r'"empresas"'
t_Nombre_Empre = r'"nombre_empresa"'
t_Fundacion = r'"fundacion"'
t_Ingresos_Anuales = r'"ingresos_anuales"'
t_Pyme = r'"pyme":'
t_Direccion = r'"direccion"'
t_Calle = r'"calle"'
t_Ciudad = r'"ciudad"'
t_Pais = r'"pais"'
t_Departamentos = r'"departamentos"'
t_Sub_Dptos = r'"subdepartamentos"'
t_Jefe = r'"jefe"'
t_Empleados = r'"empleados"'
t_Nombre = r'"nombre"'
t_Edad = r'"edad"'
t_Cargo = r'"cargo"'
t_Salario = r'"salario"'
t_Activo = r'"activo"'
t_Fec_Contra = r'"fecha_contratacion"'
t_Proyectos = r'"proyectos"'
t_Estado = r'"estado"'
t_Fec_Inicio = r'"fecha_inicio"'
t_Fec_Fin = r'"fecha_fin"'
#t_Asignacion = r":"
t_ApertLista = r'[[]'
t_CierreLista = r'[]]'
t_ApertBloque = r'[{]'
t_CierreBloque = r'[}][,]*'
t_Texto = r'[:][ ]*["][\w\s]+["]'
t_Numero = r'[\d]+'
t_Booleano = r'(true|false)'
t_Fecha = r'"(19[0-9][0-9]|20[0-9][0-9])-[1,0][0-9]-[0-3][0-9]"'



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


lexer = lex.lex()


data = '"empresas": [ {\n"nombre_empresa": "MC Donals", "fundacion": 2025, "direccion": { "calle": "Calle Falsa 123", "ciudad": "Springfield", "pais": "USA"},}'

#data = '"empresas": [{\n"nombre": "string",\n"version": "integer", "fecha_contratacion": "1999-12-31" }]'

#data = '"fecha_contratacion": "2001-12-31"'


#data = '"empresas": ['

lexer.input(data)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
