from langdetect import detect


text_1 = ("This is a sample text that is intentionally made very long to demonstrate "
          "how to properly format code according to PEP8 guidelines. The line should "
          "not exceed 79 characters in length.")

text_2 = "Цей текст містить українські літери. Він також досить довгий, щоб написати."

text_3 = ("Kupujesz pierwsze mieszkanie? A może jesteś doświadczonym inwestorem lub "
          "właścicielem firmy? W każdym przypadku nasz cel to znaleźć dla Ciebie najlepsze "
          "nieruchomości z rynku pierwotnego.")

print(detect(text_1))
print(detect(text_2))
print(detect(text_3))
