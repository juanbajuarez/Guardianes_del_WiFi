# bits & bytes
# Fecha: Junio de 2025
# Descripción: version O2 Juego "Guardianes del Wifi"
from Configurations import Configurations
import pygame
def run_game()->None:
    """
    Función principal
    """
    #Inicia modulo pygame
    pygame.init()

    #Se inicializa la pantalla
    screen_size=Configurations.get_screen_size() #Alto por ancho
    screen=pygame.display.set_mode(screen_size)

    #Título del juego
    game_title=Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    #Ciclo principal del juego
    game_over=False
    while not game_over:
        # Se verifican los eventos(teclado y ratón) del juego
        for event in pygame.event.get():
            #Un clic en cerrar el juego
            if event.type==pygame.QUIT:
                game_over=True
        #Se dibuja los elementos gráficos em la pantalla
        background=Configurations.get_background()#Fondo de la pantalla en RGB
        screen.fill(background)

        #Se actualiza la pantalla
        pygame.display.flip()
    #Se cierran los recursos del juego
    pygame.quit()

#Código a nivel de módulo.
if __name__ == '__main__':
    run_game()