def calcular_media(numeros):
    # O Python possui a função sum() e len() que tornam o cálculo direto
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    numeros = [10, 20, 30, 40, 50]
    media = calcular_media(numeros)
    print(f"A média é: {media:.2f}")

if __name__ == "__main__":
    main()
