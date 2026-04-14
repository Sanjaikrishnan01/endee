import json

class Memory:
    def __init__(self, file="data/memory.json"):
        self.file = file

    def load_memory(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []

    def save_memory(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f)

    def add(self, user, response):
        memory = self.load_memory()
        memory.append({"user": user, "response": response})
        self.save_memory(memory)
