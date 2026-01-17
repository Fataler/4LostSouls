# Музыка
define music_amberlight = "audio/bg/Amberlight-chosic.com_.mp3"
define music_lost_in_the_quiet = "audio/bg/Chromatic Heartbeat - Lost in the Quiet.mp3"
define music_hope = "audio/bg/Hope-Emotional-Soundtrack(chosic.com).mp3"
define music_snow_plains = "audio/bg/Over-the-Plains-of-Snow-MP3(chosic.com).mp3"
define music_twinkling_tinsel = "audio/bg/Twinkling Tinsel Trio - Cold Heart Hug.mp3"

# Звуки
define sfx_cat_meow = "audio/sfx/cat_meow.wav"
define sfx_cat_purr = "audio/sfx/cat_purr.wav"
define sfx_dog_eating = "audio/sfx/dog_eating.wav"
define sfx_dog_bark_happy = "audio/sfx/dog_gaf_dovolen.flac"
define sfx_dog_bark = "audio/sfx/dog_gaf.wav"
define sfx_dog_whine = "audio/sfx/dog_skulej.wav"
define sfx_page_1 = "audio/sfx/page_1.wav"
define sfx_page_2 = "audio/sfx/page_2.wav"
define sfx_page_3 = "audio/sfx/page_3.wav"
define sfx_page_4 = "audio/sfx/page_4.wav"
define sfx_page_5 = "audio/sfx/page_5.wav"
define sfx_fireworks = "audio/sfx/salut.mp3"
define sfx_snow_steps_1 = "audio/sfx/snow_steps.wav"
define sfx_snow_steps_2 = "audio/sfx/snow_steps2.wav"
define sfx_snow_step = "audio/sfx/snow_step.wav"
define sfx_snow_run = "audio/sfx/snow_run.ogg"
define sfx_winter_wind = "audio/sfx/winter_wind.wav"
define sfx_crowd = "audio/sfx/crowd_1.flac"
define sfx_cat_angry_1 = "audio/sfx/angry_cat_1.ogg"
define sfx_cat_angry_2 = "audio/sfx/cat_angry_2.ogg"
define sfx_cat_cry = "audio/sfx/cat_cry.wav"
define sfx_door_open = "audio/sfx/door_open.wav"
define sfx_slap = "audio/sfx/slap.wav"

# Интерфейс
define sfx_ui_click = "audio/sfx/UI Click.ogg"
define sfx_ui_over = "audio/sfx/UI 03 Over.ogg"


# каналы
init python:
    renpy.music.register_channel("ui", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx3", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("music2", mixer="music", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
