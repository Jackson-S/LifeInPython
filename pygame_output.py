from random import randint
from sys import argv
import pygame
from tgol_logic import TGOLLogic


class PygameOutput(object):
    """call do_next_step to draw the next frame to the screen"""
    def __init__(self):
        pygame.init()
        display_resolution = (1280, 800) if 1 <= len(argv) < 3 or\
                                            argv[1].isdigit() is False or\
                                            argv[2].isdigit() is False\
                                            else (int(argv[1]), int(argv[2]))
        self.timer = pygame.time.Clock()
        pygame_options = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
        self.display = pygame.display.set_mode(display_resolution, pygame_options)
        self.square_size = 32
        self.size = (display_resolution[0] // self.square_size + 2, display_resolution[1] // self.square_size + 2)
        self.colour_array = [[self._colours() for _ in range(self.size[0])] for _ in range(self.size[1])]
        self.logic = TGOLLogic(self.size[0], self.size[1])

    def do_next_step(self):
        self.display.blit(self._create_new_frame(), (0, 0))
        pygame.display.flip()
        self._check_events()

    def _draw(self, x, y, surface):
        square = self.square_size
        square_position = (y * square + square // 2, x * square + square // 2)
        square_size = self.square_size // 3
        pygame.draw.circle(surface, self.colour_array[x][y], square_position, square_size)

    def _create_new_frame(self):
        surface_result = pygame.Surface(self.display.get_size())
        surface_result.fill((0, 0, 0))
        array = self.logic.return_new_array()
        for x, x_val in enumerate(array):
            for y, y_val in enumerate(x_val):
                if y_val == 1:
                    self._draw(x, y, surface_result)
        return surface_result

    def _colours(self, minimum=0, maximum=255):
        return [randint(minimum, maximum) for _ in range(3)]

    def _check_events(self):
        for event in pygame.event.get():
            if (event.type == 2 and event.key == 27) or (event.type == 12):
                pygame.quit()
                quit()
