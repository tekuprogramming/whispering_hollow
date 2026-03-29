default influenced_by_whisper = 0
default follow_whisper = 0
default trust_damon = 0
default trust_iris = 0
default locations_visited = 0
default clues = []
default church_done = False
default alley_done = False
default archives_done = False
default tunnels_done = False
default hospital_done = False
default final_clues = []
default ritual_understood = False
default whisper_source_known = False
default silas_exposed = False
default hospital_clue = False
default alley_clue = False
default tunnel_clue = False

transform char_big:
    zoom 1.35

image elias happy = "images/characters/elias/elias_happy.png"
image elias neutral = "images/characters/elias/elias_neutral.png"
image elias nervous = "images/characters/elias/elias_nervous.png"
image elias suspicious = "images/characters/elias/elias_suspicious.png"
image elias thinking = "images/characters/elias/elias_thinking.png"

image damon happy = "images/characters/damon/damon_happy.png"
image damon neutral = "images/characters/damon/damon_neutral.png"
image damon nervous = "images/characters/damon/damon_nervous.png"
image damon suspicious = "images/characters/damon/damon_suspicious.png"
image damon thinking = "images/characters/damon/damon_thinking.png"

image iris happy = "images/characters/iris/iris_happy.png"
image iris neutral = "images/characters/iris/iris_neutral.png"
image iris nervous = "images/characters/iris/iris_nervous.png"
image iris suspicious = "images/characters/iris/iris_suspicious.png"
image iris thinking = "images/characters/iris/iris_thinking.png"

image silas happy = "images/characters/silas/silas_happy.png"
image silas neutral = "images/characters/silas/silas_neutral.png"
image silas nervous = "images/characters/silas/silas_nervous.png"
image silas suspicious = "images/characters/silas/silas_suspicious.png"
image silas thinking = "images/characters/silas/silas_thinking.png"

image bg town_fog = im.Scale("images/backgrounds/town_fog.jpg", 1920, 1080)
image bg town_day = im.Scale("images/backgrounds/town_day.jpg", 1920, 1080)
image bg town_night =im.Scale("images/backgrounds/town_night.jpg", 1920, 1080) 
image bg police_station = im.Scale("images/backgrounds/police_station.jpg", 1920, 1080)
image bg interrogation_room = im.Scale("images/backgrounds/interrogation_room.jpg", 1920, 1080)
image bg mayor_office = im.Scale("images/backgrounds/mayor_office.jpg", 1920, 1080)
image bg church = im.Scale("images/backgrounds/church.jpg", 1920, 1080)
image bg alley = im.Scale("images/backgrounds/alley.jpg", 1920, 1080)
image bg archives = im.Scale("images/backgrounds/archives.jpg", 1920, 1080)
image bg tunnels = im.Scale("images/backgrounds/tunnels.jpg", 1920, 1080)
image bg hospital = im.Scale("images/backgrounds/hospital.jpg", 1920, 1080)
image bg station_basement = im.Scale("images/backgrounds/station_basement.jpg", 1920, 1080)
image bg holding_room = im.Scale("images/backgrounds/holding_room.jpg", 1920, 1080)

define e = Character("Elias Ward")
define d = Character("Damon Reeves")
define i = Character("Iris Vale")
define s = Character("Silas Crowe")
define w = Character("Whisper", italic=True, what_color="#cccccc")

init python:

    def pull_mouse_toward(target_x, target_y, strength=0.08):

        if (
            renpy.get_screen("_game_menu") or
            renpy.get_screen("save") or
            renpy.get_screen("load") or
            renpy.get_screen("preferences") or
            renpy.get_screen("yesno_prompt")
        ):
            return

        mx, my = renpy.get_mouse_pos()

        if mx is None:
            return

        nx = mx + (target_x - mx) * strength
        ny = my + (target_y - my) * strength

        renpy.set_mouse_pos(int(nx), int(ny))


