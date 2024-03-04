def calculate(nLados:int, dice1: list, dice2: list):
    contador1 = 0
    contador2 = 0

    for number1 in dice1:
        for number2 in dice2:
            if number1 > number2:
                contador1 += 1
            elif number1 < number2:
                contador2 += 1

            if contador1 // 2 > nLados:
                return "first"
            elif contador2 // 2 > nLados:
                return "second"
    
    if number1 > number2:
        return "first"
    elif number2 > number1:
        return "second"
    else:
        return "tie"

# Para mejorar, el contador2 se puede inferir con solo contador 1 y nLados
def calculateSort(nLados:int, dice1: list, dice2: list):
    dice1Sorted = sorted(dice1)
    dice2Sorted = sorted(dice2)

    mitadPuntosPosibles = (nLados ** 2) // 2

    contador1 = 0
    contador2 = 0


    for i in range(len(dice2Sorted)):
        numero2 = dice2Sorted[i]
        numero1 = dice1Sorted[i]

        puntosDisponibles = nLados - i

        if numero2 > numero1:
            contador2 += puntosDisponibles
        elif numero2 < numero1:
            contador1 += puntosDisponibles
        
        if contador2 == mitadPuntosPosibles:
            return "tie"
        elif contador2 < mitadPuntosPosibles:
            return "second"
        elif contador2 > mitadPuntosPosibles:
            return "first"

