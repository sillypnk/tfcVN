# define s = DynamicCharacter('s_name', image='stella', what_prefix='"', what_suffix='"',  ctc_position="fixed")
# define c = DynamicCharacter('c_name', image='chris', what_prefix='"', what_suffix='"',  ctc_position="fixed")

# # TODO: Characters
# define k = DynamicCharacter('k_name', image='kyouto', what_prefix='"', what_suffix='"',  ctc_position="fixed")
# define h = DynamicCharacter('h_name', image='haru', what_prefix='"', what_suffix='"',  ctc_position="fixed")
# define d = DynamicCharacter('d_name', image='nhaydrel', what_prefix='"', what_suffix='"',  ctc_position="fixed")
# define r = DynamicCharacter('r_name', image='ramirez', what_prefix='"', what_suffix='"',  ctc_position="fixed")

## •❅───✧❅✦❅✧───❅•
#   Characters Init 
## •❅───✧❅✦❅✧───❅•
# Narrator
define narrator = Character(ctc="ctc", ctc_position="fixed", callback = name_callback, cb_name = None)

# Chapter 1 characters
define stephanie = Character('Stephanie', ctc="ctc", ctc_position="fixed", image="stephanie", callback = name_callback, cb_name = "stephanie")
define sarita = Character('Sarita', ctc="ctc", ctc_position="fixed", callback = name_callback, cb_name = "sarita")
define sarita_s = Character('Sarita', ctc="ctc", ctc_position="fixed", image="sarita_s", callback = name_callback, cb_name = "sarita_s")
define gabriel = Character('Gabriel', ctc="ctc", ctc_position="fixed", image="gabriel", callback = name_callback, cb_name = "gabriel")
define maria = Character('Maria', ctc="ctc", ctc_position="fixed", image="maria", callback = name_callback, cb_name = "maria" )

# Silhouettes
define s1 = Character('???', ctc="ctc", ctc_position="fixed", callback = name_callback, cb_name="s1")
define s2 = Character('???', ctc="ctc", ctc_position="fixed", callback = name_callback, cb_name="s2")
define s3 = Character('???', ctc="ctc", ctc_position="fixed", callback = name_callback, cb_name="s3")
define s4 = Character('ICT Administrator', ctc="ctc", ctc_position="fixed", callback = name_callback, cb_name="s4")

## This is for the vhs calling screen
default vhs_slots = {"left": ("r1", ""), "right": ("c2", "")}
define r1 = Character("Sarita", screen="vhs_call", show_speaker="left", show_slot_char="r1", image="sarita")
define c1 = Character("Caller", screen="vhs_call", show_speaker="left", show_slot_char="c1", image="s1")

default nvl_mode = "phone"
define nvl_n = Character(kind=nvl, ctc="ctc_nvl", ctc_position="fixed", callback=message_callback)
define snvl = Character("Sarita", kind=nvl, ctc="ctc_nvl", ctc_position="fixed", callback=message_callback)
define caller = Character("[caller_name]", kind=nvl, ctc="ctc_nvl", ctc_position="fixed", callback=message_callback)

# Chapter 2 characters
# Chapter 3 characters

## •❅───✧❅✦❅✧───❅•
#    Game Variables  
## •❅───✧❅✦❅✧───❅•
# for persistent variables 
# default persistent.<variable_name> = <variable_value>
# default <variable_name> = <variable_value>

## •❅───✧❅✦❅✧───❅•
#  Character Sprites 
## •❅───✧❅✦❅✧───❅•
## (It is much better to separate them each expressions or body changes.
## That way, the artist won't have a hard time doing a bunch of work.)
# layeredimage <character>:
    # always:
    #     "images/<character>/body.png"
        
    # group <part>:
    #     attribute <expression> default:
    #         "images/<character>/<part>_<expression>.png"
    #     attribute <expression>:
    #         "images/<character>/<part>_<expression>.png"
