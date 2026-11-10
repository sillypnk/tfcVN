################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

















## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            vbox:
                hbox:
                    textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
                null height (2 * gui.pref_spacing)
                hbox:
                    style_prefix "help_subtitle"
                    text "Keybinds"
                    text "Description"
                null height (2 * gui.pref_spacing)

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    vpgrid:
        cols 2
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

        label _("Space")
        text _("Advances dialogue without selecting choices.")

        label _("Arrow Keys")
        text _("Navigate the interface.")

        label _("Escape")
        text _("Accesses the game menu.")

        label _("Ctrl")
        text _("Skips dialogue while held down.")

        label _("Tab")
        text _("Toggles dialogue skipping.")

        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

        label _("Page Down")
        text _("Rolls forward to later dialogue.")

        label "H"
        text _("Hides the user interface.")

        label "S"
        text _("Takes a screenshot.")

        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():
    vpgrid:
        cols 2
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

        label _("Middle Click")
        text _("Hides the user interface.")

        label _("Right Click")
        text _("Accesses the game menu.")

        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():
    vpgrid:
        cols 2

        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_subtitle_hbox:
    spacing 25
    xfill True

style help_subtitle_text:
    size 28
    xalign 0.5
    textalign 0.5
    xoffset -50
    color '#d5d5d5'
    font gui.interface_text_font

style help_vpgrid:
    xspacing 20 yspacing 25
    xfill True
    right_margin 50


style help_label:
    # xsize 375
    # xoffset 375
    padding (10, 10, 10, 10)
    background gui.accent_color
    left_margin 30

style help_label_text:
    size gui.text_size
    color gui.text_color
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################








## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

# screen nvl(dialogue, items=None):
#
#     window:
#         style "nvl_window"
#
#         has vbox:
#             spacing gui.nvl_spacing
#
#         ## Displays dialogue in either a vpgrid or the vbox.
#         if gui.nvl_height:
#
#             vpgrid:
#                 cols 1
#                 yinitial 1.0
#
#                 use nvl_dialogue(dialogue)
#
#         else:
#
#             use nvl_dialogue(dialogue)
#
#         ## Displays the menu, if given. The menu may be displayed incorrectly if
#         ## config.narrator_menu is set to True.
#         for i in items:
#
#             textbutton i.caption:
#                 action i.action
#                 style "nvl_button"
#
#     add SideImage() xalign 0.0 yalign 1.0
#
#
# screen nvl_dialogue(dialogue):
#
#     for d in dialogue:
#
#         window:
#             id d.window_id
#
#             fixed:
#                 yfit gui.nvl_height is None
#
#                 if d.who is not None:
#
#                     text d.who:
#                         id d.who_id
#
#                 text d.what:
#                     id d.what_id
#
#
# ## This controls the maximum number of NVL-mode entries that can be displayed at
# ## once.
# define config.nvl_list_length = gui.nvl_list_length
#
# style nvl_window is default
# style nvl_entry is default
#
# style nvl_label is say_label
# style nvl_dialogue is say_dialogue
#
# style nvl_button is button
# style nvl_button_text is button_text
#
# style nvl_window:
#     xfill True
#     yfill True
#
#     background "gui/nvl.png"
#     padding gui.nvl_borders.padding
#
# style nvl_entry:
#     xfill True
#     ysize gui.nvl_height
#
# style nvl_label:
#     xpos gui.nvl_name_xpos
#     xanchor gui.nvl_name_xalign
#     ypos gui.nvl_name_ypos
#     yanchor 0.0
#     xsize gui.nvl_name_width
#     min_width gui.nvl_name_width
#     textalign gui.nvl_name_xalign
#
# style nvl_dialogue:
#     xpos gui.nvl_text_xpos
#     xanchor gui.nvl_text_xalign
#     ypos gui.nvl_text_ypos
#     xsize gui.nvl_text_width
#     min_width gui.nvl_text_width
#     textalign gui.nvl_text_xalign
#     layout ("subtitle" if gui.nvl_text_xalign else "tex")
#
# style nvl_thought:
#     xpos gui.nvl_thought_xpos
#     xanchor gui.nvl_thought_xalign
#     ypos gui.nvl_thought_ypos
#     xsize gui.nvl_thought_width
#     min_width gui.nvl_thought_width
#     textalign gui.nvl_thought_xalign
#     layout ("subtitle" if gui.nvl_text_xalign else "tex")
#
# style nvl_button:
#     properties gui.button_properties("nvl_button")
#     xpos gui.nvl_button_xpos
#     xanchor gui.nvl_button_xalign
#
# style nvl_button_text:
#     properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
# screen quick_menu():
#     variant "touch"

#     zorder 100

#     if quick_menu:

#         hbox:
#             style "quick_menu"
#             style_prefix "quick"

#             textbutton _("Back") action Rollback()
#             textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
#             textbutton _("Auto") action Preference("auto-forward", "toggle")
#             textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

screen upstairs_to_comlab():
    imagemap:
        ground "assets/images/splash/comlab_outside_idle.jpg"
        hover "assets/images/splash/comlab_outside_hovered.jpg"
        hotspot (699, 117, 539, 918) action Jump("main_ch01_preconflict")