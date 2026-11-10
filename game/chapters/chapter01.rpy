
label main_ch01:
    with dissolve_scene_full
    stop music

    # --- SCENE 1 --- 
    sarita "S-steph! Wait for me!"

    scene bg school_frontview with dissolve_scene_full
    play music bg1 fadein 1.0 loop

    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("School Gate")

    show sarita awkward at t21
    sarita "{i}*huff *huff*{/i} G-good morning..."
    show stephanie smile at t22
    stephanie "Good morning sari~"
    stephanie "Look, Sarita. The lighting and the morning wind is perfect for an instagram post!"
    show sarita awkward at s21
    sarita "Y-yeah… I guess."
    "This is my best friend, Stephanie. We've always been together since kindergarten and she was my one and only friend."

    show stephanie neutral with dissolve_character
    stephanie "Did you wake up well?"
    show sarita at t21
    show sarita neutral with dissolve_character
    sarita "Yeah..."

    show sarita at fo21
    hide sarita
    pause 0.3
    show stephanie at fo22
    pause 0.2
    hide stephanie

    show s1 at t21
    # s(1-3) means silhouette/s. These silhouettes are defined at definitions.rpy.
    s1 "Wait, isn’t that THE Stephanie?" 
    show s2 at t22
    s2 "Wait, really?! It is her! Oh my god, I’m such a big fan!" 
    show s1 at fo21
    hide s1
    pause 0.3
    show s2 at fo22
    pause 0.2
    hide s2

    show sarita neutral at fi21
    sarita "Aren't you mostly famous for your social media… things?"   
    show stephanie smile at fi22
    stephanie "Yup! You know, I spent half my semester break raising up more of my followers." 
    show sarita nervous at s21
    sarita "Is that so…"

    "A wave of loneliness washed over me as I listened to Steph's babbling."

    

    # --- SCENE 2 --- 
    hide screen location_header with dissolve
    $ quick_menu = False
    stop music fadeout 1.5
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve

    hide sarita with dissolve
    hide stephanie with dissolve
    # hide stephanie

    scene bg classroom with dissolve_scene_full
    play music bg3 fadein 1.0 volume 0.5 loop
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Classroom")
    
    $ quick_menu = True

    "After talking for a while, we went inside the classroom. It was quite loud and vibrant as usual."
    sarita "{i}(Steph's busy talking to her friends…){/i}"
    sarita "{i}*sigh*{/i} I better finish my remaining assignments then…"

    "As I do my assignments, my ears catch the giggling and murmurs from the seats behind me."
    "Curious—I looked behind me and saw three girls directly staring at me and grinning."

    show s2 at t11
    s2 "Isn't she Stephanie's friend?"
    show s1 at t21
    s1 "Friend? You mean her loyal dog?"
    show s3 at t33(0.60)
    s3 "I know right? Tch. She's really annoying."
    show s2 at fo11
    pause 0.3
    hide s2
    show s1 at fo21
    pause 0.3
    hide s1
    show s3 at fo33(0.60)
    pause 0.3
    hide s3

    "I immediately turned my head away and kept my eyes glued to my desk. I told myself it was okay and it would stop soon…"

    scene black with fade

    "A week passed. The whispers didn't stop. If anything, the harsh glares and the bullying only grew worse."
    "They created fake rumors, stole one of my belongings, and even threw a bucket of water at me where Stephanie couldn't see me."
    "All I could do was put my head down and endure it."
    "Then, one day…"
    hide screen location_header with dissolve
    $ quick_menu = False
    stop music fadeout 1.5
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve

    # pls take a pic of this I beg you
    # TODO: scene bg fountain with dissolve_scene_full   
    scene black with fade
    play music bg3 fadein 1.0 volume 0.5 loop
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Garden")
    $ quick_menu = True
    play sound suspense
    stephanie "...ta."
    stephanie "...rita."
    stephanie "Sarita!"
    show sarita neutral at fi21
    show stephanie angry at fi22
    sarita "!"
    show sarita awkward at s21
    sarita "Y-yeah? What were you telling me again?"
    stephanie neutral "Is everything alright? You've been spacing out lately. "
    show sarita neutral:
        ypos 1.30
        easein_cubic .30 ypos 1.20
    menu:
        sarita "I, uh…"
        "I'm okay.":
            show sarita happy with dissolve_character
            sarita "I'm alright, don't worry about me."
            stephanie "Okay. If it's something you can't tell me, I'll let you be."
            show sarita neutral with dissolve_character
            sarita "Mhm."
        "...":
            sarita "..."
            stephanie "Sarita?"
            show sarita happy with dissolve_character
            sarita "It's nothing."
            stephanie "{i}*Sigh*{/i} Whatever it is, I'm not prying into your own personal stuff. But you better tell me when you need help, okay?"
            show sarita neutral with dissolve_character
            sarita "Mhm."

    stephanie "It's your turn for your computer programming session by the way."
    show sarita awkward with dissolve_character
    sarita "Oh, right. I almost forgot, thank you for reminding me."
    show stephanie smile with dissolve_character
    stephanie "Now off you go."

    # scene black with fade
    # TODO: First imagemap that leads to the 2nd floor by taking the upstairs
    # NOTE: This will be discarded as it's just gonna be a waste of time honestly
    # call screen upstairs_to_comlab


