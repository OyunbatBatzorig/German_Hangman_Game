import random
import string

class Sentence:
    def __init__(self, german, english, entry_type):
        self.german = german
        self.english = english
        self.type = entry_type

class GameData:
    def __init__(self):
        self.entries = []
        self.used_entries_by_type = {}
        self.load_data()

    # TODO 2/3 энийг датаруу оруулах
    """
          Sentence("Wir müssen den Preis noch verhandeln.", "We still have to negotiate the price.", "sentence"),
          Sentence("Mein Arbeitgeber bietet flexible Arbeitszeiten an.", "My employer offers flexible working hours.",
                   "sentence"),
          Sentence("Arbeitgeber", "employer", "noun"),
          Sentence("verhandeln", "to negotiate", "verb"),
          Sentence("verantwortlich", "responsible", "adj"),
          Sentence("Sie ist verantwortlich für das Marketing Team.", "She is responsible for the marketing team.",
                   "sentence"),
      """,

    # TODO 3/3 энийг датагаас гаргах
    def load_data(self):
        self.entries = [


            Sentence("Hallo, zusammen.", "Hello, everybody. (1)", "sentence"),
            Sentence("Ich heiße Oyunbat und ich studiere Advanced Industrial Engineering an der TH Rosenheim.",
                     "My name is Oyunbat and I study Advanced Industrial Engineering at TH Rosenheim. (2)", "sentence"),
            Sentence("Ich freue mich, dass ich heute das Thema Arbeit und Beruf vorstellen darf.",
                     "I’m happy to give a short presentation today about work and career. (3)", "sentence"),
            Sentence("ich hoffe, es gefällt Ihnen.", "i hope you enjoy it. (4)","sentence"),
            Sentence("Hier ist der Inhalt meiner Präsentation.", "Here is the structure of my presentation. (5)",
                     "sentence"),
            Sentence("Zuerst spreche ich über mein Berufsfeld und meine Erfahrungen.",
                     "First, I will talk about my professional field and experience. (6)", "sentence"),
            Sentence("Dann erzähle ich von meinem Traumberuf und warum ich ihn gewählt habe.",
                     "Then, I’ll speak about my dream job and why I chose it. (7)", "sentence"),
            Sentence("Danach stelle ich drei neue Wörter zum Thema vor.",
                     "After that, I will introduce 3 new words related to the topic. (8)", "sentence"),
            Sentence("Zum Abschluss spielen wir gemeinsam ein Spiel.", "At the end, we play a game together. (9)","sentence"),
            Sentence("Beginnen wir mit meinem Berufsfeld.","Let’s start with my professional field. (10)","sentence"),
            Sentence("Ich bin industrial engineer.", "I’m an industrial engineer. (11)", "sentence"),
            Sentence("Jetzt studiere ich an der TH Rosenheim und habe im Bachelor auch Industrial engineering in Mongolei studiert.",
                     "I am now studying at the TH Rosenheim and also studied industrial engineering in Mongolia for my bachelor's degree. (12)", "sentence"),
            Sentence("Das ist ein sehr flexibles Studium – ich kann in vielen Bereichen arbeiten.",
                     "This is a very flexible degree – I can work in many industries. (13)","sentence"),
            Sentence("Ich interessiere mich besonders für IT und Technologie.",
                     "I’m especially interested in IT and technology. (14)", "sentence"),
            Sentence("Ich möchte diese Bereiche kombinieren, weil die Digitalisierung wichtig ist.",
                     "I want to combine these fields because digitalization is important. (15)", "sentence"),
            Sentence("Man kann damit auch international und flexibel arbeiten.",
                     "It also allows you to work internationally and flexibly. (16)","sentence"),
            Sentence("Auf der nächsten Folie sehen wir Bilder von meinen bisherigen Erfahrungen.",
                     "On the next slide, you can see some pictures from my past experiences. (17)","sentence"),
            Sentence("Ich habe als Projektmanager und in der Produktentwicklung gearbeitet.",
                     "I worked as a project manager and in product development. (18)", "sentence"),
            Sentence("Ich habe viel mit Menschen gearbeitet, geplant, organisiert, mit anderen Partnern verhandelt und digitale Medien erstellt.",
                     "I worked a lot with people, planned, organized, negotiated with other partners and created digital media. (19)", "sentence"),
            Sentence("Hier sehen Sie einige der Schlüsselwörter, die meine Erfahrung beschreiben.","Here you can see some of the key words that describe my experience. (20)", "sentence"),
            Sentence("mit Menschen arbeiten","working with people (20)","sentence"),
            Sentence("organisieren", "to organize (21)", "verb"),
            Sentence("planen", "to plan (22)", "verb"),
            Sentence("verhandeln", "to negotiate (23)", "verb"),
            Sentence("digitale Medieninhalte erstellen", "create digital media content (24)", "sentence"),
            Sentence("Hier können Sie einige meiner Programmiererfahrungen sehen.",
                     "Here you can see some of my programming projects. (25)","sentence"),
            Sentence("Ich habe Spiele und Webseiten gemacht.", "I have created games and websites. (26)", "sentence"),
            Sentence("Aber in letzter Zeit konzentriere ich mich beim Programmieren mehr darauf, Deutsch zu lernen.",
                     "But recently, I’ve focused more on learning German. (27)","sentence"),
            Sentence("Am Ende der Präsentation zeige ich Ihnen das kleine Spiel, das ich erstellt habe.",
                     "At the end of the presentation, I'll show you the small game I created. (28)","sentence"),
            Sentence("Jetzt geht es weiter mit meinen Plänen.","Now let’s talk about the plan. (29)","sentence"),
            Sentence("Ich möchte ein Praktikum in einem internationalen Unternehmen machen.",
                     "I want to do an internship in an international company. (30)", "sentence"),
            Sentence("Mein Traumberuf ist es, als digitaler Nomade zu arbeiten.",
                     "My dream job is to work as a digital nomad. (31)", "sentence"),
            Sentence("Weil ich mit meiner Familie verschiedene Länder erkunden und flexibel arbeiten möchte.",
                     "Because I want to see different countries with my family and work flexibly. (32)", "sentence"),
            Sentence("Hier sind drei neue Wörter zum Thema Arbeit und Beruf.",
                     "Here are three new words related to work and career. (33)","sentence"),
            Sentence("Das erste Wort ist - Arbeitgeber, es bedeutet employer auf Englisch.",
                     "The first word is - employer, it means employer in English. (34)", "sentence"),
            Sentence("Mein Arbeitgeber bietet flexible Arbeitszeiten an.","My employer offers flexible working hours. (35)","sentence"),
            Sentence("Das nächste Wort ist - verhandeln, to negotiate auf Englisch.",
                     "The next word is - verhandeln, to negotiate in English. (36)", "sentence"),
            Sentence("Wir müssen den Preis noch verhandeln.", "We still have to negotiate the price. (37)","sentence"),
            Sentence("Das letzte Wort ist - verantwortlich, es bedeutet responsible auf Englisch.",
                     "The last word is - verantwortlich, it means responsible in English. (38)","sentence"),
            Sentence("Sie ist verantwortlich für das Marketing Team.","She is responsible for the marketing team. (39)","sentence"),
            Sentence("Jetzt möchte ich mit euch ein Spiel spielen.", "Now I would like to play a game with you. (40)",
                     "sentence"),
            Sentence("Ich bin der Spielleiter, und ihr seid die Spieler.", "I am the host, and you are the players. (41)",
                     "sentence"),
            Sentence("Es ist ein Hangman Spiel.", "It is a hangman game. (42)", "sentence"),
            Sentence("Das ist die Regel.","This is the rule. (43)","sentence"),
            Sentence("Lassen Sie es mich für Sie vorlesen.","Let me read it for you. (44)","sentence"),
            Sentence("Ihr könnt einen Buchstaben oder ein Wort sagen.", "You can say one letter or one word. (45)",
                     "sentence"),
            Sentence("Kannst du mir einen Buchstaben oder ein Wort sagen?","Can you tell me one letter or one word? (46)","sentence"),
            Sentence("Ja, wunderbar","Yes, wonderful (47)","sentence"),
            Sentence("Es tut mir leid, Sie haben ein Leben verloren.","Sorry, you lost a life. (48)","sentence"),
            Sentence("Herzlichen Glückwunsch an euch alle.", "Congratulations to you all. (49)","sentence"),
            Sentence("Vielen Dank für eure Aufmerksamkeit!", "Thank you very much for your attention! (50)", "sentence"),
            Sentence("Ich beende meine kurze Präsentation mit einer Folie hierzu.",
                     "I will end my short presentation with a slide about this. (51)", "sentence"),
            Sentence("Habt ihr noch Fragen?", "Do you have any questions? (52)", "sentence"),
        ]
        self.used_entries_by_type = {}
        for entry in self.entries:
            if entry.type not in self.used_entries_by_type:
                self.used_entries_by_type[entry.type] = set()

    def get_random_entry(self, entry_type=None):
        if entry_type:
            available = [e for e in self.entries if e.type == entry_type and e.german not in self.used_entries_by_type[entry_type]]
            if not available:
                return None
            entry = random.choice(available)
            self.used_entries_by_type[entry_type].add(entry.german)
            return entry
        else:
            all_types = list(set(e.type for e in self.entries))
            possible = [e for e in self.entries if e.german not in self.used_entries_by_type[e.type]]
            if not possible:
                return None
            entry = random.choice(possible)
            self.used_entries_by_type[entry.type].add(entry.german)
            return entry