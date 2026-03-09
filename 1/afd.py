def afd_ajedrez(cadena):
    estado = 0
    i = 0
    while i < len(cadena):
        char = cadena[i]
        if estado == 0:
            if char.isalpha(): estado = 1
            else: estado = 6 
        elif estado == 1:
            if char.isalpha(): estado = 1
            elif char == '-': estado = 2
            elif char == ' ': estado = 3
            else: estado = 6
        elif estado == 2:
            if char == '>': estado = 4
            else: estado = 6
        elif estado == 3:
            if char == 'X':
                if i + 1 < len(cadena) and cadena[i+1] == ' ':
                    estado = 4
                    i += 1 #
                else: estado = 6
            else: estado = 6
        elif estado == 4:
            if char.isalnum(): estado = 5
            else: estado = 6
        elif estado == 5:
            if char.isalnum(): estado = 5
            else: estado = 6
        elif estado == 6:
            break
        i += 1
        
    return estado == 5

def test_file(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(f"Resultados de las pruebas ({nombre_archivo})")
            
            for linea in archivo:
                movimiento = linea.strip() 
                
                if not movimiento:
                    continue 
                
                es_valido = afd_ajedrez(movimiento)
                
                resultado = "ACEPTADO" if es_valido else "RECHAZADO"
                print(f"[{resultado}] -> '{movimiento}'")
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Asegúrate de que esté en la misma carpeta.")

test_file('pruebas.txt')