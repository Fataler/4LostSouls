image bg_book_shelf = "images/BookShelf/BookShelf.png"
image book_shelf_button = "images/BookShelf/Book.png"
image book_shelf_stars = At(Transform("images/BookShelf/Stars.png"), candle_pulsation_alpha())

default inspect = None

screen book_shelf_screen():
    sensitive (not inspect and not _menu)
    default is_hovered = False

    fixed:
        at show_screen_transform()
        add "bg_book_shelf"

        imagebutton:
            pos(583, 243)
            idle "book_shelf_button"
            hover At("book_shelf_button", set_bright_hovered(0.03))
            action Return("read_book")
            hovered SetScreenVariable("is_hovered", True)
            unhovered SetScreenVariable("is_hovered", False)
            focus_mask True
            activate_sound sfx_ui_click

        if is_hovered:
            $ star_pos = (600, 500)
            add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(120, -180, 0.0)
            add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(-100, -150, 0.5)
            add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(160, -100, 1.0)
            add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(-140, -80, 1.5)
            add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(30, -220, 2.0)

label book_shelf_test:
    call screen book_shelf_screen()
    "Test"
    return

label book_shelf:
    $ renpy.force_autosave()

    show screen book_shelf_screen
    $ result = ui.interact()

    if result == "read_book":
        $ inspect = "reading"
        "Эту? Но ведь мы её уже много раз читали."
        "Ничего! Это моя любимая история!"
        hide screen book_shelf_screen
        $ inspect = None
        return

    $ renpy.block_rollback()
    return
