class NumeroNaturalError(Exception):
    def __init__(self, mensaje="El ingreso debe ser un número natural."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def es_numero_natural(valor):
    if not isinstance(valor, int) or valor < 1:
        raise NumeroNaturalError()

def calcular_divisores(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    return divisores

def obtener_numero_natural():
    while True:
        try:
            entrada = input("Ingrese un número natural: ")
            numero = int(entrada)
            es_numero_natural(numero)
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        except NumeroNaturalError as e:
            print(e)

if __name__ == '__main__':
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")