label start:

    scene bg town_fog
    with fade

    "Ravenbrook greeted me the way dying towns often do - quietly, as if hoping I wouldn't notice how wrong everything felt."

    "Fog pressed against the buildings, swallowing edges, softening shapes. Even sound seemed reluctant to travel."

    "I checked the case file again. One missing woman. No witnesses willing to commit to a statement. No signs of struggle."

    "Places like this don't ask for help, I thought."
    
    "They wait for things to disappear."

    e "Alright. Let's see what you're hiding."

    play sound "whisper.ogg"

    w "Elias..."

    "I stopped walking."

    "No footsteps behind me. No voices nearby."

    "Just my name, breathed out like it already belonged to the fog."

    jump arrival_choice

label arrival_choice:

    menu:
        "Acknowledge the whisper":
            $ follow_whisper += 1
            $ influenced_by_whisper += 1
            "I didn't turn around. Whatever it was, panic would only make it worse."
            "Still... my skin prickled, like I'd been noticed."
            jump police_station_intro

        "Ignore it and focus on the case":
            $ follow_whisper = max(0, follow_whisper - 1)
            "I exhaled slowly. Stress does things to the mind. Especially in places like this."
            "I needed facts, not ghosts."
            jump police_station_intro

label police_station_intro:

    scene bg police_station
    with fade

    show damon suspicious at left, char_big
    show elias neutral at right, char_big

    "The police station looked more like an afterthought than a building meant to enforce order."

    "A man leaned against a desk near the entrance - tall, broad-shouldered, eyes sharp enough to cut."

    d "You must be Ward."

    "His tone wasn't hostile. But it wasn't welcoming either."

    e "Detective Elias Ward. I'm here about the missing woman."

    d "Damon Reeves. Local law enforcement."

    "He didn't offer a handshake. Didn't offer much of anything."

    show damon suspicious at char_big

    d "We've handled it."

    "That was the first lie."

    menu:
        "Press Damon for details":
            $ trust_damon += 1
            show elias suspicious at char_big
            "I met his stare. Long enough to make silence uncomfortable."
            e "Then you won't mind telling me what you missed."
            "His jaw tightened."
            jump damon_reacts

        "Let it go for now":
            "I nodded. Too easily."
            "Sometimes people talked more when they thought you weren't listening."
            jump damon_reacts

label damon_reacts:

    d "We've got a witness. Iris Vale."

    "The way he said her name - clipped, cautious - told me she wasn't just a witness."

    d "She's... unstable."

    "Or scared, I thought."

    e "Where can I find her?"

    d "Interview room. Down the hall."

    "As I walked away, I felt his eyes on my back."

    "Some people guard secrets like they're protecting someone. Others guard them like they're protecting themselves."

    hide damon
    hide elias

    jump iris_intro

label iris_intro:

    scene bg interrogation_room
    with fade

    show iris nervous at center, char_big
    show elias neutral at right, char_big

    "Iris Vale sat alone at the metal table, fingers locked together so tightly her knuckles had gone pale."

    "She looked young. Too young to be carrying this much fear."

    "Her eyes snapped up when I entered."

    i "You're not from here."

    e "That obvious?"

    "A weak smile flickered across her face. Then vanished."

    i "They said someone would come."

    "They. Not Damon. Not the police."

    e "I'm here to ask about what you saw."

    "She swallowed."

    i "I didn't see it happen."

    "First sentence. First contradiction."

    "Good. That meant there was truth buried somewhere underneath."

    menu:
        "Push gently - establish trust":
            $ trust_iris += 1
            "I pulled the chair back slowly and sat."
            e "Then tell me what you did see."
            jump iris_soft_path

        "Apply pressure - test her story":
            $ trust_iris -= 1
            "I stayed standing."
            e "You gave a statement. Statements come from something."
            jump iris_hard_path

label iris_soft_path:

    show iris thinking at char_big
    show elias neutral at char_big

    "Her shoulders loosened just a little."

    i "I heard her scream."

    i "And then... something else."

    e "What kind of something?"

    i "Like a voice. But not a person."

    play sound "whisper.ogg"

    w "She remembers."

    "My chest tightened."

    hide iris
    hide elias

    jump post_iris

label iris_hard_path:

    show iris nervous at char_big
    show elias suspicious at char_big

    "Her eyes darted to the one-way mirror."

    i "They're listening."

    e "Who is?"

    "She shook her head violently."

    i "If I say it out loud, it hears."

    play sound "whisper.ogg"

    w "Careful."

    "I felt the word settle somewhere behind my eyes."

    hide iris
    hide elias

    jump post_iris

