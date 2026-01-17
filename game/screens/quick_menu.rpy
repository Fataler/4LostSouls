## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

image auto_off_button = "gui/A.png"
image roll_back_off = "gui/rollbek.png"

init python:
    class q_state:
        open = False
        debug = False

screen quick_menu():

    zorder 100

    if quick_menu and book_nvl_mode:
        if not q_state.open:
            fixed:
                anchor (1.0, 1.0)
                pos (1.0, 0.3)
                xsize 188
                ysize 115
                
                add "gui/Lenta_small.png"
                
                if q_state.debug:
                    add Solid("#ff000055")
                
                button:
                    area (25, 5, 140, 70)
                    action SetField(q_state, "open", True)
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("Открыть меню")
        else:
            fixed:
                anchor (1.0, 0.0)
                pos (1.0, 0.2)
                xsize 186
                ysize 617
                
                add "gui/Lenta_Bolbshoy.png"
                
                if q_state.debug:
                    add Solid("#0000ff55")
                
                button:
                    area (110, 190, 80, 45)
                    action Rollback()
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("Откат")

                if not renpy.can_rollback():
                    add "roll_back_off":
                        pos (149, 206)

                button:
                    area (110, 235, 80, 45)
                    action ShowMenu('save')
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("Сохранить")

                button:
                    area (90, 280, 80, 45)
                    action ShowMenu('load')
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("Загрузить")

                button:
                    area (70, 325, 80, 45)
                    action ShowMenu('preferences')
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("Настройки")

                button:
                    area (50, 370, 80, 45)
                    action Preference("auto-forward", "toggle")
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip ("Авто: Вкл" if _preferences.afm_enable else "Авто: Выкл")

                if (not _preferences.afm_enable):
                    add "auto_off_button":
                        pos (69, 378)
                        zoom 1.02

                button:
                    area (50, 415, 80, 45)
                    action MainMenu()
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("В меню")

                button:
                    area (50, 460, 80, 45)
                    action SetField(q_state, "open", False)
                    if q_state.debug:
                        background Solid("#00ff0055")
                    else:
                        background None
                    tooltip _("Закрыть")

        $ tooltip = GetTooltip()
        if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True
                has frame padding 15,15,15,15
                background None#Solid("#00000038")
                text tooltip style "tooltip"

        
    key "game_menu" action ToggleField(q_state, "open")

init python:
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")