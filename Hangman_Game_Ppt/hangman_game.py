import string
from display_helper import DisplayHelper
from hangman_art import stages

SPECIAL_CHARS = set("!?.,:;()[]{}-<>\"'")

class HangmanGame:
    def __init__(self, sentence_obj, new_words_list):
        self.sentence_obj = sentence_obj
        self.german = sentence_obj.german
        self.english = sentence_obj.english
        self.lives = 6
        self.guessed_letters = set()
        self.guessed_words = set()
        self.german_words = self.extract_clean_words()
        self.stages = stages
        self.new_words_list = new_words_list

    def display_stages(self):
        print(self.stages[self.lives])

    def extract_clean_words(self):
        words = []
        for word in self.german.split():
            clean = ''.join(ch for ch in word if ch not in SPECIAL_CHARS)
            words.append(clean)
        return words

    def process_guess(self, guess):
        guess = guess.strip()
        if not guess:
            print("⚠️ Please enter something.")
            return

        if len(guess) == 1:  # letter guess (case-sensitive now)
            if guess in self.guessed_letters:
                print("⚠️ You already guessed that letter.")
            else:
                self.guessed_letters.add(guess)
                if guess in self.german:
                    print("✅ Correct letter!")
                else:
                    self.lives -= 1
                    self.display_stages()
                    print(f"❌ Wrong letter! Lives left: {self.lives}")

        else:  # word or words (case-sensitive now)
            words_guessed_now = guess.split()
            incorrect = False
            for word in words_guessed_now:
                if word in self.german_words:
                    if word not in self.guessed_words:
                        self.guessed_words.add(word)
                        print(f"✅ Correct word: {word}")
                    else:
                        print(f"⚠️ You already guessed the word: {word}")
                else:
                    incorrect = True
            if incorrect:
                self.lives -= 1
                self.display_stages()
                print(f"❌ One or more incorrect words. Lives left: {self.lives}")

        ## print(DisplayHelper.display_hidden(self.german, self.guessed_letters, self.guessed_words))
        print("English sentence:", self.english)

    def is_won(self):
        for word in self.german.split():
            clean = ''.join(ch for ch in word if ch not in SPECIAL_CHARS)
            if clean in self.guessed_words:
                continue
            for ch in clean:
                if ch not in self.guessed_letters:
                    return False
        return True

    def run(self):
        print("English sentence:", self.english)
        print("Guess the German: (Case sensitive!)")

        while self.lives > 0:
            print("\n" + DisplayHelper.display_hidden(self.german, self.guessed_letters, self.guessed_words))

            if self.is_won():
                print("🎉 Glückwunsch! You guessed the sentence.")
                self.new_words_list.append((self.german, self.english))
                return True

            guess = input("Your guess (letter or word/words): ")
            self.process_guess(guess)

        print(f"\n💀 Game Over! The sentence was: '{self.german}'")
        self.new_words_list.append((self.german, self.english))
        return False