label post_iris:

    scene bg police_station
    with fade

    show damon neutral at left, char_big
    show elias neutral at right, char_big

    "When I left the room, my notes were a mess."

    "A scream. A voice. A town pretending not to notice."

    "That's when Damon stopped me in the hall."

    d "The mayor wants to see you."

    e "The mayor?"

    d "Silas Crowe."

    "Of course he did."

    "Small towns always funnel power into one smiling face."

    jump silas_intro

label silas_intro:

    scene bg mayor_office
    with fade

    show silas happy at center, char_big
    show elias neutral at right, char_big

    "Silas Crowe's office was warm - deliberately so."

    "Wood-paneled walls. Soft lighting. Everything designed to put people at ease."

    "It didn't work."

    s "Detective Ward."

    "He rose from behind his desk, offering a hand."

    "I noticed his eyes first. Dark. Observant. Curious in a way that felt... personal."

    e "Mayor Crowe."

    s "Ravenbrook appreciates your concern."

    "He held my gaze just a second longer than necessary."

    "I couldn't tell if he was assessing me - or already deciding what I was worth."

    s "We value peace here."

    "The Whisper stirred."

    show silas suspicious at char_big
    show elias nervous at char_big

    w "He knows you."

    menu:
        "Challenge his authority politely":
            show elias suspicious at char_big
            "I kept my voice even."
            e "Peace doesn't come from ignoring problems."
            hide silas
            hide elias
            jump end_act_one

        "Let him lead the conversation":
            "I nodded, letting him talk."
            "People reveal more when they think they're in control."
            hide silas
            hide elias
            jump end_act_one

label end_act_one:

    scene bg town_fog
    with fade

    "When I stepped back into the fog, Ravenbrook felt smaller."

    "Not empty."

    "Crowded."

    "By secrets. By watchers."

    play sound "whisper.ogg"

    w "You're already part of it."

    "I wasn't sure when that had happened."

    jump act_two

label act_two:

    scene bg town_fog
    with fade

    "The air outside Silas Crowe's office felt heavier than before."

    "Not colder. Not thicker."

    "Just... aware."

    "I'd dealt with powerful men before. Politicians. Business owners. Crime lords in tailored suits."

    "Silas was different."

    "He hadn't threatened me."

    "He hadn't warned me."

    "He'd simply looked at me like I was already involved."

    play sound "whisper.ogg"

    w "He sees what you are."

    "I clenched my jaw and started walking."

    "I needed facts. Evidence. Something solid enough to anchor me."

    jump investigation_hub

screen investigation_menu(church_done, alley_done, archives_done,
    tunnels_done, hospital_done, influenced_by_whisper, follow_whisper):
    
    add Solid("#00000080")
    default forced = None
    default forced_index = None
    default visible = []

    python:
          visible = []

          if not church_done:
            visible.append("church")
          if not alley_done:
            visible.append("alley")
          if not archives_done:
            visible.append("archives")
          if not tunnels_done:
            visible.append("tunnels")
          if not hospital_done:
            visible.append("hospital")

          if influenced_by_whisper >= 2 or follow_whisper >= 2:
            if "alley" in visible:
                forced = "alley"
            elif "church" in visible:
                forced = "church"
            elif "archives" in visible:
                forced = "archives"
            elif "tunnels" in visible:
                forced = "tunnels"
            elif "hospital" in visible:
                forced = "hospital"

          if forced in visible:
            forced_index = visible.index(forced)

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5

        if not church_done:
            textbutton "Investigate the abandoned church":
                action Return("church")
                hovered SetScreenVariable("hovered", "church")

        if not alley_done:
            textbutton "Search the alleyways behind the town center":
                action Return("alley")
                hovered SetScreenVariable("hovered", "alley")

        if not archives_done:
            textbutton "Search the city archives":
                action Return("archives")
                hovered SetScreenVariable("hovered", "archives")

        if not tunnels_done:
            textbutton "Explore the underground tunnels":
                action Return("tunnels")
                hovered SetScreenVariable("hovered", "tunnels")

        if not hospital_done:
            textbutton "Check the old hospital":
                action Return("hospital")
                hovered SetScreenVariable("hovered", "hospital")

        if church_done or alley_done or archives_done or tunnels_done or hospital_done:
            textbutton "I've seen enough":
                action Return("done")

    if forced_index is not None:
        timer 0.03 repeat True action Function(
        pull_mouse_toward,
        960,
        500 + forced_index * 55,
        0.06
    )

