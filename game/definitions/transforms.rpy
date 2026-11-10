## •❅───✧❅✦❅✧───❅•
#      Transforms 
## •❅───✧❅✦❅✧───❅•
## Scene Transitions ##
# region [SCENE TRANSITIONS]
define dissolve = Dissolve(0.25)
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)
define dissolve_character = Dissolve(0.3, alpha=True)
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])
# endregion

## Custom Warpers ##
init python early:
    import math

    # Ease Out Back (Overshoots slightly then returns) - The MatPat "Pop"
    @renpy.atl_warper
    def ease_out_back(t):
        s = 1.70158
        t -= 1
        return (t * t * ((s + 1) * t + s) + 1)

    # Ease Out Expo (Fast start, extremely smooth slow down)
    @renpy.atl_warper
    def ease_out_expo(t):
        return 1 if t == 1 else 1 - math.pow(2, -10 * t)

    # Ease In Out Quint (Very slow start, fast middle, very slow end)
    @renpy.atl_warper
    def easeinout_quint(t):
        if t < 0.5:
            return 16 * t * t * t * t * t
        else:
            t -= 1
            return 1 + 16 * t * t * t * t * t

    # Ease Out Elastic (The "Jiggle" or "Boing")
    @renpy.atl_warper
    def ease_out_elastic(t):
        c4 = (2 * math.pi) / 3
        if t == 0: return 0
        if t == 1: return 1
        return math.pow(2, -10 * t) * math.sin((t * 10 - 0.75) * c4) + 1

define cg_z = 0.45
## CG Transform Functions ##
transform tcommon(x=960, z=cg_z, dist=300, dir=-1):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.20
        zoom z * 1.00 alpha 0.00
        xoffset (dist * dir)
        xcenter x
        easein_cubic 1.05 xoffset 0 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein_cubic .8 xcenter x zoom z * 1.00
            easein_cubic .8 xcenter x
        parallel:
            easein_cubic .5 yoffset 0 ypos 1.20

# 1 character on screen
transform t11(z=cg_z):
    tcommon(960, z)
# 2 characters on screen
transform t21(z=cg_z):
    tcommon(440, z)
transform t22(z=cg_z):
    tcommon(1410, z, dir=1)
transform t31(z=cg_z):
    tcommon(300)
transform t32(z=cg_z):
    tcommon(950)
transform t33(z=cg_z):
    tcommon(1540, z=z, dir=1)
# endregion

## CG Animations & Transitions ##
# region [focus]
transform focus(x=960, z=cg_z):
    yanchor 1.0 ypos 1.20 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.20
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0
# endregion

# region [zoom]
transform tzoom(x=960, z=cg_z):
    subpixel True
    xcenter x 
    yoffset 0 ypos 1.20 yanchor 1.0
    zoom z*1.00
    easein .5 zoom z*2.30 ypos 2.42

transform z11(z=cg_z):
    tzoom(960, z)

transform z21(z=cg_z):
    tzoom(440, z)
transform z22(z=cg_z):
    tzoom(1410, z)
# endregion

# region [sink]
transform sink(x=960, z=cg_z):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.20 zoom z*1.00 alpha 1.00 subpixel True
    easein_cubic .5 ypos 1.30

transform s21(z=cg_z):
    sink(440, z)
transform s22(z=cg_z):
    sink(1410, z)
transform s31(z=cg_z):
    sink(300, z)
transform s32(z=cg_z):
    sink(950, z)
transform s33(z=cg_z):
    sink(1540, z)
# endregion

# region [bounce]
transform bounce(x=960, z=cg_z):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.20 zoom z*1.00 alpha 1.00 subpixel True
    easein 0.3 yoffset -40
    easeout 0.3 yoffset 0
    repeat
# endregion

# region [panic]
transform panic(x=960, z=cg_z):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.20 zoom z*1.00 alpha 1.00 subpixel True

    parallel:
        block:
            linear 0.05 xoffset 10
            linear 0.05 xoffset -10
            repeat
    parallel:
        block:
            linear 0.05 yoffset -5
            linear 0.05 yoffset 5
            repeat
# endregion


# region [leftin] 
transform leftin(x=440, z=0.95):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.20 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

transform l21(z=0.95):
    leftin(440, z)
