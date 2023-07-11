from automata.tm import NondeterministicTuringMachine
from automata.base.exceptions import RejectionException

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qf'}

tm = NondeterministicTuringMachine(
    estados=estados,
    input_symbols={'a', 'b', 'c', 'Z', 'x', 'Y', 'B'},
    tape_symbols={'a', 'b', 'c', 'Z', 'x', 'Y', 'B', '#'},
    blank_symbol='#',
    initial_state='q0',
    final_states={'qf'}
)

tm.transitions = {
    'q0': {
        'a': {('q1', 'x', 'R')},
        'b': {('q4', 'Y', 'R')},
        'Z': {('q6', 'Z', 'R')}
    },
    'q1': {
        'a': {('q1', 'a', 'R')},
        'b': {('q2', 'b', 'R')}
    },
    'q2': {
        'b': {('q2', 'b', 'R')},
        'Z': {('q2', 'Z', 'R')},
        'c': {('q3', 'Z', 'L')}
    },
    'q3': {
        'b': {('q3', 'b', 'L')},
        'a': {('q3', 'a', 'L')},
        'Z': {('q3', 'Z', 'L')},
        'x': {('q0', 'x', 'R')}
    },
    'q4': {
        'b': {('q4', 'b', 'R')},
        'Z': {('q4', 'Z', 'R')},
        'c': {('q4', 'Z', 'L')}
    },
    'q5': {
        'b': {('q5', 'b', 'L')},
        'Z': {('q5', 'Z', 'L')},
        'Y': {('q0', 'Y', 'R')}
    },
    'q6': {
        'Z': {('q6', 'Z', 'R')},
        'B': {('qf', 'B', 'L')}
    }
}

try:
    # Probar las cadenas
    strings = ['abcc', 'aabccc', 'aaabcccc', 'aaabbccccc']
    for string in strings:
        if tm.accepts_input(string):
            print(f"Cadena '{string}' aceptada por la máquina de Turing no determinística.")
        else:
            print(f"Cadena '{string}' no aceptada por la máquina de Turing no determinística.")
except RejectionException:
    print(f"Cadena '{string}' no aceptada por la máquina de Turing no determinística.")