label investigation_hub:

    "I laid out my options carefully, knowing each choice could change everything."

    $ choice = renpy.call_screen("investigation_menu",
                                 church_done=church_done,
                                 alley_done=alley_done,
                                 archives_done=archives_done,
                                 tunnels_done=tunnels_done,
                                 hospital_done=hospital_done,
                                 influenced_by_whisper=influenced_by_whisper,
                                 follow_whisper=follow_whisper)

    if choice == "church":
        $ church_done = True
        $ locations_visited += 1
        jump church_investigation

    elif choice == "alley":
        $ alley_done = True
        $ locations_visited += 1
        jump alley_investigation

    elif choice == "archives":
        $ archives_done = True
        $ locations_visited += 1
        jump archives_investigation

    elif choice == "tunnels":
        $ tunnels_done = True
        $ locations_visited += 1
        jump tunnels_investigation

    elif choice == "hospital":
        $ hospital_done = True
        $ locations_visited += 1
        jump hospital_investigation

    else:
        jump post_investigation_merge

transform move_cursor_to(target_y):
    yanchor 0.5
    yoffset 0
    linear 0.2 yoffset target_y

screen church_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 3 and not ritual_understood:
            forced = "examine"

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5

        textbutton "Examine the altar closely":
            action Return("examine")

        textbutton "Inspect the candles":
            action Return("candles")

        textbutton "Check the pews and walls":
            action Return("pews")

        textbutton "Pull back - observe without touching":
            action Return("observe")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            500,
            0.08
        )


label church_investigation:

    scene bg church
    with fade

    "Dust hung in the air, undisturbed. No services in years."
    "Yet the place didn't feel abandoned."
    "Candles sat half-melted near the altar."

    e "Someone's been using this."

    "As I stepped closer, the Whisper surged."

    play sound "whisper.ogg"

    w "This is where they listen."

    if influenced_by_whisper >= 2:
        "A strange pull guided my eyes toward the altar."

    $ choice = renpy.call_screen("church_choice", influenced_by_whisper=influenced_by_whisper)

    if choice == "examine":
        $ influenced_by_whisper += 1
        "Dark stains soaked into the cloth."
        "Too deliberate to be an accident."
        $ clues.append("Blood-stained altar cloth")
        "My stomach turned."
    elif choice == "candles":
        "Half-melted candles formed strange patterns, like they had been arranged deliberately."
        $ clues.append("Patterned candle arrangement")
    elif choice == "pews":
        "Scratches and scrawls lined the pews. Some words almost readable: 'Listen. Obey. Remember.'"
        $ clues.append("Scratched warning in pews")
    elif choice == "observe":
        "I kept my distance, taking photos instead."
        $ clues.append("Signs of recent ritual use")

    "Footsteps echoed behind me."

    show damon suspicious at left, char_big
    show elias nervous at right, char_big

    d "You shouldn't be here."

    "Damon stood in the doorway, face tight."

    e "You knew."

    "He didn't deny it."

    d "People stay safe if they follow rules."

    "Rules, I thought."
    
    "Or sacrifices."

    hide damon
    hide elias

    jump investigation_hub

screen alley_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 3 and not ritual_understood:
            forced = "follow"

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5

        textbutton "Follow the footprints":
            action Return("follow")

        textbutton "Examine strange objects in the alley":
            action Return("examine_objects")

        textbutton "Mark the location and pull back":
            action Return("pull_back")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            500,
            0.08
        )

