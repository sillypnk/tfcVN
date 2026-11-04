init offset = -1

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

# region [screen - navigation]
screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        ypos gui.navigation_ypos
        # yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("settings")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is empty
style navigation_button_text is empty

style navigation_button:
    size_group "navigation"
    padding (10, 10, 160, 10)
    background None
    hover_background "#ffff"
    hover_sound "assets/audio/m_click.mp3"
    activate_sound "assets/audio/m_click_2.mp3"

style navigation_button_text:
    color gui.interface_text_color
    font gui.interface_text_font
    size gui.button_text_size
    hover_color "#000000"

# style navigation_button:
#     size_group "navigation"
#     properties gui.button_properties("navigation_button")

# style navigation_button_text:
#     properties gui.text_properties("navigation_button")
# endregion


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

# region [screen - main_menu]
screen main_menu():
    tag menu
    style_prefix "main_menu"
    # on "show" action Play("sound", config.main_menu_music, fadein=1.0, relative_volume=0.5)

    window at TerminalDefault(0.5 if persistent.terminal_glow else 0.0):
        add gui.main_menu_background

        # text "[config.name!t]":
        #     style "main_menu_title"
        add "menu_logo"

        text "Version [config.version]":
            style "main_menu_ver"

        hbox:
            textbutton _("Start") action Start()
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Settings") action ShowMenu("settings")
            # TODO: (A1) - Make a ending screen button and screen
            # textbutton _("Endings") action None

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=not main_menu)

style main_menu_window is empty

style main_menu_hbox:
    spacing 65
    xalign 0.5
    yalign 0.5
    yoffset 250

style main_menu_ver:
    color gui.interface_text_color font gui.interface_text_font size 25
    xalign 1.0 yalign 1.0
    xoffset -30 yoffset -30

style main_menu_button:
    padding (30, 10, 30, 10)
    background None
    hover_background "#ffff"
    hover_sound "assets/audio/m_click.mp3"
    activate_sound "assets/audio/m_click_2.mp3"

style main_menu_button_text:
    color gui.interface_text_color
    font gui.interface_text_font
    hover_color "#000000"

style main_menu_window:
    xalign 0 yalign 0
    yfill True
    xfill True
style main_menu_title:
    # The gui variables are in the game/gui.rpy
    # size gui.title_text_size
    # font gui.vhs_name_font
    # color gui.interface_text_color
    # This centers the title horizontally
    xalign 0.5 yalign 0.5
    yoffset -35
# endregion

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

define wiggle = 0.20

# region [screen - game_menu]
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    window at TerminalDefault(0.5 if persistent.terminal_glow else 0.0): 
        add gui.main_menu_background
    # if main_menu:
    #     add gui.main_menu_background
    # else:
    #     add gui.game_menu_background

        frame:
            style "game_menu_outer_frame"

            hbox:

                ## Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            vbox:
                                spacing spacing

                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            spacing spacing

                            transclude

                    else:

                        transclude

        use navigation

        textbutton _("Return"):
            style "return_button"

            action Return()

        label title

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")


style game_menu_window is empty
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_window:
    xalign 0 yalign 0
    yfill True
    xfill True

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
# endregion


# region [screen - quick_menu]
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        vbox:
            style_prefix "quick"
            style "quick_menu"
            # xpos 150

            imagebutton auto "gui/button/quick_back_%s.png" action Rollback() 
            imagebutton auto "gui/button/quick_skip_%s.png":
                action Skip() alternate Skip(fast=True, confirm=True) 
                selected renpy.config.skipping
            imagebutton auto "gui/button/quick_auto_%s.png":
                action Preference("auto-forward", "toggle")
                selected preferences.afm_enable
            imagebutton auto "gui/button/quick_save_%s.png" action ShowMenu('save')

            # textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("Auto") action Preference("auto-forward", "toggle")
            # textbutton _("Save") action ShowMenu('save')
            # textbutton _("Settings") action ShowMenu('settings')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is vbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    # xalign 0.5
    xalign 1.0 yalign 1.0
    xoffset -240
    yoffset -45
    spacing 5

# style quick_button:
#     properties gui.button_properties("quick_button")

# style quick_button_text:
#     properties gui.text_properties("quick_button")

# transform q_fadein:
#     on hover:
#         alpha 0.0
#         linear 0.15 alpha 1.0
#     on idle:
#         alpha 1.0
#         linear 0.15 alpha 0.0

style quick_button:
    properties gui.button_properties("quick_button")
    padding (10, 10, 10, 10)
    background None
    hover_background "#ffff"
    hover_sound "assets/audio/m_click.mp3"
    activate_sound "assets/audio/m_click_2.mp3"

style quick_button_text:
    properties gui.text_properties("quick_button")
    font gui.interface_text_font
    size 20
    hover_color "#000000"
# endregion

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

# region [screen - about]
screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
# endregion

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

# region [screen - save]
screen save():

    tag menu

    use file_slots(_("Save"))
# endregion


# region [screen - save]
screen load():

    tag menu

    use file_slots(_("Load"))
# endregion

# region [screen - file_slots]
screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        mouse "slot_cursor"

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")
# endregion


## Settings screen ##########################################################
##
## The settings screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

# region [screen - settings]
screen settings():

    tag menu

    use game_menu(_("Settings"), scroll="viewport"):

        vbox:
            style_prefix "header"
            vbox:
                text "Visuals and Screen"
                add Solid ('#8888887f', xysize=(670, 3)):
                    xoffset 5
                null height 2

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "check"
                    label _("Misc")
                    textbutton _("Enable Glow") action ToggleVariable("persistent.terminal_glow")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            # For spacing between the two options
            null height (4 * gui.pref_spacing)

            vbox:
                text "Dialogues and Audio"
                add Solid ('#8888887f', xysize=(670, 3)):
                    xoffset 5
                null height 2
            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style header_text:
    size 50
    color gui.accent_color
    font gui.interface_text_font
    xoffset 5

style header_vbox:
    spacing 25
    xfill True

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    left_padding 50

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    left_padding 50

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525
    ysize 38
    
    # Remove default thumbs
    thumb None
    thumb_shadow None
    hover_thumb None
    hover_thumb_shadow None

    idle_right_bar Frame("gui/slider/horizontal_idle_empty.png", 4, 4, 4, 4)
    idle_left_bar Frame("gui/slider/horizontal_idle_full.png", 4, 4, 4, 4)
    
    hover_right_bar Frame("gui/slider/horizontal_hover_empty.png", 4, 4, 4, 4)
    hover_left_bar Frame("gui/slider/horizontal_hover_full.png", 4, 4, 4, 4)

    # Centers the fill inside the container perfectly
    bar_vertical False
    yalign 0.5
    
    # Gutter prevents the fill from spilling out of the borders
    left_gutter 4   
    right_gutter 4

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675
    spacing 10
# endregion

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

# region [screen - history]
screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
# endregion