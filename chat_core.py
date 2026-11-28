import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

MEMORY_FILE = "memory.json"
MODEL = "openai/gpt-oss-20b"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)


def extract_facts(user_message, reply):
    prompt = (
        "From the exchange below, extract only durable facts worth remembering "
        "long-term (names, preferences, project details). "
        "Reply with a JSON object only, no other text. "
        "If there is nothing worth remembering, reply with {}.\n\n"
        f"User: {user_message}\nAssistant: {reply}"
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.choices[0].message.content.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def chat(message):
    memory = load_memory()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": f"memory (in JSON): {memory} user prompt: {message}"}],
    )
    reply = response.choices[0].message.content
    memory.update(extract_facts(message, reply))
    save_memory(memory)
    return reply