label alley_investigation:

    scene bg alley
    with fade

    if not alley_done:
        "Fog swallowed everything beyond arm's reach."
    else:
        "The alleyways felt like they were closing in..."

    if influenced_by_whisper >= 2:
        "Every step felt watched, as if the fog itself guided me."

    "Halfway down the block, I noticed footprints."
    "Bare feet."
    "Fresh."

    $ clues.append("Bare footprints in fog")

    play sound "whisper.ogg"
    w "You're close."

    $ choice = renpy.call_screen("alley_choice", influenced_by_whisper=influenced_by_whisper)

    if choice == "follow":
        $ follow_whisper += 1
        $ influenced_by_whisper += 1
        "My pulse quickened as the fog thickened."
        "The feeling of being watched grew sharper."
        jump alley_deeper
    elif choice == "examine_objects":
        "Discarded scraps of paper and an old charm lay against the wall."
        $ clues.append("Paper scraps and charm")
        $ alley_clue = True
        "I studied the markings; they seemed ritualistic."
        jump alley_deeper
    elif choice == "pull_back":
        "I took photos and stepped away, uneasy."
        jump alley_deeper

label alley_deeper:

    "A shape moved at the edge of my vision."

    "When I turned, it was gone."

    "But the feeling remained."

    "Watched."

    jump investigation_hub

screen archives_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 4 and not whisper_source_known:
            forced = "ledger"

    vbox:
        spacing 22
        xalign 0.5
        yalign 0.5

        textbutton "Read the ledger of disappearances":
            action Return("ledger")

        textbutton "Examine city maps":
            action Return("maps")

        textbutton "Look through police records":
            action Return("records")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            500,
            0.07
        )

label archives_investigation:

    scene bg archives
    with fade

    "Dusty shelves stretched to the ceiling, filled with old records."
    "I flipped through ledgers, maps, and old police reports."

    "Some reports were decades old, detailing disappearances no one had remembered."

    $ choice = renpy.call_screen(
    "archives_choice",
    influenced_by_whisper=influenced_by_whisper)

    if choice == "ledger":
        $ final_clues.append("Ledger showing ritual intervals")
        $ final_clues.append("Diary of previous sacrifice")

    elif choice == "maps":
        $ final_clues.append("Map with repeated locations")

    elif choice == "records":
        $ final_clues.append("Suppressed police cases")

    "A cold chill ran down my spine as I realized how long this had been going on."

    jump investigation_hub

screen tunnels_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 4 and not whisper_source_known:
            forced = "symbols"

    vbox:
        spacing 22
        xalign 0.5
        yalign 0.5

        textbutton "Follow the symbols deeper":
            action Return("symbols")

        textbutton "Take photos and mark location":
            action Return("photos")

        textbutton "Listen for movement":
            action Return("listen")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            500,
            0.07
        )

label tunnels_investigation:

    scene bg tunnels
    with fade

    "The underground tunnels were damp and claustrophobic."
    "Graffiti and symbols covered the walls. Some freshly carved."

    $ choice = renpy.call_screen(
        "tunnels_choice",
        influenced_by_whisper=influenced_by_whisper)

    if choice == "symbols":

        $ final_clues.append("Strange markings on tunnel walls")
        $ tunnel_clue = True

        "I traced the carvings with my fingers."
        "The edges were sharp. Recent."

        e "These aren't old."

        play sound "whisper.ogg"
        w "Closer."

    elif choice == "photos":

        $ final_clues.append("Tunnel carvings photographed")
        $ tunnel_clue = True

        "I snapped a few photos."
        "The flash distorted the markings."

        e "That shouldn't look like that..."

        play sound "whisper.ogg"
        w "You see it now."

    elif choice == "listen":

        play sound "whisper.ogg"

        "I held my breath."

        "The whisper wasn't echoing."

        "It was breathing."

        e "I'm not alone."

        $ influenced_by_whisper += 1

    jump investigation_hub

screen hospital_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 4 and not whisper_source_known:
            forced = "listen"

    vbox:
        spacing 22
        xalign 0.5
        yalign 0.5

        textbutton "Check the patient records":
            action Return("records")

        textbutton "Investigate rooms":
            action Return("rooms")

        textbutton "Listen carefully":
            action Return("listen")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            555,
            0.08
        )

