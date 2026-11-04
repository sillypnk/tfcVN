style chat_title:
    font gui.text_font
    size 50
    bold True
    kerning 10
    color "#000"
    xalign 0.5

style chat_name_tag:
    font gui.text_font
    size 30
    color "#000"
    textalign 0.5

style chat_text:
    font gui.text_font
    size 25
    color "#fff"
    kerning 4
    line_spacing 15
    xmaximum 850       # Prevents text from hitting the borders

# style panel_frame:
#     background Frame("images/ui/panel_border.png", 4, 4)

# ============ MAIN SCREEN ============
screen chat_logs():
    # Background
    fixed:
        at TerminalDefault(0.5 if persistent.terminal_glow else 0.0)
        add "#000000"
        # add "images/ui/noise_overlay.png" alpha 0.1
        
        # Title bar
        vbox:
            xalign 0.5 yalign 0.5
            spacing 50

            frame:
                xalign 0.5
                xsize 500
                background "#e0e0e0"
                padding (50, 15)
                text "CHAT LOGS" style "chat_title"
            
            # Three panels
            hbox:
                yalign 0.5
                xalign 0.5
                spacing 40
                
                # LEFT: Supposedly the caller 
                frame:
                    background None
                    xysize (400, 650)
                    add Frame("gui/white-border.png", 5, 5, 5, 5)
                    viewport:
                        mousewheel False
                        draggable False

                        add Image("assets/images/splash/call-icon.png"):
                            size (200, 200)
                    # text "N/A":
                    #     font gui.text_font
                    #     size 50
                    #     color "#fff"
                    #     xalign 0.5
                    #     yalign 0.5
                        
                
                # RIGHT: Chat window
                frame:
                    xysize (1100, 650)
                    background None
                    add Frame("gui/white-border.png", 10, 10, 10, 10)
                    use chat_window
                
                # RIGHT: The character's portrait
                # frame:
                #     background None
                #     xysize (400, 610)
                #     add Frame("gui/white-border.png", 2, 2, 2, 2)
                    # text "N/A":
                    #     font gui.text_font
                    #     size 50
                    #     color "#fff"
                    #     xalign 0.5
                    #     yalign 0.5

init -1 python:
    def delayed_scroll():
        import time
        time.sleep(0.05)
        try:
            adj = renpy.get_widget("chat_logs", "chat_vp").yadjustment
            adj.change(adj.range)
            renpy.restart_interaction()
        except Exception as e:
            print(f"Scroll failed: {e}")
    
    def message_callback(event, **kwargs):
        if event == "begin":
            renpy.sound.play("assets/audio/m_click.mp3")
        if event == "end":
            # Delay slightly to let the next screen rebuild
            renpy.invoke_in_thread(delayed_scroll)

screen chat_window(items=None):
    vbox:
        # 1. Scrollable message area
        null height 3

        viewport id "chat_vp":
            yinitial 1.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            ysize 560
            xoffset -5
            
            vbox:
                # spacing between each message
                spacing 50
                xfill True
                
                null height 15   # <-- top padding
                
                for who, what, kind in nvl_list:
                    use chat_bubble(who, what)
                
                if items:
                    vbox spacing 5:
                        xalign 0.5
                        for i in items:
                            textbutton i.caption action i.action
                
                null height 15   # bottom padding

        null height 3
        
        # Divider
        frame:
            background Solid("#fff")
            ysize 1
            xfill True
            xalign 0.5
            xmargin 50
        
        # Input bar
        frame:
            # background Frame("gui/white-border.png", 10, 10, 10, 10)
            background None
            xfill True
            ysize 60
            xpadding 30
            xmargin 30
            
            hbox:
                yalign 0.5
                xfill True
                
                text "Send a message...":
                    font gui.text_font
                    size 18
                    color "#888"
                    yalign 0.5
                
                # imagebutton:
                #     idle "gui/send-icon.png"
                #     action NullAction()
                #     yalign 0.5
                #     xalign 1.0

screen chat_bubble(who, what):
    $ who_str = str(who) if who else ""
    $ is_player = (who_str == "Sarita")
    # $ align_x = 1.0 if is_player elif whoe_str == "" 0.5 else 0.0
    default align_x = 1.0
    
    # Using xoffset to give breathing room from the side borders
    # (acts as inline-margin similar to css)
    default side_margin = -65 
    python:
        if is_player:
            align_x = 1.0
            side_margin = -65
        elif who_str == "":
            align_x = 0.5
            side_margin = 0
        else:
            align_x = 0.0
            side_margin = 40
    
    vbox:
        xalign align_x
        xoffset side_margin
        # Spacing between the name tag and the dialogue/message
        spacing 20
        
        # Name tag
        if who_str:
            frame:
                background "#e0e0e0"
                padding (20, 5)
                text who_str style "chat_name_tag"
                xalign align_x
        
        # Message text
        text what style "chat_text":
            text_align align_x

image ctc_nvl:
    "gui/ctc.png"
    xalign 0.87 yalign 0.825 
    xoffset -5 
    alpha 0.0
    zoom 0.75
    subpixel True
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat