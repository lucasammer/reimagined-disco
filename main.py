import handydandy
import random
import time

while True:
    colors = [handydandy.colors.HEADER, handydandy.colors.OKBLUE ,handydandy.colors.OKCYAN, handydandy.colors.OKGREEN, handydandy.colors.WARNING, handydandy.colors.FAIL, handydandy.colors.BOLD, handydandy.colors.UNDERLINE]
    color = random.choice(colors)
    words = ['progressive', 'door', 'seminar', 'mold', 'disco', 'disco', 'contrast', 'foreigner', 'disco', 'plain', 'magnetic', 'cathedral', 'unity', 'disco', 'disco']
    word = random.choice(words)
    time.sleep(.1)
    handydandy.colors.replonly.printc(word, color)