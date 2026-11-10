# sarita gets phished and gives her account to the unknown number
label pre_bad():
    hide screen phone_ui with moveoutbottom
    "After inserting my credentials into the link, it redirect me to a blank page."
    "That's when I realized I have been tricked. The link was fake, and I didn't noticed."

    show screen phone_ui with moveinbottom
    $ send_phone_message(phone_config["phone_player_name"], "You tricked me! Was that your intention all along!?", "themessenger")
    $ send_phone_message(msgr_name, "Well, it was your fault for trust a suspicious in the first place <emoji_sob>", "themessenger", 3)
    sarita "(Now, I messed up big time...)"
    $ send_phone_message(msgr_name, "Since I have gotten your personal information. I am moving on to Stephanie's account.", "themessenger")
    $ send_phone_message(msgr_name, "Don't worry though, if you give me Stephanie's account. I can let you free and act like nothing happened.", "themessenger")
    "Having no choice, I've decided to give out Steph's account. Fortunately, the unknown message did actually let go of it and I immediately had to change my private information."
    "But..."
    hide screen location_header with dissolve
    $ quick_menu = False
    stop music fadeout 1.5
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve
    jump bad_ed
    
# sarita doesn't get phished but doesn't log out steph's account
label pre_neutral():
    "After not receiving any more responses from the unknown sender, my gaze stayed locked on the monitor as the time passed by."
    "Thinking about the possibility of Stephanie pretending to be my friend made me rethink my decisions."
    "I've known her for years, but the moment I noticed that she's been avoiding me these past few days made me realize that perhaps, I did something bad."
    sarita "(Why is my life like this…)"
    sarita "(I totally forgot, I have an upcoming class next. Should I just leave this…?)"
    menu:
        "Knowing the possibility that Stephanie may not like me anymore, I have a feeling that she deserves to be exploited somehow, but…"

        "(Log Stephanie's accounts before going out.)":
            sarita "She might not like me anymore, but it doesn't really mean that I could just leave this as it is."
            sarita "Maybe I'll just report the conversation I had and tell Stephanie about her session left open."
            hide screen location_header with dissolve
            $ quick_menu = False
            stop music fadeout 1.5
            scene black with fade
            hide top_frame with dissolve
            hide bottom_frame with dissolve
            jump good_ed

        "(Leave the computer as-is and rush out.)":
            sarita "..."
            sarita "I'll just leave here as it is, so that Stephanie can just come back to it."
            hide screen location_header with dissolve
            $ quick_menu = False
            stop music fadeout 1.5
            scene black with fade
            hide top_frame with dissolve
            hide bottom_frame with dissolve
            jump neutral_ed

####################
#### BAD ENDING ####
####################
label bad_ed():
    # scene black with fade
    # TODO: please do the centered text with the black background or something
    # show text "One week later…" at truecenter
    # pause 0.85
    # hide text with dissolve

    scene bg school_frontview with dissolve_scene_full
    # TODO: Change the music or something
    play music bg1 fadein 1.0 loop
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("School Entrance")

    "The sun was bright, but the air felt heavy as I walked into school the next morning."
    "Crowds of students were gathered around—whispering and holding up their phones."
    "Then… a school security staff member and an ICT Administrator walked up to us."     

    s4 "Sarita, correct? We need you to come to the Principal's office immediately. You too, Stephanie."
    "I could hear the beat of my heart—thumping so loudly. The whole world felt like it stopped the moment I heard my name."
    show sarita nervous at t31
    show stephanie neutral at tcommon(650)
    sarita "B-but why?"
    s4 "Stephanie reported to us that someone had just used her account, and that she couldn't use it anymore. She had admitted that she left her session open last week."
    s4 "Coincidentally, our network security logs showed signs that a {b}certain{/b} person was using the active computer to access Stephanie's accounts without authorization. That's how her information was stolen."
    s4 "Now, that {b}someone{/b} is none other than you, Sarita."
    show stephanie base_03 worried at hop(650)
    stephanie "Sarita…? You… you were the one who did this to me? But... why?"
    sarita "No! Steph, listen to me! There was a weirdo—someone messaged me —t-they threatened me!"
    stephanie "You had access to my open account, you had other options yet you gave my data away? I trusted you, Sarita. I trusted you! You were my best friend! You're a traitor!"
    hide stephanie with dissolve_character
    sarita "Steph—!"

    hide screen location_header
    hide top_frame
    hide bottom_frame 
    with dissolve
    $ quick_menu = False
    scene cg badending with dissolve_cg
    $ quick_menu = True
    "Stephanie turned away, tears streaming down her face. She walked away, surrounded by her angry fans who glared at me with pure hatred." 

    "By giving in to revenge and clicking that fake link, I lost everything."
    "That 'person' used me as a scapegoat. In the end, all the traces pointed straight to me."

    scene black with fade
    "My student account was suspended, I faced formal disciplinary action, and my friendship with Stephanie was broken beyond repair."
    "In the end, I dropped out of school as I couldn't handle the harsh treatment and the endless glares."
    jump endgame



