# region scene_1
layeredimage scene_1_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/1/Hover.png"
    always:
        image:
            "illustrations/1/Hover_Lada.png"
        at delay_appear(delay = 2.0, time = 1.0)
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
    pause 2.0
    linear 0.5 alpha 0.0
    xoffset 160
    zoom 0.8
    linear 0.5 alpha 1.0
    pause 2.0
    linear 0.5 alpha 0.0
    xoffset 320
    yoffset 300
    zoom 0.4
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
        image:
            "illustrations/4/4_0004_juvnost.png"
        at _shake(force_x = 3.0, speed = 0.08, do_repeat = True)
    always:
        image:
            "illustrations/4/4_0003_sneg_snizu.png"
    always:
        image:
            "illustrations/4/4_0002_svet2.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/4/4_0001_svet.png"
        at candle_pulsation_alpha(delay = 0.3), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/4/4_0000_sneg.png"
        at candle_pulsation_alpha(delay = 0.6), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
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
        image:
            "illustrations/5/5_0002_Пиксельный-слой.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/5/5_0001_Пиксельный-слой.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/5/5_0000_Пиксельный-слой.png"
    always:
        "snow_image"
# endregion

# region scene_6
layeredimage scene_6_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/6/fon.png"
    always:
        "illustrations/6/1.png"
    always:
        image:
            "illustrations/6/jmih.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/6/stars.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/6/sneg.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "illustrations/6/effect.png"
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
        image:
            "illustrations/7/sneg.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/7/jmih.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "snow_image"
# endregion

# region scene_8
define time_tiktok = 1.5

layeredimage scene_8_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/8/8.png"
    always:
        image:
            "illustrations/8/8_dver.png"
            pause 3.0
            linear 0.5 alpha 0.0
    always:
        "illustrations/8/8_svet.png"
    always:
        image:
            linear 0.2 alpha 0.0
            "illustrations/8/8_tiktok_1.png"
            linear 0.2 alpha 1.0
            pause time_tiktok
            linear 0.2 alpha 0.0
            "illustrations/8/8_tiktok_2.png"
            linear 0.2 alpha 1.0
            pause time_tiktok
            linear 0.2 alpha 0.0
            "illustrations/8/8_tiktok_3.png"
            linear 0.2 alpha 1.0
            pause time_tiktok
            repeat
# endregion

# region scene_9
layeredimage scene_9_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/9/fon.png"
    always:
        image:
            "illustrations/9/Lada.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
    always:
        image:
            "illustrations/9/svet1.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/9/svet2.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/9/ekran_1.png"
            pause 2.5
            "illustrations/9/ekran_2.png"
            pause 2.5
            "illustrations/9/ekran_3.png"
            pause 2.5
            repeat
# endregion

# region scene_10
layeredimage scene_10_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/10/fon.png"
    always:
        image:
            "illustrations/10/alo.png"
        at hue_cycle(time = 3.0)
# endregion

# region scene_11
layeredimage scene_11_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/11/fon.png"
    always:
        image:
            "illustrations/11/Lada.png"
        at offset_animated(x_offset = 0, y_offset = 15, time = 3.0)
    always:
        image:
            "illustrations/11/svet.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_12
layeredimage scene_12_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/12/12_0004_fon.png"
    always:
        image:
            "illustrations/12/lada.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
    always:
        image:
            "illustrations/12/svet.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "illustrations/12/sneg_1.png"
    always:
        "illustrations/12/sneg_2.png"
    always:
        "snow_image"
# endregion

# region scene_13
layeredimage scene_13_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/13/fon.png"
    always:
        "illustrations/13/eda_1.png"
    always:
        image:
            "illustrations/13/lada_4.png"
    always:
        image:
            "illustrations/13/kisli_3.png"
        at offset_animated(x_offset = 0, y_offset = 7, time = 0.6)
    always:
        image:
            "illustrations/13/svet_1.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/13/svet_2.png"
        at candle_pulsation_alpha(delay = 0.2), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/13/svet_3.png"
        at candle_pulsation_alpha(delay = 0.4), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/13/svet_4.png"
        at candle_pulsation_alpha(delay = 0.6), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/13/svet_5.png"
        at candle_pulsation_alpha(delay = 0.8), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "illustrations/13/sneg_2.png"
    always:
        "snow_image"
