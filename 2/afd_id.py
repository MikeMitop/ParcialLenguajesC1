def afd_id(cadena):
    estado = 0
    if not cadena:
        return False
        
    for char in cadena:
        if estado == 0:
            if char.isalpha(): 
                estado = 1
            else: 
                estado = 2
        elif estado == 1:
            if char.isalnum(): 
                estado = 1
            else: 
                estado = 2
        elif estado == 2:
            break
            
    return estado == 1

def access_file(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(f"Resultados de las pruebas de ID ({nombre_archivo})")
            
            for linea in archivo:
                identificador = linea.strip() 
                
                if not identificador:
                    continue 
                
                es_valido = afd_id(identificador)
                
                resultado = "ACEPTA" if es_valido else "NO ACEPTA"
                print(f"[{resultado}] -> '{identificador}'")
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")

access_file('pruebas_id.txt')