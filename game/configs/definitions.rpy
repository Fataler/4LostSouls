#constants
default persistent.first_start = True
default persistent.game_completed = False
define URL_JAM = "https://vk.com/chapel_jam"

#screens
default MAIN_MENU_SCREEN = "main_menu"
default PAUSE_MENU_SCREEN = "pause_menu"

define splash_enabled = False

default textbox_style = "gui/textbox.png"

# chars
define book_nvl = Character(None, kind=nvl, what_style="book_nvl_text")
define girl = Character(None)
define mom = Character(None)

default book_current_img = None

default book_nvl_mode = False
default book_text_side = "left"
default book_page_stanzas = 2