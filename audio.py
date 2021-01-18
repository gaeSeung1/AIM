import pygame
import time

file = "/home/pi/Desktop/AIM/yonsei.wav"

def music(mfile):
    try:
        pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)
        pygame.mixer.music.load(mfile)
        pygame.mixer.music.play()
        print("Play Music")
        while pygame.mixer_music.get_busy():
            time.sleep(0.1)

    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nStop Music")

def main():
    music(file)


main()