# bits & bytes
# Fecha: Junio de 2025
# Descripción: version O3 Juego "Guardianes del Wifi"
# Configuraciones del juego

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)            # Alto por ancho
    _game_title = "Guardianes del Wifi"  #Título del juego
    _troll_size=(250,250)
    _pantallazo_size=(250,250)
    _fps = 8
    _sheet_frames_pantallazo_per_row=4
    _sheet_frames_troll_per_row=4
    _sheet_frames_pantallazo_per_column=2
    _pantallazo_frame_delay = 24

    # Rutas de las imágenes utilizadas para las clases Background, SnakeBlock y Apple.
    _background_image_path = "../Media/background_image.png"
    _troll_sheet_path="../Media/Troll.png"
    _pantallazo_sheet_path="../Media/Pantallazo.png"
    _lol_sheet_path="../Media/Lol.png"
    _xd_sheet_path="../Media/Xd.png"

    #Métodos de acceso
    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para _screen_size
        :return:
        """
        return cls._screen_size
    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_troll_sheet_path(cls) -> str:
        """
        Getter para _troll_sheet_path.
        """
        return cls._troll_sheet_path

    @classmethod
    def get_pantallazo_sheet_path(cls) -> str:
        """
        Getter para _pantallazo_sheet_path.
        """
        return cls._pantallazo_sheet_path

    @classmethod
    def get_lol_sheet_path(cls) -> str:
        """
        Getter para _lol_sheet_path.
        """
        return cls._lol_sheet_path

    @classmethod
    def get_xd_sheet_path(cls) -> str:
        """
        Getter para _xd_sheet_path.
        """
        return cls._xd_sheet_path

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_troll_size(cls) -> tuple[int, int]:
        """
        Getter para _troll_size
        :return:
        """
        return cls._troll_size
    @classmethod
    def get_pantallazo_size(cls) -> tuple[int, int]:
        """
        Getter para _pantallazo_size
        :return:
        """
        return cls._pantallazo_size

    @classmethod
    def get_frames_pantallazo_per_row(cls) -> int:
        """
        Getter para _frames_pantallazo_per_row.
        """
        return cls._sheet_frames_pantallazo_per_row

    @classmethod
    def get_frames_pantallazo_per_column(cls) -> int:
        """
        Getter para _frames_pantallazo_per_column.
        """
        return cls._sheet_frames_pantallazo_per_column

    @classmethod
    def get_frames_troll_per_row(cls) -> int:
        """
        Getter para _frames_pantallazo_per_row.
        """
        return cls._sheet_frames_troll_per_row

    @classmethod
    def get_pantallazo_frame_delay(cls) -> int:
        """
        Getter para _pantallazo_frame_delay.
        """
        return cls._pantallazo_frame_delay