transform l22(z=0.95):
    leftin(1410, z)
# endregion 

# region [hop]
transform hop(x=960, z=cg_z):
    subpixel True
    xcenter x 
    yoffset 0 yanchor 1.0 ypos 1.20
    zoom z*1.00
    alpha 1.00 
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform h11(z=cg_z):
    hop(960, z)
transform h21(z=cg_z):
    hop(440, z)
transform h22(z=cg_z):
    hop(1410, z)
transform h31(z=cg_z):
    hop(300, z)
transform h32(z=cg_z):
    hop(950, z)
transform h33(z=cg_z):
    hop(1540, z)
    
# endregion

#region [teasing_giggle]
transform teasing_giggle(x=960, z=cg_z):
    subpixel True
    xcenter x 
    yoffset 0 yanchor 1.0 ypos 1.20
    zoom z*1.00
    alpha 1.00 
    block:
        # Hop Up and tilt right
        linear 0.15 yoffset -20 xoffset 2 rotate 1
        # Back down to center
        linear 0.15 yoffset 0 xoffset 0 rotate 0
        # Hop Up and tilt left
        linear 0.15 yoffset -20 xoffset -2 rotate -1
        # Back down to center
        linear 0.15 yoffset 0 xoffset 0 rotate 0
        repeat

transform tg11(z=cg_z):
    teasing_giggle(960, z)
transform tg21(z=cg_z):
    teasing_giggle(440, z)
transform tg22(z=cg_z):
    teasing_giggle(1410, z)
transform tg31(z=cg_z):
    teasing_giggle(300, z)
transform tg32(z=cg_z):
    teasing_giggle(950, z)
#endregion

# region [angry jitter]
transform angry_jitter(x=960, z=cg_z):
    subpixel True
    xcenter x
    yoffset 0 yanchor 1.0 ypos 1.20
    zoom z*1.00
    alpha 1.00
    block:
        xoffset 3 yoffset 1
        pause 0.02
        xoffset -3 yoffset -1
        pause 0.02
        xoffset 2 yoffset -2
        pause 0.02
        xoffset -2 yoffset 2
        pause 0.02
        repeat

transform aj11(z=cg_z):
    angry_jitter(960, z)
transform aj21(z=cg_z):
    angry_jitter(440, z)
transform aj22(z=cg_z):
    angry_jitter(1410, z)
transform aj31(z=cg_z):
    angry_jitter(300, z)
transform aj32(z=cg_z):
    angry_jitter(950, z)
#endregion

transform rage(x=960, z=cg_z):
    subpixel True
    xcenter x
    yoffset 0 yanchor 1.0 ypos 1.20
    zoom z*1.00
    alpha 1.00
    xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3

# region [hide]
transform hide(z=cg_z):
    subpixel True
    transform_anchor True
    on hide:
        easein_cubic .6 alpha 0.00 yoffset 20

transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -500

transform rhide(duration=.75):
    subpixel True
    on hide:
        easeout_cubic duration xcenter 3000
# endregion

transform fadeout(x=960, z=cg_z):
    subpixel True
    xcenter x
    yoffset 0 yanchor 1.0 ypos 1.20
    zoom z*1.00
    alpha 1.00
    easein_cubic 0.7 alpha 0.0

transform fo11(z=cg_z):
    fadeout(960, z)
transform fo21(z=cg_z):
    fadeout(440, z)
transform fo22(z=cg_z):
    fadeout(1410, z)
transform fo31(z=cg_z):
    fadeout(300, z)
transform fo32(z=cg_z):
    fadeout(950, z)
transform fo33(z=cg_z):
    fadeout(1540, z)

transform fadein(x=960, z=cg_z):
    subpixel True
    xcenter x
    yoffset 0 yanchor 1.0 ypos 1.20
    zoom z*1.00
    alpha 0.0
    easein_cubic 0.3 alpha 1.0

transform fi11(z=cg_z):
    fadein(960, z)
transform fi21(z=cg_z):
    fadein(440, z)
transform fi22(z=cg_z):
    fadein(1410, z)
transform fi31(z=cg_z):
    fadein(300, z)
transform fi32(z=cg_z):
    fadein(950, z)
transform fi33(z=cg_z):
    fadein(1540, z)

transform vignette:
    alpha 0
    linear 2.0 alpha 1