label main_ch01_preconflict():
    hide screen location_header with dissolve
    $ quick_menu = False
    stop music fadeout 1.5
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve

    scene bg comlab with dissolve_scene_half
    play music bg3 fadein 1.0 volume 0.5 loop
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Computer Lab")
    
    $ quick_menu = True
    "Ironically, I was too early so there were only a few people in the computer lab."
    "While browsing through the computers, I saw one where its screen was glowing brightly"
    "I went to the computer and what I saw was…"

    hide screen location_header with dissolve
    hide top_frame with dissolve
    hide bottom_frame with dissolve
    scene cg sarita_lab01 with dissolve_scene_half
    "Fortunately, no one has noticed nor touched the computer at all. It was just sitting there—it's like—it was waiting for me."
    ### TODO: Should show an exclamation bubble or a bell pop up during this specific dialogue
    # - also add "mikudayo" sfx with a bell followed by it
    # play sound miku_ringtone
    "All of a sudden, the sound of vibrations emitted from my phone. Hearing my favourite voiceline from my favourite character {i}Hatsune Miku{/i} with a follow up sound effect of a bell was enough to tell that someone messaged me."
    "My hands reached for my phone."
    scene cg sarita_computer_front with dissolve_cg
    sarita "(An unknown number? Wait…)"
    window hide
    $ reset_phone_data()
    $ phone_start()
    # Params: sender, msg, channel_name
    $ send_phone_message(msgr_name, "How are you doing, Sarita?", "themessenger", do_pause=False)
    play sound notif_wonderhoy
    $ phone_pause(0.85)
    "!"
    show screen phone_ui with moveintop
    # NOTE: Instead of an exclaation mark in a dialogue, maybe show a exclamation sticker instead.
    # Params: preview_msg, msg_sent, action (Call/Jump)
    window hide
    $ present_phone_choices([
        ("How do you know my name?", None, Jump("msgrintro_firstchoice")), 
        ("Who are you?", "Who is this? A classmate of mine? A stalker?", Jump("msgrintro_secondchoice"))
        ], "themessenger")

label msgrintro_firstchoice:
    $ send_phone_message(msgr_name, "I'm afraid that will be none of your business.", "themessenger")
    jump msgrintro_aftermath
    return

label msgrintro_secondchoice:
    $ send_phone_message(msgr_name, "Calling me a stalker… that hurts me you know.", "themessenger")
    $ send_phone_message(msgr_name, "Though, I guess you could say that.", "themessenger")
    jump msgrintro_aftermath
    return

