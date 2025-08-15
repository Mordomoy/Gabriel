import random

# Lista de frases icônicas por nível de gayzura
frases = [
    (0, "Hétero até no modo avião. Nem um glitter passou perto."),
    (10, "Só um pezinho na pista... mas ainda nega até o último segundo."),
    (20, "Curte Lady Gaga em segredo. Tá começando a desconfiar."),
    (30, "Já deu uma olhadinha no boy da academia. Só curiosidade, né?"),
    (40, "Sabe a coreografia de 'Single Ladies'. Coincidência?"),
    (50, "Meio termo: metade arco-íris, metade negação."),
    (60, "Já foi em uma festa LGBTQIA+ e amou. Tá quase lá!"),
    (70, "Usa cropped e glitter sem medo. A vibe tá fluindo!"),
    (80, "Canta Pabllo Vittar no chuveiro e tem playlist de divas pop."),
    (90, "Já tá dando close certo. Só falta assumir no grupo da família."),
    (100, "Ícone LGBTQIA+! Brilha mais que a bola de espelhos da boate.")
]

# Solicita o nome da pessoa
nome = input("Digite o nome da pessoa para medir a gayzura: ")

# Gera porcentagem aleatória
porcentagem = random.randint(0, 100)

# Seleciona frase mais próxima
frase_escolhida = max(frases, key=lambda x: x[0] if x[0] <= porcentagem else -1)[1]

# Exibe resultado
print("\n✨ Resultado Gayzura ✨")
print(f"👤 Nome: {nome}")
print(f"🌈 Nível de gayzuraa: {porcentagem}%")
print(f"💬 {frase_escolhida}")
