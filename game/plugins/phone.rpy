# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                           © 2026 Kesash                                                   ║                                    
# ║                          All Rights Reserved (except where I say otherwise).                              ║  
# ║         (Also, these copyright blocks take forever to make, someone make a tool c: please)                ║                                                                          
# ║                                                                                                           ║              
# ║                              This code is free to use in actual projects.                                 ║                                                           
# ║                          Games, apps, mods, cursed visual novels - go for it.                             ║                                                                   
# ║                                                                                                           ║              
# ║                                                CONDITIONS:                                                ║                                            
# ║                            - You MAY use this code in a project of your own.                              ║                                                                
# ║                      - You MAY NOT redistribute this code by itself, modified or not.                     ║                                                                               
# ║         - You MAY NOT repackage it as a standalone library, template, or "phone system but better".       ║                                                                                                          
# ║                    - If someone is downloading *just* this code, you're doing it wrong.                   ║                                                                                   
# ║                                                                                                           ║              
# ║                       In short: ship something with it. Don't just re-upload it.                          ║                                                                         
# ║                                                                                                           ║              
# ║                                               CREDIT:                                                     ║                      
# ║                           Keep this notice intact and visible in the source.                              ║                                                                 
# ║                               No sneaky deletions. No "oops I forgot".                                    ║                                                       
# ║                                                                                                           ║              
# ║                                             LIABILITY:                                                    ║                         
# ║                                   This code is provided "as is".                                          ║                                             
# ║                                       I am NOT responsible for:                                           ║                                        
# ║                                        - Bugs                                                             ║                     
# ║                                        - Broken saves                                                     ║                             
# ║                                        - Bricked games                                                    ║                              
# ║                                        - Emotional damage                                                 ║                                 
# ║                                        - Whatever unholy thing you choose to build with it                ║                                                                  
# ║                                                                                                           ║              
# ║                                   If it explodes, that's on you.                                          ║                                            
# ║                                                                                                           ║              
# ║                                           COMMERCIAL USE:                                                 ║                             
# ║                             Yes, you can use it in commercial projects.                                   ║                                                         
# ║                              No, that does not mean I owe you support.                                    ║                                                       
# ║                 If you're making bank and feeling generous, I won't stop you from saying hi.              ║                                                                                          
# ║                                                                                                           ║              
# ║                                                  TL;DR:                                                   ║                    
# ║                                           Use it in a real project                                        ║                                         
# ║                                                Keep the credit                                            ║                                
# ║                                           Don't redistribute it alone                                     ║                                            
# ║                                                 Don't blame me                                            ║                               
# ║                                                                                                           ║              
# ║                                                  DISCLAIMER:                                              ║                         
# ║                              This code is provided as a technical tool only.                              ║                                                             
# ║                        Any content, themes, or material produced using it are solely the                  ║                                                                               
# ║                                       responsibility of the end user.                                     ║                                             
# ║                       Use of this code does not constitute endorsement of any resulting work.             ║
# ║                                                                                                           ║
# ║                    Also, if you do use it, please tell me... I want to play some games :)                 ║
# ║                                  (Even if they are weird, I don't judge)                                  ║
# ║                                                                                                           ║
# ║                                  Yes i tried to center all the text                                       ║
# ║                                         No it did not go well                                             ║
# ║                                                                                                           ║      
# ║                                         Respect the code. Pet the fox.                                    ║                                      
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║                                                                                                           ║   
# ║                                            /\   /\                                                        ║   
# ║                                           //\\_//\\     ____                                              ║        
# ║                                           \_     _/    /   /                                              ║        
# ║                                            / * * \    /^^^]                                               ║       
# ║                                            \_\O/_/    [   ]                                               ║       
# ║                                             /   \_    [   /                                               ║       
# ║                                             \     \_  /  /                                                ║      
# ║                                              [ [ /  \/ _/                                                 ║     
# ║                                             _[ [ \  /_/                                                   ║     
# ╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════╣
# ║  Want help coding your game? Reach out! Just message me on itch :) or Discord at kesash_                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╝

#####################################################
#### 3400 lines of stress. AKA the phone system ##### 
#####################################################

# I get why you might be here. Curiosity? To learn? Maybe to change something. BUT BE WARNED, this was my first every renpy project. 
# When I started this I had to google how to bring up a screen.... (but hey, look at me now!)
# Like there are things in here that even I don't know if they actually do anything anymore... the initial release was like 300 lines of code? Then FEATURE BLOAT, and here we are, well over 2000. 
# This whole thing is not noted correctly, at all, the functions are all in random orders, like it's a mess. But it's a mess that I made so I just 'know' where everything is I guess....
# If theres a feature you want then message me on itch (or a comment, cos, ENGAGEMENT) and i'll do my best to add it. Please don't drive yourself mad trying to modify this thing unless you REALLY know what you're doing. 
# If you still want to mess with this monstrosity? Good luck :D 

default typing_dot_cycle = ["", ".", "..", "..."] # Deprecated
default typing_dots = "" # Deprecated
default reusable_index = 99999999999 # Depricated?
default current_conversation = None
default _var_kps_tick_list = []
default _var_kps_phone_timer = 0
default is_typing = False
default persistent.persistent_gallery = []
default phone_data = {}
default persistent.seen_message_threads = {}
default current_contact = None
default click_to_send = True
default var_kps_phone_locked = True
default phone_shell_x = int((config.screen_width - PHONE_INNER_W) / 2)
default phone_shell_y = int((config.screen_height - PHONE_INNER_H) / 2)
$ renpy.music.set_volume(var_kps_notification_volume, channel="kps_phone_notifications")
$ renpy.music.set_volume(var_kps_message_sound_volume, channel="kps_phone_messages")
default _ikps_last_tick_time = 0

screen _kps_phone_tick_screen():
    zorder -99999999
    timer 1.0 repeat True action Function(_kps_phone_tick) 


default phone_screen_bg = "#0f1115"
init python:
    import copy
    import uuid
    import ast
    import textwrap
    import renpy.store as store
    import math # YAY MATH :D
    import time # If only this gave me more of it
    import random
    phone_data = {}
    character_info_for_dialogue = None
    config.overlay_screens.append("_kps_phone_tick_screen")
    _ikps_store_name_cache = {}
    renpy.music.register_channel("kps_phone_notifications", mixer="sfx", loop=False)
    renpy.music.register_channel("kps_phone_messages", mixer="sfx", loop=False)
    messaging_enabled = True
    



    def _kps_phone_tick():
        global _ikps_last_tick_time
        import time
        now = time.time()
        elapsed = now - _ikps_last_tick_time
        if elapsed < 1.0:
            return
        _ikps_last_tick_time = now
        _var_kps_phone_timer = getattr(store, "_var_kps_phone_timer")
        if _var_kps_phone_timer >= 100 * 60 * 60:
            setattr(store, "_var_kps_phone_timer", 0)
        setattr(store, "_var_kps_phone_timer", _var_kps_phone_timer + 1)
        _var_kps_phone_timer += 1
        for item in _var_kps_tick_list[:]:
            if "_base_speed" not in item:
                item["_base_speed"] = item["speed"]
            if _var_kps_phone_timer % item['speed'] != 0:
                continue
            if item.get("condition"):
                if not eval(item["condition"], {}, vars(store)):
                    continue
            convo_cond = item["conversation"].get("condition", None)
            if convo_cond:
                if not eval(convo_cond, {}, vars(store)):
                    continue
            send_function = kps_notif_if_sent if item.get("notif", True) else kps_send_next_if_pending
            if send_function(item['conversation'], *item['dont_send_keys']):
                base = item["_base_speed"]
                varience = item.get("varience", None)
                if varience is None:
                    longest = math.ceil(base * _var_kps_tick_speed_varience)
                elif varience == 0:
                    longest = base
                else:
                    longest = math.ceil(base * math.ceil(varience))
                item["speed"] = random.randint(base, longest)
            elif item['perm'] == False:
                _var_kps_tick_list.remove(item)
                renpy.retain_after_load()


#### USER FUNCTIONS ####
    
    def kps_add_contact_to_tick_list(conversation: dict, speed: int, notif: bool, perm: bool, conditions: str, *dont_send_keys, varience: int=None):
        for item in _var_kps_tick_list:
            if item.get("conversation") == conversation:
                item["speed"] = speed
                item["perm"] = perm
                item["dont_send_keys"] = dont_send_keys
                item["condition"] = conditions
                item['notif'] = notif
                item['varience'] = varience
                return False  

        _var_kps_tick_list.append({
            "conversation": conversation,
            "speed": speed,
            "perm": perm,
            "dont_send_keys": dont_send_keys,
            "notif": notif,
            "condition": conditions,
            "varience": varience
        })
        return True  


    def kps_remove_contact_from_tick_list(conversation) -> None:
        global _var_kps_tick_list
        before = len(_var_kps_tick_list)
        _var_kps_tick_list = [
            x for x in _var_kps_tick_list
            if x.get("conversation") != conversation
        ]


