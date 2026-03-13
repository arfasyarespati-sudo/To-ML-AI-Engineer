import time
import sys
from threading import Thread


def animate_text(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print() 

def sing_song():
    lyrics = [
        ("TANTEEEE...", 0.08),
        ("Sudah terbiasa terjadi tante...", 0.1),
        ("Teman datang ketika lagi butuh saja...", 0.1),
        ("Coba kalau lagi susah...", 0.15),
        ("Mereka semua menghilaaaaaang...", 0.12)
    ]
    
    delays = [0.5, 1, 1, 1, 0.5]

    for i in range(len(lyrics)):
        delay = delays[i]
        lyric, speed = lyrics[i]
        time.sleep(delay)
        animate_text(lyric, speed)

sing_song()