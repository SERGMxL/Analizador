import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    'CADENA',
    'RETURN',
    'VOID',
    'INT',
    'ENDL',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'FLotante',  # Nuevo token para flotantes
    'CURRENCY',  # Nuevo token para currency

    'ASIGNAR',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

    'MINUSMINUS',
    'PLUSPLUS',

    #Condiones
    'SI',
    'SINO',
    #Ciclos
    'MIENTRAS',
    'PARA',
    #logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    # Symbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    
    # Otros
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
)

# Expresiones regulares para tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='

t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'
t_NUMERAL = r'\#'
t_PLUSPLUS = r'\+\+'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUAL = r'=='
t_MAYORDER = r'<<'
t_MAYORIZQ = r'>>'
t_DISTINTO = r'!='

# Expresión regular para reconocer valores de currency
def t_CURRENCY(t):
    r'\$\d+(\.\d+)?'
    return t

# Expresión regular para reconocer flotantes, incluyendo '0.00' y '.00'
def t_FLotante(t):
    r'\d+\.\d+|\.\d+'
    t.value = float(t.value)
    return t


# Expresión regular para reconocer enteros
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Expresión regular para reconocer identificadores
def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

# Expresión regular para reconocer cadenas
def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Función para manejar errores
def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                                     str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Función de prueba
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type),
                                                                          str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

# Instanciamos el analizador léxico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)
