import json

def save_state(state, filename="state.json"):
    """
    Зберігає стан у файл JSON.
    """
    with open(filename, "w") as f:
        json.dump(state, f)

def load_state(filename="state.json"):
    """
    Завантажує стан із файлу JSON.
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
