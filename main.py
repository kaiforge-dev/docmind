# Importiert die Anthropic-Bibliothek, damit wir mit Claude sprechen können
import anthropic

# Importiert die Funktion die unseren API-Key aus der .env Datei liest
from dotenv import load_dotenv

# Liest den API-Key aus der .env Datei und macht ihn verfügbar
load_dotenv()

# Erstellt eine Verbindung zu Anthropic (nutzt automatisch den Key aus .env)
client = anthropic.Anthropic()

# Schickt eine Nachricht an Claude und speichert die Antwort
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Was ist RAG und warum ist es wichtig für AI Engineers? Erkläre es in 3 Sätzen."}
    ]
)

# Gibt Claudes Antwort im Terminal aus
print(message.content[0].text)


