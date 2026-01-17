init -1:
    transform set_bright_hovered(brightness_level=0.1):
        matrixcolor BrightnessMatrix(brightness_level)

    transform set_tint_hovered(tint_color="#ffcccc"):
        matrixcolor TintMatrix(tint_color)

    transform sway_hover:
        subpixel True
        rotate_pad False
        on hover:
            block:
                ease 0.13 xoffset 2 yoffset 1
                ease 0.12 xoffset -2 yoffset -1
                ease 0.17 xoffset 1 yoffset -2
                ease 0.12 xoffset -1 yoffset 2
                ease 0.16 xoffset 1.5 yoffset -1.5
                ease 0.2 xoffset 0 yoffset 0
        on idle:
            linear 0.5 rotate 0.0 xoffset 0 yoffset 0

    transform candle_pulsation:
        subpixel True
        
        block:
            ease 0.8 zoom 1.01 alpha 1.0
            ease 1.2 zoom 0.99 alpha 0.95
            ease 1.0 zoom 1.005 alpha 0.98
            ease 1.5 zoom 0.995 alpha 1.0
            ease 0.9 zoom 1.01 alpha 0.96
            ease 1.3 zoom 1.0 alpha 1.0
            pause 0.5
            repeat

    transform candle_pulsation_alpha(delay = 0.0, clamp_alpha = 0.5):
        pause delay
        ease 0.5 alpha clamp_alpha
        ease 1.0 alpha 1.0
        ease 0.8 alpha 1.0
        ease 1.0 alpha 0.70
        ease 1.0 alpha clamp_alpha
        pause 0.5
        repeat

    transform show_screen_transform(show_time=0.5, hide_time=0.5):
        on show:
            alpha 0.0
            linear show_time alpha 1.0
        on hide:
            linear hide_time alpha 0.0

    transform offset_animated(x_offset = 0, y_offset = 0, time = 1.0):
        subpixel True
        xoffset 0
        yoffset 0
        ease time xoffset x_offset yoffset y_offset
        ease time xoffset 0 yoffset 0
        repeat

    transform appear(time = 1.0, delay = 0.0):
        alpha 0.0
        pause delay
        linear time alpha 1.0

    transform disappear(time = 1.0, delay = 0.0):
        alpha 1.0
        pause delay
        linear time alpha 0.0

    transform _shake(force_x = 10.0, speed = 0.1, do_repeat = False):
        subpixel True
        xoffset 0
        yoffset 0
        block:
            linear speed xoffset force_x
            pause speed
            linear speed xoffset -force_x
            pause speed
            linear speed xoffset force_x
            pause speed
            linear speed xoffset 0
            repeat (1000 if do_repeat else 0)

    transform crt:
        parallel:
            function WaveShader(amp=0.05, period=17.219, speed=4, direction="horizontal", damp=(0.999,0.043))

    transform dizzy:
        parallel:
            function WaveShader(amp=(1,1), period=(1,2), speed=(1.5,1.5), direction="horizontal", damp=(1,0), double="horizontal")

    transform crt_effects:
        parallel:
            blend "multiply" alpha 0.5
        parallel:
            function WaveShader(amp=0.05, period=17.219, speed=4, direction="vertical", damp=(0.043,1.0))

    image crt = At("Backgrounds/crt.png", crt_effects)

    transform hover_effect(opac=1):
        on show:
            alpha 0.0
        on hover:
            ease 0.25 alpha opac
        on idle:
            ease 0.25 alpha 0.0 blend "add"

    transform magic_star_particle(x_dist, y_dist, delay_time, duration=3.0):
        subpixel True
        alpha 0.0 xoffset 0 yoffset 0
        pause delay_time
        block:
            parallel:
                ease duration * 0.4 alpha 1.0
                ease duration * 0.6 alpha 0.0
            parallel:
                linear duration xoffset x_dist yoffset y_dist
            alpha 0.0 xoffset 0 yoffset 0
            repeat

    transform cinematic_focus(x=0.5, y=0.5, target_zoom=1.2, duration=3.0):
        subpixel True
        zoom 1.0 anchor (0.5, 0.5) pos (0.5, 0.5)
        ease duration zoom target_zoom anchor (x, y)

    transform cinematic_focus_out(x=0.5, y=0.5, start_zoom=1.2, duration=3.0):
        subpixel True
        zoom start_zoom anchor (x, y) pos (0.5, 0.5)
        ease duration zoom 1.0 anchor (0.5, 0.5)

    transform move_by_circle(cx=0.5, cy=0.5, radius=100, duration=2.0, start_angle=0.0, clockwise=True):
        xpos cx
        ypos cy
        function circle_motion(radius, duration, start_angle, clockwise)
        repeat

init python:
        import math
        def _circle_motion(radius, duration, start_angle_deg, clockwise, trans, st, at):
            if duration <= 0.0:
                progress = 0.0
            else:
                progress = (st % duration) / duration
            direction = -1.0 if clockwise else 1.0
            angle_rad = math.radians(start_angle_deg) + direction * (2.0 * math.pi * progress)
            trans.xoffset = radius * math.cos(angle_rad)
            trans.yoffset = radius * math.sin(angle_rad)
            return 0
        circle_motion = renpy.curry(_circle_motion)