# bits & bytes
# Fecha: Junio de 2025
# Descripción: version O3 Juego "Guardianes del Wifi"
# Funcionalidades del juego

import pygame
from Configurations import Configurations
from Media import Background
from Pantallazo import Pantallazo
def game_event()->bool:
    """
    Función que administra los eventos del juego.
    Return: La bandera del fin del juego.
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock: pygame.time.Clock,background:Background,pantallazo:Pantallazo)->None:
    """
    Función que administra los elementos visuales del juego
    """

    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    #animacion del pantallazo
    pantallazo.update_animation()

    #Se dibuja el pantallazo
    pantallazo.blit(screen)
    # Se actualiza la pantalla
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())