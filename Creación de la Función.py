# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento basado en un porcentaje.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (10% por defecto).
    :return: El monto del descuento.
    """
    # Cálculo del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo con el monto total (descuento predeterminado del 10%)
    monto_total1 = 1000  # ejemplo de compra
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1

    # Segunda llamada: con el monto total y un porcentaje de descuento personalizado
    monto_total2 = 1500  # ejemplo de compra
    porcentaje_descuento2 = 20  # descuento personalizado
    descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    monto_final2 = monto_total2 - descuento2

    # Mostrar los resultados
    print(f"Compra 1:")
    print(f"Monto total: ${monto_total1}")
    print(f"Descuento aplicado: ${descuento1}")
    print(f"Monto final a pagar: ${monto_final1}\n")

    print(f"Compra 2:")
    print(f"Monto total: ${monto_total2}")
    print(f"Descuento aplicado: ${descuento2}")
    print(f"Monto final a pagar: ${monto_final2}")
