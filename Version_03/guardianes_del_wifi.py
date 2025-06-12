# bits & bytes
# Fecha: Junio de 2025
# Descripción: version O3 Juego "Guardianes del Wifi"
from Configurations import Configurations
import pygame
from Game_functionalities import game_event,screen_refresh
from Media import Background
from Pantallazo import Pantallazo
from Troll import Troll
def run_game()->None:
    """
    Función principal
    """
    #Inicia modulo pygame
    pygame.init()

    # Se inicializa la pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background = Background()
    pantallazo = Pantallazo(screen)
    troll = Troll(screen)


    #Ciclo principal del juego
    game_over=False
    while not game_over:
        game_over = game_event()
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen, clock, background,pantallazo)
        # Se cierran los recursos del juego
    #Se cierran los recursos del juego
    pygame.quit()

#Código a nivel de módulo.
if __name__ == '__main__':
    run_game()