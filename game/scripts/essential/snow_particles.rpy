init -1 python:
    SNOW_COUNT_SMALL = 100
    SNOW_COUNT_MED = 70
    SNOW_COUNT_LARGE = 30
    
    SNOW_SPEED_SMALL = (50, 100)
    SNOW_SPEED_MED = (100, 200)
    SNOW_SPEED_LARGE = (200, 350)
    
    SNOW_DRIFT = (30, 80)
    
    SNOW_SYMBOL = "●"
    SNOW_FONT = "gui/fonts/DejaVuSansMono.ttf"

image snow_p_small:
    Text(SNOW_SYMBOL, font=SNOW_FONT, size=6, color="#ffffff9a")
    alpha 0.4

image snow_p_med:
    Text(SNOW_SYMBOL, font=SNOW_FONT, size=12, color="#ffffff9a")
    alpha 0.6

image snow_p_large:
    Text(SNOW_SYMBOL, font=SNOW_FONT, size=18, color="#ffffff9a")
    alpha 0.8

image snow_image:
    crop (0, 0, 900, 1200)
    
    contains:
        SnowBlossom("snow_p_small", count=SNOW_COUNT_SMALL*2, border=50, xspeed=SNOW_DRIFT, yspeed=SNOW_SPEED_SMALL, start=0, fast=True)
    contains:
        SnowBlossom("snow_p_med", count=SNOW_COUNT_MED*2, border=50, xspeed=SNOW_DRIFT, yspeed=SNOW_SPEED_MED, start=0, fast=True)
    contains:
        SnowBlossom("snow_p_large", count=SNOW_COUNT_LARGE*2, border=50, xspeed=SNOW_DRIFT, yspeed=SNOW_SPEED_LARGE, start=0, fast=True)