label msgrintro_aftermath:
    $ send_phone_message(msgr_name, "Either way, I did message you out of nowhere and I do apologize for that.", "themessenger")
    $ present_phone_choices([
        ("What's your motive?", "What's your purpose for messaging me?", None)
        ], "themessenger")
    $ send_phone_message(msgr_name, "It's not a big deal. I've seen you get bullied by those girls and I just want to say that I've experienced being bullied by them before. I ended up getting suspended for one week, yet they were free. Life's pretty unfair isn't it?", "themessenger")
    $ send_phone_message(phone_config["phone_player_name"], "...and?", "themessenger")
    $ send_phone_message(msgr_name, "Well, I just want to help you that's all. Look, I got the credentials on one of their accounts. In fact, I know what they're planning for you next.", "themessenger")
    $ send_phone_message(phone_config["phone_player_name"], "What do you want me to do?", "themessenger")
    $ send_phone_message(msgr_name, "It's quite simple. I'll let you in their group chat and do whatever you want to do with it. Report them, harass them, spread the rumors—I'll let you be. As long as you agree with helping me destroy their pride and make them suffer the way they've made us suffer. So, what do you say?", "themessenger")
    $ present_phone_choices([
        # Pre bad ending
        ("Fine, I'll do it.", "...sure. I'll do it.", Jump("pre_badending_choices")), 
        # Pre good ending
        ("(Ask him how to get in)", "Can I ask a question first? How would you exactly let me in their group chat?", Jump("pre_goodending_choices")), 
        # Pre neutral ending
        ("I need to think about it.", "Give me time to think about it first...", Jump("pre_neutralending_choices"))
        ], "themessenger")

# ---------------------------
label pre_badending_choices:
    $ send_phone_message(msgr_name, "Good... good. I knew I'd count on you.", "themessenger")
    $ send_phone_message(msgr_name, "For starters, you have to login your account with this link first and I'll let you in.", "themessenger")
    $ send_phone_message(msgr_name, "https://facebook.net/login/13ab2wra20aivnk6qlea?register=", "themessenger")
    $ send_phone_message(msgr_name, "It's safe no worries. I'm not evil enough to trick you, am I right?", "themessenger")
    $ send_phone_message(phone_config["phone_player_name"], "Alright...", "themessenger")
    jump pre_bad

label pre_goodending_choices:
    $ send_phone_message(msgr_name, "I'll be dropping a link for you to log in, then you will get automatically added to their group. Simple as that.", "themessenger")
    $ send_phone_message(msgr_name, "Why? Got any problems?", "themessenger")
    pause
    hide screen phone_ui with moveoutbottom
    $ phone_end()
    sarita "(That's already suspicious on its own… What should I do?)"
    window hide
    # TODO: Please do this I swear
    menu:
        "(Ignore the unknown number)":
            sarita "(I think it'd be better if I ignored this.)"
            $ renpy.sound.play("audio/assets/images/phone/receive.mp3", channel="sound")
            # NOTE: I think we make the the exclamation sticker(?) appear here again just for dramatic effect
            sarita "!"
            $ phone_start()
            show screen phone_ui
            window hide
            $ send_phone_message(msgr_name, "Ah ah. Don't even think of running away now.", "themessenger")
            $ send_phone_message(msgr_name, "You already agreed. There's no turning back now.", "themessenger")
            window show
            sarita "(Since when did I agree?)"
            sarita "(Are they just purposely dumb?)"

        "(Screenshot the whole conversation and report it to the ICT administrator)":
            sarita "(If they are ever here, I need to keep my composure and pretend that I'm going to the bathroom.)"
            "After going outside, I screenshotted the whole conversation and I immediately ran as fast as I could to report the whole conversation to an ICT administrator."
            "They told me that they will pinpoint the suspect as soon as possible and I should not be worried anymore."
            jump good_ed


    # $ present_phone_choices([("(Screenshot the whole conversation and report to the ICT administrator)", None, Jump("sarita_reports")), ("", None, Jump())], "themessenger")
    
