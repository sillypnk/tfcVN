screen location_header(current_location="???"):
    style_prefix "location_header"

    fixed: 
        at glide, TerminalDefault(0.5 if persistent.terminal_glow else 0.0)

        hbox:
            align (0.05, 0.05)
            spacing 45
            # Settings & History Buttons
            imagebutton auto "gui/button/settings_%s.png" action ShowMenu("settings") yalign 0.5
            imagebutton auto "gui/button/history_%s.png" action ShowMenu("history") yalign 0.5

        # Center Location Text
        hbox:
            # align (0.5, 0.063)
            align (0.5, 0.050)
            spacing 15
            
            add "gui/header_arrow-left.png" yalign 0.5 yoffset 2
            text "[current_location]" style "current_location_text" yalign 0.5 yoffset -2
            add "gui/header_arrow-right.png" yalign 0.5 yoffset 2

transform glide:
    on show:
        alpha 0.0
        pause .7
        easeinout_quint 1.8 alpha 1
    on replace:
        alpha 1
        pause .7
        easeinout_quint 1.8 alpha 0

style current_location_text:
    font gui.text_font
    color gui.accent_color
    kerning 4
    size 53
    textalign 0.5