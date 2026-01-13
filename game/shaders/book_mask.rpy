init -2 python:
    renpy.register_shader(
        "fx.book_mask",
        variables=r"""
            uniform float u_time;
            uniform float u_mask_scale;
            uniform float u_mask_speed;
            uniform float u_mask_base;
            uniform float u_mask_noise;
            uniform float u_mask_edge;
        """,
        fragment_functions=r"""
            float bm_hash(vec2 p) {
                return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758);
            }

            float bm_noise(vec2 p) {
                vec2 i = floor(p);
                vec2 f = fract(p);

                float a = bm_hash(i);
                float b = bm_hash(i + vec2(1.0, 0.0));
                float c = bm_hash(i + vec2(0.0, 1.0));
                float d = bm_hash(i + vec2(1.0, 1.0));

                vec2 u = f * f * (3.0 - 2.0 * f);
                return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
            }

            float bm_fbm(vec2 p) {
                float v = 0.0;
                float a = 0.5;
                for (int i = 0; i < 3; i++) {
                    v += a * bm_noise(p);
                    p *= 2.0;
                    a *= 0.5;
                }
                return v;
            }
        """,
        fragment_450=r"""
            vec2 uv = v_tex_coord.xy;

            vec2 t = vec2(u_time * u_mask_speed, u_time * u_mask_speed * 0.67);
            float n = bm_fbm(uv * u_mask_scale + t);

            vec2 p = abs(uv - 0.5);
            float d = max(p.x, p.y);

            float safe_edge = clamp(u_mask_base + (n - 0.5) * u_mask_noise, 0.1, 0.48);
            float mask = smoothstep(safe_edge, safe_edge - u_mask_edge, d);

            vec4 c = texture2D(tex0, uv, u_lod_bias);
            float a = c.a * mask;
            gl_FragColor = vec4(c.rgb * a, a);
        """
    )

transform book_masked(
    scale=12.0,
    speed=0.1,
    base=0.48,
    noise=0.15,
    edge=0.1
):
    mesh True
    shader "fx.book_mask"

    u_mask_scale scale
    u_mask_speed speed
    u_mask_base base
    u_mask_noise noise
    u_mask_edge edge

    pause 1.0/30
    repeat

transform book_page_fade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0