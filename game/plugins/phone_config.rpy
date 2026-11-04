init:
    # Time between recieved messages (don't set it to 0, it will break)
    default auto_speak_timer = 5

    # True will mean all messages will be sent with the above timer
    # False will vary the delay based on the message length of the NEXT message (so the one they are currently typing)
    # Raising or lowering the auto_speak_timer will still effect the time between messages even if this is set to False 
    # For anyone interested the math is message_timer_delay = max(min_speak_timer, min(len(list(character_info['current_dialogue'][true_current_index + 1].values())[0]) * (auto_speak_timer*0.025), max_speak_timer))
    default static_speak_timer = False

    # REMEMBER THESE CAN BE SET MID CONVERSATION USING {'code':'auto_speak_timer = 999'} IF YOU WANT TO SLOW DOWN/SPEED UP AT CERTAIN POINTS.

    # Just adds or removes the skip button entirely
    default show_skip_button = True

    # How fast the messages send when the skip messages button is pressed (again, dont set to 0)
    default skip_speed_timer = 0.5

    # This is how many columns there are for your images in the gallery. Rows is done automatically
    default image_columns = 2

    # Shows the typing indicator so you can see if the person is sending a message. 
    default is_typing_indicator = True

    # If set to true gallery unlocks will be persistant accross saves
    default persistent_gallery = False

    # You CAN set the image size with every image you send, but if they are all the same size.. thats a pain
    # So set this and you can just pass images in as {"image":"imagepath.png"}
    # This is just for the image preview sizes as they are seen inside the chat 
    default chat_image_size = [216, 384]
    
    # The message that replaces a deleted message
    default deleted_message_replacement = "This message was deleted"
 
    # Enable or disable the settings scree
    default settings_screen_shown = True

    # Enable or disable allowing message speed adjust
    default allow_speed_adjust = True

    # Enable or disable message animations 
    default message_animations = True
    
    # Says it all really... 
    default force_disable_all_phones = False

    # This is what the phone does when you press the back button from the phone home screen
    # Hide("phone_home") is a given, but the Show is me showing the GUI I created, you may not want to use that, so this is here to be easily modified

    default ikps_phone_home_back_action = [
        Show("phone_icon_overlay"),
        Hide("phone_home"),
    ]

    # Toggle false and the back button will dissapear from the home screen. (User cant close phone at all)
    default var_kps_show_back_button_home = True

    # Toggle false and the back button for contacts will be disabled (User cant close the current convo)
    default var_kps_show_back_button_contact = True

    # Notification sound
    default var_kps_phone_notification_sound = "audio/COMCell_Message 1 (ID 1111)_BigSoundBank.com.ogg"

    # Yea I set these the same here, but they can be different
    default var_kps_message_sent_sound = "COMCell_Message sent (ID 1313)_BigSoundBank.com.ogg"

    default var_kps_message_recieved_sound = "COMCell_Message sent (ID 1313)_BigSoundBank.com.ogg"

    # When you add a conversation to the tick list it will use this variance, so for example, if you add it on a 10 second
    # timer, with the varience at 2, it will send every 10-20 seconds, 0.5 varience -> 10 - 15 seconds, 10 varience -> 10 - 100 seconds (timer - timer*varience)
    # (the tick list is a list of conversations that will progress regardless of player input. Even if they are idle, phone closed, they will recieve messages)
    default _var_kps_tick_speed_varience = 2



    # Enable allowing clickthrough (so you can play the game with the phone still open)
    default var_kps_allow_clickthrough_toggle = True


    # UI CUSTOMISATION?! WOW I OUTDID MYSELF! (Did I mention I suck at UI?) 
    default speaker_colors = {
    # Set text colours for different speakers like this:
    #"mc": "#2f6cffcc",
    }

    # Minimum amount of time between messages, or short ones send REAL fast
    default min_speak_timer = 1

    # min_speak_timer gets set to 0.1 when skipping so we need a way to store what it started as, dont touch :)
    default original_min_speak_timer = min_speak_timer

    # Max speak timer between messages, to stop long ones... yk... taking too long
    default max_speak_timer = 6

    default original_max_speak_timer = max_speak_timer

    default var_kps_default_profile = "mc/mc_profile.png"



init -99:

    default var_kps_text_size = 17
    
    # The starting volume for notifications
    default var_kps_notification_volume = 0.5

    # Starting volume for message sounds
    default var_kps_message_sound_volume = 0.5



# Set to false before release :)
define config.developer = True



########### DONT CHANGE ANYTHING PAST THIS LINE ###########