##### USER FUNCTIONS #####

    def kps_add_member_to_convo(which_convo: dict, member_name: str, member_data: dict = None) -> None:
        """
        Adds a new member to a conversation.
        If you pass in an existing member you can also use that to change their dict (for things like pfp)
        """
        if not isinstance(which_convo, dict):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_add_member_to_convo()\n"
                "The first parameter must be a conversation dict created with kps_build_conversation()"
            )
        if not isinstance(member_name, str):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_add_member_to_convo()\n"
                "The second parameter must be a string representing the member name"
            )
        if member_data is not None and not hasattr(member_data, "get"):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_add_member_to_convo()\n"
                "The third parameter must be a dict or None"
            )
    
        members = which_convo.get("members", {})
        members[member_name] = member_data or {}
        which_convo["members"] = members
        #print(which_convo["members"])
    
    
    def kps_remove_member_from_convo(which_convo: dict, member_name: str) -> None:
        """
        Removes a member from a conversation.
        """
        if not isinstance(which_convo, dict):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_remove_member_from_convo()\n"
                "The first parameter must be a conversation dict created with kps_build_conversation()"
            )
        if not isinstance(member_name, str):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_remove_member_from_convo()\n"
                "The second parameter must be a string representing the member name"
            )
    
        members = which_convo.get("members", {})
        members.pop(member_name, None)
        which_convo["members"] = members
        which_convo["members"]
    
    
    def kps_rename_member_in_convo(which_convo: dict, old_name: str, new_name: str) -> None:
        """
        Renames a member in a conversation while preserving all member data.
        """
        if not isinstance(which_convo, dict):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_rename_member_in_convo()\n"
                "The first parameter must be a conversation dict created with kps_build_conversation()"
            )
        if not isinstance(old_name, str) or not isinstance(new_name, str):
            raise TypeError(
                "Error: You have passed an incorrect parameter into kps_rename_member_in_convo()\n"
                "The second and third parameters must be strings"
            )
    
        members = which_convo.get("members", {})
        if old_name in members:
            members[new_name] = members.pop(old_name)
        which_convo["members"] = members
        which_convo["members"]





    def kps_open_messaging_screen(which_convo: dict, which_phone: dict = phone_data, disable_back = False) -> None:
        """
        Opens the texting screen directly. 
        Which_convo -> The convesation you would like to open
        which_phone -> Which phone to open it on, will default to last phone opened
        disable_back -> Disable the back button for the convo. If you do this rememeber to re-enable it. 
        """
        

        if not isinstance(which_convo, dict):
            raise TypeError("Error: You have passed an incorrect parameter into kps_open_messaging_screen()\n"
            "The first parameter is the conversation/contact, created with kps_build_conversation()")
        if not isinstance(which_phone, dict):
            raise TypeError("Error: You have passed an incorrect parameter into kps_open_messaging_screen()\n"
            "The second parameter is the phone dict for the phone you wish to open")
        if not isinstance(disable_back, bool):
            raise TypeError("Error: You have passed an incorrect parameter into kps_open_messaging_screen()\n"
            "The third parameter is True/False for disabling the back button on the chat screen")
        store.phone_data = copy.deepcopy(which_phone)
        if disable_back:
            var_kps_show_back_button_contact = False
        # Yeaaaa if you don't set it first it doesn't work, sometimes. I've fought renpy screens for so long 
        # I just gave up questioning things like this. 
        store.current_conversation = which_convo
        renpy.show_screen("dynamic_scrollable_text", current_conversation)
        


    def kps_update_conversation(which_contact: dict, what_conversation: list, conditionals: str = None) -> None:
        """
        Updates the current conversation loaded into the phone for a certain conversation. 

        First parameter is the conversation you wish to update, created with kps_build_conversation()
        Second parameter is the new conversation list you wish to load in. 
        """
        if not isinstance(which_contact, dict):
            raise TypeError("You have passed an incorrect variable into 'update_conversation', the first parameter must be a conversation/contact you created using build_conversation(), or a conversation dict you created manually.")
        if not isinstance(what_conversation, list):
            raise TypeError("You have passed an incorrect variable into 'update_conversation', the second parameter must be a conversation list.")
        which_contact['current_dialogue'] = what_conversation
        new_index_name = get_store_name_of(which_contact['current_dialogue']) + "_index_kps_"
        which_contact['current_index'] = new_index_name
        which_contact['conditions'] = conditionals
        if not hasattr(store, new_index_name):
            setattr(store, new_index_name, 0)

    def kps_get_conversation_index(which_contact_or_convo, return_string = False):
        """
        Will return the value of the index for the current conversation if you pass the conversation dict in
        Will return the value of the index for any conversation if you pass the conversation list in
        Will return the name of the variable holding that index if you pass in return_string = True (Can be used for some advanced things)
        """
        if isinstance(which_contact_or_convo, dict):
            
            if return_string:
                return which_contact_or_convo['current_index']
            else:
                index_name = which_contact_or_convo['current_index']
                try:
                    return getattr(store, index_name)
                except:
                    setattr(store, index_name, 0)
                    return 0
        elif isinstance(which_contact_or_convo, list):
            list_name = get_store_name_of(which_contact_or_convo)
            if not list_name:
                raise ValueError(
                    "kps_get_conversation_index: can't derive index name for this conversation list.\n"
                    "Cause: the list is not a store variable (it was likely created at runtime).\n"
                    "Fix: define it with `default your_convo = []` then modify it dynamically."
                )
            index_name = list_name + "_index_kps_"
            if return_string:
                return index_name
            else:
                try:
                    return getattr(store, index_name)
                except:
                    setattr(store, index_name, 0)
                    return getattr(store, index_name)

        else:
            raise TypeError("You have passed an incorrect variable into 'get_conversation_index', must be a conversation/contact you created using build_conversation(), or a conversation dict you created manually.")


    def kps_set_conversation_index(contact_or_list: "dict or list", set_to: int = 0) -> None:
        """
        Sets the current index for any conversation. This is where the conversation will continue from when loaded into the phone
        If you pass in the conversation dict you created with kps_build_conversation() it will update the one currently loaded into the phone
        If you pass in a conversation list it will update the index for that conversation list
        """
        if isinstance(contact_or_list, dict):
            index_name = contact_or_list["current_index"]
            #print("dict - " ,index_name)
            setattr(store, index_name, set_to)
        elif isinstance(contact_or_list, list):
            list_name = get_store_name_of(contact_or_list)
            index_name = list_name + "_index_kps_"
            #print("list - " ,index_name)
            setattr(store, index_name, set_to)
        else:
            raise TypeError(
                "You have passed an incorrect variable into 'set_conversation_index', must be a conversation list, or a conversation/contact you created using build_conversation()"
            )


    def kps_member(name: str, *args, **config) -> dict:
        """
        Create a member to be added to a conversation. First parameter is their name. This conversation will then appear on any phones that have an owner with the same name.
        Any parameters after that are to set things like profile, click to send, etc. Please check docs for full list. 
        """
        if not isinstance(name, str):
            raise TypeError(
                "kps_member could not complete \n"
                "Cause: First parameter must be a string, their name \n"
                "Note: This may be from a kps_build_conversation() function, as kps_member() is used as an parameter"
            )
        if args:
            raise TypeError(
                "kps_member could not complete \n"
                "Cause: An incorrect parameter was passed after the name \n"
                f"Parameters that caused this: {args!r}\n"
                "Fix: Ensure all parameters passed after the name are the format -> 'setting_this_var' = set_to \n"
                "Example: kps_member('Kesash', disable_messaging = True, profile = 'test.png') \n"
                "Note: This may be from a kps_build_conversation() function, as kps_member() is used as an argument"
            )
        return {name: dict(config)}




    def kps_build_conversation(current_dialogue: list, *members: dict, group_profile: str = None, group_name: str = None):
        """
        Builds a conversation dict for you, so it will appear on all members phones. 
        The first parameter is the conversation that starts loaded into the phone, can be an empty list. 
        After that pass all members in using kps_member(name, *args)
        Set a profile piture with group_profile = '/path/toimage.png
        And if it is a group chat set a group name with group_name
        """
        members_dict = {}

        st = renpy.store
        
        for m in members:
            if not isinstance(m, dict):
                raise TypeError(
                    "Members must be created using member()"
                )

            for name, config in m.items():
                if "profile" not in config or config["profile"] is None:
                    config["profile"] = "SET_A_PROFILE.PNG"
                members_dict[name] = config
                member_part = "_".join(sorted(members_dict))
        suffix = uuid.uuid4().hex[:4]
        if len(members) > 0:
            name = f"{member_part}-{suffix}"
        else:
            name = get_store_name_of(current_dialogue) + f"-{suffix}" 

        if group_name is not None:
            name = group_name

        completed_dict = {
            "name": name,
            "profile":group_profile,
            "current_index": None,
            "all_dialogue": [],
            "current_dialogue": current_dialogue,
            "scroll_to_bottom": False,
            "delay_next_message": False,
            "members": members_dict,
        }

        if not hasattr(st, "phone_messages_registry") or st.phone_messages_registry is None:
            st.phone_messages_registry = []

        st.phone_messages_registry.append(completed_dict)

        return completed_dict


    def kps_send_next_if_pending(convo: dict, *dont_send_keys: str):
        """
        Will check the current conversation in a conversation dict and send the next message if there is one
        Additional parameters are keys, if the next message has that key, it will not send
        """
        if not isinstance(convo, dict):
            raise TypeError(
                "kps_send_next_if_pending could not complete \n"
                "Cause: A non dict parameter was passed as the first parameter \n"
                "Fix: Ensure the first parameter is the dict created with kps_build_conversation() \n"
            )
        for x in dont_send_keys:
            if not isinstance(x, str):
                raise TypeError(
                "kps_send_next_if_pending could not complete \n"
                "Cause: A non string parameter was passed as the second parameter \n"
                "Fix: Ensure all parameters for the dont send keys are strings \n"
                "did you mean to pass this as which_phone=? using the kps_notif_if_sent() function?"
            ) # BECAUSE THATS WHAT I DID! SO NOW ITS IN THE ERROR HANDLER!
        if convo['name'] == getattr(store, "_var_kps_current_convo", None):
            return None

        try:
            idx = getattr(store, convo["current_index"])
        except:
            kps_set_conversation_index(convo)
            idx = getattr(store, convo["current_index"])
        dialogue = convo.get("current_dialogue", [])
        if idx < 0 or idx >= len(dialogue):
            return False

        next_item = dialogue[idx]

        if isinstance(next_item, list):
            return False

        if isinstance(next_item, dict) and dont_send_keys:
            if any(key in next_item for key in dont_send_keys):
                return False

        entry = dialogue.pop(idx)
        entry["seen"] = True
        convo["all_dialogue"].append(entry)
        return True

    def kps_send_message_to_phone(which_conversation: dict, from_who: str, saying_what: str) -> None:
        "Sends a message to a closed conversation \n"
        "First parameter is the conversation \n"
        "Sencond is the key (or who says it), Third is the message"

        if not isinstance(which_conversation, dict):
            raise TypeError(
                "kps_send_message_to_phone could not complete \n"
                "Cause: A non dict parameter was passed as the first parameter \n"
                "Fix: Ensure the first parameter is the dict created with kps_build_conversation() \n"
            )

        if not isinstance(from_who, str):
                raise TypeError(
                "kps_send_message_to_phone could not complete \n"
                "Cause: A non string parameter was passed as the second parameter \n"
                "Fix: Name of who sent the message/message key must be a string \n"
            )

        if not isinstance(saying_what, str):
                raise TypeError(
                "kps_send_message_to_phone could not complete \n"
                "Cause: A non string parameter was passed as the third parameter \n"
                "Fix: Message sent must be a string"
            )
        #print(current_conversation, " - ", which_conversation["name"])
        if (
        not renpy.get_screen("dynamic_scrollable_text")
        and not renpy.get_screen("dynamic_scrollable_text_group")
        ) or current_conversation != which_conversation["name"]:
            which_conversation["all_dialogue"].append({from_who:saying_what, "seen":True})
        else:
            _kps_play_message_sent_received_sound(which_conversation)
            which_conversation["all_dialogue"].append({from_who:saying_what})

    
    def kps_notif_if_sent(convo: dict, *dont_send_keys: str, which_phone:dict = phone_data) -> bool:
        """
        Combines kps_send_next_if_pending() and kps_phone_notif_show()
        """
        if kps_send_next_if_pending(convo, *dont_send_keys):
            kps_phone_notif_show(convo, which_phone=which_phone)
            return True
        else:
            return False

    def kps_open_phone(phone: dict, click_to_send_enabled: bool = True) -> None:
        """
        Do I need to say what this does? It opens the phone.....
        Pass the phone dict as the first parameter
        If you pass 'False' as the second it will disable messaging for the entire phone
        """

        phone_data.clear()
        phone_data.update(phone)
        renpy.store.ivkps_active_phone_ref = phone
        # Ensure we always have a theme set (and migrate legacy background if needed).
        try:
            ikps_ensure_theme()
        except Exception:
            pass
        renpy.store.click_to_send = click_to_send_enabled
        renpy.show_screen("phone_home")


    def kps_build_conversation_list(script_text):
        builder_list = []
        lines = script_text.splitlines()
        i = 0

        def _fix_quotes(s):
            return (s.replace("“", "\"")
                    .replace("”", "\"")
                    .replace("‘", "'")
                    .replace("’", "'")
                )  # If anyone actually uses these....

        while i < len(lines):
            raw_line = lines[i]

            if not raw_line.strip():
                i += 1
                continue

            stripped = _fix_quotes(raw_line.strip())
            # print(stripped)

            if stripped.startswith("{") and stripped.endswith("}"):
                expr = stripped
                try:
                    obj = renpy.python.py_eval(expr)
                except Exception:
                    try:
                        obj = ast.literal_eval(expr)
                    except Exception as e:
                        raise Exception(
                            "kps_build_conversation_list: Invalid {..} expression: %r (%s)" % (stripped, e)
                        )

                builder_list.append(obj)
                i += 1
                continue

            if stripped.startswith("["):
                try:
                    parsed = ast.literal_eval(stripped)
                    if isinstance(parsed, list) and parsed and isinstance(parsed[0], list):
                        builder_list.append(parsed)
                        i += 1
                        continue
                except Exception:
                    pass

            if stripped.startswith("[") and stripped.endswith("]"):
                try:
                    parsed = ast.literal_eval("[" + stripped + "]")
                    builder_list.append(parsed)
                    i += 1
                    continue
                except Exception as e:
                    raise Exception(
                        "kps_build_conversation_list: Invalid choices literal: %r (%s)" % (stripped, e)
                    )

            work = raw_line.lstrip()
            colon_index = work.find(":")
            if colon_index == -1:
                raise Exception("kps_build_conversation_list: Missing ':' in line: %r" % work)

            speaker = _fix_quotes(work[:colon_index].strip())
            # print(speaker)

            message = work[colon_index + 1:]
            message = message.lstrip(" \t")

            # print(message)
            msg_check = message.lstrip(" \t")
            # This. Was. Pain.
            if speaker == "code" and msg_check.startswith(('"""', "'''", "```")):
                delim = msg_check[:3]  # Hehe, smiley face :3
                buf = []
                rest = msg_check[3:]  # Aww, sad face 3:

                # If the opening and closing delimiter are on the same line.
                if delim in rest:
                    before, _, _ = rest.partition(delim)
                    buf.append(before)
                    code_text = "\n".join(buf)
                    code_text = textwrap.dedent(code_text).strip("\n")
                    builder_list.append({"code": code_text})
                    i += 1
                    continue

                if rest.strip():
                    buf.append(rest)

                i += 1
                found_close = False
                while i < len(lines):
                    line = lines[i]
                    if delim in line:
                        before, _, _ = line.partition(delim)
                        buf.append(before)
                        found_close = True
                        break
                    buf.append(line)
                    i += 1

                if not found_close:
                    raise Exception(
                        "kps_build_conversation_list: Unterminated code block (missing %s)" % delim
                    )

                code_text = "\n".join(buf)
                code_text = textwrap.dedent(code_text).strip("\n")
                builder_list.append({"code": code_text})
                i += 1
                continue

            if speaker != "code":
                message = _fix_quotes(message)

            builder_list.append({speaker: message})
            i += 1

        return builder_list


    #### USER FUNCTIONS END ####

    def _kps_ensure_index(contact):
        index_name = contact['current_index']
        try:
            getattr(store, index_name)
        except:
            setattr(store, index_name, 0)
        

    def _kps_play_message_sent_received_sound(entry):
        if not (renpy.get_screen("dynamic_scrollable_text") or renpy.get_screen("dynamic_scrollable_text_group")):
            return
        if not isinstance(entry, dict):
            return
        sender = next(iter(entry.keys()), None)
        me = phone_data.get("name")
        if sender in ("code", "system", "delete"):
            return
        if sender == me:
            renpy.play(var_kps_message_sent_sound, channel="kps_phone_messages")
        else:
            renpy.play(var_kps_message_recieved_sound, channel="kps_phone_messages")


    def get_store_name_of(obj):
        for k, v in store.__dict__.items():
            if v is obj:
                _ikps_store_name_cache[id(v)] = k
                return k
        return None


    def kps_apply_notification_volume(volume):
        var_kps_notification_volume = round(float(volume), 2)
        renpy.music.set_volume(var_kps_notification_volume, channel="kps_phone_notifications")

    def kps_apply_message_volume(volume):
        var_kps_message_sound_volume = round(float(volume), 2)
        renpy.music.set_volume(var_kps_message_sound_volume, channel="kps_phone_messages")




    ######## END OF NEW FUNCTIONS ########



    

    

    # Look..... i tried... okay? I cant do styling :')

    # Did it for you  /n

    # I KNOWWW TYYYYY /k

    # Choice buttons.
    # Uses the theme colours defined in the UI section below.

    

    # This fun little function *should* instannnnnnnnnnnnnnnntly finish a conversation, load all remaining messages in. (My n got stuck while typing that, leaving it there)
    def complete_conversation(contact):
        index_var_name = contact['current_index']
        while len(contact['current_dialogue']) > getattr(store, index_var_name):
            current_index = getattr(store, index_var_name)
            contact['all_dialogue'].append(contact['current_dialogue'][current_index])
            setattr(store, index_var_name, current_index + 1)

    # scanning for all chats to add to a global list on game start. Dont think I use this anymore.... havent checked....
    def scan_for_chats():
            req = {"all_dialogue", "members", "current_index", "current_dialogue"}
            for global_name, obj in store.__dict__.items():
                if isinstance(obj, dict) and req.issubset(obj.keys()):
                    if obj not in phone_messages_registry:
                        phone_messages_registry.append(obj)





    # New function for this, now unused
    def set_index_for_convo(index_var, set_as):
            setattr(store, str(index_var) + "_index_kps_", int(set_as))


    # And this, theres a better one 
    def send_message_now(contact_map, message):
        contact_map['all_dialogue'].append({contact_map['name']:message, 'seen':True})



    def add_next_line(character_info):
        renpy.retain_after_load()
        dialogue_name = character_info["current_dialogue"]
        if isinstance(dialogue_name, str):
            dialogue_list = getattr(store, dialogue_name)
        else:
            dialogue_list = dialogue_name
        index_name = character_info["current_index"]
        idx = getattr(store, index_name)
        if idx < len(dialogue_list):
            entry = dialogue_list[idx]
            character_info["all_dialogue"].append(entry)

            _kps_play_message_sent_received_sound(entry) # <- once here

            setattr(store, index_name, idx + 1)
            character_info["scroll_to_bottom"] = True
            renpy.retain_after_load()



    def conditional_add_line(character_info):
        index_name = character_info["current_index"]
        idx = getattr(store, index_name)
        dialogue_name = character_info["current_dialogue"]
        dialogue_list = getattr(store, dialogue_name) if isinstance(dialogue_name, str) else dialogue_name
        if idx >= len(dialogue_list):
            return
        entry = dialogue_list[idx]
        if isinstance(entry, dict):
            add_next_line(character_info)
        elif isinstance(entry, list):
            renpy.show_screen('dynamic_scrollable_text', character_info, True)


    def handle_choice(choice_var_name, character_info):
        cond = character_info.get("conditions", None)
        if cond is not None and not eval(cond, {}, vars(store)):
            return
        if character_info["members"][phone_data["name"]].get("disable_messaging", False):
            pass
        else:
            renpy.retain_after_load()
            choice_list = getattr(store, choice_var_name)

            first_entry = choice_list[0] # Add this line

            
            _kps_play_message_sent_received_sound(first_entry) # And run it here

            character_info["all_dialogue"].append(choice_list[0])
            character_info["scroll_to_bottom"] = True
            character_info_name = get_store_name_of(character_info)
            update_current_convo(character_info_name, {
                "current_dialogue": choice_list,
                "current_index": f"{choice_var_name}_index_kps_",
                "scroll_to_bottom": True
            })
            set_index_for_convo(choice_var_name, 1)
            renpy.checkpoint()
            renpy.retain_after_load()


    # Look, ill be honest, I think this being here is just a leftover from deleting a function that used it
    # But im too afraid to delete it in case it just breaks everything......

    renpy.restart_interaction()


    def auto_advance_to_player(character_info, name = "me"):
        #print(character_info)
        cond = character_info.get("conditions", None)
        #print("auto - ", cond)
        if cond is not None and not eval(cond, {}, vars(store)):
            return
        renpy.retain_after_load()
        index_name = character_info["current_index"]
        idx = getattr(store, index_name)
        dialogue_list = character_info["current_dialogue"]
        if isinstance(dialogue_list, str):
            dialogue_list = getattr(store, dialogue_list)
        if idx < len(dialogue_list):
            entry = dialogue_list[idx]
            if isinstance(entry, dict) and list(entry.keys())[0] == name:
                return
            if isinstance(entry, list):
                return
            character_info["all_dialogue"].append(entry)

            _kps_play_message_sent_received_sound(entry) # <- again here

            character_info["scroll_to_bottom"] = True
            setattr(store, index_name, idx + 1)
            renpy.checkpoint()
            renpy.retain_after_load()
            renpy.restart_interaction()
    
    def show_choices_now(character_info):
        renpy.retain_after_load()
        renpy.restart_interaction()
        return [Hide("dynamic_scrollable_text"), Show("dynamic_scrollable_text", character_info=character_info, continue_list=True)]
    

    # This runs automatically when an image is sent in a chat, but you can run it manually to unlock an image int he gallery :) Just use the image path
    def unlock_image(filename):
        filename = filename.lower()
        for data in gallery_data.values():
            for path in data["images"]:
                if path.endswith(filename):
                    if path not in unlocked_images:
                        if persistent_gallery:
                            persistent.persistent_gallery.append(path)
                            renpy.save_persistent()
                        else:
                            unlocked_images.append(path)


    def soft_delete_by_value(character_info, value, pop_message = True):
        try:
            index = next(i for i, d in enumerate(character_info["all_dialogue"]) if value in d.values())
            if character_info["all_dialogue"][index]:
                for key, item in character_info["all_dialogue"][index].items():
                    if item == value:
                        character_info["all_dialogue"][index] = {"system":deleted_message_replacement}
                        #if pop_message:
                        #    character_info["all_dialogue"].pop()
        except (StopIteration, IndexError):
            pass

    def hard_delete_by_value(character_info, value):
        try:
            index = next(
                i for i, d in enumerate(character_info["all_dialogue"])
                if isinstance(d, dict) and value in d.values()
            )
            character_info["all_dialogue"].pop(index)
            return True
        except (StopIteration, KeyError, TypeError, IndexError):
            return False

    # If you want to handle more message types you can add them in here, this is just what it does based on the key entered

    def handle_message_types(dialogue_list):
        i = 0
        while i < len(dialogue_list):
            entry = dialogue_list[i]
            if not isinstance(entry, dict):
                i += 1
                continue
            if "code" in entry:
                code = entry["code"]
                print(code)
                exec(code, globals())
                dialogue_list.pop(i)     
                continue
            if "image" in entry:
                unlock_image(entry["image"])
                i += 1
                continue
            if "delete" in entry:
                soft_delete_by_value({"all_dialogue": dialogue_list}, entry["delete"])
                dialogue_list.pop(i)
                continue
            i += 1


    # Why is this defined here and not at the top? Well, thats because...... yep.....
    # Why did i write that instead of just moving it with the rest?
    # Why am I still adding comments?!?!?!?!?? AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    skipping_messages_enabled = False

    # WHYYY DID THIS TAKE 3 HOURSSSS WHEN ADDING THE SKIP FEATUREEEEE
    def calculate_message_delay(persistant_message_index, true_current_index, current_character_name, min_speak_timer, max_speak_timer, character_info_for_dialogue):
        global skipping_messages_enabled

        #Code messages now trigger instantly!! YAY!!!
        try:
            next_entry = character_info_for_dialogue['current_dialogue'][true_current_index]
            if isinstance(next_entry, dict) and next_entry.get("code", False):
                return 0.00001
        except:
            pass
        message_timer_delay = skip_speed_timer
        #if current_character_name != current_conversation:
        #    return message_timer_delay
        if persistant_message_index <= true_current_index:
            skipping_messages_enabled = False
            min_speak_timer = original_min_speak_timer
        if not static_speak_timer and not skipping_messages_enabled:
            try:
                message_timer_delay = max(min_speak_timer, min(len(list(character_info_for_dialogue['current_dialogue'][true_current_index + 1].values())[0]) * (auto_speak_timer * 0.01), max_speak_timer))
                print("message timer delay made dynamic")
            except Exception as e:
                # It doesnt like it when the next chat is a choice (so list of lists), this just stops it breaking
                #print(e)
                #print("message timer delay made static")
                message_timer_delay = auto_speak_timer
        elif not skipping_messages_enabled:
            message_timer_delay = auto_speak_timer
            #print("we hit the elif :c")
        print(str(message_timer_delay) + " message timer delay")
        return message_timer_delay


    def update_current_convo(main_name, update_info):
        # Update the main one
        if isinstance(main_name, str):       
            if hasattr(store, main_name):
                getattr(store, main_name).update(update_info)
        else:
            main_name['current_dialogue'] = update_info
            new_index = str(get_store_name_of(update_info)) + "_index_kps_"
            main_name['current_index'] = new_index
        
    # New one!


    



    def mark_entry_seen(entry):
        if isinstance(entry, dict):
            k = next(iter(entry.keys()), None)
            # Don't auto-mark videos/images seen unless you also handle "seen video" rendering.
            if k not in ("video", "image"):
                entry["seen"] = True
                renpy.restart_interaction()


