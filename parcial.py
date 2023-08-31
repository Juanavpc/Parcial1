# Función para calcular la distancia euclidiana entre dos puntos
def distancia(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Función principal para encontrar los dos puntos más cercanos
def pares_cercanos(puntos):
    n = len(puntos)
    
    # Si hay pocos puntos, se resuelve directamente
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                dist = distancia(puntos[i], puntos[j])
                if dist < min_dist:
                    min_dist = dist
                    pair = (puntos[i], puntos[j])
        return pair, min_dist
    
    # Ordenar los puntos por coordenada x
    puntos.sort(key=lambda x: x[0])
    mid = n // 2
    punto_medio = puntos[mid]
    
    izquierda = puntos[:mid]
    derecha = puntos[mid:]
    
    # Recursivamente encontrar los pares más cercanos en las mitades izquierda y derecha
    par_izq, dist_izq = pares_cercanos(izquierda)
    par_der, dist_der = pares_cercanos(derecha)
    
    # Elegir el par con la menor distancia de las mitades
    if dist_izq < dist_der:
        min_pair = par_izq
        min_dist = dist_izq
    else:
        min_pair = par_der
        min_dist = dist_der
    
    cercanos_en_banda = []
    for punto in puntos:
        if abs(punto[0] - punto_medio[0]) < min_dist:
            cercanos_en_banda.append(punto)
    
    cercanos_en_banda.sort(key=lambda x: x[1])
    
    # Buscar pares cercanos en la "banda" de puntos cerca del punto medio
    for i in range(len(cercanos_en_banda)):
        for j in range(i + 1, min(i + 8, len(cercanos_en_banda))):
            dist = distancia(cercanos_en_banda[i], cercanos_en_banda[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = (cercanos_en_banda[i], cercanos_en_banda[j])
    
    return min_pair, min_dist

# Decorador para manejar argumentos de la función
def args_decorator(func):
    def wrapper(*args):
        puntos = args[0]
        return func(puntos)
    return wrapper

# Decorador para manejar argumentos de palabra clave de la función
def kwargs_decorator(func):
    def wrapper(**kwargs):
        puntos = kwargs.get('puntos', [])
        return func(puntos)
    return wrapper

# Aplicar el decorador de argumentos a la función principal
@args_decorator
def encontrar_pares_cercanos_args(puntos):
    return pares_cercanos(puntos)

# Aplicar el decorador de argumentos de palabra clave a la función principal
@kwargs_decorator
def encontrar_pares_cercanos_kwargs(**kwargs):
    return pares_cercanos(kwargs['puntos'])

# Ejemplo de uso
puntos = [(1, 2), (4, 6), (7, 8), (9, 10), (2, 5)]
resultado, distancia_minima = encontrar_pares_cercanos_args(puntos)
print("Pares más cercanos:", resultado)
print("Distancia mínima:", distancia_minima)
