image bg_book_shelf = "images/BookShelf/BookShelf.png"
image book_shelf_button = "images/BookShelf/Book.png"
image book_shelf_stars = At(Transform("images/BookShelf/Stars.png"), candle_pulsation_alpha(smooth=True))

screen book_shelf_screen():
    default is_hovered = False
    add "bg_book_shelf"

    imagebutton:
        pos(583, 243)
        idle "book_shelf_button"
        action Return()
        hovered SetScreenVariable("is_hovered", True)
        unhovered SetScreenVariable("is_hovered", False)
        focus_mask True

    if is_hovered:
        # Центральная точка вылета звезд
        $ star_pos = (600, 500)
        # Равномерно распределяем направления (x, y) и задержки
        add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(120, -180, 0.0)
        add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(-100, -150, 0.5)
        add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(160, -100, 1.0)
        add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(-140, -80, 1.5)
        add "images/BookShelf/Stars.png" pos star_pos anchor(0.5, 0.5) at magic_star_particle(30, -220, 2.0)

label book_shelf:
    call screen book_shelf_screen()
    "a"
    return