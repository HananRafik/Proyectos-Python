# Juego de Trivial
import random

preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuesta": "Paris", 
        "categoria": "Geografía"
    },
    {
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "respuesta": "1939",
        "categoria": "Historia" 
    },
    {
        "pregunta": "¿Cuál es el elemento químico más abundante en el universo?",
        "respuesta": "Hidrogeno",
        "categoria": "Ciencia"
    },
    {
        "pregunta": "¿Quién pintó La Mona Lisa?", 
        "respuesta": "Leonardo da Vinci",
        "categoria": "Arte"
    }
]

def jugar_trivial():
    puntos = 0
    preguntas_realizadas = []
    
    print("\n¡Bienvenido al Juego de Trivial!")
    print("Responde correctamente para ganar puntos\n")
    
    while len(preguntas_realizadas) < len(preguntas):
        pregunta = random.choice([p for p in preguntas if p not in preguntas_realizadas])
        preguntas_realizadas.append(pregunta)
        
        print(f"\nCategoría: {pregunta['categoria']}")
        print(f"Pregunta: {pregunta['pregunta']}")
        
        respuesta = input("Tu respuesta: ").strip().lower()
        
        if respuesta == pregunta['respuesta'].lower():
            print("¡Correcto! +1 punto")
            puntos += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}")
    
    print(f"\nJuego terminado! Puntuación final: {puntos}/{len(preguntas)}")

if __name__ == "__main__":
    jugar_trivial()
