import random

def kelime_tahmin_oyunu():
    with open("easywords.txt", "r", encoding="utf-8") as dosya:
        kelimeler = dosya.read().splitlines()

    hedef_kelime = random.choice(kelimeler).lower()
    dogru_tahmin = False
    tahmin_edilen_harfler = []

    print("Welcome to the English Word Guessing Game!")

    while not dogru_tahmin:
        kelime_gosterimi = "".join([harf if harf in tahmin_edilen_harfler else '_' for harf in hedef_kelime])
        print(f"Tahmin edilen kelime: {kelime_gosterimi}")

        if '_' not in kelime_gosterimi:
            print("Tebrikler! Kelimenin tamamını doğru tahmin ettiniz.")
            break

        tahmin = input("Bir harf veya kelime tahmini yapın veya pes edin ('q' yazın): ").lower()

        if tahmin == 'q':
            print(f"Üzgünüm! Doğru kelimeyi bulamadınız. Kelime: {hedef_kelime}")
            break
        elif tahmin.isalpha() and len(tahmin) == 1:
            if tahmin in tahmin_edilen_harfler:
                print("Bu harfi zaten tahmin ettiniz. Başka bir harf deneyin.")
            elif tahmin in hedef_kelime:
                print("Harika! Doğru tahmin ettiniz.")
                tahmin_edilen_harfler.append(tahmin)
            else:
                print("Üzgünüm, yanlış tahmin. Başka bir harf deneyin.")
        elif tahmin.isalpha() and len(tahmin) > 1:
            if tahmin == hedef_kelime:
                print(f"Tebrikler! Kelimenin tamamını doğru tahmin ettiniz: {hedef_kelime}")
                break
            else:
                print("Üzgünüm, yanlış tahmin. Başka bir kelime deneyin.")
        else:
            print("Lütfen geçerli bir harf veya kelime girin.")

    print("Oyun bitti. Teşekkür ederiz!")

if __name__ == "__main__":
    kelime_tahmin_oyunu()
