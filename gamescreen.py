import pygame as pg

class GameBoard:
    """
    A class to represent the game board for a Jeopardy buzzer system.

    Attributes
    ----------
    BLACK : tuple
        RGB color for black.
    WHITE : tuple
        RGB color for white.
    PINK : tuple
        RGB color for pink.
    LIME : tuple
        RGB color for lime.
    GREEN : tuple
        RGB color for green.
    BLUE : tuple
        RGB color for blue.
    HIGHLIGHT : tuple
        RGB color for highlight.
    INVALID : tuple
        RGB color for invalid input.
    FILL : int
        Value to fill the rectangle.
    EMPTY : tuple
        RGB color for an empty state.

    Methods
    -------
    __init__(screen_height=800, screen_width=1200):
        Initializes the game board with specified screen height and width.
    
    display_buzzer_window():
        Displays the initial buzzer window on the screen.
    
    display_player_name(name, contestant_number):
        Displays the name of the player at the specified contestant number position.
    
    display_buzzer_active():
        Displays the "GO!" indicator on the screen when the buzzer is active.
    """
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PINK = (255, 0, 255)
    LIME = (0, 255, 0)
    GREEN = (69, 255, 69)
    BLUE = (32, 88, 230)
    HIGHLIGHT = (153, 204, 255)
    INVALID = (200, 50, 50)
    FILL = 0
    EMPTY = (0, 0, 0)

    def __init__(self, screen_height: int = 800, screen_width: int = 1200):
        """
        Initializes the game board with the specified screen height and width.

        Parameters
        ----------
        screen_height : int, optional
            The height of the game screen (default is 800).
        screen_width : int, optional
            The width of the game screen (default is 1200).
        """

        # Set up the display
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.mega_font = pg.font.SysFont("uroob", 512)
        self.xlarge_font = pg.font.SysFont("uroob", 172)
        self.large_font = pg.font.SysFont("uroob", 96)
        self.reg_font = pg.font.SysFont("uroob", 72)

        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption('Jeopardy Buzzer System')

        # Title
        text = self.xlarge_font.render('Shipardy!', True, self.LIME)
        text_pos = (self.screen_width // 2 - text.get_width() // 2, 100 - text.get_height() // 2)
        self.screen.blit(text, text_pos)

        self.display_buzzer_window()

    def display_buzzer_window(self):
        """
        Displays the initial buzzer window on the screen.
        """

        # Buzzer Indicator
        rect_x = 100
        rect_y = 200
        rect_width = 700
        rect_height = 500
        border_width = 5
        pg.draw.rect(self.screen, self.BLACK, (rect_x, rect_y, rect_width, rect_height))
        pg.draw.rect(self.screen, self.WHITE, (rect_x, rect_y, rect_width, rect_height), border_width)

        pg.display.flip()

    def display_player_name(self, name: str, contestant_number: int):
        """
        Displays the name of the player at the specified contestant number position.

        Parameters
        ----------
        name : str
            The name of the contestant.
        contestant_number : int
            The position number of the contestant.
        """
        
        text = self.reg_font.render(name, True, self.PINK)
        text_pos = (120, 250 + 70 * contestant_number - text.get_height() // 2)
        self.screen.blit(text, text_pos)
        pg.display.flip()

    def display_buzzer_active(self):
        """
        Displays the "GO!" indicator on the screen when the buzzer is active.
        """
        
        text = self.mega_font.render("GO!", True, self.GREEN)
        text_pos = (self.screen_width // 3 - text.get_width() // 2, self.screen_height // 1.5 - text.get_height() // 2)
        self.screen.blit(text, text_pos)
        pg.display.flip()
