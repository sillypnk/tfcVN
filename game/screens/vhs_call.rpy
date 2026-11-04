init offset = -1

screen vhs_call(who, what, speaker, slot_char):
    style_prefix "vhs"
    zorder 50  

    # $ current_speaker_tag = renpy.get_say_image_tag()

    python:
        # 1. Grab current line traits safely
        current_speaker_tag = renpy.get_say_image_tag()
        current_attributes = renpy.get_attributes(current_speaker_tag) or []
        
        # Convert attributes tuple (e.g., ('nervous',)) to a space-separated string ("nervous")
        expr_str = " ".join(current_attributes)

        # 2. Only update the persistent states on an actual dialogue step (not prediction)
        if not renpy.predicting():
            if speaker == "left":
                # Save both the character object name and their active expression string
                vhs_slots["left"] = (slot_char, expr_str)
            elif speaker == "right":
                vhs_slots["right"] = (slot_char, expr_str)

    # 3. Pull our saved structures out of the global store
    $ left_data = vhs_slots["left"]
    $ right_data = vhs_slots["right"]

    # 4. Safely extract character objects with foolproof tag and name fallbacks
    $ left_obj = globals().get(left_data[0])
    $ left_base_tag = left_obj.image_tag if left_obj else "teto"
    $ left_display = " ".join(filter(None, (left_base_tag, left_data[1])))
    $ left_name = left_obj.name if left_obj else "Victim 1"

    $ right_obj = globals().get(right_data[0])
    $ right_base_tag = right_obj.image_tag if right_obj else "adachi"
    $ right_display = " ".join(filter(None, (right_base_tag, right_data[1])))
    $ right_name = right_obj.name if right_obj else "Victim 2"

    fixed:
        at VHS
        add Solid("#050505")

        # LEFT FRAME
        vbox: 
            style "vhs_left_vbox"
            frame:
                viewport:
                    mousewheel False
                    draggable False
                    add Solid("#000000")
                    
                    add left_display:
                        zoom 0.95
                        matrixcolor SaturationMatrix(0) * ContrastMatrix(10)
                        xalign 0.5 yalign 1
                
            text "{static}[left_name]{/static}" style "vhs_name" 
            
            # Direct properties bypass the default textbox overrides
            if speaker == "left":
                text what id "what":
                    color "#fff"
                    size 30
                    font gui.vhs_dialogue_font
                    outlines [(2, "#000", 0, 0)]
                    xalign 0.5
                    xmaximum 500  
                    yminimum 80
            else:
                text " ":
                    yminimum 80
                    size 30

        # RIGHT FRAME  
        vbox:
            style "vhs_right_vbox"
            frame:
                viewport:
                    mousewheel False
                    draggable False
                    add Solid("#000000")
                    
                    add right_display:
                        zoom 0.75
                        matrixcolor SaturationMatrix(0) * ContrastMatrix(10)
                        xalign 0.5 yalign 1

            text "{static}[right_name]{/static}" style "vhs_name" 
            
            if speaker == "right":
                text what id "what":
                    color "#fff"
                    size 30
                    font gui.vhs_dialogue_font
                    outlines [(2, "#000", 0, 0)]
                    xalign 0.5
                    xmaximum 500  
                    yminimum 80
            else:
                text " ":
                    yminimum 80
                    size 30

style vhs_left_vbox:
    xpos 250 yalign 0.5
style vhs_right_vbox:
    xalign 1.0 xoffset -250 yalign 0.5
style vhs_frame:
    xysize (550, 700)
    xalign 0.5
    background None
style vhs_name:
    xalign 0.5 yoffset 30
    color "#fff"
    size 40
    font gui.name_text_font
    bold True
    outlines [(2, "#000", 0, 0)]