label hospital_investigation:

    scene bg hospital
    with fade

    "Broken beds and rusted equipment filled the old hospital."
    "A faint whisper called from the end of the hallway."

    $ choice = renpy.call_screen(
        "hospital_choice",
        influenced_by_whisper=influenced_by_whisper)

    if choice == "records":

        $ final_clues.append("Hospital patient logs missing")
        $ hospital_clue = True

        "The cabinets were empty."
        "Files torn out. Recently."

        e "Someone erased them."

        play sound "whisper.ogg"
        w "Names forgotten."

    elif choice == "rooms":

        $ final_clues.append("Hospital ritual traces")
        $ hospital_clue = True

        "One room was colder than the rest."

        "Symbols painted beneath peeling wallpaper."

        e "This wasn't treatment."

        e "It was preparation."

        play sound "whisper.ogg"
        w "You understand."

    elif choice == "listen":

        play sound "whisper.ogg"

        "The whisper was closer here."

        "Right behind me."

        e "...Who's there?"

        $ influenced_by_whisper += 1

    jump investigation_hub

screen damon_choice_screen(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 3:
            forced = "details"

    vbox:
        spacing 25
        xalign 0.5
        yalign 0.5

        textbutton "Condemn him":
            action Return("condemn")

        textbutton "Press for details":
            action Return("details")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            545,
            0.09
        )

label post_investigation_merge:

    scene bg police_station
    with fade

    if locations_visited == 1:
        "I had begun to see the rot beneath Ravenbrook's surface."
    elif locations_visited > 1:
        "I had seen enough of Ravenbrook to understand how deep the rot went."

    "Damon found me later."

    "Not as an officer."

    "As a man who'd already made too many compromises."
   
    show damon nervous at left, char_big
    show elias suspicious at right, char_big

    d "You don't understand."

    e "Then explain it."

    d "The Whisper keeps things calm."

    "There it was."

    d "No murders. No riots. No chaos."

    e "Just disappearances."

    "He looked away."

    $ choice = renpy.call_screen(
    "damon_choice_screen",
    influenced_by_whisper=influenced_by_whisper)
    
    if choice == "condemn":
        $ trust_damon -= 1
        e "You're trading lives for comfort."
        d "You think it's that simple? It's not about comfort... it's about survival."
        jump silas_hint

    elif choice == "details":
        $ trust_damon += 1
        e "Who decides who disappears?"
        d "Silas."
        jump silas_second_meeting

label silas_hint:
    "Damon didn't answer directly, only averted his eyes."
    "I knew he was holding something back, but I'd have to find it on my own."
    hide damon
    hide elias
    jump silas_second_meeting

screen silas_pressure_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 2:
            forced = "hesitate"

    vbox:
        spacing 25
        xalign 0.5
        yalign 0.5

        textbutton "Reject him outright":
            action Return("reject")

        textbutton "Hesitate - listen":
            action Return("hesitate")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            555,
            0.09
        )

label silas_second_meeting:

    scene bg mayor_office
    with fade

    show silas neutral at center, char_big
    show elias nervous at right, char_big

    "Silas was waiting."

    "This time, no pretense."

    s "You've learned enough to be dangerous."

    e "You're sacrificing people."

    s "I'm preserving a system."

    "He stepped closer."

    show silas suspicious at char_big

    s "And you, Detective... you hear it too."

    play sound "whisper.ogg"

    w "He understands you."

    "The room felt too small."

    $ choice = renpy.call_screen(
    "silas_pressure_choice",
    influenced_by_whisper=influenced_by_whisper)

    if choice == "reject":
        hide silas
        hide elias
        jump midpoint_event

    elif choice == "hesitate":
        $ influenced_by_whisper += 1
        show elias thinking at char_big
        "I didn't step back."
        "That scared me more than anything he'd said."
        hide silas
        hide elias
        jump midpoint_event

