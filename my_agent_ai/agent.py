from memory import Memory

class Agent:
    def __init__(self):
        self.memory = Memory()

    def run(self, user_input):
        past = self.memory.load_memory()

        if past:
            last = past[-1]["user"]
            response = f"You said '{last}' before. Now you said '{user_input}'"
        else:
            response = f"First time you said: {user_input}"

        self.memory.add(user_input, response)
        return response