####################
## NEUTRAL ENDING ##
####################
label neutral_ed():
    scene black with fade
    # TODO: please do the centered text with the black background or something
    show text "One week later…" at truecenter
    pause 0.85
    hide text with dissolve
    stop music fadeout 0.5

    scene bg classroom with dissolve_scene_full
    # TODO: Change the music or something
    play music bg2 fadein 1.0  loop
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Classroom")
    show sarita neutral at t21
    sarita "Steph…"
    show stephanie neutral at t22
    stephanie "Hm? What is it?"
    sarita "Can we talk for a moment?"
    show stephanie smile with dissolve_character
    stephanie "Oho~ do you have a crush?"
    show stephanie happy with dissolve_character
    stephanie "Or maybe—maybe you won or you scored higher on a test???"
    show stephanie smile with dissolve_character
    stephanie "Oh, it's defi—"
    sarita "No… Steph. It's… it's something serious."
    show stephanie neutral with dissolve_character
    stephanie "Oh…. Tell me about it."
    sarita "Will you not be mad…?"
    show stephanie smile with dissolve_character
    stephanie "If it's not stealing my snacks, I won't. Just trust me!"

    # hide screen location_header with dissolve
    # hide top_frame with dissolve
    # hide bottom_frame with dissolve
    hide screen location_header
    hide top_frame
    hide bottom_frame 
    with dissolve
    hide sarita
    hide stephanie 
    with dissolve_character
    window hide
    $ quick_menu = False
    scene black with fade
    # TODO: Again. Black screen with text on it.
    centered "I told Stephanie the encounter that I had with the unknown messenger and what they were plotting…"
    extend "Except I didn't tell her what the unknown messenger's been talking about her."

    scene bg classroom with dissolve_scene_half
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Classroom")
    $ quick_menu = True
    show sarita neutral at t21
    show stephanie neutral at t22
    sarita "...and yeah, that's the gist of it."
    stephanie "So there was a weirdo who randomly messaged you and tried to convince you—by saying you can expose the plan of those girls?"
    stephanie "..."
    show stephanie angry with dissolve_character
    stephanie "Sarita, you… You could have just told me everything right from the start."
    # TODO: New expression for sarita here (different kind of nervous)
    sarita "B-but you were ignoring me! Aren't you the one who's at fault here?"
    stephanie "What are you talking about? I was busy with the student council stuff! My mind was full of nothing but papers and events. I couldn't spend my time with you and I do apologize for that okay!?"
    sarita "(!)"
    # TODO: New expression for sarita here (Sad expression or something)
    sarita "(Oh… So I messed up.)"
    show stephanie base_02 worried with dissolve_character
    stephanie "Don't tell me you misunderstood everything…"
    show sarita awkward at s21
    sarita "I-I did."
    # TODO: New expression for stephanie here (disappointed or something)
    # show stephanie base_02 disappointed with dissolve_charasater
    stephanie "{i}Sigh{/i} I can't believe you left my session open and didn't even bother to log it all out. It was rather a good thing that I reported it immediately after an ICT administrator told me. I couldn't have imagined the worst."
    show sarita neutral at t21
    sarita "..."
    show stephanie base neutral with dissolve_character
    stephanie "..."
    # show stephanie base_02 disappointed with dissolve_charasater
    stephanie "You know what, come here. I forgive you."
    sarita "I'm sorry… I'm so sorry."

    # TODO: New CG ending, sarita is hugging stephanie while crying because she's a crybaby googoogaagaa
    "I buried my face in her shoulder, my fingers clawing as a sob tore its way out of my throat, and tears soaking the shoulder of her uniform."
    "I avoided falling for the illegitimate link. However, I still exposed Stephanie to danger by leaving her accounts opened."
    jump endgame

###################
### GOOD ENDING ###
###################
label good_ed():
    scene black with fade
    # TODO: please do the centered text with the black background or something
    show text "One week later…" at truecenter
    pause 0.85
    hide text with dissolve

    scene bg school_frontview with dissolve_scene_full
    # TODO: Change the music or something
    play music bg1 fadein 1.0 loop
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("School Entrance")

    "While Stephanie and I were talking near at the school entrance. A woman suddenly approached us with a tablet in hand, smiling."
    sarita "(Based from her ID, she seems like an ICT administrator...)"
    sarita "(Oh, is this about the report I did last week?)"
    show sarita neutral at t21
    show stephanie neutral at t22
    s4 "Stephanie, sarita. Am I correct?"
    stephanie "Yes, maam."
    s4 "I've got news to tell you both."
    s4 "Thanks to sarita's quick reporting last week, we were able to block a malicious phishing domain across the entire campus Wi-Fi network."
    s4 "She also manually logged off Stephanie's unattended session where she left her accounts opened before anyone could exploit it."
    # TODO: New expression for stephanie (surprised / shocked?)
    stephanie "Sarita… You did all of that?"
    s4 "She saved your accounts. You owe her a big thank you—and a lesson to sign out at a public device everytime."
    "Stephanie remained standing as she looked at me with wide eyes before pulling me into a tight hug."
    hide screen location_header 
    hide top_frame
    hide bottom_frame 
    with dissolve
    scene cg goodending with dissolve_scene_full
    sarita "S-stephanie?"
    stephanie "I knew I'd trust you!"
    sarita "...you know I only did the good deed, right?"
    sarita "Also, you really gotta stop forgetting logging out your accounts."
    stephanie "Note taken!"
    "After that moment, I told everything to Stephanie how everything happened."
    # Jump to endgame where it will show the explainer explaining the ending or something...
    jump endgame