from collections import defaultdict

# Har user ki chat memory
user_memory = defaultdict(list)

MAX_HISTORY = 20


def add_message(user_id: int, role: str, content: str):
    user_memory[user_id].append({
        "role": role,
        "content": content
    })

    if len(user_memory[user_id]) > MAX_HISTORY:
        user_memory[user_id] = user_memory[user_id][-MAX_HISTORY:]


def get_history(user_id: int):
    return user_memory[user_id]


def clear_history(user_id: int):
    user_memory[user_id] = []