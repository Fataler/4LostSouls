#images 


# Фоны
image bg_book = "images/book/Fon_kniga.png"
image bg_book_elka = At(Button(child="images/book/Elka.png", action=NullAction(), focus_mask=True, style="empty"), sway_hover)
image bg_book_svet = At(Transform("images/book/Svet_book.png", anchor=(1.0, 0.0)), candle_pulsation)
image book_logo = "images/book/logo_black.png"


# credits images
image credits_bg:
    "images/Credits/Credits.png"

image credits_us:
    "images/Credits/thanks.png"

image credits_img_1:
    "images/Credits/1.png"
image credits_img_2:
    "images/Credits/2.png"
image credits_img_3:
    "images/Credits/3.png"
image credits_img_4:
    "images/Credits/4.png"
image credits_img_5:
    "images/Credits/5.png"

## Общие изображения
image bg_black = Solid("#000")
image bg_white = Solid("#fff")
image bg_red = Solid("#ff1304")
image bg_paper = Solid("#FFE7CE")

image bg_black_t_10 = Solid("#0000001a")
image bg_black_t_20 = Solid("#00000033")
image bg_black_t_30 = Solid("#0000004d")
image bg_black_t_40 = Solid("#00000066")
image bg_black_t_50 = Solid("#00000080")
image bg_black_t_60 = Solid("#00000099")
image bg_black_t_70 = Solid("#000000b3")
image bg_black_t_80 = Solid("#000000cc")
image bg_black_t_90 = Solid("#000000e6")

image bg_menu_main = "gui/menu/bg_old.png"



## Эффекты
transform darken:
    matrixcolor TintMatrix("#000000") * OpacityMatrix(0.7)

transform lighten:
    matrixcolor TintMatrix("#eef13a") * OpacityMatrix(0.3)

# Анимированное затемнение
transform fade_to_dark:
    linear 1.0 matrixcolor TintMatrix("#000000") * OpacityMatrix(0.0)
    linear 1.0 matrixcolor TintMatrix("#000000") * OpacityMatrix(0.7)

# Анимированное осветление
transform fade_to_light:
    linear 1.0 matrixcolor TintMatrix("#000000") * OpacityMatrix(0.7)
    linear 1.0 matrixcolor TintMatrix("#000000") * OpacityMatrix(0.0)


