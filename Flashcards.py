class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return  self.word + " ( " + self.meaning + " ) "

flash = []
print("Welcome to Flashcards!")

while True:
    word = input("Enter the name you want to add to flashcard : ")
    meaning = input("Enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 , if you want to add another flashcard otherwise enter 1 :"))

    if option == 1:
        break
    else:
        continue

print("\nYour flashcards : ")
for f in flash:
    print(">", f)