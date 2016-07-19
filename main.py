import pygame_output

DISPLAY = pygame_output.PygameOutput()
while True:
    DISPLAY.timer.tick(3)
    DISPLAY.do_next_step()