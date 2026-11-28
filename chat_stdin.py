import sys
from chat_core import chat

message = sys.stdin.readline().strip()
print(chat(message))