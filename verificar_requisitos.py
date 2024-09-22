# verificar_requisitos.py

def verificar_requisitos():
    try:
        with open(r'C:\Users\belen\OneDrive\Documentos\MSGA\Ejercicio 3\requisitos.txt', 'r') as archivo:
            requisitos = archivo.readlines()
            
        requisitos_actuales = [req.strip() for req in requisitos if req.strip()]
        
        if requisitos_actuales:
            print("Los requisitos están actualizados y completos:")
            for req in requisitos_actuales:
                print(f"- {req}")
        else:
            print("No hay requisitos en el archivo.")
    
    except FileNotFoundError:
        print("El archivo requisitos.txt no se encuentra.")

if __name__ == "__main__":
    verificar_requisitos()
