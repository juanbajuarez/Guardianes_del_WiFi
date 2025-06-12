import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Troll(Sprite):

    """
    Clase que contiene el fondo de pantalla
    """
    def __init__(self,screen):
        """

        """
        super().__init__()

        self._frames=[]

        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_troll_sheet_path()
        troll_sheet = pygame.image.load(sheet_path)

        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_troll_per_row()
        sheet_width = troll_sheet.get_width()
        sheet_height = troll_sheet.get_height()
        troll_frame_width = sheet_width // sheet_frames_per_row
        troll_frame_height = sheet_height

        """NUEVO."""
        # Se obtiene el tamaño para escalar cada frame.
        troll_frame_size = Configurations.get_troll_size()

        """NUEVO."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * troll_frame_width
            y = 0
            subsurface_rect = (x, y, troll_frame_width, troll_frame_height)
            frame = troll_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, troll_frame_size)

            self._frames.append(frame)

        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.left = screen_rect.left
        self.rect.centery = screen_rect.centery


    def blit (self,screen:pygame.surface.Surface)->None:
            """
            Se utiliza para dibujar el soldado en pantalla
            """
            screen.blit(self.image,self.rect)
