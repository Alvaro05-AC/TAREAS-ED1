# Importamos las clases (asegúrate que estén en el mismo directorio o en módulos separados)
from Modelo_Dinamico.Automovil_Dinamico import AutomovilDinamico
from Modelo_Estatico.Automovil_Estatico import AutomovilEstatico

def main():
    print("===== AUTOMÓVIL ESTÁTICO =====")
    # Crear un automóvil con lista estática
    auto_estatico = AutomovilEstatico("Toyota", "Corolla", 2020)

    # Mostrar sus datos con getters
    print("Marca:", auto_estatico.get_marca())
    print("Modelo:", auto_estatico.get_modelo())
    print("Año:", auto_estatico.get_año())

    # Modificar datos con setters
    auto_estatico.set_marca("Honda")
    auto_estatico.set_modelo("Civic")
    auto_estatico.set_año(2022)

    # Mostrar de nuevo después de modificar
    print("\nDespués de modificar (estático):")
    print("Marca:", auto_estatico.get_marca())
    print("Modelo:", auto_estatico.get_modelo())
    print("Año:", auto_estatico.get_año())

    print("\n===== AUTOMÓVIL DINÁMICO =====")
    # Crear un automóvil con diccionario dinámico
    auto_dinamico = AutomovilDinamico("Ford", "Focus", 2018)

    # Mostrar sus datos con getters
    print("Marca:", auto_dinamico.get_marca())
    print("Modelo:", auto_dinamico.get_modelo())
    print("Año:", auto_dinamico.get_año())

    # Modificar datos con setters
    auto_dinamico.set_marca("Chevrolet")
    auto_dinamico.set_modelo("Onix")
    auto_dinamico.set_año(2023)

    # Mostrar de nuevo después de modificar
    print("\nAumentando un automovil (dinámico):")
    print("Marca:", auto_dinamico.get_marca())
    print("Modelo:", auto_dinamico.get_modelo())
    print("Año:", auto_dinamico.get_año())

if __name__ == "__main__":
    main()
