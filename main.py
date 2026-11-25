import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)


memory = load_memory()

while True:
    prompt = input(": ")
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"memory (in JSON): {memory} user prompt: {prompt}"}],
    )
    reply = response.choices[0].message.content
    print(reply)

    memory["last_prompt"] = prompt
    memory["last_reply"] = reply
    save_memory(memory)