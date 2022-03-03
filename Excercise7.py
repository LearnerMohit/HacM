#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
 # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 10
    eyessecs = 20
    exsecs = 30

while True:
    if time() - init_water > watersecs:
        print("Water Drinking Time. Enter'drank' to stop the  reminder")
        musiconloop('water.mp3','drank')
        init_water = time()
        log_now("Drank water at")

    if time()-init_eyes > eyessecs:
        print("Eyes Exercise Time. Enter 'doneeyes' to stop the reminder")
        musiconloop('eyes.mp3','doneeyes')
        init_eyes = time()
        log_now("Eyes exercise at")

    if time()-init_exercise > exsecs:
        print("physical Exercise Time. Enter 'doneex' to stop the reminder")
        musiconloop('physical.mp3', 'doneex')
        init_exercise = time()
        log_now("Physical exercise at ")

