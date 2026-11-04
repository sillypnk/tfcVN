label main_ch01:
    with dissolve_scene_full
    stop music

    # --- SCENE 1 --- 
    sarita "W-wait for me, steph!"
    stephanie "Come on! you can be faster than that!"

    scene bg school_frontview with dissolve_scene_full
    play music bg1 fadein 1.0 loop

    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("School Gate")

    show sarita awkward at t21
    sarita "{i}*huff *huff*{/i} G-good morning."
    show stephanie smile at t22
    stephanie "Good morning~"
    stephanie "Look at this lighting, Sarita! The morning wind is doing wonders for my hair. Perfect for a quick story post!"
    show sarita awkward at s21
    sarita "A-ah... yeah, it looks really nice on you."

    "Stephanie and I have been best friends since kindergarten... but standing next to her, I always feel like an accidental background extra."

    show stephanie neutral with dissolve_character
    stephanie "Did you wake up well?"
    show sarita at t21
    show sarita neutral with dissolve_character
    sarita "Y-yeah."

    show sarita at fo21
    hide sarita
    show stephanie at fo22
    hide sarita
    show s1 at t21
    # s(1-3) means silhouette/s. These silhouettes are defined at definitions.rpy.
    s1 "Wait, isn’t that THE Stephanie?" 
    show s2 at t22
    s2 "Wait, really?! It is her! Oh my god, I’m such a big fan!" 
    show s1 at fo21
    hide s1
    show s2 at fo22
    hide s2

    "I slowly lower my head as I listen to the whispers and cheers surrounding us from every direction." 

    show sarita neutral at fi21
    sarita "You're really popular, Steph." 
    show stephanie smile at fi22
    stephanie "Hehe, of course I am! You know, I spent half my break keeping up with my social media followers." 

    "Stephanie gently slides her fingers into my palm and locks her grip with mine. Her hand feels warm and reassuring." 

    show stephanie neutral with dissolve_character
    stephanie "Hey, sarita?"
    sarita "Yeah?"
    stephanie "Are you nervous for your first day?"
    show sarita awkward with dissolve_character
    sarita "I-I am, but I am also pretty excited."
    show stephanie happy with dissolve_character
    stephanie "Don't worry! You've got this. I believe in you."
    show sarita happy with dissolve_character
    sarita "Thank you, steph."


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

    "We went inside our assigned classroom. It was quiet at first... but that didn't last long."
    "The moment break time arrived, the room erupted into noise." 

    show stephanie happy at t31
    stephanie "Mariaaaa! Long time no see!"
    show maria happy zorder 3 at t32
    maria "Stephie! It really has been a long time hehe. How have you been?"
    stephanie "You know me. I’ve been taking care of my beautiful appearance since the vacation started!"
    stephanie neutral "Ugh, dad didn’t want me to go to south korea thoooooough~"
    maria neutral "Why’s that?"
    stephanie "He said he was too busy with the upcoming local elections, so I couldn't go anywhere for fun." 
    show gabriel smile zorder 2 at t33
    gabriel "Yoooo! What are we talking about?"

    "I hadn't realized, stephanie's middle school friends enrolled here as well."

    show stephanie happy zorder 4 at h31
    stephanie "Gabriel? Long time no see!"
    show gabriel happy zorder 2 at h33
    gabriel "Hahahaha! Sure is!"
    show stephanie smile with dissolve_character
    stephanie "You're really loud as usual."
    show gabriel smile with dissolve_character
    gabriel "You don't say?"
    show gabriel neutral with dissolve_character
    gabriel "?"
    show gabriel smile with dissolve_character
    gabriel "Oh, yo, Sarita! Didn't even see you sitting there behind Steph. What’s up?" 
    # show sarita awkward zorder 1 at t21
    sarita_s awkward "Oh-uh, I'm okay. Just listening."
    maria "So, Steph, what did you and Sarita do during the break?"
    show stephanie neutral with dissolve_character 
    stephanie "Oh, we just hung out at some local spots. Nothing special."
    show maria happy zorder 3 at h32
    maria "Aww, local dates?"
    show stephanie worried with dissolve_character
    show gabriel happy zorder 2 at h33
    gabriel "Yiiiiiiiie~"
    show stephanie angry zorder 4 at rage(300)
    stephanie "Gab… You…"
    show gabriel smile with dissolve_character
    show maria neutral with dissolve_character
    gabriel "Whoopsies. See y'all."
    show gabriel at rhide
    hide gabriel
    pause 0.8
    # gabriel hussed
    stephanie "Come back here gabriel!!!"
    show stephanie at rhide(.50)
    hide stephanie
    pause 0.5
    # screen shakes and loud sfx ig
    # with vpunch
    # pause 0.8
    # with hpunch
    # pause 0.4
    # with vpunch
    # TODO: Awkward expression
    # show maria awkward at dissolve_character
    show maria smile with dissolve_character
    maria "Oh boy, they're going to cause trouble again. I'm gonna go ahead and stop them, see ya later sarita."
    sarita_s "O-okay."
    show maria at hide
    hide maria
    "..."
    "They… are really loud as always."
    pause 0.7

    # --- SCENE 3  --- 
    show s1 at t11
    s1 "Okay class, take your seats. We're starting our introductions."

    hide screen location_header with dissolve
    $ quick_menu = False
    scene black with fade
    stop music fadeout 0.5
    hide top_frame with dissolve
    hide bottom_frame with dissolve

    scene black with fade
    centered "{size=50}{color=#ffffff}After Introductions{w=0.5}.{w=0.5}.{w=0.5}.{/color}{/size}"

    $ quick_menu = True
    scene bg classroom with dissolve_scene_full
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Classroom")

    show gabriel happy at t31
    gabriel "Man~ I was sweating bullets during my turn!"
    show maria happy at t32
    maria "Haha, I had to cover my mouth because you kept stuttering!"
    show gabriel neutral at s31
    gabriel "Guh...!"
    show stephanie neutral at t33
    stephanie "That's to be expected. It's the first day of school, after all."
    stephanie "By the way... Sarita, you were shaking pretty hard earlier. Are you feeling alright?"
    sarita_s awkward "Y-yeah... My heart was just pounding the second they called my name..."
    show maria neutral with dissolve_character
    maria "Steph's the only one who didn't flinch."
    show stephanie smile with dissolve_character
    stephanie "Well, I'm used to being in front of people."

    # Screen tint or subtle vignette effect to show internal isolation
    show vignette onlayer top at vignette

    "While we were talking, my ears caught the quiet giggling and murmurs from the seats behind us."

    show stephanie at hide
    hide stephanie
    show maria at hide
    hide maria
    show gabriel at hide
    hide gabriel

    s1 "That's them! Stephanie and her group!"
    s2 "I know, I follow her art account! But wait... who's the white-haired girl with them?"
    s3 "Oh, that's the weird girl who turned bright red and froze during her intro, lol."
    s1 "Yikes. She looks like a total outcast clinging to Steph..."

    "I kept my eyes glued to my desk and endured every comment. I told myself it was just first-day talk... that it would stop soon."

    # --- SCENE 4 --- 
    hide screen location_header with dissolve
    $ quick_menu = False
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve
    hide vignette onlayer top with dissolve

    scene black with fade
    $ quick_menu = True
        
    "A week passed. The whispers didn't stop. If anything, the harsh glares and subtle insults only grew worse."
    "All I could do was put my head down and endure it."

    scene bg classroom with dissolve_scene_full
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Classroom")

    show stephanie smile at t11
    stephanie "Sarita, do you want to grab lunch with us today?"
    show stephanie neutral with dissolve_character
    stephanie "...Sarita?"

    "Stephanie steps closer and taps my shoulder."

    stephanie "Hey, are you okay? You look pale."
    sarita_s awkward "Y-yeah! I'm fine... just tired. Shall we go?"
    stephanie "Hm, If you say so…"

    show stephanie at hide
    hide stephanie

    show vignette onlayer top at vignette
    s1 "Tch. She's always tailing behind Stephanie like a lost puppy."
    s2 "Right? It's so annoying to watch."
    s3 "Hey... girls, I have an idea."

    scene black with fade
    hide vignette onlayer top with dissolve

    # TODO: CG #1 —— Sarita looking through her things at her bag.
    # scene cg sarita_01 with dissolve
    sarita "..."
    sarita "Wait... where's my project?"
    "I'm pretty sure I brought it before I left home…"

    sarita "H-hey, Steph...?"
    stephanie "What's up?"
    sarita "Have you seen my project?"
    # She's checking her own screen without looking up
    stephanie "Hmm? Which project are you referring to?"
    sarita "Our science project."
    stephanie "Well, no. Did you leave it somewhere else or—"
    sarita "No! I checked everywhere! My bag, under the desk... it's gone!"
    stephanie "Okay, okay, calm down now. You can just make it again since the deadline is still tomorrow. I can help you."

    sarita "No, sarita! You don't understand! I worked hard on it! I worked tirelessly just to finish it! I can't just… I can't just lose it…!"

    "We asked the rest of the class, but everyone claimed they didn't see a thing."
    "And then, across the room, I saw those three girls in the back row."
    "Behind their fake sympathetic expressions and hollow grins, I finally know the truth."
    "They took it... and Steph didn't even notice it."


    hide screen location_header with dissolve
    $ quick_menu = False
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve
    hide vignette onlayer top with dissolve

    ## ========================================== 
    ## =============== ACT II =================== 
    ## ========================================== 
    scene black with fade
    $ quick_menu = True
    scene bg comlab with dissolve_scene_full
    show top_frame at top_bar_pos
    show bottom_frame at bottom_bar_pos
    show screen location_header("Computer Lab")

    "A week passed after I lost the one I worked hard for. It was a great thing that I made another one and was still able to pass. But I can't forgive them for it."
    "Anyways, our first class today is programming. The computer lab was quiet, filled only with the steady clicking of mechanical keyboards."
    "Apparently, the computer that I was using yesterday was taken by a classmate of mine. So I ended up sitting to stephanie's computer."

    sarita_s "Huh...?"

    hide screen location_header with dissolve
    $ quick_menu = False
    scene black with fade
    hide top_frame with dissolve
    hide bottom_frame with dissolve

    # TODO: CG #2 —— Sarita staring at sarita's computer
    scene cg sarita_lab01 with dissolve_cg
    $ quick_menu = True
    "The monitor lit up. It seems like she forgot to log out her accounts. On the screen was stephanie's primary social media accounts and a personal cloud storage."
    sarita "{i}*mumbling*{/i} She was so rushed to meet her fans after her turn that she didn't even sign out."
    "My fingers hovered over the keyboard. Her entire private life was wide open right in front of me."
    sarita "{i}*mumbling*{/i} I could log her out safely... or check her messages and see what she really says about me behind my back."

    "All of a sudden, the sound of vibrations emitted from my phone. Hearing the song from my favorite artist 'wave to earth' was enough to tell that someone was indeed calling me."

    "My hands reached for my phone."
    sarita "...an unknown number? They might have made a mistake. I better tell them off."

    $ caller_name = "???"
    $ quick_menu = False
    scene black with dissolve_cg
    window hide
    show screen chat_logs with dissolve_scene_half

    snvl "H-hello…?"
    caller "Well, well. What do we have here? How pitiful of you, sarita."
    snvl "W-Who are you and how did you know my name?!"
    caller "Calm down. I'm just a friend who sees how much you suffer while that 'best friend' of yours shines."
    caller "Now, look at the screen. One click, and you can give her a taste of her own medicine."
    snvl "I… I shouldn't…"
    caller "I know, I know. You're her 'best friend'"
    caller "How hilarious. Does she even deserve you? She looked like she barely cared when your project was missing. Making a new one she says? Haha! It must be nice having someone to make your project isn't it?"
    snvl "W-what gives you the right to—?!"
    caller "Oh no no, don't be such a hypocrite now. You wanted her out of your life didn't you?"

    nvl_n "Every insult from the past two weeks echoed in my head. My chest burned with resentment."

    snvl "How...Do you know all of that?"
    caller "I'm afraid that'd be out of your business."
    caller "So? What are you going to do, sarita?"