transform slide_in_right:
    xoffset 300
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

transform slide_in_left:
    xoffset -300
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

############################################################################
########################  START OF REFACTORED CODE  ########################
############################################################################

init python:

    def ikps_prepare_chat_state(character_info_for_dialogue, continue_list=False, is_group=False):
        """
        Does phone stuff, dont use. Ever.
        """
        _kps_ensure_index(character_info_for_dialogue)

        # Make sure the skip toggle exists 
        if 'skipping_messages_enabled' not in globals():
            globals()['skipping_messages_enabled'] = False

        # GEt current_dialogue 
        current_dialogue = character_info_for_dialogue.get("current_dialogue", [])
        if isinstance(current_dialogue, str):
            try:
                current_dialogue = getattr(store, current_dialogue)
                character_info_for_dialogue["current_dialogue"] = current_dialogue
            except Exception:
                pass

        full_list = current_dialogue
        if isinstance(full_list, str):
            full_list = globals().get(full_list, full_list)

        work_list_name = character_info_for_dialogue.get("all_dialogue", [])
        index_name = character_info_for_dialogue.get("current_index", None)

        true_current_index = getattr(store, index_name) if index_name else 0

        # Persistent logging for the skip feature.
        if not hasattr(persistent, "seen_message_threads") or persistent.seen_message_threads is None:
            persistent.seen_message_threads = {}

        if index_name not in persistent.seen_message_threads:
            persistent.seen_message_threads[index_name] = 0
        persistant_message_index = persistent.seen_message_threads[index_name]

        message_time_delay = calculate_message_delay(
            persistant_message_index,
            true_current_index,
            character_info_for_dialogue.get('name', ''),
            min_speak_timer,
            max_speak_timer,
            character_info_for_dialogue
        )

        persistent.seen_message_threads[index_name] = max(
            true_current_index,
            persistent.seen_message_threads.get(index_name, true_current_index)
        )

        # Handle message types.

        handle_message_types(work_list_name)

        # Mark older messages seen
        for e in work_list_name[:-1]:
            if isinstance(e, dict) and not e.get("seen", False):
                k = next(iter(e.keys()), None)
                if k not in ("video", "image"):
                    e["seen"] = True

        # Decide what happens next (continue/click/cjoice).
        idx = true_current_index
        next_entry = None
        if isinstance(full_list, (list, tuple)) and idx < len(full_list):
            next_entry = full_list[idx]

        jump_to_choices = False
        auto_continue = True

        if next_entry is not None:
            # If the next message is from the player and click-to-send is enabled
            if (
                isinstance(next_entry, dict)
                and list(next_entry.keys())[0] == phone_data.get('name')
                and click_to_send
            ):
                auto_continue = False

            # If the next item is a choice list
            elif isinstance(next_entry, list):
                jump_to_choices = (not continue_list)
                auto_continue = False

            # Depricated? Think so. Doesnt hurt anyone though
            elif (not is_group) and (not isinstance(next_entry, dict)):
                jump_to_choices = (not continue_list)
                auto_continue = False

        # Typing indicator
        is_typing = False
        if auto_continue and (not continue_list):
            if isinstance(full_list, (list, tuple)) and idx < len(full_list):
                if character_info_for_dialogue.get('name') == getattr(store, 'current_conversation', None):
                    is_typing = True

        # Change title if not group
        title = character_info_for_dialogue.get('name', 'Messages')
        if not is_group:
            current_user = phone_data.get('name')
            members = character_info_for_dialogue.get('members', {}) or {}
            for key in members.keys():
                if key != current_user:
                    title = key
                if title is None:
                    title = "Unknown"

        return {
            "full_list": full_list,
            "work_list_name": work_list_name,
            "index_name": index_name,
            "true_current_index": true_current_index,
            "persistant_message_index": persistant_message_index,
            "message_time_delay": message_time_delay,
            "idx": idx,
            "next_entry": next_entry,
            "jump_to_choices": jump_to_choices,
            "auto_continue": auto_continue,
            "is_typing": is_typing,
            "title": title,
        }


    def ikps_group_typing_subtitle(next_entry):
        """Group chat subtitle when typing indicator is active."""
        if not isinstance(next_entry, dict):
            return "Typing…"
        
        key = next(iter(next_entry), None)
    

        if key == "image":
            speaker = next_entry.get("speaker") or "Someone"
            return speaker + " is sending an image..."
        
        # Normal messages: key is the speaker's name.
        if key not in {"code", "image", "video", "system", "delete"} and key is not None:
            return key + " is typing..."
        
        return "..."

    def ikps_last_message_preview(char):
        """
        Returns the last displayable dialogue string for previews,
        or None if nothing valid exists.
        """
        if not char or not char.get("all_dialogue"):
            return None

        for entry in reversed(char["all_dialogue"]):
            if not isinstance(entry, dict) or not entry:
                continue

            key, value = next(iter(entry.items()))

            if key in {"code", "image", "video", "delete"}:
                continue

            if isinstance(value, str) and value:
                return value.replace("{", "{{").replace("}", "}}")

        return None

