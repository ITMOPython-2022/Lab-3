def sqrEquation(A, B, C):
    D = B ** 2 - 4 * A * C
    if D > 0:
        x1 = round((D ** 0.5 - B) / (A * 2), 2)
        x2 = round((B * -1 - D ** 0.5) / (A * 2), 2)
        text = f'{x1}, {x2}'
    elif D == 0:
        x1 = round((B * -1) / (A * 2), 2)
        text = f'{x1}'
    else:
        text = 'No roots.'

    return text