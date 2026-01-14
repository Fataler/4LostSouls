label start:
    show menu_okno at cinematic_focus(x=0.62, target_zoom = 1.35)
    show snow_image at cinematic_focus(x=0.62, target_zoom = 1.35)
    show menu_fon at cinematic_focus(x=0.62, target_zoom = 1.35)
    show menu_svet at cinematic_focus(x=0.62, target_zoom = 1.35), candle_pulsation_alpha()


    "Привет"

    jump start_book

    scene black

    show menu_okno at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show snow_image at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show menu_fon at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show menu_svet at cinematic_focus_out(x=0.62, start_zoom=1.35), candle_pulsation_alpha()

    "Cпокойной ночи"
    $ MainMenu(confirm=False)
    #jump start_book
#    menu:
#            "Начало игры":
#                jump day_0_prologue
#            "room_1":
#                jump room_1
