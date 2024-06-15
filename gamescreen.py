import pygame as pg

class GameBoard:


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

    def __init__(self, screen_height: int=800, screen_width: int=1200):

        # Set up the display
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption('Jeopardy Buzzer System')
        self.mega_font = pg.font.SysFont("uroob", 512)
        self.xlarge_font = pg.font.SysFont("uroob", 172)
        self.large_font = pg.font.SysFont("uroob", 96)
        self.reg_font = pg.font.SysFont("uroob", 72)    

        # Title 
        text = self.xlarge_font.render('Shipardy!', True, self.LIME)
        text_pos = (self.screen_width // 2 - text.get_width() // 2, 100 - text.get_height() // 2)
        self.screen.blit(text,text_pos)

        self.display_buzzer_window()

    def display_buzzer_window(self):

        # BuzzerIndicator
        rect_x = 100
        rect_y = 200
        rect_width = 700
        rect_height = 500
        border_width = 5
        pg.draw.rect(self.screen, self.BLACK, (rect_x, rect_y, rect_width, rect_height))
        pg.draw.rect(self.screen, self.WHITE, (rect_x, rect_y, rect_width, rect_height), border_width)

        pg.display.flip()


    def display_player_name(self, name: str, contestant_number):
        text = self.reg_font.render(name, True, self.PINK)
        text_pos = (120, 250 + 70*contestant_number - text.get_height() // 2)
        # text_pos = text.get_rect(centerx=1000, y=100)
        self.screen.blit(text, text_pos)
        pg.display.flip()

    def display_buzzer_active(self):
        text = self.mega_font.render("GO!", True, self.GREEN)
        text_pos = (self.screen_width // 3 - text.get_width() // 2, self.screen_height // 1.5 - text.get_height() // 2)
        self.screen.blit(text, text_pos)
        pg.display.flip()
