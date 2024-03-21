import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 5
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("""Ingrese el nivel de dificultad al que quieres jugar
      1 = Facil
      2 = Medio
      3 = Dificil""")
nivel = int(input("Nivel = "))
while 3 < nivel or nivel < 1:
   nivel = int(input("Ingrese un valor valido "))
match nivel:
    case 1:
       letters = []
       guessed_letters = ["a","e","i","o","u"]
       for letter in secret_word:
          if letter in guessed_letters:
            letters.append(letter)
          else:
              letters.append("_")
       word_displayed = "".join(letters)
    case 2:
        inicio = 0
        fin = len(secret_word)-1
        letters=[]
        letters.append(secret_word[inicio])
        for x in range(inicio+1,fin):
            letters.append("_")
        letters.append(secret_word[fin])
        word_displayed = "".join(letters)
        guessed_letters.append(secret_word[inicio])
        guessed_letters.append(secret_word[fin])
    case 3:
        word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
fallos = 0
print("Intentos = " , (max_attempts - fallos))
while fallos < max_attempts:
 # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
# Solucion del bug con un dato vacio, no se gasta intento si se ingresa
    while letter == "":
        print("El valor ingresado no es valido")
        letter= input("Ingrese una letra ")
# Verificar si la letra ya ha sido adivinada, se gasta intento
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
 # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
 # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fallos += 1
        print("Intentos = " , (max_attempts - fallos))
 # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
     print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
     break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")