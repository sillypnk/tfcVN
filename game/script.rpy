######################
##  SCRIPT STARTER  ##
######################
## All files in .rpy extension are just combined into this file.

label start:
    jump main_ch01

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    return