init 99 python:
    # Start of the most cursed code youve ever seen    
    # Imagine someone doing this in a normal python programme? Got to love the cursed stuff you can get away with cos its renpy....
    # Yea i need to be consistant with how I call store, but it works now, not touching it again...

    def ikps_sync_phone_registry():
        st = renpy.store
        st.phone_messages_registry = []

        seen_names = {
            c.get("name")
            for c in st.phone_messages_registry
            if isinstance(c, dict) and c.get("name")
        }
        req = {"all_dialogue", "members", "current_index", "current_dialogue", "name"}
        for _, obj in st.__dict__.items():
            if isinstance(obj, dict) and req.issubset(obj.keys()):
                n = obj.get("name")
                if n and n not in seen_names:
                    st.phone_messages_registry.append(obj)
                    seen_names.add(n)

    def ikps_ensure_indexes_for_all_lists():
        def ikps_is_this_a_convo(v):
            if not isinstance(v, list) or not v:
                return False
            idxs = [0, len(v)//2, -1]
            for i in idxs:
                x = v[i]
                if not isinstance(x, (list, dict)):
                    return False
            return True
        for name, value in list(vars(store).items()):
            if ikps_is_this_a_convo(value):
                index_name = name + "_index_kps_"
                if not hasattr(store, index_name):
                    setattr(store, index_name, 0)


    def ikps_print_index_vars():
        for name in vars(store).keys():
            if name.endswith("_index_kps_"):
                print(name)

    

    def ikps_rebuild_kps_store_name_cache():
        _ikps_store_name_cache.clear()
        for k, v in store.__dict__.items():
            if k == "_ikps_store_name_cache":
                continue
            _ikps_store_name_cache[id(v)] = k

    def ikps_ensure_indexes_from_dialogue_lists():
        for convo in phone_messages_registry:
            if convo['current_index'] is None:
                store_name = get_store_name_of(convo['current_dialogue'])
                index_name = store_name + "_index_kps_"
                convo['current_index'] = index_name

    def ikps_reassign_convos():
        st = renpy.store
        for item in st.phone_messages_registry:
            try:
                list_name = item["current_index"].removesuffix("_index_kps_")
                item['current_dialogue'] = getattr(st, list_name)
            except:
                pass


    def phone_bootstrap():
        ikps_sync_phone_registry()
        ikps_ensure_indexes_for_all_lists()
        ikps_ensure_indexes_from_dialogue_lists()
        ikps_rebuild_kps_store_name_cache()
        ikps_reassign_convos()
        renpy.block_rollback()

    config.start_callbacks.append(phone_bootstrap)
    config.after_load_callbacks.append(phone_bootstrap)




#################################################################################
#################################################################################
#################################################################################


# ----------------------------------------#
#        Phone UI Theme                   #
# ----------------------------------------#

init -15 python:
    
    # I SAID ID NEVER DO THIS AGAIN, WHY AM I DOING THIS AGAIN, YOU OWE ME ALL THE PIZZA (n)
    # Maybe a slice? 🤣 (kesa)
    # Hmph (n)

    PHONE_ZOOM = 1
    PHONE_BORDER_IMG = "images/gui/phone_boarder.png"

    PHONE_INNER_W = 400
    PHONE_INNER_H = 800

    class IKPSPhoneTheme(object):
        def __init__(self, key, label, **colors):
            self.key = key
            self.label = label
            for k, v in colors.items():
                setattr(self, k, v)

    PHONE_DEFAULT_THEME = "midnight"

    PHONE_THEMES = {
        "midnight": IKPSPhoneTheme(
        "midnight", "Midnight",
        bg="#0f1115",
        glass="#111526cc",
        panel="#171c2ddd",
        panel_soft="#00000055",
        statusbar="#00000022",
        topbar="#0000002a",
        stroke="#ffffff14",
        text="#e9ecff",
        muted="#a9b0d6",
        accent="#7aa2ff",
        accent_2="#9a7aff",
        badge="#ff5a7a",
        bubble_sent="#2f6cffcc",
        bubble_sent_hover="#3a78ffdd",
        bubble_recv="#ffffff18",
        chip="#ffffff14",
        typing_chip="#ffffff18",
        card_bg="#ffffff10",
        card_hover="#ffffff18",
        icon_hover="#ffffff18",
        rounded_bg="#ffffffdd",
        rounded_text="#000000",
        bar_right="#ffffff20",
        thumb="#ffffffaa",
    ),

        "slate": IKPSPhoneTheme(
        "slate", "Daylight",
        bg="#f6f7fb",
        glass="#ffffffcc",
        panel="#ffffffee",
        panel_soft="#0000000a",
        statusbar="#00000008",
        topbar="#0000000c",
        stroke="#00000014",
        text="#1a1f2e",
        muted="#5d667a",
        accent="#2f6cff",
        accent_2="#ff4d9d",
        badge="#ff2d55",
        bubble_sent="#2f6cffcc",
        bubble_sent_hover="#3a78ffdd",
        bubble_recv="#0000000a",
        chip="#00000008",
        typing_chip="#00000010",
        card_bg="#00000006",
        card_hover="#0000000c",
        icon_hover="#0000000c",
        rounded_bg="#111827",
        rounded_text="#ffffff",
        bar_right="#00000012",
        thumb="#00000055",
    ),

        "navy": IKPSPhoneTheme(
        "navy", "Ink & Gold",
        bg="#071220",
        glass="#0a1627cc",
        panel="#0f223ddd",
        panel_soft="#00000055",
        statusbar="#00000022",
        topbar="#0000002a",
        stroke="#ffffff14",
        text="#e9f0ff",
        muted="#a7b6d6",
        accent="#f6c177",
        accent_2="#ff2d55",
        badge="#00d1ff",
        bubble_sent="#f6c177cc",
        bubble_sent_hover="#ffd08add",
        bubble_recv="#ffffff18",
        chip="#ffffff12",
        typing_chip="#ffffff18",
        card_bg="#ffffff0e",
        card_hover="#ffffff18",
        icon_hover="#ffffff18",
        rounded_bg="#ffffffdd",
        rounded_text="#000000",
        bar_right="#ffffff20",
        thumb="#ffffffaa",
    ),

        "ocean": IKPSPhoneTheme(
        "ocean", "Sky",
        bg="#e9f7ff",
        glass="#ffffffcc",
        panel="#ffffffee",
        panel_soft="#0000000a",
        statusbar="#00000008",
        topbar="#0000000c",
        stroke="#00000012",
        text="#0b2a33",
        muted="#47606b",
        accent="#00a3ff",
        accent_2="#00ffb3",
        badge="#ff7a18",
        bubble_sent="#00a3ffcc",
        bubble_sent_hover="#34b8ffdd",
        bubble_recv="#0000000a",
        chip="#00000008",
        typing_chip="#00000010",
        card_bg="#00000006",
        card_hover="#0000000c",
        icon_hover="#0000000c",
        rounded_bg="#0b2a33",
        rounded_text="#ffffff",
        bar_right="#00000012",
        thumb="#00000055",
    ),

        "rose": IKPSPhoneTheme(
        "rose", "Blush",
        bg="#fff0f6",
        glass="#ffffffcc",
        panel="#ffffffee",
        panel_soft="#0000000a",
        statusbar="#00000008",
        topbar="#0000000c",
        stroke="#00000012",
        text="#2b1020",
        muted="#7a5166",
        accent="#ff4d9d",
        accent_2="#b78cff",
        badge="#00d1ff",
        bubble_sent="#ff4d9dcc",
        bubble_sent_hover="#ff79b5dd",
        bubble_recv="#0000000a",
        chip="#00000008",
        typing_chip="#00000010",
        card_bg="#00000006",
        card_hover="#0000000c",
        icon_hover="#0000000c",
        rounded_bg="#2b1020",
        rounded_text="#ffffff",
        bar_right="#00000012",
        thumb="#00000055",
    ),

        "mint": IKPSPhoneTheme(
        "mint", "Matcha",
        bg="#eafff5",
        glass="#ffffffcc",
        panel="#ffffffee",
        panel_soft="#0000000a",
        statusbar="#00000008",
        topbar="#0000000c",
        stroke="#00000012",
        text="#05241f",
        muted="#3f6b60",
        accent="#00c98a",
        accent_2="#00d1ff",
        badge="#ff2d55",
        bubble_sent="#00c98acc",
        bubble_sent_hover="#00e0a0dd",
        bubble_recv="#0000000a",
        chip="#00000008",
        typing_chip="#00000010",
        card_bg="#00000006",
        card_hover="#0000000c",
        icon_hover="#0000000c",
        rounded_bg="#05241f",
        rounded_text="#ffffff",
        bar_right="#00000012",
        thumb="#00000055",
    ),

        "ember": IKPSPhoneTheme(
        "ember", "Ember",
        bg="#1a0c05",
        glass="#1a0c05cc",
        panel="#2a1206dd",
        panel_soft="#00000055",
        statusbar="#00000022",
        topbar="#0000002a",
        stroke="#ffffff14",
        text="#fff1e6",
        muted="#d4b0a0",
        accent="#ff7a18",
        accent_2="#ffd166",
        badge="#00d1ff",
        bubble_sent="#ff7a18cc",
        bubble_sent_hover="#ff9738dd",
        bubble_recv="#ffffff16",
        chip="#ffffff12",
        typing_chip="#ffffff18",
        card_bg="#ffffff10",
        card_hover="#ffffff18",
        icon_hover="#ffffff18",
        rounded_bg="#ffffffdd",
        rounded_text="#000000",
        bar_right="#ffffff20",
        thumb="#ffffffaa",
    ),

        "lavender": IKPSPhoneTheme(
        "lavender", "Lilac",
        bg="#f4efff",
        glass="#ffffffcc",
        panel="#ffffffee",
        panel_soft="#0000000a",
        statusbar="#00000008",
        topbar="#0000000c",
        stroke="#00000012",
        text="#1a102b",
        muted="#5d4f7a",
        accent="#7c3aed",
        accent_2="#ff4d9d",
        badge="#00ffb3",
        bubble_sent="#7c3aedcc",
        bubble_sent_hover="#9a6bffdd",
        bubble_recv="#0000000a",
        chip="#00000008",
        typing_chip="#00000010",
        card_bg="#00000006",
        card_hover="#0000000c",
        icon_hover="#0000000c",
        rounded_bg="#1a102b",
        rounded_text="#ffffff",
        bar_right="#00000012",
        thumb="#00000055",
    ),

        "matrix": IKPSPhoneTheme(
        "matrix", "Matrix",
        bg="#030605",
        glass="#030605cc",
        panel="#07120bdd",
        panel_soft="#00000055",
        statusbar="#00000022",
        topbar="#0000002a",
        stroke="#00ff6630",
        text="#d9ffe8",
        muted="#6fffab",
        accent="#00ff66",
        accent_2="#00ffaa",
        badge="#ff2bd6",
        bubble_sent="#00ff66cc",
        bubble_sent_hover="#00ff86dd",
        bubble_recv="#00ff6618",
        chip="#00ff6612",
        typing_chip="#00ff6620",
        card_bg="#00ff6610",
        card_hover="#00ff6618",
        icon_hover="#00ff6618",
        rounded_bg="#d9ffe8",
        rounded_text="#000000",
        bar_right="#00ff6620",
        thumb="#00ff66cc",
    ),

        "rainbow": IKPSPhoneTheme(
        "rainbow", "Rainbow",
        bg="#fffbe6",
        glass="#ffffffcc",
        panel="#ffffffee",
        panel_soft="#0000000a",
        statusbar="#00000008",
        topbar="#0000000c",
        stroke="#00000014",
        text="#1a1a1a",
        muted="#555555",
        accent="#ff2d55",
        accent_2="#00d1ff",
        badge="#7c3aed",
        bubble_sent="#00d1ffcc",
        bubble_sent_hover="#34ddffdd",
        bubble_recv="#ff2bd612",
        chip="#7c3aed12",
        typing_chip="#34c75914",
        card_bg="#00000006",
        card_hover="#0000000c",
        icon_hover="#0000000c",
        rounded_bg="#1a1a1a",
        rounded_text="#ffffff",
        bar_right="#00000012",
        thumb="#00000055",
    ),
}




    PHONE_C_BG       = PHONE_THEMES[PHONE_DEFAULT_THEME].bg
    PHONE_C_TEXT     = PHONE_THEMES[PHONE_DEFAULT_THEME].text
    PHONE_C_MUTED    = PHONE_THEMES[PHONE_DEFAULT_THEME].muted
    PHONE_C_SOFT     = PHONE_THEMES[PHONE_DEFAULT_THEME].panel_soft
    PHONE_C_ACCENT   = PHONE_THEMES[PHONE_DEFAULT_THEME].accent
    PHONE_C_ACCENT_2 = PHONE_THEMES[PHONE_DEFAULT_THEME].accent_2

    PHONE_C_BADGE    = PHONE_THEMES[PHONE_DEFAULT_THEME].badge
    PHONE_THEME_SWATCHES = [(t.label, t.key, t.bg) for t in PHONE_THEMES.values()]

    def ikps_ensure_theme():
        try:
            pd = getattr(store, "phone_data", None)
            ref = getattr(renpy.store, "ivkps_active_phone_ref", None)

            t = pd.get("theme") if isinstance(pd, dict) else None
            if isinstance(t, str) and t in PHONE_THEMES:
                if isinstance(ref, dict):
                    ref["theme"] = t
                return t

            rt = ref.get("theme") if isinstance(ref, dict) else None
            if isinstance(rt, str) and rt in PHONE_THEMES:
                if isinstance(pd, dict):
                    pd["theme"] = rt
                return rt

            legacy_bg = None
            bg_list = None
            if isinstance(pd, dict):
                bg_list = pd.get("background")
            elif isinstance(ref, dict):
                bg_list = ref.get("background")

            if isinstance(bg_list, list) and bg_list:
                legacy_bg = bg_list[0]

            chosen = None
            if isinstance(legacy_bg, str) and legacy_bg.startswith("#"):
                for key, th in PHONE_THEMES.items():
                    if th.bg.lower() == legacy_bg.lower():
                        chosen = key
                        break

            if chosen is None:
                chosen = PHONE_DEFAULT_THEME

            if isinstance(pd, dict):
                pd["theme"] = chosen
            if isinstance(ref, dict):
                ref["theme"] = chosen

            return chosen
        except Exception:
            return PHONE_DEFAULT_THEME

    def ikps_get_theme():
        return ikps_ensure_theme()

    def ikps_theme():
        return PHONE_THEMES.get(ikps_get_theme(), PHONE_THEMES[PHONE_DEFAULT_THEME])

    def ikps_theme_color(attr, fallback=None):
        try:
            val = getattr(ikps_theme(), attr)
            if val is None and fallback is not None:
                return fallback
            return val
        except Exception:
            return fallback

    def ikps_style(base_name):
        return "{}_{}".format(base_name, ikps_get_theme())

    def ikps_set_phone_theme(theme_key):
        try:
            if not isinstance(theme_key, str) or theme_key not in PHONE_THEMES:
                theme_key = PHONE_DEFAULT_THEME

            pd = getattr(store, "phone_data", None)
            if isinstance(pd, dict):
                pd["theme"] = theme_key

            ref = getattr(renpy.store, "ivkps_active_phone_ref", None)
            if isinstance(ref, dict):
                ref["theme"] = theme_key

            renpy.restart_interaction()
        except Exception:
            renpy.restart_interaction()

    def set_phone_background(bg_value):
        try:
            if isinstance(bg_value, str) and bg_value.startswith("#"):
                for key, th in PHONE_THEMES.items():
                    if th.bg.lower() == bg_value.lower():
                        ikps_set_phone_theme(key)
                        return
            ikps_set_phone_theme(PHONE_DEFAULT_THEME)
        except Exception:
            ikps_set_phone_theme(PHONE_DEFAULT_THEME)
init python:


    from renpy.style import Style
    try:
        Solid
    except NameError:
        import renpy
        Solid = (getattr(getattr(renpy.display, "image", None), "Solid", None)
                or getattr(getattr(renpy.display, "im", None), "Solid"))

    try:
        Frame
    except NameError:
        import renpy
        Frame = renpy.display.layout.Frame

    def _kps_make_style(name, parent):
        s = Style(parent)
        setattr(style, name, s)
        return s

    def _ikps_build_theme_styles():
        for key, th in PHONE_THEMES.items():

            s = _kps_make_style("phone_glass_" + key, "frame")
            s.background = None
            s.padding = (14, 14)

            s = _kps_make_style("phone_panel_" + key, "frame")
            s.background = None
            s.padding = (12, 12)

            s = _kps_make_style("phone_panel_soft_" + key, "frame")
            s.background = Frame(Solid(th.panel_soft), 16, 16)
            s.padding = (10, 10)

            # Top bars
            s = _kps_make_style("phone_statusbar_" + key, "frame")
            s.background = Frame(Solid(th.statusbar), 12, 12)
            s.padding = (8, 4)

            s = _kps_make_style("phone_topbar_" + key, "frame")
            s.background = Frame(Solid(th.topbar), 14, 14)
            s.padding = (10, 10)

            s = _kps_make_style("phone_title_" + key, "text")
            s.color = th.text
            s.size = 22
            s.bold = True

            s = _kps_make_style("phone_subtitle_" + key, "text")
            s.color = th.muted
            s.size = 14

            s = _kps_make_style("phone_status_text_" + key, "text")
            s.color = th.muted
            s.size = 12

            s = _kps_make_style("phone_body_text_" + key, "text")
            s.color = th.text
            s.size = 18

            s = _kps_make_style("phone_hint_text_" + key, "text")
            s.color = th.muted
            s.size = 16
            s.italic = True

            s = _kps_make_style("phone_icon_btn_" + key, "button")
            s.background = Frame(Solid("#00000000"), 12, 12)
            s.hover_background = Frame(Solid(th.icon_hover), 12, 12)
            s.padding = (8, 8)

            s = _kps_make_style("phone_card_btn_" + key, "button")
            s.background = Frame(Solid(th.card_bg), 16, 16)
            s.hover_background = Frame(Solid(th.card_hover), 16, 16)
            s.padding = (10, 10)
            s.xfill = True

            s = _kps_make_style("phone_fab_btn_" + key, "button")
            s.background = Frame(Solid(th.accent), 18, 18)
            s.hover_background = Frame(Solid(th.accent_2), 18, 18)
            s.padding = (10, 10)

            s = _kps_make_style("rounded_button_" + key, "text_button")
            s.background = Frame(Solid(th.rounded_bg), 16, 16)
            s.hover_background = Frame(Solid(th.accent), 16, 16)
            s.padding = (10, 10)
            s.xminimum = 180
            s.yminimum = 44

            s = _kps_make_style("phone_bubble_sent_" + key, "frame")
            s.background = Frame(Solid(th.bubble_sent), 18, 18)
            s.padding = (8, 8)

            s = _kps_make_style("phone_bubble_recv_" + key, "frame")
            s.background = Frame(Solid(th.bubble_recv), 18, 18)
            s.padding = (8, 8)

            s = _kps_make_style("phone_system_chip_" + key, "frame")
            s.background = Frame(Solid(th.chip), 14, 14)
            s.padding = (10, 6)

            s = _kps_make_style("phone_typing_chip_" + key, "frame")
            s.background = Frame(Solid(th.typing_chip), 14, 14)
            s.padding = (10, 6)

            s = _kps_make_style("phone_choice_btn_" + key, "button")
            s.background = Frame(Solid(th.bubble_sent), 18, 18)
            s.hover_background = Frame(Solid(th.bubble_sent_hover), 18, 18)
            s.padding = (16, 12)
            s.yminimum = 54

            s = _kps_make_style("phone_choice_btn_text_" + key, "text")
            s.color = "#ffffff"
            s.size = 20
            s.xalign = 0.5
            s.textalign = 0.5

    _ikps_build_theme_styles()
init python:
    def phone_shell_dragged(drags, drop):
        d = drags[0]
        x = int(d.x)
        y = int(d.y)
        keep = 80
        w = int(getattr(d, "w", PHONE_INNER_W))
        h = int(getattr(d, "h", PHONE_INNER_H))
        sw = config.screen_width
        sh = config.screen_height
        min_x = -w + keep
        max_x = sw - keep
        min_y = -h + keep
        max_y = sh - keep
        if x < min_x: x = min_x
        if x > max_x: x = max_x
        if y < min_y: y = min_y
        if y > max_y: y = max_y
        store.phone_shell_x = x
        store.phone_shell_y = y


screen phone_shell(title=None, subtitle=None, back_action=None, var_kps_show_back=True, show_border=True, right_action=None, right_icon=None):

    python:
        renpy.retain_after_load()
    draggroup:
        xfill True
        yfill True

        drag:
            drag_name "phone_shell"
            draggable True
            droppable False
            dragged phone_shell_dragged

            xpos phone_shell_x
            ypos phone_shell_y
            drag_handle (0, 0, 1.0, 140)   

            fixed:
                xsize PHONE_INNER_W
                ysize PHONE_INNER_H

                if show_border:
                    add PHONE_BORDER_IMG xalign 0.5 yalign 0.6 zoom PHONE_ZOOM
                $ _bg = ikps_theme_color("bg", PHONE_C_BG)
                if isinstance(_bg, str) and _bg.startswith("#"):
                    add Solid(_bg) xsize PHONE_INNER_W ysize PHONE_INNER_H
                else:
                    add Solid(PHONE_C_BG) xsize PHONE_INNER_W ysize PHONE_INNER_H

                frame:
                    style ikps_style("phone_glass")
                    background None
                    xfill True
                    yfill True

                    vbox:
                        spacing 10

                        frame:
                            style ikps_style("phone_statusbar")
                            xfill True
                            hbox:
                                spacing 8
                                $ _t = time.strftime("%H:%M")
                                text _t style ikps_style("phone_status_text")
                                null width 0 xfill True
                                text "▮▮▮" style ikps_style("phone_status_text")
                                text "KPS" style ikps_style("phone_status_text")

                        if title is not None:
                            use phone_topbar(title=title, subtitle=subtitle, back_action=back_action,
                                            var_kps_show_back=var_kps_show_back, right_action=right_action, right_icon=right_icon)

                        transclude





screen phone_topbar(title, subtitle=None, back_action=None, var_kps_show_back=True, right_action=None, right_icon=None):

    frame:
        style ikps_style("phone_topbar")
        xfill True

        hbox:
            spacing 10
            yalign 0.5

            if var_kps_show_back:
                button:
                    style ikps_style("phone_icon_btn")
                    action (back_action if back_action is not None else Return())
                    add "gui/back_button.png" xysize (34, 34)

            vbox:
                spacing 2
                text title style ikps_style("phone_title")
                if subtitle:
                    text subtitle style ikps_style("phone_subtitle")


            null width 0 xfill True

            if right_icon and right_action is not None:
                button:
                    style ikps_style("phone_icon_btn")
                    yoffset -4
                    action right_action
                    add right_icon xysize (40, 40)

# ----------------------------------------#
#          Dialogue Screen                #
# ----------------------------------------#

screen dynamic_scrollable_text(character_info_for_dialogue, continue_list=False, set_scroll_to_bottom = False):
    modal var_kps_phone_locked
    zorder 100
    tag kps_phone
    predict False
    default yadj = renpy.display.behavior.Adjustment()
    

    if set_scroll_to_bottom:
        $ yadj.value = float('inf')

    $ _kps_state = ikps_prepare_chat_state(character_info_for_dialogue, continue_list=continue_list, is_group=False)
    $ full_list = _kps_state["full_list"]
    $ work_list_name = _kps_state["work_list_name"]
    $ index_name = _kps_state["index_name"]
    $ true_current_index = _kps_state["true_current_index"]
    $ message_time_delay = _kps_state["message_time_delay"]
    $ idx = _kps_state["idx"]
    $ auto_continue = _kps_state["auto_continue"]
    $ jump_to_choices = _kps_state["jump_to_choices"]
    $ is_typing = _kps_state["is_typing"]
    $ var_kps_text_size = getattr(store, "var_kps_text_size", 20)

    on "show" action [
        SetVariable("_var_kps_current_convo", character_info_for_dialogue["name"]),
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_var_kps_current_convo", None),
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    if jump_to_choices:
        timer 0.01 action [
            SetDict(character_info_for_dialogue, "scroll_to_bottom", True),
            Hide("dynamic_scrollable_text"),
            Show("dynamic_scrollable_text", character_info_for_dialogue=character_info_for_dialogue, continue_list=True)
        ]

    if auto_continue and (not continue_list):
        if idx < len(full_list) and character_info_for_dialogue['name'] == current_conversation:
            $ is_typing = True
        else:
            $ is_typing = False
        if character_info_for_dialogue.get("members", {}).get(phone_data.get("name"), {}).get("disable_messaging", False) == False:
            timer message_time_delay repeat True action Function(auto_advance_to_player, character_info_for_dialogue)

    # Main UI
    $ _title = _kps_state["title"]
    $ _cond = character_info_for_dialogue.get("conditions", None)
    $ _ok = (_cond is None) or eval(_cond, {}, vars(store))
    $ _sub = ("Typing…" if (_ok and is_typing and is_typing_indicator and messaging_enabled) else None)
    if len(character_info_for_dialogue['members']) == 1:
        $ _title = "Unknown"
    # Skip button in the top bar 
    $ _show_skip = (persistent.seen_message_threads[index_name] > true_current_index) and show_skip_button
    $ _skip_icon = ("gui/skip_button_selected.png" if skipping_messages_enabled else "gui/skip_button.png")
    $ _skip_action = None
    if _show_skip:
        if not skipping_messages_enabled:
            $ _skip_action = [
                SetVariable("message_timer_delay", skip_speed_timer),
                SetVariable("skipping_messages_enabled", True),
                SetVariable("min_speak_timer", 0)
            ]
        else:
            $ _skip_action = [
                SetVariable("message_timer_delay", auto_speak_timer),
                SetVariable("skipping_messages_enabled", False),
                SetVariable("min_speak_timer", original_min_speak_timer)
            ]

    use phone_shell(title=_title, subtitle=_sub,
        back_action=([
            Hide("dynamic_scrollable_text"), 
            Show("character_select"),
            SetVariable("current_conversation", None),
            SetVariable("_var_kps_current_convo", None)
            ] if var_kps_show_back_button_contact else []), 
        right_action=_skip_action, 
        right_icon=(_skip_icon if _show_skip else None)):

        fixed:
            xfill True
            yfill True

            # Chat list panel
            frame:
                style ikps_style("phone_panel")
                xfill True
                yfill True

                has viewport yadjustment yadj id "chat_vp":
                    draggable True
                    mousewheel True

                    vbox:
                        xfill True
                        spacing 8

                        for entry in work_list_name:
                            $ key, value = list(entry.items())[0]

                            if key == "image":
                                if 'scale' in entry:
                                    $ imgwidth = entry['scale'][0] 
                                    $ imgheight = entry['scale'][1]
                                else:
                                    $ imgwidth, imgheight = chat_image_size[0], chat_image_size[1]
                                $ is_me = entry.get('sender', None) == phone_data['name']
                                #$ print(entry.get('sender', None))
                                #$ print(phone_data['name'])
                                $ side = 1.0 if is_me else 0.0
                                frame:
                                    background None
                                    padding (0, 0)
                                    xmaximum 320
                                    xalign side

                                    button:
                                        background None
                                        action Show("fullscreen_image", image_path=value)
                                        add Image(value) size (imgwidth, imgheight)



                            elif key == "video" and not entry.get('seen', False):
                                $ video_path = value["file"]
                                $ thumbnail = value.get("thumbnail", "gui/video_thumbnail.png")
                                button:
                                    background None
                                    action Show("fullscreen_video", video_path=video_path)
                                    add Image(thumbnail) size (216, 384)

                                # If youre reading this, hi :) 
                                # Also, why? This code is a mess, i swear deleteing a comment could break it all!
                                # UNLESS YOURE TRYING TO STEAL MY CODE?! WELL. IN WHICH CASE. BOOO.

                            else:
                                $ speaker = key
                                $ line = value
                                $ color = ikps_theme_color("text", PHONE_C_TEXT)

                                $ safe_line = line if not isinstance(line, str) else line.replace("{", "{{").replace("}", "}}")
                                if speaker == phone_data['name']:

                                    if not entry.get('seen', False) and message_animations:
                                        frame at slide_in_right:
                                            style ikps_style("phone_bubble_sent")
                                            xalign 1.0
                                            xmaximum 320

                                            $ reply_raw  = entry.get("reply", None)
                                            $ reply_line = None if not reply_raw else (reply_raw if isinstance(reply_raw, str) else str(reply_raw))
                                            if reply_line:
                                                $ reply_line = reply_line.replace("\n", " ").replace("\r", " ").strip()
                                                $ reply_line = (reply_line[:33] + "...") if len(reply_line) > 36 else reply_line
                                                $ reply_line = reply_line.replace("{", "{{").replace("}", "}}")

                                            vbox:
                                                spacing 6

                                                if reply_line:
                                                    frame:
                                                        background Frame(Solid(ikps_theme_color("chip", "#00000033")), 14, 14)
                                                        padding (10, 8)

                                                        hbox:
                                                            spacing 10
                                                            add Solid(ikps_theme_color("accent", "#ff8a00")) xsize 4 ysize 20
                                                            text reply_line color ikps_theme_color("muted", "#b9c7ff") size 14 substitute False

                                                text safe_line color color size var_kps_text_size substitute False
                                    else:
                                        frame:
                                            style ikps_style("phone_bubble_sent")
                                            xalign 1.0
                                            xmaximum 320

                                            $ reply_raw  = entry.get("reply", None)
                                            $ reply_line = None if not reply_raw else (reply_raw if isinstance(reply_raw, str) else str(reply_raw))
                                            if reply_line:
                                                $ reply_line = reply_line.replace("\n", " ").replace("\r", " ").strip()
                                                $ reply_line = (reply_line[:33] + "...") if len(reply_line) > 36 else reply_line
                                                $ reply_line = reply_line.replace("{", "{{").replace("}", "}}")

                                            vbox:
                                                spacing 6

                                                if reply_line:
                                                    frame:
                                                        background Frame(Solid(ikps_theme_color("chip", "#00000033")), 14, 14)
                                                        padding (2, 2)

                                                        hbox:
                                                            spacing 2
                                                            add Solid(ikps_theme_color("accent", "#ff8a00")) xsize 4 ysize 20
                                                            text reply_line color ikps_theme_color("muted", "#b9c7ff") size 14 substitute False

                                                text safe_line color color size var_kps_text_size substitute False

                                elif speaker == "system":

                                    frame:
                                        style ikps_style("phone_system_chip")
                                        xalign 0.5
                                        text safe_line style ikps_style("phone_status_text") color ikps_theme_color("muted", PHONE_C_MUTED)

                                else:

                                    if not entry.get('seen', False) and message_animations:
                                        frame at slide_in_left:
                                            style ikps_style("phone_bubble_recv")
                                            xalign 0.0
                                            xmaximum 320

                                            $ reply_raw  = entry.get("reply", None)
                                            $ reply_line = None if not reply_raw else (reply_raw if isinstance(reply_raw, str) else str(reply_raw))
                                            if reply_line:
                                                $ reply_line = reply_line.replace("\n", " ").replace("\r", " ").strip()
                                                $ reply_line = (reply_line[:33] + "...") if len(reply_line) > 36 else reply_line
                                                $ reply_line = reply_line.replace("{", "{{").replace("}", "}}")

                                            vbox:
                                                spacing 6

                                                if reply_line:
                                                    frame:
                                                        background Frame(Solid(ikps_theme_color("chip", "#00000033")), 14, 14)
                                                        padding (10, 8)

                                                        hbox:
                                                            spacing 10
                                                            add Solid(ikps_theme_color("accent", "#ff8a00")) xsize 4 ysize 20
                                                            text reply_line color ikps_theme_color("muted", "#b9c7ff") size 14 substitute False

                                                text safe_line color color size var_kps_text_size
                                    else:
                                        frame:
                                            style ikps_style("phone_bubble_recv")
                                            xalign 0.0
                                            xmaximum 320

                                            $ reply_raw  = entry.get("reply", None)
                                            $ reply_line = None if not reply_raw else (reply_raw if isinstance(reply_raw, str) else str(reply_raw))
                                            if reply_line:
                                                $ reply_line = reply_line.replace("\n", " ").replace("\r", " ").strip()
                                                $ reply_line = (reply_line[:33] + "...") if len(reply_line) > 36 else reply_line
                                                $ reply_line = reply_line.replace("{", "{{").replace("}", "}}")

                                            vbox:
                                                spacing 6

                                                if reply_line:
                                                    frame:
                                                        background Frame(Solid(ikps_theme_color("chip", "#00000033")), 14, 14)
                                                        padding (10, 8)

                                                        hbox:
                                                            spacing 10
                                                            add Solid(ikps_theme_color("accent", "#ff8a00")) xsize 4 ysize 20
                                                            text reply_line color ikps_theme_color("muted", "#b9c7ff") size 14 substitute False

                                                text safe_line color color size var_kps_text_size


                        if continue_list:
                            $ choice_list = full_list[-1]
                            $ n_choices = len(choice_list)

                            # Rough button and spacing sizes
                            $ btn_h = 54
                            $ spacing = 10
                            $ panel_pad = 20  
                            $ _spacer_h = (btn_h * n_choices) + (spacing * (n_choices - 1)) + panel_pad 

                            null height _spacer_h

            # Manual "next" / send icon 
            if continue_list == False and (not auto_continue):
                $ cond = character_info_for_dialogue.get("conditions", None)
                if cond is None or eval(cond, {}, vars(store)):
                    button:
                        style ikps_style("phone_fab_btn")
                        xalign 0.99
                        yalign 0.95
                        xoffset 10
                        action [Function(conditional_add_line, character_info_for_dialogue),
                                Function(renpy.retain_after_load)]  
    
                        add "gui/message_icon.png" xysize (44, 44)

            # Choices overlay
            if continue_list:
                $ choice_list = full_list[-1]
                $ choice_w = int(PHONE_INNER_W * 0.78)  

                frame:
                    style ikps_style("phone_panel_soft")
                    xfill True
                    yalign 1.0

                    vbox:
                        xfill True
                        spacing 10

                        for choice in choice_list:
                            textbutton choice[0]:
                                style ikps_style("phone_choice_btn")
                                text_style ikps_style("phone_choice_btn_text")
                                xsize choice_w
                                xalign 0.5
                                text_xalign 0.5      
                                text_yalign 0.5      

                                action [
                                    Function(handle_choice, choice[1], character_info_for_dialogue),
                                    Function(renpy.checkpoint),
                                    Show("dynamic_scrollable_text", character_info_for_dialogue=character_info_for_dialogue, continue_list=False),
                                    Function(renpy.restart_interaction)
                                        ]

    # Scroll to bottom helper 
    if character_info_for_dialogue.get("scroll_to_bottom", False):
        $ yadj.value = float('inf')
        $ character_info_for_dialogue["scroll_to_bottom"] = False

    # Typing dots animation 
    
    if work_list_name:
        $ _last = work_list_name[-1]
        if isinstance(_last, dict):
            $ _k = next(iter(_last.keys()), None)
            if _k not in ("video", "image") and (not _last.get("seen", False)) and message_animations:
                timer 0.35 repeat False action Function(mark_entry_seen, _last)


screen dynamic_scrollable_text_group(character_info_for_dialogue, continue_list=False, set_scroll_to_bottom = False):
    modal var_kps_phone_locked
    # Yes, 99% of this is  just copy pasted from the normal logic, cos why not.... why fix what isnt broken :D 
    predict False
    tag kps_phone
    zorder 100


    default yadj = renpy.display.behavior.Adjustment()

    if set_scroll_to_bottom:
        $ yadj.value = float('inf')

    # Tracking who sent the last message to see if we need to add a thing to say who they are
    default last_speaker = None 

    $ _kps_state = ikps_prepare_chat_state(character_info_for_dialogue, continue_list=continue_list, is_group=True)
    $ full_list = _kps_state["full_list"]
    $ work_list_name = _kps_state["work_list_name"]
    $ index_name = _kps_state["index_name"]
    $ true_current_index = _kps_state["true_current_index"]
    $ message_time_delay = _kps_state["message_time_delay"]
    $ idx = _kps_state["idx"]
    $ auto_continue = _kps_state["auto_continue"]
    $ jump_to_choices = _kps_state["jump_to_choices"]
    $ is_typing = _kps_state["is_typing"]
    $ next_entry = _kps_state["next_entry"]
    $ _title = _kps_state["title"]
    $ _sub = ("Typing…" if (is_typing and is_typing_indicator) else None)
    if _sub is not None and work_list_name:
        $ _sub = ikps_group_typing_subtitle(next_entry)

    on "show" action [
        SetVariable("_var_kps_current_convo", character_info_for_dialogue["name"]),
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_var_kps_current_convo", None),
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    if jump_to_choices:
        timer 0.01 action [
            SetDict(character_info_for_dialogue, "scroll_to_bottom", True),
            Hide("dynamic_scrollable_text_group"),
            Show("dynamic_scrollable_text_group", character_info_for_dialogue=character_info_for_dialogue, continue_list=True)
        ]

    if auto_continue and (not continue_list):
        if idx < len(full_list) and character_info_for_dialogue['name'] == current_conversation:
            $ is_typing = True
        else:
            $ is_typing = False
        if character_info_for_dialogue.get("members").get(phone_data.get("name")).get("disable_messaging", False) == False:
            timer message_time_delay repeat True action Function(auto_advance_to_player, character_info_for_dialogue)

    # Skip button in the top bar 
    $ _show_skip = (persistent.seen_message_threads[index_name] > true_current_index) and show_skip_button
    $ _skip_icon = ("gui/skip_button_selected.png" if skipping_messages_enabled else "gui/skip_button.png")
    $ _skip_action = None
    if _show_skip:
        if not skipping_messages_enabled:
            $ _skip_action = [
                SetVariable("message_timer_delay", skip_speed_timer),
                SetVariable("skipping_messages_enabled", True),
                SetVariable("min_speak_timer", 0)
            ]
        else:
            $ _skip_action = [
                SetVariable("message_timer_delay", auto_speak_timer),
                SetVariable("skipping_messages_enabled", False),
                SetVariable("min_speak_timer", original_min_speak_timer)
            ]

    use phone_shell(title=_title, subtitle=_sub, back_action=[
            Hide("dynamic_scrollable_text_group"), 
            Show("character_select"),
            SetVariable("current_conversation", None),
            SetVariable("_var_kps_current_convo", None)],
            right_action=_skip_action, right_icon=(_skip_icon if _show_skip else None)):

        

        fixed:
            xfill True
            yfill True

            # Chat list panel
            frame:
                style ikps_style("phone_panel")
                xfill True
                yfill True

                has viewport yadjustment yadj id "chat_vp":
                    draggable True
                    mousewheel True

                    vbox:
                        xfill True
                        spacing 8

                        for entry in work_list_name:
                            $ key, value = list(entry.items())[0]

                            if key == "image":
                                if 'speaker' in entry:
                                    if last_speaker != entry['speaker']:
                                        frame:
                                            style ikps_style("phone_system_chip")
                                            xalign 0
                                            text entry['speaker'] style ikps_style("phone_status_text") color ikps_theme_color("muted", PHONE_C_MUTED)
                                        $ last_speaker = entry['speaker']

                                if 'scale' in entry:
                                    $ imgwidth = entry['scale'][0]
                                    $ imgheight = entry['scale'][1]
                                else:
                                    $ imgwidth, imgheight = chat_image_size[0], chat_image_size[1]
                                button:
                                    background None
                                    action Show("fullscreen_image", image_path=value)
                                    add Image(value) xalign 0.0 size (imgwidth, imgheight)

                            elif key == "video" and not entry.get('seen', False):
                                if 'speaker' in entry:
                                    if last_speaker != entry['speaker']:
                                        frame:
                                            style ikps_style("phone_system_chip")
                                            xalign 0
                                            text speaker style ikps_style("phone_status_text") color ikps_theme_color("muted", PHONE_C_MUTED)
                                        $ last_speaker = entry['speaker']
                                $ video_path = value["file"]
                                $ thumbnail = value.get("thumbnail", "gui/video_thumbnail.png")
                                button:
                                    background None
                                    action Show("fullscreen_video", video_path=video_path)
                                    add Image(thumbnail) size (216, 384)

                                # Wow this only took me 2 energy drinks of time? I'm improving.....

                            else:
                                $ speaker = key
                                $ line = value
                                $ color = ikps_theme_color("text", PHONE_C_TEXT)
                                $ safe_line = line if not isinstance(line, str) else line.replace("{", "{{").replace("}", "}}")
                                if speaker == phone_data['name']:
                                    $ last_speaker = None
                                    if not entry.get('seen', False) and message_animations:
                                        frame at slide_in_right:
                                            style ikps_style("phone_bubble_sent")
                                            xalign 1.0
                                            xmaximum 320
                                            text safe_line color color size var_kps_text_size substitute False
                                    else:
                                        frame:
                                            style ikps_style("phone_bubble_sent")
                                            xalign 1.0
                                            xmaximum 320
                                            text safe_line color color size var_kps_text_size substitute False

                                elif speaker == "system":
                                    $ last_speaker = None
                                    frame:
                                        style ikps_style("phone_system_chip")
                                        xalign 0.5
                                        text safe_line style ikps_style("phone_status_text") color ikps_theme_color("muted", PHONE_C_MUTED)

                                else:
                                    if speaker != last_speaker:
                                        # logic for speaker change here
                                        frame:
                                            style ikps_style("phone_system_chip")
                                            xalign 0
                                            text speaker style ikps_style("phone_status_text") color ikps_theme_color("muted", PHONE_C_MUTED)
                                        $ last_speaker = speaker
                                    if not entry.get('seen', False) and message_animations:
                                        frame at slide_in_left:
                                            style ikps_style("phone_bubble_recv")
                                            xalign 0.0
                                            xmaximum 320
                                            text safe_line color color size var_kps_text_size
                                    else:
                                        frame:
                                            style ikps_style("phone_bubble_recv")
                                            xalign 0.0
                                            xmaximum 320
                                            text safe_line color color size var_kps_text_size

                        if continue_list:
                            null height 240

            # Manual "next" / send icon 
            if continue_list == False and (not auto_continue):
                button:
                    style ikps_style("phone_fab_btn")
                    xalign 0.97
                    yalign 0.95
                    action [Function(conditional_add_line, character_info_for_dialogue),
                            Function(renpy.retain_after_load)] 
                        
                    add "gui/message_icon.png" xysize (44, 44)

            # Choices overlay
            if continue_list:
                $ choice_list = full_list[-1]

                frame:
                    style ikps_style("phone_panel_soft")
                    xfill True
                    yalign 1.0

                    vbox:
                        spacing 10
                        for choice in choice_list:
                            textbutton choice[0] style ikps_style("rounded_button"):
                                text_color ikps_theme_color("rounded_text", "#0b0e14")
                                action [
                                    Function(handle_choice, choice[1], character_info_for_dialogue),
                                    Show("dynamic_scrollable_text_group", character_info_for_dialogue=character_info_for_dialogue, continue_list=False)
                                ]
    
    if work_list_name:
        $ _last = work_list_name[-1]
        if isinstance(_last, dict):
            $ _k = next(iter(_last.keys()), None)
            if _k not in ("video", "image") and (not _last.get("seen", False)) and message_animations:
                timer 0.35 repeat False action Function(mark_entry_seen, _last)

    # Scroll to bottom helper 
    if character_info_for_dialogue.get("scroll_to_bottom", False):
        $ yadj.value = float('inf')
        $ character_info_for_dialogue["scroll_to_bottom"] = False




# ----------------------------------------#
#          Fullscreen Videos              #
# ----------------------------------------#

screen fullscreen_video(video_path):

    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag fullscreen_video
    zorder 200

    add Solid("#000000cc")
    add Movie(size=(1280, 720), play=video_path) xalign 0.5 yalign 0.5

    key "dismiss" action Hide("fullscreen_video")

    button:
        action Hide("fullscreen_video")
        background None
        xfill True
        yfill True

# ----------------------------------------#
#          Fullscreen Images              #
# ----------------------------------------#

screen fullscreen_image(image_path, background=False):

    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag fullscreen_image

    zorder 200

    add Solid("#000000cc")
    add image_path:
        xalign 0.5
        yalign 0.5
        fit "contain"

    key "dismiss" action Hide("fullscreen_image")

    # Close button
    button:
        style ikps_style("phone_icon_btn")
        xalign 0.96
        yalign 0.06
        action Hide("fullscreen_image")
        text "✕" style ikps_style("phone_title") size 18

    if background:
        button:
            style ikps_style("phone_fab_btn")
            xalign 0.96
            yalign 0.92
            action [SetVariable("phone_screen_bg", image_path), Hide("fullscreen_image")]
            add "gui/confirm_tick.png" xysize (44, 44)

# ----------------------------------------#
#          Character Select               #
# ----------------------------------------#

screen character_select():
    modal var_kps_phone_locked
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag kps_phone


    $ unlocked_contacts = []

    python:
        for conversation in phone_messages_registry:
            for key, item in conversation.items():
                if key == "members":
                    if phone_data["name"] in item:
                        unlocked_contacts.append(conversation)
        

        for contact in unlocked_contacts:
            _kps_ensure_index(contact)
            
            
                

    use phone_shell(title="Contacts", subtitle="Pick a chat", back_action=[Show("phone_home")]):

        frame:
            style ikps_style("phone_panel")
            xfill True
            yfill True

            has viewport:
                mousewheel True
                draggable True

                vbox:
                    spacing 10
                    xfill True
                    for char in unlocked_contacts:
                        
                        if len(char['members']) > 2:
                            $ group_chat = True
                        else:
                            $ group_chat = False
                        $ profile = var_kps_default_profile
                        $ name = "Unknown"
                        if not group_chat: 
                            for key, item in char['members'].items():
                                if key != phone_data['name']:
                                    $ name = key
                                    $ profile = item.get('profile' ,var_kps_default_profile)
                                if key == phone_data['name']:
                                    $ should_disable = bool(item.get("disable_messaging", False))
                                    $ should_disable_inverse = not should_disable
                                if force_disable_all_phones:
                                    $ should_disable_inverse = False
                            button:
                                style ikps_style("phone_card_btn")
                                action [
                                    Hide("dynamic_scrollable_text"),
                                    Hide("character_select"),
                                    Function(renpy.retain_after_load),
                                    Function(lambda char=char: char.__setitem__("scroll_to_bottom", True)),
                                    SetVariable("current_conversation", char["name"]),
                                    SetVariable("messaging_enabled", should_disable_inverse),
                                    Show("dynamic_scrollable_text", character_info_for_dialogue=char)
                                ]

                                has hbox:
                                    spacing 12
                                    xfill True

                                fixed:
                                    xysize (62, 62)
                                    add profile size (62, 62)

                                    $ char_current_index = getattr(store, char['current_index'])
                                    $ char_current_dialogue = char['current_dialogue']
                                    if isinstance(char_current_dialogue, str):
                                        $ char_current_dialogue = getattr(store, char_current_dialogue)
                                    if char_current_index < len(char_current_dialogue):
                                        add Solid(ikps_theme_color("badge", PHONE_C_BADGE)) xysize (14, 14) xpos 46 ypos 2

                                vbox:
                                    spacing 2
                                    xfill True
                                    xalign 0.0
                                    text name style ikps_style("phone_body_text") xalign 0.0 textalign 0.0
                                    $ _preview = ""
                                    $ _preview = ikps_last_message_preview(char)
                                    if _preview:
                                        text _preview style ikps_style("phone_status_text") color ikps_theme_color("muted", PHONE_C_MUTED) xmaximum 260 xalign 0.0 textalign 0.0
                        if group_chat:
                            for key, item in char['members'].items():
                                if key == phone_data['name']:
                                    $ should_disable = bool(item.get("disable_messaging", False))
                                    $ should_disable_inverse = not should_disable
                                if force_disable_all_phones:
                                    $ should_disable_inverse = False
                            $ profile = char.get('profile' ,var_kps_default_profile)
                            $ name = char["name"]
                            button:
                                style ikps_style("phone_card_btn")
                                action [
                                    Hide("dynamic_scrollable_text_group"),
                                    Hide("character_select"),
                                    Function(renpy.retain_after_load),
                                    Function(lambda char=char: char.__setitem__("scroll_to_bottom", True)),
                                    SetVariable("current_conversation", char["name"]),
                                    SetVariable("messaging_enabled", should_disable_inverse),
                                    Show("dynamic_scrollable_text_group", character_info_for_dialogue=char)
                                ]

                                has hbox:
                                    spacing 12
                                    xfill True

                                fixed:
                                    xysize (62, 62)
                                    add profile size (62, 62)


                                    $ char_current_index = getattr(store, char['current_index'])
                                    $ char_current_dialogue = char['current_dialogue']
                                    if isinstance(char_current_dialogue, str):
                                        $ char_current_dialogue = getattr(store, char_current_dialogue)
                                    if char_current_index < len(char_current_dialogue):
                                        add Solid(ikps_theme_color("badge", PHONE_C_BADGE)) xysize (14, 14) xpos 46 ypos 2

                                vbox:
                                    spacing 2
                                    xfill True
                                    xalign 0.0
                                    text name style ikps_style("phone_body_text") xalign 0.0 textalign 0.0
                                    $ _preview = ""
                                    $ _preview = ikps_last_message_preview(char)

# ----------------------------------------#
#             Gallery Screen              #
# ----------------------------------------#

screen gallery_character_select():
    modal var_kps_phone_locked
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag kps_phone

    zorder 100

    $ rows = math.ceil(len(character_names_to_scan)/image_columns)

    use phone_shell(title="Gallery", subtitle="Pick a character", back_action=[Hide("gallery_character_select"), Show("phone_home")]):

        frame:
            style ikps_style("phone_panel")
            xfill True
            yfill True

            has viewport:
                mousewheel True
                draggable True

                grid image_columns rows spacing 16:
                    for char_name, data in phone_data['gallery'].items():
                        $ profile = data["gallery image"]

                        button:
                            style ikps_style("phone_card_btn")
                            xsize 160
                            ysize 120
                            action Show("gallery_view_screen", character=char_name)

                            has vbox
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            add profile size (72, 72) xalign 0.5
                            text char_name style ikps_style("phone_status_text") xalign 0.5

# ----------------------------------------#
#          Gallery View Screen            #
# ----------------------------------------#

screen gallery_view_screen(character):
    modal var_kps_phone_locked
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag kps_phone

    zorder 100

    $ images = gallery_data[character]["images"]
    $ rows = math.ceil(len(images)/image_columns)
    $ all_unlocked = list(set(unlocked_images + (persistent.persistent_gallery or [])))

    use phone_shell(title=character, subtitle="Gallery", back_action=[Hide("gallery_view_screen"), Show("gallery_character_select")]):

        frame:
            style ikps_style("phone_panel")
            xfill True
            yfill True

            has viewport:
                mousewheel True
                draggable True

                grid image_columns rows spacing 16:
                    for img_path in images:

                        if img_path in all_unlocked:
                            button:
                                style ikps_style("phone_card_btn")
                                xsize 155
                                ysize 276
                                action Show("fullscreen_image", image_path=img_path)
                                add img_path size (155, 276)
                        else:
                            fixed:
                                xsize 155
                                ysize 276
                                add img_path size (155, 276)
                                add Solid("#000000f2") xysize (155, 276)
                                text "LOCKED" style ikps_style("phone_status_text") color "#ffffff66" xalign 0.5 yalign 0.5

# ----------------------------------------#
#        Theme Select Screen              #
# ----------------------------------------#

screen background_select:
    modal var_kps_phone_locked

    use phone_shell(title="Themes", subtitle="Tap to apply", back_action=[Hide("background_select"), Show("phone_home")]):

        $ theme_list = (PHONE_THEME_SWATCHES if "PHONE_THEME_SWATCHES" in globals() else [])


        if theme_list:
            frame:
                style ikps_style("phone_panel_soft")
                xfill True
                yfill True

                viewport:
                    xfill True
                    yfill True
                    draggable True
                    mousewheel True
                    scrollbars "vertical"

                    vpgrid:
                        cols 2
                        spacing 14
                        xalign 0.5

                        for label, key, preview in theme_list:
                            $ th = PHONE_THEMES.get(key, None)
                            $ prev_recv = th.bubble_recv if th else "#ffffff18"
                            $ prev_sent = th.bubble_sent if th else "#2f6cffcc"

                            button:
                                style ikps_style("phone_card_btn")
                                xsize 155
                                ysize 140
                                action Function(ikps_set_phone_theme, key)

                                has vbox
                                spacing 10
                                xalign 0.5
                                yalign 0.5

                                fixed:
                                    xysize (120, 80)
                                    add Solid(preview) xysize (120, 80)
                                    add Solid(prev_recv) xysize (56, 22) xpos 10 ypos 12
                                    add Solid(prev_sent) xysize (56, 22) xpos 54 ypos 44

                                    if ikps_get_theme() == key:
                                        add "gui/confirm_tick.png" zoom 0.07 xalign 1.0 yalign 0.0 xoffset 6 yoffset -6

                                text label style ikps_style("phone_status_text") xalign 0.5

        else:
            text "No themes found." style ikps_style("phone_hint_text") xalign 0.5


# ----------------------------------------#
#            Settings Screen              #
# ----------------------------------------#


screen phone_settings_screen():
    modal var_kps_phone_locked

    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag kps_phone

    zorder 100

    use phone_shell(title="Settings", subtitle="Tweak things", back_action=[Hide("phone_settings_screen"), Show("phone_home")]):

        frame:
            style ikps_style("phone_panel")
            xfill True
            yfill True

            vbox:
                spacing 16
                xfill True



                frame:
                    style ikps_style("phone_panel_soft")
                    xfill True

                    vbox:
                        spacing 8

                        text "Average Message Delay" style ikps_style("phone_body_text")
                        text "[auto_speak_timer:.2f] seconds" style ikps_style("phone_status_text")

                        bar:
                            value VariableValue("auto_speak_timer", min=0.1, max=20.0, step=0.1)
                            xmaximum 320
                            ymaximum 12
                            left_bar Solid(PHONE_C_ACCENT)
                            right_bar Solid("#ffffff20")
                            thumb Solid("#ffffffaa")

                        text "Message delay when skipping" style ikps_style("phone_body_text")
                        text "[skip_speed_timer:.2f] seconds" style ikps_style("phone_status_text")

                        bar:
                            value VariableValue("skip_speed_timer", min=0.1, max=1.0, step=0.01)
                            xmaximum 320
                            ymaximum 12
                            left_bar Solid(PHONE_C_ACCENT)
                            right_bar Solid("#ffffff20")
                            thumb Solid("#ffffffaa")


                        text "Notification volume" style ikps_style("phone_body_text")
                        text "[var_kps_notification_volume:.2f]" style ikps_style("phone_status_text")

                        bar:
                            value VariableValue("var_kps_notification_volume", min=0.0, max=1.0, step=0.01)
                            changed kps_apply_notification_volume(var_kps_notification_volume)
                            xmaximum 320
                            ymaximum 12
                            left_bar Solid(PHONE_C_ACCENT)
                            right_bar Solid("#ffffff20")
                            thumb Solid("#ffffffaa")

                        text "Message volume" style ikps_style("phone_body_text")
                        text "[var_kps_message_sound_volume:.2f]" style ikps_style("phone_status_text")

                        bar:
                            value VariableValue("var_kps_message_sound_volume", min=0.0, max=1.0, step=0.01)
                            changed kps_apply_message_volume(var_kps_message_sound_volume)
                            xmaximum 320
                            ymaximum 12
                            left_bar Solid(PHONE_C_ACCENT)
                            right_bar Solid("#ffffff20")
                            thumb Solid("#ffffffaa")

                        text "Text size" style ikps_style("phone_body_text")
                        text "[var_kps_text_size:.0f]" style ikps_style("phone_status_text")

                        bar:
                            value VariableValue("var_kps_text_size", min=5, max=30, step=1)
                            xmaximum 320
                            ymaximum 12
                            left_bar Solid(PHONE_C_ACCENT)
                            right_bar Solid("#ffffff20")
                            thumb Solid("#ffffffaa")

                        if var_kps_allow_clickthrough_toggle:
                            text "Allow Clickthrough (Close phone to apply)" style ikps_style("phone_body_text")
                            null width 0 xfill True

                            textbutton ("☑" if not var_kps_phone_locked else "☐"):
                                style ikps_style("phone_status_text")  
                                action ToggleVariable("var_kps_phone_locked", True, False)



                text "More settings can live here later." style ikps_style("phone_hint_text")

# ----------------------------------------#
#              Home Screen                #
# ----------------------------------------#

screen phone_home():
    modal var_kps_phone_locked
    zorder 100
    tag kps_phone
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]





    use phone_shell(title="Home", subtitle="[phone_data['name'].capitalize()]'s phone", back_action=([ikps_phone_home_back_action] if var_kps_show_back_button_home else []), var_kps_show_back=True):

        frame:
            style ikps_style("phone_panel")
            xfill True
            yfill True

            vbox:
                spacing 18
                xalign 0.5
                yalign 0.5

                # App grid
                grid 3 2 spacing 18:
                    xalign 0.5

                    button:
                        style ikps_style("phone_card_btn")
                        xysize (110, 110)
                        action [Show("character_select"), Hide("phone_home")]
                        vbox:
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            add "gui/message_icon.png" xysize (48, 48) xalign 0.5
                            text "Messages" style ikps_style("phone_status_text") xalign 0.5

                    button:
                        style ikps_style("phone_card_btn")
                        xysize (110, 110)
                        action [Hide("phone_home"), Show("gallery_character_select")]
                        vbox:
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            add "gui/gallery_icon.png" xysize (48, 48) xalign 0.5
                            text "Gallery" style ikps_style("phone_status_text") xalign 0.5

                    if settings_screen_shown:
                        button:
                            style ikps_style("phone_card_btn")
                            xysize (110, 110)
                            action [Hide("phone_home"), Show("phone_settings_screen")]
                            vbox:
                                spacing 8
                                xalign 0.5
                                yalign 0.5
                                add "gui/settings_icon.png" xysize (48, 48) xalign 0.5
                                text "Settings" style ikps_style("phone_status_text") xalign 0.5
                    else:
                        null

                    button:
                        style ikps_style("phone_card_btn")
                        xysize (110, 110)
                        action [Hide("phone_home"), Show("background_select")]
                        vbox:
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            add "gui/background_icon.png" xysize (48, 48) xalign 0.5
                            text "Themes" style ikps_style("phone_status_text") xalign 0.5

                    if hasattr(store, "wordle_game_app"):
                        button:
                            style ikps_style("phone_card_btn")
                            xysize (110, 110)
                            action [Hide("phone_home"), Show("phone_games_screen")]
                            vbox:
                                spacing 8
                                xalign 0.5
                                yalign 0.5
                                add "gui/game_icon.png" xysize (48, 48) xalign 0.5
                                text "Games" style ikps_style("phone_status_text") xalign 0.5
                    

                        if hasattr(store, "nav_left_action"):
                            button:
                                style ikps_style("phone_card_btn")
                                xysize (110, 110)
                                action [Hide("phone_home"), Show("ikps_date_app")]
                                vbox:
                                    spacing 8
                                    xalign 0.5
                                    yalign 0.5
                                    add "gui/dating_icon.png" xysize (48, 48) xalign 0.5
                                    text "Dating app" style ikps_style("phone_status_text") xalign 0.5



###################################################
################## NOTIFICATIONS ##################
###################################################


init -10 python:
    if "phone_toast" not in config.layers:
        config.layers.append("phone_toast")

    if hasattr(config, "menu_clear_layers") and "phone_toast" in config.menu_clear_layers:
        config.menu_clear_layers.remove("phone_toast")


init -2:
    style toast_sender_text is default:
        size 28
        color "#f2f2f2"
        outlines [(2, "#00000088", 0, 0)]

    style toast_msg_text is default:
        size 22
        color "#d6d6d6"
        outlines [(2, "#00000066", 0, 0)]

transform toast_anim:
    on show:
        yoffset -120
        alpha 0.0
        easeout 0.18 yoffset 0 alpha 1.0
    on hide:
        easein 0.18 yoffset -120 alpha 0.0


init python:
    

    PHONE_NOTIF_DM_SCREEN = "dynamic_scrollable_text"
    PHONE_NOTIF_GROUP_SCREEN = "dynamic_scrollable_text_group"
    PHONE_NOTIF_TOAST_SCREEN = "phone_notif_toast"
    PHONE_NOTIF_LAYER = "phone_toast"

    def phone_notif_open(conversation, group_chat, which_phone):
        if not isinstance(conversation, dict):
            return

        if not hasattr(store, "phone_data") or store.phone_data is None or not isinstance(store.phone_data, dict):
            store.phone_data = {}
        else:
            store.phone_data = dict(store.phone_data)

        if isinstance(which_phone, dict) and "name" in which_phone:
            store.phone_data = copy.deepcopy(which_phone)

        owner_name = store.phone_data.get("name")

        if group_chat:
            current_conversation = conversation.get("name")
            screen_name = PHONE_NOTIF_GROUP_SCREEN
        else:
            other_person = next(m for m in conversation["members"] if m != phone_data["name"])
            current_conversation = other_person
            screen_name = PHONE_NOTIF_DM_SCREEN
        setattr(store, "current_conversation", conversation["name"])
        renpy.show_screen(
            screen_name,
            character_info_for_dialogue=conversation,
            continue_list=False,
            set_scroll_to_bottom = True
        )


    def kps_phone_notif_show(conversation: dict, 
        sender: "str or None" = None, 
        message: "str or None" = None, 
        pfp: "str or None" = None,
        group_chat: bool = False,
        which_phone: "dict or None" = None,
        timeout: float = 2.5):
        """
        Sends a notification, click to open the conversation where the message came from. 
        All aspects of the notification can be modified by passing additional parameters, but are optional. 
        Will send from the last phone opened by default. Pass which_phone =, to change. 
        """

        

        if not isinstance(conversation, dict):
            return

        store = renpy.store

        if not hasattr(store, "phone_data") or store.phone_data is None or not isinstance(store.phone_data, dict):
            store.phone_data = {}

        owner_name = None
        if isinstance(which_phone, dict) and "name" in which_phone:
            owner_name = which_phone.get("name")
        else:
            owner_name = store.phone_data.get("name")

        other_person = None
        if not group_chat:
            members = conversation.get("members") or {}
            for k in members.keys():
                if k != owner_name:
                    other_person = k
                    break


        if sender is None:
            sender = conversation.get("name", "group") if group_chat else (other_person or "unknown")


        if pfp is None:
            if group_chat:
                pfp = conversation.get("profile")
            else:
                members = conversation.get("members") or {}
                if other_person and other_person in members:
                    pfp = (members.get(other_person) or {}).get("profile")


        if message is None:
            dialogue = conversation.get("all_dialogue") or []
            last = dialogue[-1] if dialogue else None

            if not isinstance(last, dict) or not last:
                message = "has messaged you"

            if "code" in last:
                return 

            else:
                if not group_chat:
                    if other_person and other_person in last and isinstance(last.get(other_person), str):
                        message = last[other_person]
                    elif "image" in last:
                        message = ("%s sent an image" % other_person) if other_person else "Sent an image"
                    else:
                        message = "has messaged you"
                else:
                    if "image" in last:
                        img_sender = last.get("sender")
                        message = ("%s sent an image" % img_sender) if img_sender else "Sent an image"
                    else:
                        members = conversation.get("members") or {}
                        picked = None
                        for k, v in last.items():
                            if not isinstance(v, str):
                                continue
                            if k in ("system", "delete", "image", "sender", "scale"):
                                continue
                            if k in members or picked is None:
                                picked = v
                                if k in members:
                                    break
                        message = picked if picked is not None else "has messaged you"

        try:
            renpy.hide_screen(PHONE_NOTIF_TOAST_SCREEN, layer=PHONE_NOTIF_LAYER)
        except Exception:
            renpy.hide_screen(PHONE_NOTIF_TOAST_SCREEN)
        _kps_ensure_index(conversation)
        renpy.play(var_kps_phone_notification_sound, channel="kps_phone_notifications")
        renpy.show_screen(
            PHONE_NOTIF_TOAST_SCREEN,
            sender=sender,
            message=message,
            pfp=pfp,
            conversation=conversation,
            group_chat=group_chat,
            which_phone=which_phone,
            timeout=timeout,
            _layer=PHONE_NOTIF_LAYER
        )

        renpy.restart_interaction()


screen phone_notif_toast(sender, message, pfp=None, conversation=None, group_chat=False, which_phone=None, timeout=2.5):
    zorder 9999999

    button:
        xalign 0.5
        yalign 0.0
        yoffset 24

        action [
            Function(renpy.hide_screen, "phone_notif_toast", layer="phone_toast"),
            Function(phone_notif_open, conversation, group_chat, which_phone),
        ]

        at toast_anim

        background Frame(Solid("#0b0d12e6"), 18, 18)
        padding (18, 12)
        xmaximum 980

        has hbox spacing 14

        if pfp:
            add pfp:
                xsize 72
                ysize 72
        else:
            add Solid("#1f2430"):
                xsize 72
                ysize 72

        vbox:
            spacing 4
            text sender style "toast_sender_text"
            text message style "toast_msg_text":
                xmaximum 860
                slow_cps None

    timer timeout action Function(renpy.hide_screen, "phone_notif_toast", layer="phone_toast")



# ----------------------------------------#
#              Games Screen               #
# ----------------------------------------#

screen phone_games_screen():
    zorder 100
    tag kps_phone
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    python:
        renpy.hide("phone_icon_overlay")




    use phone_shell(title="Games", subtitle="Games", back_action=[Hide("phone_games_screen"), Show("phone_home")]):

        frame:
            style ikps_style("phone_panel")
            xfill True
            yfill True

            vbox:
                spacing 18
                xalign 0.5
                yalign 0.5

                # App grid
                grid 3 2 spacing 18:
                    xalign 0.5

                    button:
                        style ikps_style("phone_card_btn")
                        xysize (110, 110)
                        action [Show("phon_minigame_wordle")]
                        vbox:
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            add "gui/phonedle_icoon.png" xysize (48, 48) xalign 0.5
                            text "Phonedle" style ikps_style("phone_status_text") xalign 0.5
                    
                    button:
                        style ikps_style("phone_card_btn")
                        xysize (110, 110)
                        action [Show("phone_tetris_screen")]
                        vbox:
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            add "gui/phonetris_icon.png" xysize (48, 48) xalign 0.5
                            text "Phonetris" style ikps_style("phone_status_text") xalign 0.5



