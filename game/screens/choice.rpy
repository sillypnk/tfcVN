init offset = -1

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

image choice_static_animated:
    # Display the first static frame
    "gui/button/choice_hover-kf-01.png"
    0.15 # Wait 0.05 seconds
    
    # Display the second static frame
    "gui/button/choice_hover-kf-02.png"
    0.15
    
    # Display the third static frame
    "gui/button/choice_hover-kf-03.png"
    0.15

    # Display the third static frame
    "gui/button/choice_hover-kf-04.png"
    0.15
    
    # Loop back to the beginning automatically
    repeat

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    # xoffset -30
    # ypos 500
    # yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.