label pre_neutralending_choices:
    $ send_phone_message(msgr_name, "Why the sudden hesitation? Don't tell me you're siding with them?", "themessenger")
    jump pre_neutralending_choices02


label pre_neutralending_choices02:
    $ choices = [
        ("Alright, fine. I'll help you.", None, Jump("s_helps")), 
    ]

    python:
        if not s_curious_done:
            choices.insert(0, ("Can't you just do it yourself?", None, Jump("s_curious")))
        if not s_doubts_done:
            choices.insert(0, ("What if I don't agree?", "...and what If I don't agree with your plan?", Jump("s_doubts")))
        if s_doubts_done:
            choices.append(("How would you let me in?", "How would you let me in their group chat?", Jump("s_hesitates")))

    $ present_phone_choices(choices, "themessenger")
    return

# -----------------------------
label s_curious:
    $ send_phone_message(msgr_name, "You do know that I would immediately get caught and be kicked out of this school if I ever report this right?", "themessenger")
    $ send_phone_message(msgr_name, "I stole one of the girls' accounts and read their chats without consent. Do you think they'd let me off easily?", "themessenger")
    $ send_phone_message(msgr_name, "Look, I get it if you don't trust me. But you're going to keep getting hurt, as well as the other victims if we don't do something now.", "themessenger")
    sarita "(That's true...)"
    window hide
    $ s_curious_done = True
    jump pre_neutralending_choices02
label s_doubts:
    $ send_phone_message(msgr_name, "Surrrrreeeelly you would—won't you?", "themessenger")
    $ send_phone_message(msgr_name, "Well, if there was ever a chance that you may not agree, you're going to keep getting hurt as well as the other victims. Don't you think about yourself and others?", "themessenger")
    $ s_doubts_done = True
    jump pre_neutralending_choices02
label s_hesitates:
    $ send_phone_message(msgr_name, "'ll be dropping a link for you to log in, then you will get automatically added to their group. Simple as that.", "themessenger")
    $ phone_pause(2.5)
    $ send_phone_message(msgr_name, "No need to fear as the link is safe. Trust me.", "themessenger")
    sarita "(It is definitely not safe...)"
    window hide
    $ send_phone_message(phone_config["phone_player_name"], "I changed my mind… This… this is wrong. I can't just invade their privacy and expose them. I… I don't want to be like them. And I don't want to be like you either.", "themessenger")
    $ send_phone_message(msgr_name, "You don't know anything, sarita. They used you, manipulated you, and always picked on you. A small thing like this isn't even that bad compared to what you have experienced.", "themessenger")
    $ phone_pause(3)
    $ send_phone_message(msgr_name, "Did you know that your so-called \"best friend\" planned all this? She was pretending to be your best friend. She hates you, she's jealous of you. If you don't do this, you'll surely regret this.", "themessenger")
    $ phone_pause(3.2)
    $ send_phone_message(phone_config["phone_player_name"], "Even if that is true, you're just using me as an excuse to commit horrible acts against them.", "themessenger")
    $ phone_pause(3.2)
    $ send_phone_message(phone_config["phone_player_name"], "Besides, there's also a possibility that what you're going to send won't be legitimate and could potentially steal my information if I were to insert my credentials.", "themessenger")
    $ phone_pause(4.0)
    $ send_phone_message(phone_config["phone_player_name"], "Hello???", "themessenger")
    pause 1.0
    hide screen phone_ui with moveoutbottom
    $ phone_end()
    jump pre_neutral
    
label s_helps:
    $ send_phone_message (msgr_name, "I'll drop a link for you to log in, which will automatically add you to their group chat. Simple as that, right?", "themessenger")
    $ send_phone_message(phone_config["phone_player_name"], "...alright.", "themessenger")
    $ send_phone_message (msgr_name, "That's great to know. I knew I'd trust you.", "themessenger")
    $ send_phone_message (msgr_name, "Here's the link.", "themessenger")
    $ send_phone_message (msgr_name, "https://facebook.net/login/13ab2wra20aivnk6qlea?register=", "themessenger")
    jump pre_bad
