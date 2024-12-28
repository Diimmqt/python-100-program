import time
import sys

def jalanin_lirik():
    lirik = [
        ("When you go", 0.3),
        ("and would you even turn to stay", 0.12),
        ("I don't love you", 0.08),
        ("like I did yesterday", 0.10),
    ]

    delay = [0.3, 0.3, 0.4, 0.3]

    print("\n I Don't Love You - My Chemical Romance ")
    time.sleep(2)

    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')

    

jalanin_lirik()
