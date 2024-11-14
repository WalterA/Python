def verifica_condizioni(X: bool, Y: bool, Z: bool) -> str:
    if X and Y or Z:
        return "Azione permessa"
    else:
        return "Azione negata"
    