# layeredimage stephanie:
#jlk    always:
#         "images/characters/stephanie/base.png"

#     group expressions:
#         # This will set the default expression of the sprite
#         attribute neutral default:
#             "images/characters/stephanie/neutral.png"

image s1 = "assets/images/characters/silhouette.png"
image s2 = "assets/images/characters/silhouette-2.png"
image s3 = "assets/images/characters/silhouette-3.png"
image s4 = "assets/images/characters/silhouette-3.png"

layeredimage stephanie:
    at sprite_highlight('stephanie')

    group body:
        attribute base default:
            "assets/images/characters/stephanie/base_01.png"
        attribute base_02:
            "assets/images/characters/stephanie/base_02.png"
        attribute base_03:
            "assets/images/characters/stephanie/base_03.png"
        
    group expressions:
        attribute neutral default:
            "assets/images/characters/stephanie/exp_neutral.png"
        # Can be combined with base_03 (base_03 + worried)
        attribute worried:
            "assets/images/characters/stephanie/exp_worried.png"
        # Can be combined with base_03 (terrified + base_03)
        attribute terrified:
            "assets/images/characters/stephanie/exp_terrified.png"
        attribute happy:
            "assets/images/characters/stephanie/exp_happy.png"
        attribute smile:
            "assets/images/characters/stephanie/exp_smile.png"
        attribute angry:
            "assets/images/characters/stephanie/exp_angry.png"

layeredimage sarita:
    at sprite_highlight('sarita')
    group body:
        attribute base_01 default:
            "assets/images/characters/sarita/base_01.png"

    group expressions:
        attribute neutral default:
            "assets/images/characters/sarita/exp_neutral.png" 
        attribute happy:
            "assets/images/characters/sarita/exp_happy.png" 
        attribute awkward:
            "assets/images/characters/sarita/exp_awkward.png" 

image side sarita_s = LayeredImageProxy("sarita", Transform(zoom=0.30))

layeredimage maria:
    at sprite_highlight('maria')
    always:
        "assets/images/characters/maria/base_01.png"

    group expressions:
        attribute neutral default:
            "assets/images/characters/maria/exp_neutral.png"
        attribute smile:
            "assets/images/characters/maria/exp_smile.png"
        attribute happy:
            "assets/images/characters/maria/exp_happy.png"

layeredimage gabriel:
    at sprite_highlight('gabriel')
    always:
        "assets/images/characters/gabriel/base_01.png"

    group expressions:
        attribute neutral default:
            "assets/images/characters/gabriel/exp_neutral.png"
        attribute smile:
            "assets/images/characters/gabriel/exp_smile.png"
        attribute happy:
            "assets/images/characters/gabriel/exp_happy.png"
    

## •❅───✧❅✦❅✧───❅•
#  [Assets] : Audio
## •❅───✧❅✦❅✧───❅•
## Syntax:
## define audio.<name> = "<src>"
# Background Music 
define audio.bg1 = "assets/audio/bgm/Relaxing in the Afternoon.mp3"
define audio.bg2 = "assets/audio/bgm/Two worlds, Two Summers.mp3"
define audio.bg3 = "assets/audio/bgm/boasting.mp3"
define audio.bg4 = "audio/Out of the cold, into the Warmth.mp3"
define audio.main = "audio/2.ogg"

# Sound Effects
define audio.suspense = "assets/audio/sfx/suspense_buildup.mp3"
# define audio.chair_move = "audio/chair_move.mp3"
# define audio.chair_drag = "audio/chair_drag.mp3"
# define audio.body_fall = "audio/body_fall.mp3"
# define audio.clock_ticking = "audio/clock_ticking.mp3"
# define audio.sliding_door_open = "audio/sliding_door_open.mp3"
# define audio.sliding_door_slam = "audio/sliding_door_slam.mp3"
define audio.notif_wonderhoy = "assets/audio/sfx/wonderhoy.mp3"