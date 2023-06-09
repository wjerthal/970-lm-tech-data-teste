def soma(a, b):
    print('soma')
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b     
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")

def subtracao(a, b):
    print('subtracao')
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")

def multiplicacao(a, b):
    print('multiplicacao')
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")

def divisao(a, b):
    print('divisao')    
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and (b != 0):
        return a / b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos e 'b' diferente de zero, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")
