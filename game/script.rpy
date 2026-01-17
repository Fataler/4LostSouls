label start:
    $ quick_menu = False
    $ book_nvl_mode = False
    
    show menu_okno at cinematic_focus(x=0.62, target_zoom = 1.35)
    show snow_image at cinematic_focus(x=0.62, target_zoom = 1.35)
    show menu_fon at cinematic_focus(x=0.62, target_zoom = 1.35)
    show menu_svet at cinematic_focus(x=0.62, target_zoom = 1.35), candle_pulsation_alpha()

    girl "Мам! Мам! А почитаешь мне сказку перед сном?"

    mom "Нужно скорее засыпать. Новогодние каникулы закончились, и завтра тебе снова в школу."

    girl "Но только одну, небольшую..."

    mom "Хорошо! Выбирай, какую хочешь."
    
    girl "Ура-а! Спасибо!"

    call book_shelf from _call_book_shelf

    mom "Тогда ложись поудобнее и слушай."

    call start_book from _call_start_book

    call label_credits from _call_label_credits

    scene black

    show menu_okno:
        anchor (0.62, 0.5) 
        pos (0.5, 0.5)
        zoom 1.35
    show snow_image:
        anchor (0.62, 0.5) 
        pos (0.5, 0.5)
        zoom 1.35
    show menu_fon_completed:
        anchor (0.62, 0.5) 
        pos (0.5, 0.5)
        zoom 1.35
    show menu_svet at candle_pulsation_alpha():
        anchor (0.62, 0.5) 
        pos (0.5, 0.5)
        zoom 1.35
    with dissolve


    "Вот и всё! Ну, как тебе история?"
    "*звуки сопения*"
    
    "Ха-ха! Доброй ночи тебе, дочка!"
    
    show menu_okno at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show snow_image at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show menu_fon_completed at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show menu_svet at cinematic_focus_out(x=0.62, start_zoom=1.35), candle_pulsation_alpha()

    $ renpy.pause(3.0, hard=True)
    

    $ persistent.game_completed = True
    $ MainMenu(confirm=False)
