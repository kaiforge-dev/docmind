# Importiert die Anthropic-Bibliothek für die Claude API
import anthropic

# Importiert die Funktion die unseren API-Key aus der .env Datei liest
from dotenv import load_dotenv

# Liest den API-Key aus der .env Datei
load_dotenv()

# Erstellt eine Verbindung zu Anthropic
client = anthropic.Anthropic()

# Eine Liste die den gesamten Chatverlauf speichert
# Claude hat kein Gedaechtnis - wir muessen bei jeder Nachricht den ganzen Verlauf mitschicken
conversation_history = []

# Begruessung im Terminal
print("=== DocMind Chat ===")
print("Chatte mit Claude. Tippe 'exit' zum Beenden.")
print()

# Endlosschleife - laeuft bis der User 'exit' tippt
while True:
    # Fragt den User nach einer Eingabe
    user_input = input("Du: ")

    # Wenn der User 'exit' tippt, wird die Schleife beendet
    if user_input.lower() == "exit":
        print("Tschuess!")
        break

    # Wenn der User einfach Enter drueckt ohne Text, ueberspring diese Runde
    if not user_input.strip():
        continue

    # Fuegt die User-Nachricht zum Chatverlauf hinzu
    conversation_history.append({"role": "user", "content": user_input})

    # Schickt den gesamten Chatverlauf an Claude und bekommt eine Antwort
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system="Du bist DocMind, ein hilfreicher Assistent der Fragen zu Dokumenten und AI-Themen beantwortet. Antworte auf Deutsch.",
        messages=conversation_history
    )

    # Holt den Text aus Claudes Antwort
    assistant_message = message.content[0].text

    # Fuegt Claudes Antwort zum Chatverlauf hinzu (damit Claude sich erinnert)
    conversation_history.append({"role": "assistant", "content": assistant_message})

    # Zeigt Claudes Antwort im Terminal
    print(f"\nClaude: {assistant_message}\n")