# endregion

# region scene_14
layeredimage scene_14_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/14/14_0003_Пиксельный-слой.png"
    always:
        image:
            "illustrations/14/14_0002_girlanda.png"
        at hue_cycle(time = 3.0)
    always:
        "illustrations/14/14_0001_jmih.png"
    always:
        image:
            "illustrations/14/14_0000_stars.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_15
layeredimage scene_15_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/15/fon.png"
    always:
        image:
            "illustrations/15/shobak.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
    always:
        image:
            "illustrations/15/jmih.png"
        at candle_pulsation_alpha(delay = 0.0)
    always:
        image:
            "illustrations/15/svet.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_16
layeredimage scene_16_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/16/fon.png"

    always:
        image:
            alpha 0.0
            pause 5.0
            "illustrations/16/shobak_2.png"
            linear 0.5 alpha 1.0
        at _shake(force_x = 1.0, speed = 0.1, do_repeat = True)
    always:
        image:
            "illustrations/16/stars1.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/16/svet.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "illustrations/16/snow.png"
    always:
        "snow_image"
        
    always:
        "illustrations/16/ramka.png"
        
    always:
        image:
            "illustrations/16/shobak_1.png"
            pause 5.0
            linear 0.5 alpha 0.0
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
# endregion

# region scene_17
layeredimage scene_17_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/17/fon.png"
    always:
        image:
            "illustrations/17/ruka.png"
        at offset_animated(x_offset = -5, y_offset = 5, time = 2.0)
    always:
        image:
            "illustrations/17/jmih.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/17/stars.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/17/svet1.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/17/svet2.png"
        at candle_pulsation_alpha(delay = 0.3), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_18
layeredimage scene_18_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/18/1.png"
    always:
        image:
            pause 6.0
            alpha 0.0
            "illustrations/18/2.png"
            linear 3 alpha 1.0
# endregion

# region scene_19
layeredimage scene_19_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/19/fon.png"
    always:
        image:
            "illustrations/19/kisli.png"
        at _shake(force_x = 1.0, speed = 0.08, do_repeat = True)
    always:
        "illustrations/19/sneg_melkiy.png"
    always:
        "illustrations/19/sneg.png"
    always:
        "illustrations/19/svet.png"
    always:
        "illustrations/19/svet2.png"
    always:
        "snow_image"
# endregion

# region scene_20
layeredimage scene_20_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/20/fon.png"
    always:
        image:
            "illustrations/20/kisli.png"
        at offset_animated(x_offset = 0, y_offset = 6, time = 3.0)
    always:
        image:
            "illustrations/20/girlanda.png"
        at hue_cycle(time = 3.0)
    always:
        image:
            "illustrations/20/svet1.png"
    always:
        image:
            "illustrations/20/svet2.png"
        at  hue_cycle(time = 3.0)# candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_21
layeredimage scene_21_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/21/21_0003_fon.png"
    always:
        image:
            "illustrations/21/21_0001_ruka.png"
        at offset_animated(x_offset = 25, y_offset = 0, time = 2.0)
    always:
        image:
            "illustrations/21/21_0002_noga.png"
        at offset_animated(x_offset = 0, y_offset = 25, time = 2.5)
    always:
        image:
            "illustrations/21/21_0000_kisli.png"
        at _shake(force_x = 3.0, speed = 0.1, do_repeat = True)
# endregion

# region scene_22
layeredimage scene_22_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/22/fon.png"
    always:
        image:
            pause 7.0
            xoffset 80
            alpha 0.0
            "illustrations/22/kot.png"
            ease 1 alpha 1.0 xoffset 0
        at offset_animated(x_offset = 0, y_offset = 15, time = 3.0)
    always:
        image:
            "illustrations/22/stars_nad_kotom.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/22/svet_luna_nad_kotom.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_23
layeredimage scene_23_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/23/fon.png"
    always:
        "illustrations/23/Lada.png"
    always:
        image:
            "illustrations/23/Ruki.png"
        at offset_animated(x_offset = 2, y_offset = 10, time = 2.0)
    always:
        image:
            "illustrations/23/tear_1.png"
            pause 0.2
            "illustrations/23/tear_2.png"
            pause 0.2
            "illustrations/23/tear_3.png"
            pause 0.2
            "illustrations/23/tear_4.png"
            pause 0.2
            repeat

    always:
        "snow_image"
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

