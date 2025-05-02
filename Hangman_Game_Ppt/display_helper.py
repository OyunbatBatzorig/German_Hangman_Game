SPECIAL_CHARS = set("!?.,:;()[]{}-<>\"'")

class DisplayHelper:
    @staticmethod
    def display_hidden(original_sentence, guessed_letters, guessed_words):
        words = original_sentence.split()
        display = []

        for word in words:
            clean = ''.join(ch for ch in word if ch not in SPECIAL_CHARS)
            if clean in guessed_words:
                display.append(word)
            else:
                revealed = ""
                for ch in word:
                    if ch in guessed_letters or ch in SPECIAL_CHARS or ch == " ":
                        revealed += ch
                    else:
                        revealed += "_"
                display.append(revealed)
        return " ".join(display)
