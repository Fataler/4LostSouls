image menu_svet = "gui/menu/Menu_2_svet.png"
image menu_fon = "gui/menu/Menu_1.png"
image menu_fon_completed = "gui/menu/Menu_1_completed.png"
image menu_okno = "gui/menu/Menu_2_okno.png"

image menu_logo = "gui/menu/logo_white.png"
image menu_pin = "gui/menu/pin.png"

screen main_menu(from_game_menu=False):
    tag menu

    on "show" action Function(stop_all_sfx)
    on "replace" action Function(stop_all_sfx)
    on "start" action Function(stop_all_sfx)

    $ elements_apperar_time = 0.5
        
    add "bg_black"
    add "menu_okno"
    add "snow_image":
        pos (900, 0)

    if persistent.game_completed:
        add "menu_fon_completed"
    else:
        add "menu_fon"

    add "menu_svet" at candle_pulsation_alpha

    add "menu_logo":
        at delay_appear(1, elements_apperar_time)
        pos (150, 80)

    textbutton "Игра создана в рамках Капелла Jam 3 2026":
        at delay_appear(1 + 1.75, elements_apperar_time)
        pos (0.025, 0.95)
        text_size 20
        text_align 0.5
        action OpenURL(URL_JAM)
        hover_mouse "inspect"

    style_prefix "main_menu"

    vbox:
        spacing 5
        align (0.11, 0.76)
    
        button action Start() at delay_appear(1 + 0.25, elements_apperar_time):
            style "main_menu_button"
            hbox:
                spacing 20
                add "menu_pin" at pin_hover_transform yalign 0.5
                text _("Начать") style "main_menu_button_text" size 70 yalign 0.5

        button action ShowMenu("load") at delay_appear(1 + 0.5, elements_apperar_time):
            style "main_menu_button"
            hbox:
                spacing 20
                add "menu_pin" at pin_hover_transform yalign 0.5
                text _("Загрузить") style "main_menu_button_text" size 40 yalign 0.5

        button action ShowMenu("preferences") at delay_appear(1 + 0.75, elements_apperar_time):
            style "main_menu_button"
            hbox:
                spacing 20
                add "menu_pin" at pin_hover_transform yalign 0.5
                text _("Настройки") style "main_menu_button_text" size 40 yalign 0.5

        button action [ShowMenu("about")] at delay_appear(1 + 1, elements_apperar_time):
            style "main_menu_button"
            hbox:
                spacing 20
                add "menu_pin" at pin_hover_transform yalign 0.5
                text _("Об игре") style "main_menu_button_text" size 40 yalign 0.5

        if renpy.variant("pc"):
            button action Quit(confirm=not main_menu) at delay_appear(1 + 1.25, elements_apperar_time):
                style "main_menu_button"
                hbox:
                    spacing 20
                    add "menu_pin" at pin_hover_transform yalign 0.5
                    text _("Выход") style "main_menu_button_text" size 40 yalign 0.5

    if show_main_menu_fade:
        add "bg_black" at menu_alpha_out(1)
        timer 1 action SetVariable("show_main_menu_fade", False)

style main_menu_button:
    properties gui.button_properties("main_menu")

style main_menu_button_text is gui_button_text

style main_menu_button_text:
    properties gui.text_properties("main_menu")
    color gui.interface_text_color
    hover_color gui.hover_color
    text_align 0.0
    xalign 0.0
    font gui.interface_text_font
    outlines [(2, "000000AA", 0, 0)]

style main_menu_vbox is vbox:
    xalign 1.0
    #xoffset -30
    #yoffset -30
    xmaximum 1200
    yalign 1.0

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    properties gui.text_properties("version")

transform hover_scale:
    anchor (0.5, 0.5)
    rotate 0
    on idle:    
        parallel:
            linear 0.1 xzoom 1.0 yzoom 1.0
    on hover:
        parallel:
            linear 0.1 xzoom 1.1 yzoom 1.1

transform menu_alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform alpha_in(time=0.5):
    alpha 0
    linear time alpha 1

transform alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform jam_logo_transform:
    on hover:
        matrixcolor HueMatrix(0)
        linear 5 matrixcolor HueMatrix(360)
        repeat

transform pin_hover_transform:
    alpha 0.0
    on hover:
        linear 0.4 alpha 1.0
    on idle:
        alpha 0.0
