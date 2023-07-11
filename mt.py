from automata.fa.dfa import DFA
from automata.base.exceptions import RejectionException

## Definir el alfabeto
alfabeto = {'a', 'b', 'c'}

# Definir los estados
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qf'}

dfa = DFA(
    estados=estados,
    input_symbols=alfabeto,
    transitions={},
    initial_state='q0',
    final_states={'qf'}
)

# Definir las transiciones
dfa.transitions = {
    'q0': {
        'a':('q1', 'x', 'R'),
        'b':('q4','Y', 'R'),
        'Z':('q6','Z','R')
          },


    'q1': {
        'a': ('q1', 'a', 'R'),
        'b':( 'q2', 'b' 'R')      
           },
    'q2': {
        'b': ('q2', 'b', 'R'), 
        'Z': ('q2','Z', 'R'), 
        'c': ('q3', 'Z','L')
           },

    'q3': {
        'b': ('q3','b','L'), 
        'a': ('q3', 'a','L'),
        'Z': ('q3','Z', 'L'), 
        'x': ('q0','x','R')
           },

    'q4': {
        'b': ('q4','b','R'),
        'Z': ('q4','Z','R'),
        'c': ('q4','Z','L')         
           },
    'q5': {
        'b':( 'q5','b','L'),
        'Z':('q5','Z','L'),
        'Y':('q0','Y','R')
           },

    'q6': {
        'Z':( 'q6', 'Z', 'R'),
        'B': ('qf', 'B','L')
        }
}

try:
    # Probar una cadena
    input_string = 'aabbbccc'
    if dfa.accepts_input(input_string):
        print(f"Cadena '{input_string}' aceptada por la máquina de Turing.")
    else:
        print(f"Cadena '{input_string}' no aceptada por la máquina de Turing.")
except RejectionException:
    print(f"Cadena '{input_string}' no aceptada por la máquina de Turing.")