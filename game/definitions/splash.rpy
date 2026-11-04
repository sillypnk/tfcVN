## •❅───✧❅✦❅✧───❅•
##  [Assets]: Splashes
## •❅───✧❅✦❅✧───❅•
## These are the images that are shown before the game is started.
## image bg <bg_name> = "<bg_src>"

image menu_logo:
    subpixel True
    "assets/images/splash/the_caller_title.png"
    xalign 0.5 yalign 0.5
    zoom 1.20

image top_frame = Frame("gui/header.png", ysize=159, xfill=True)
image bottom_frame = Frame("gui/background_frame.png", ysize=330, xfill=True)

transform top_bar_pos:
    subpixel True
    # ypos -500
    xpos -500
    alpha 0
    easein_cubic 1 xpos 0 alpha 1 #ypos 0 alpha 1

transform bottom_bar_pos:
    subpixel True
    yalign 1.0
    yoffset 500
    alpha 0
    easein_cubic 1 yoffset 0 alpha 1

image vignette = "assets/images/splash/vignette.png"