label midpoint_event:

    scene bg town_fog
    with fade

    "I didn't go back to my motel."

    "Something had shifted in Ravenbrook."

    "The fog pressed low enough to scrape rooftops."

    "Streetlights flickered - not out, but... hesitant."

    play sound "whisper.ogg"

    w "Too late."

    "My phone buzzed."

    "Unknown Number."

    "A single message:"

    centered "{i}She's gone.{/i}"

    e "...Iris."

    "I ran."

    scene bg police_station
    with dissolve

    "The police station was dark."

    "Not closed."

    "Abandoned."

    "Papers littered the front desk."

    "Coffee cups cold."

    "Doors hanging open."

    e "Damon?"

    "No answer."

    "Only the hum of fluorescents."

    "And something underneath it."

    "Chanting."

    play sound "whisper.ogg"

    w "Below."

    scene bg station_basement
    with fade

    "I followed the sound down stairs I hadn't seen before."

    "Concrete."

    "Rust."

    "Symbols carved into the walls."

    "Fresh."

    e "This wasn't here earlier."

    "A door stood open at the end of the corridor."

    "Light spilled out."

    scene bg holding_room
    with dissolve

    "Blood."

    "Not pooled."

    "Smeared."

    "Dragging marks across the floor."

    e "Jesus..."

    "Chains hung from hooks bolted into the ceiling."

    "One of them was still swinging."

    play sound "whisper.ogg"

    w "You were close."

    if trust_iris > 0:
        "My chest tightened."

        "I should've stayed with her."

    "Footsteps behind me."

    show damon nervous at left, char_big
    show elias nervous at right, char_big

    d "Don't move."

    "Damon stood in the doorway."

    "Gun shaking."

    show elias suspicious at char_big

    e "Where is she?"

    "Damon stayed silent."

    $ choice = renpy.call_screen("damon_midpoint_choice", influenced_by_whisper=influenced_by_whisper)

    if choice == "challenge":
        $ trust_damon -= 1
        e "I won't let this continue in silence."
        if hospital_clue or alley_clue:
            e "I've seen it all, Damon. The suffering. The blood. The chains."
            if hospital_clue:
                e "The basement ward... people shackled to the walls."
            if alley_clue:
                e "And the alley... traces of rituals everywhere."
                "Damon's face tightened, his hands clenched."
                d "You weren't supposed to find out."
        else:
            d "You think you understand, but you don't."
            d "Survival isn't about morality. It's about choices."
        jump act_three

    elif choice == "probe":
        $ trust_damon += 1
        e "Talk to me. How do you live with all this?"
        "Damon hesitated, his eyes darting toward the shadows."
        if hospital_clue or alley_clue:
            d "I do what I must. Some truths are too dangerous to speak."
        else:
            d "It's not something I can explain. It's easier to follow, than to question."
        e "Following isn't living. It's surviving at a cost."
        jump act_three

label evaluate_clues:

    if (
        "Ledger showing ritual intervals" in final_clues and
        "Strange markings on tunnel walls" in final_clues
    ):
        $ ritual_understood = True
        "The timing. The symbols."
        "They weren't praying."
        "They were broadcasting something."

    if (
        "Hospital patient logs missing" in final_clues and
        "Suppressed police cases" in final_clues
    ):
        $ silas_exposed = True
        "Crowe had his hands in every record."
        "This wasn't tradition."
        "It was infrastructure."

    if (
        "Patterned candle arrangement" in clues and
        "Strange markings on tunnel walls" in final_clues
    ):
        $ whisper_source_known = True
        "Amplifiers."
        "Not altars."
        "Transmitters."

    return

label act_three:

    scene bg town_fog
    with fade

    if ritual_understood:
        "I knew how the ritual worked now."

    if whisper_source_known:
        "The symbols weren't mystical."
        "They were machinery."

    if not ritual_understood:
        "I was still missing something."


    "The fog felt different now."

    "Not heavier."

    "Closer."

    "I knew what Ravenbrook was. I knew what it cost to keep it quiet."

    "And I knew there was no way to walk away without choosing a side."

    play sound "whisper.ogg"

    w "You've always been listening."

    "I stopped in the middle of the street."

    e "This ends tonight."

screen final_choice_screen(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 2:
            forced = "church"

    vbox:
        spacing 25
        xalign 0.5
        yalign 0.5

        textbutton "Go to the church - end the ritual":
            action Return("church")

        textbutton "Confront Silas directly":
            action Return("silas")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            500,
            0.1
        )

label final_choice:

    $ choice = renpy.call_screen("final_choice_screen", influenced_by_whisper=influenced_by_whisper)

    if choice == "church":
        jump final_church
    elif choice == "silas":
        jump final_silas

