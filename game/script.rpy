label start:
    $ quick_menu = False
    $ book_nvl_mode = False
    
    show menu_okno at cinematic_focus(x=0.62, target_zoom = 1.35)
    show snow_image at cinematic_focus(x=0.62, target_zoom = 1.35)
    show menu_fon at cinematic_focus(x=0.62, target_zoom = 1.35)
    show menu_svet at cinematic_focus(x=0.62, target_zoom = 1.35), candle_pulsation_alpha()

    "Мам! Мам! А почитаешь мне сказку перед сном?"

    "Нужно скорее засыпать. Новогодние каникулы закончились и завтра тебе снова в школу."

    "Но только одну, небольшую..."

    "Хорошо! выбирай, какую хочешь."
    
    "Ураа! Спасибо!" 

    call book_shelf

    "Тогда ложись поудобнее и слушай."

    call start_book

    call label_credits

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


    "Вот и всё! Ну как тебе история?"
    "*звуки сопения*"
    
    "Ха-ха! Доброй ночи тебе, дочка!"
    
    show menu_okno at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show snow_image at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show menu_fon_completed at cinematic_focus_out(x=0.62, start_zoom=1.35)
    show menu_svet at cinematic_focus_out(x=0.62, start_zoom=1.35), candle_pulsation_alpha()

    $ renpy.pause(3.0, hard=True)
    

    $ persistent.game_completed = True
    $ MainMenu(confirm=False)