# region scene_27
layeredimage scene_27_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/27/fon.png"
    always:
        image:
            "illustrations/27/kisli.png"
        at offset_animated(x_offset = 0, y_offset = 15, time = 3.0)
    always:
        image:
            "illustrations/27/stars1.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/27/stars2.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_28
layeredimage scene_28_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/28/zaokonie.png"
    always:
        "snow_image"
    always:
        "illustrations/28/fon.png"
    always:
        image:
            "illustrations/28/cheli.png"
    always:
        image:
            "illustrations/28/stars.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/28/svet.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_29
layeredimage scene_29_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/29/fon.png"
    always:
        image:
            "illustrations/29/kisli.png"
        at offset_animated(x_offset = 0, y_offset = 5, time = 2.5)
    always:
        image:
            "illustrations/29/girlanda1_1.png"
        at hue_cycle(time = 3.0)
    always:
        image:
            "illustrations/29/girlanda2_2.png"
        at hue_cycle(time = 3.5)
    always:
        image:
            "illustrations/29/stars1_4.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/29/stars2_5.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/29/svet1_3.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/29/svet2_6.png"
        at candle_pulsation_alpha(delay = 0.3), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
# endregion

# region scene_30
layeredimage scene_30_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/30/fon.png"
    always:
        image:
            "illustrations/30/Lada.png"
    always:
        image:
            "illustrations/30/kisli.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
    always:
        image:
            "illustrations/30/stars.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/30/svet.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/30/svet2.png"
        at candle_pulsation_alpha(delay = 0.5), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "illustrations/30/sneg.png"
    always:
        "snow_image"
# endregion

# region scene_31
layeredimage scene_31_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/31/fon.png"
    always:
        image:
            "illustrations/31/kisli.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
    always:
        image:
            "illustrations/31/stars.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        "illustrations/31/snow.png"
    always:
        image:
            "illustrations/31/wind.png"
        at offset_animated(x_offset = 20, y_offset = 5, time = 1.0)
    always:
        "snow_image"
# endregion

# region scene_32
layeredimage scene_32_image:
    at Transform(crop=(0, 0, 900, 1200), size=(600, 800), subpixel=True)
    always:
        "illustrations/32/fon.png"
    always:
        image:
            "illustrations/32/varejka.png"
        at offset_animated(x_offset = 0, y_offset = 10, time = 3.0)
    always:
        image:
            "illustrations/32/jmih.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 5, y_offset = 5, time = 3.0)
    always:
        image:
            "illustrations/32/heart.png"
        at candle_pulsation_alpha(delay = 0.0), offset_animated(x_offset = 0, y_offset = 5, time = 2.5)
    
    always:
        image:
            "illustrations/32/konec.png"
        at offset_animated(x_offset = 0, y_offset = 5, time = 2.5)

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
    scene scene_6_image
    "scene_6_image"
    scene scene_7_image
    "scene_7_image"
    scene scene_8_image
    "scene_8_image"
    scene scene_9_image
    "scene_9_image"
    scene scene_10_image
    "scene_10_image"
    scene scene_11_image
    "scene_11_image"
    scene scene_12_image
    "scene_12_image"
    scene scene_13_image
    "scene_13_image"
    scene scene_14_image
    "scene_14_image"
    scene scene_15_image
    "scene_15_image"
    scene scene_16_image
    "scene_16_image"
    scene scene_17_image
    "scene_17_image"
    scene scene_18_image
    "scene_18_image"
    scene scene_19_image
    "scene_19_image"
    scene scene_20_image
    "scene_20_image"
    scene scene_21_image
    "scene_21_image"
    scene scene_22_image
    "scene_22_image"
    scene scene_23_image
    "scene_23_image"
    scene scene_24_image
    "scene_24_image"
    scene scene_25_image
    "scene_25_image"
    scene scene_26_image
    "scene_26_image"
    scene scene_27_image
    "scene_27_image"
    scene scene_28_image
    "scene_28_image"
    scene scene_29_image
    "scene_29_image"
    scene scene_30_image
    "scene_30_image"
    scene scene_31_image
    "scene_31_image"
    scene scene_32_image
    "scene_32_image"
    return
# endregion
