# region scene_1
layeredimage scene_1_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/1/Hover.png"
    always:
        image:
            "illustrations/1/Hover_Lada.png"
        at delay_appear(delay = 1.0, time = 1.0)
    always:
        image:
            "illustrations/1/Hover_stars.png"
        #at , 
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
        blend "add"
    always:
        image:
            "illustrations/1/Hover_blesk.png"
        at offset_animated(x_offset = 4, y_offset = -4, time = 2.0)
    always:
        "snow_image"
# endregion

# region scene_2
layeredimage scene_2_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/2/fon.png"
    always:
        image:
            "illustrations/2/2_Lada.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 2.0)
    always:
        "illustrations/2/2_svet.png"
    always:
        image:
            "illustrations/2/2_svet_2.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_3
transform scene_3_lada_move:
    subpixel True
    xoffset 0
    yoffset 0
    # pause 1.0
    # linear 0.5 alpha 0.0
    # xoffset 160
    # zoom 0.8
    linear 0.5 alpha 1.0

image lada_3 = "illustrations/3/Lada.png"

layeredimage scene_3_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/3/Fon.png"
    always:
        image:
            "illustrations/3/Lada.png"
        at scene_3_lada_move
    always:
        "illustrations/3/svet2.png"
    always:
        image:
            "illustrations/3/svet1.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 15, time = 2.0)
    # always:
    #     "snow_image"
# endregion

# region scene_4
layeredimage scene_4_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/4/4_0005_fon.png"
    always:
        "illustrations/4/4_0004_juvnost.png"
    always:
        "illustrations/4/4_0003_sneg_snizu.png"
    always:
        "illustrations/4/4_0002_svet2.png"
    always:
        "illustrations/4/4_0001_svet.png"
    always:
        "illustrations/4/4_0000_sneg.png"
    always:
        "snow_image"
# endregion

# region scene_5
layeredimage scene_5_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/5/5_0004_Пиксельный-слой.png"
    always:
        "illustrations/5/5_0003_Пиксельный-слой.png"
    always:
        "illustrations/5/5_0002_Пиксельный-слой.png"
    always:
        "illustrations/5/5_0001_Пиксельный-слой.png"
    always:
        "illustrations/5/5_0000_Пиксельный-слой.png"
    always:
        "snow_image"
# endregion

# region scene_7
layeredimage scene_7_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/7/fon.png"
    always:
        "illustrations/7/stars.png"
    always:
        "illustrations/7/sneg.png"
    always:
        "illustrations/7/jmih.png"
    always:
        "snow_image"
# endregion

# region scene_8
layeredimage scene_8_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/8/8.png"
    always:
        "illustrations/8/8_dver.png"
    always:
        "illustrations/8/8_svet.png"
    always:
        image:
            "illustrations/8/8_tiktok_1.png"
            pause 0.2
            "illustrations/8/8_tiktok_2.png"
            pause 0.2
            "illustrations/8/8_tiktok_3.png"
            pause 0.2
            repeat
# endregion

# region scene_10
layeredimage scene_10_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/10/fon.png"
    always:
        "illustrations/10/alo.png"
# endregion

# region scene_14
layeredimage scene_14_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/14/14_0003_Пиксельный-слой.png"
    always:
        "illustrations/14/14_0002_girlanda.png"
    always:
        "illustrations/14/14_0001_jmih.png"
    always:
        "illustrations/14/14_0000_stars.png"
# endregion

# region scene_19
layeredimage scene_19_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/19/fon.png"
    always:
        "illustrations/19/sneg_melkiy.png"
    always:
        "illustrations/19/sneg.png"
    always:
        "illustrations/19/svet.png"
    always:
        "illustrations/19/svet2.png"
    always:
        "illustrations/19/kisli.png"
    always:
        "snow_image"
# endregion

# region scene_20
layeredimage scene_20_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/20/fon.png"
    always:
        "illustrations/20/girlanda.png"
    always:
        "illustrations/20/svet1.png"
    always:
        "illustrations/20/svet2.png"
    always:
        "illustrations/20/kisli.png"
# endregion

# region scene_24
layeredimage scene_24_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/24/24.png"
    always:
        "snow_image"
# endregion

# region scene_25
layeredimage scene_25_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/25/fon.png"
    always:
        image:
            "illustrations/25/25_0009_salut_1.png"
            linear 0.5 alpha 1.0
            "illustrations/25/25_0008_salut_2.png"
            pause 0.2
            "illustrations/25/25_0007_salut_3.png"
            pause 0.2
            "illustrations/25/25_0006_salut_4.png"
            pause 0.2
            "illustrations/25/25_0005_salut_5.png"
            pause 0.2
            "illustrations/25/25_0004_salut_6.png"
            pause 0.2
            "illustrations/25/25_0003_salut_7.png"
            pause 0.2
            "illustrations/25/25_0002_salut_8.png"
            pause 0.2
            "illustrations/25/25_0001_salut_9.png"
            pause 0.2
            "illustrations/25/25_0000_salut_10.png"
            linear 2.2 alpha 0.0
            pause 2.2
            repeat
    always:
        "snow_image"
# endregion

# region scene_26
layeredimage scene_26_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/26/fon.png"
    always:
        image:
            "illustrations/26/stars.png"
        at candle_pulsation_alpha
    always:
        "snow_image"
# endregion

# region Test Label
label test_illustrations:
    scene scene_1_image
    "scene_1_image"
    scene scene_2_image
    "scene_2_image"
    scene scene_3_image
    "scene_3_image"
    scene scene_4_image
    "scene_4_image"
    scene scene_5_image
    "scene_5_image"
    scene scene_7_image
    "scene_7_image"
    scene scene_8_image
    "scene_8_image"
    scene scene_10_image
    "scene_10_image"
    scene scene_14_image
    "scene_14_image"
    scene scene_19_image
    "scene_19_image"
    scene scene_20_image
    "scene_20_image"
    scene scene_24_image
    "scene_24_image"
    scene scene_25_image
    "scene_25_image"
    scene scene_26_image
    "scene_26_image"
    return
# endregion
