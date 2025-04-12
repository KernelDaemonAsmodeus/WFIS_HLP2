class SimpleChatBot:
    def __init__(self, questions : list[str]):
        self.question = questions

    def __iter__(self):
        return iter(self.question)

    def __next__(self):
        i=0
        if i < len(self.question):
            i += 1
        return self.question[i]


bot = SimpleChatBot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
for question in bot:
print(question)
input() # Użytkownik wpisuje odpowiedź