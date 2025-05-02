import database
from database import GameData
from hangman_game import HangmanGame
from hangman_art import logo

class GameRunner:
    def __init__(self):
        self.data = GameData()
        self.new_words_list = []
        self.learned_sentences = 0
        self.learned_entries_by_type = {}

    def start(self):
        print("\n🇩🇪 Welcome to German Hangman!\n")
        print("Guess the correct German translation of the given English sentence or word.\n")
        print("🧠 Game Rules:")
        print("1. You have 6 lives.")
        print("2. You can guess one letter or one full word at a time.")
        print("3. Capitalization matters!")
        print("   - The first word in a sentence is always capitalized.")
        print("   - All nouns in German are capitalized.")
        print("4. If you guess a full word correctly, it will be fully revealed.")
        print("5. If you guess a letter, all instances of that letter will be shown.")
        print("6. If you guess a letter that is not in the sentence, you lose 1 life.")
        print("7. If you guess a full word that is incorrect, you lose 1 life.")
        print("8. Special characters like punctuation are ignored — no need to guess them.\n")
        print("🎯 The goal is to fully reveal the German sentence before running out of lives.")
        print("⭐ Tip: Think about verb position, article-noun matching, and common phrases.")
        print("💡 Good luck, and viel Erfolg! 🇩🇪\n")

        while True:
            print("Options: sentence, noun, verb, adj")
            category = input("\nYour choice (or type 'exit' to quit): ").strip()
            if category.lower() == 'exit':
                break

            sentence = self.data.get_random_entry(entry_type=category if category else None)
            if not sentence:
                if category:
                    print(f"✅ You've completed all '{category}' entries!")
                else:
                    print("✅ You've completed all entries in the database!")
                continue

            game = HangmanGame(sentence, self.new_words_list)
            won = game.run()
            if won:
                self.learned_sentences += 1
                self.learned_entries_by_type.setdefault(sentence.type, 0)
                self.learned_entries_by_type[sentence.type] += 1
                # TODO 1/3 энийг бас өөрчлөх хэрэгтэй, ppt-тэй өдөр
                print(f"📚 You've successfully learned {self.learned_sentences}/52 sentence(s) so far!")
                print("📊 Breakdown by type:")
                for etype, count in self.learned_entries_by_type.items():
                    print(f" - {etype}: {count}")
                print("---------------------------------------------")

        print("\n📝 New words you encountered during this session:")
        for german, english in self.new_words_list:
            print(f"- {german} → {english}")

if __name__ == '__main__':
    print(logo)
    GameRunner().start()

# TODO 1: special charactertisc dotor n baihar bolohgui bn
# TODO 2: bug ugiig n yj gedgere bish duusgachihwal bolno