screen final_church_choice(influenced_by_whisper=0):
     
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 2:
            forced = "hesitate"

    vbox:
        spacing 26
        xalign 0.5
        yalign 0.5

        textbutton "Stop the ritual":
            action Return("stop")

        textbutton "Hesitate":
            action Return("hesitate")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            555 + ["stop","hesitate"].index(forced)*60,
            0.1
        )

label final_church:

    scene bg church
    with fade

    show elias nervous at center, char_big

    "The church was alive."

    "Candles burned. Voices murmured."

    "People knelt before the altar - not praying, but listening."

    "At the centre stood the missing woman."

    "Alive."

    "Terrified."

    play sound "whisper.ogg"

    w "This keeps them safe."

    $ choice = renpy.call_screen(
    "final_church_choice",
    influenced_by_whisper=influenced_by_whisper)

    if choice == "stop":
        $ influenced_by_whisper -= 1
        show elias suspicious at char_big
        e "This ends now."
        jump church_interrupt

    elif choice == "hesitate":
        $ influenced_by_whisper += 1
        "For one moment, I understood the appeal."
        jump church_interrupt


label church_interrupt:

    "The chanting stopped."

    "Someone screamed."

    "Chaos rippled through the room."

    "And then - silence."

    jump ending_evaluation

screen final_silas_choice(influenced_by_whisper=0):
    
    add Solid("#00000080")
    default forced = None

    python:
        if influenced_by_whisper >= 2:
            forced = "accept"

    vbox:
        spacing 26
        xalign 0.5
        yalign 0.5

        textbutton "Reject Silas":
            action Return("reject")

        textbutton "Accept his offer":
            action Return("accept")

    if forced:

        timer 0.03 repeat True action Function(
            pull_mouse_toward,
            960,
            555,
            0.12
        )

label final_silas:

    scene bg mayor_office
    with fade

    show silas happy at center, char_big
    show elias nervous at right, char_big

    "Silas didn't look surprised to see me."

    s "I was wondering when you'd choose."

    e "You've been using the Whisper."

    s "No. I've been listening."

    "He stepped closer."

    s "You hear it the way I do."

    play sound "whisper.ogg"

    show silas suspicious at char_big
    show elias thinking at char_big

    w "Stay."

    $ choice = renpy.call_screen(
    "final_silas_choice",
    influenced_by_whisper=influenced_by_whisper)

    if choice == "reject":
        $ influenced_by_whisper -= 1
        e "I'm not like you."
        jump ending_evaluation

    elif choice == "accept":
        $ influenced_by_whisper += 1
        "I didn't answer."
        "And that was answer enough."
        jump ending_evaluation

label ending_evaluation:

    if (influenced_by_whisper <= 1 and trust_iris > 0 and ritual_understood and whisper_source_known) and ("Blood-stained altar cloth" in clues or whisper_source_known):
        jump good_ending

    elif influenced_by_whisper >= 2:

        jump bad_ending

    else:
        jump neutral_ending

label good_ending:

    scene bg town_day
    with fade

    "The ritual was broken."

    "The Whisper faded into nothing more than an echo."

    "People remembered what they'd done."

    "Some cried."

    "Some ran."

    "Some stayed silent."

    "Iris testified."

    "Damon resigned."

    "And Silas Crowe vanished before sunrise."

    "As I left Ravenbrook, the fog finally lifted."

    "For the first time since arriving, the city felt empty."

    "And that was enough."

    return

label neutral_ending:

    scene bg town_fog
    with fade

    "The ritual continued."

    "But it changed."

    "Under my direction."

    "People stopped disappearing randomly."

    "Order replaced fear."

    "Iris stopped returning my calls."

    "Silas stood beside me - not as a ruler, but as something closer."

    "An equal."

    "A witness."

    "Ravenbrook slept peacefully."

    "And I listened."

    return

label bad_ending:

    scene bg town_night
    with fade

    "I stopped fighting it."

    "The Whisper filled every thought."

    "Every doubt."

    "Every memory."

    "Silas watched as I disappeared."

    "Not with guilt."

    "With understanding."

    "Ravenbrook remained safe."

    "And I became what it needed."

    return