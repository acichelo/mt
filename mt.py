from automata.tm import TuringMachine

# Definir la descripción
descripcion = {
    'alfabeto': {'a', 'b', 'c'},
    'blank_symbol': '~',
    'estados': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    'estado_inicial': 'q0',
    'estados_aceptados': {'q3'},
    'estados_rechazados': {'q4'},
    'transiciones': {
        'q0': {
            'a': ('q1', 'x', 'R'),
            'b': ('q0', 'b', 'R'),
            'c': ('q2', 'x', 'R'),
            '~': ('q3', '~', 'L')
        },
        'q1': {
            'a': ('q1', 'a', 'R'),
            'b': ('q1', 'b', 'R'),
            'c': ('q1', 'c', 'R'),
            '~': ('q5', '~', 'L')
        },
        'q2': {
            'a': ('q2', 'a', 'R'),
            'b': ('q2', 'b', 'R'),
            'c': ('q2', 'c', 'R'),
            '~': ('q2', '~', 'R'),
            'x': ('q3', 'x', 'L')
        },
        'q5': {
            'a': ('q5', 'a', 'L'),
            'b': ('q5', 'b', 'L'),
            'c': ('q5', 'c', 'L'),
            'x': ('q5', 'x', 'L'),
            '~': ('q6', '~', 'R')
        }
    }
}

# Crear la instancia de la Máquina de Turing
tm = TuringMachine(descripcion)

# Función para determinar si una cadena cumple con el criterio de aceptación
def determinarSiAcepta(input_string):
    tm.initialize(input_string)
    tm.process()
    tape_contents = tm.get_tape().get_symbols()
    count_a = tape_contents.count('a')
    count_c = tape_contents.count('c')
    if count_c > count_a:
        return "aceptada"
    else:
        return "rechazada"

# Ejemplo de uso
input_string = "abcc"
result = determinarSiAcepta(input_string)
print(f"La cadena '{input_string}' es {result}.")