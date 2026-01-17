## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

define book_stanzas_padding = {
    1: 300,
    2: 180,
    3: 100,
    4: 40
}

transform book_img_left:
    subpixel True
    anchor (0.5, 0.5)
    pos (0.30, 0.5)

transform book_img_right:
    subpixel True
    anchor (0.5, 0.5)
    pos (0.71, 0.5)

screen nvl(dialogue, items=None):

    if book_nvl_mode:
        $ text_w = 750
        $ page_h = 800
        $ current_padding = book_stanzas_padding.get(book_page_stanzas, 40)
        $ book_stanzas_spacing = 40

        if book_text_side == "left":
            $ d_left = dialogue
            $ d_right = []
        else:
            $ d_left = []
            $ d_right = dialogue

        fixed:
            # Левая страница
            if d_left:
                frame:
                    background None
                    at book_img_left
                    xsize text_w ysize page_h
                    left_padding 180
                    top_padding current_padding
                    vbox:
                        spacing book_stanzas_spacing
                        for d in d_left:
                            if d == dialogue[-1]:
                                text d.what id d.what_id style "book_nvl_text" at appear(0.5)
                            else:
                                text d.what id d.what_id style "book_nvl_text"

            # Правая страница
            if d_right:
                frame:
                    background None
                    at book_img_right
                    xsize text_w ysize page_h
                    left_padding 160
                    right_padding 0
                    top_padding current_padding
                    vbox:
                        spacing book_stanzas_spacing
                        for d in d_right:
                            if d == dialogue[-1]:
                                text d.what id d.what_id style "book_nvl_text" at appear(0.5)
                            else:
                                text d.what id d.what_id style "book_nvl_text"

            if items:
                vbox:
                    align (0.5, 0.85)
                    for i in items:
                        textbutton i.caption:
                            action i.action
                            text_style "book_nvl_text"
                            text_hover_color "#8b5e34"

    else:
        window:
            style "nvl_window"
            has vbox:
                spacing gui.nvl_spacing
            if gui.nvl_height:
                vpgrid:
                    cols 1
                    yinitial 1.0
                    use nvl_dialogue(dialogue)
            else:
                use nvl_dialogue(dialogue)
            for i in items:
                textbutton i.caption:
                    action i.action
                    style "nvl_button"
        add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        if d == dialogue[-1]:
            window at appear(0.5):
                id d.window_id

                fixed:
                    yfit gui.nvl_height is None

                    if d.who is not None:

                        text d.who:
                            id d.who_id

                    text d.what:
                        id d.what_id
        else:
            window:
                id d.window_id

                fixed:
                    yfit gui.nvl_height is None

                    if d.who is not None:

                        text d.who:
                            id d.who_id

                    text d.what:
                        id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background None
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    size gui.text_size + 5

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")
    
style book_nvl_text:
    xpos 0
    xanchor 0
    xsize None
    xmaximum 600
    
    font "gui/fonts/Lora-Regular.ttf"
    size 27
    line_spacing 7
    color "#2b1d0e"
    xalign 0.0
    text_align 0.0
    layout "tex"
    subpixel True