## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

image about_bg = "gui/menu/About.png"

screen about():

    tag menu

    add "about_bg"
    
    add "snow_image_full":
        alpha 0.5

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    fixed:
        use game_menu(_("Об игре"), scroll="viewport", show_background=False, x_offset=400):

            style_prefix "about"

            vbox:

                text "[config.name!t]"
                text _("Версия [config.version!t]\n")

                ## gui.about обычно установлено в options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is text:
    color gui.interface_text_color
    font gui.interface_text_font

style about_label_text:
    size gui.label_text_size
