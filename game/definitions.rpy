#CHARACTERS AND SPRITES
define a = Character("Anna", color="#6d5e5a")
define b = Character("Bella", color="#920000")
define c = Character("Cara", color="#9933ff")
define q = Character("???", color="#000000")

#ROUTES
define anna_route = True
define bella_route = True
define cara_route = True
define all_route = False

#CHARACTERS
image anna emotions:
    "Characters/anna/anna annoyed.png"
    pause 0.25
    "Characters/anna/anna challenge.png"
    pause 0.25
    "Characters/anna/anna embarrassed.png"
    pause 0.25
    "Characters/anna/anna glad.png"
    pause 0.25
    "Characters/anna/anna mad.png"
    pause 0.25
    "Characters/anna/anna smile.png"
    pause 0.25
    "Characters/anna/anna smug.png"
    pause 0.25
    "Characters/anna/anna talk.png"
    pause 0.25
    "Characters/anna/anna thinking.png"
    pause 0.25
    repeat

image bella emotions:
    "Characters/bella/bella annoyed.png"
    pause 0.25
    "Characters/bella/bella embarrassed.png"
    pause 0.25
    "Characters/bella/bella smile.png"
    pause 0.25
    "Characters/bella/bella smug.png"
    pause 0.25
    "Characters/bella/bella talk.png"
    pause 0.25
    repeat

image cara emotions:
    "Characters/cara/cara smile.png"
    pause 0.25
    "Characters/cara/cara smug.png"
    pause 0.25
    "Characters/cara/cara talk.png"
    pause 0.25
    repeat
image anna glitch:
    "Characters/anna/anna glad.png"
    pause 1.0
    "Characters/bella/bella embarrassed.png"
    pause 0.5
    "Characters/anna/anna mad.png"
    pause 1.0
    "Characters/cara/cara smile.png"
    pause 0.5
    repeat

#BACKGROUNDS
image road:
    "Background/Road/road_bg.jpg"

image room dawn:
    "Background/Room/room_dawn_light_off.jpg"

image room dusk:
    "Background/Room/room_dusk_light_off.jpg"

image room noon:
    "Background/Room/room_noon_light_off.jpg"

image room night:
    "Background/Room/room_night_light_off.jpg"

image park:
    "Background/Park/park.jpg"
    im.FactorScale("Background/Park/park.jpg",0.5)

image arcade_bg:
    "Background/arcade.jpg"
    im.FactorScale("Background/arcade.jpg",1.25)

image foodcourt_bg:
    "Background/foodcourt.jpg"

image timelapse_bg:
    "Background/Park/park.jpg"
    im.FactorScale("Background/Park/park.jpg",0.5)
    pause 2.0
    "Background/arcade.jpg"
    im.FactorScale("Background/arcade.jpg",1.25)
    pause 2.0
    "Background/foodcourt.jpg"
    pause 2.0
    repeat

image rewrite_room:
    "Background/Room/room_noon_light_off.jpg"
    pause 0.25
    "Background/Room/room_dawn_light_off.jpg"
    pause 0.25
    "Background/Room/room_night_light_off.jpg"
    pause 0.25
    "Background/Room/room_dusk_light_off.jpg"
    pause 0.25
    repeat

image all_bg:
    "Background/Room/room_noon_light_off.jpg"
    pause 0.25
    "Background/Room/room_dawn_light_off.jpg"
    pause 0.25
    "Background/Room/room_night_light_off.jpg"
    pause 0.25
    "Background/Room/room_dusk_light_off.jpg"
    pause 0.25
    "Background/Park/park.jpg"
    im.FactorScale("Background/Park/park.jpg",0.5)
    pause 0.25
    "Background/arcade.jpg"
    im.FactorScale("Background/arcade.jpg",1.25)
    pause 0.25
    "Background/foodcourt.jpg"
    pause 0.25
    repeat


#GUI
image ffbtn:
    im.FactorScale("buttons/ffwrd.png", 0.15)

image savebtn:
    im.FactorScale("buttons/save.png", 0.15)

image loadbtn:
    im.FactorScale("buttons/load.png", 0.15)

image prefsbtn:
    im.FactorScale("buttons/prefs.png", 0.15)

image historybtn:
    im.FactorScale("buttons/history.png", 0.15)

image backbtn:
    im.FactorScale("buttons/back.png", 0.15)

#AUDIO
define audio.cassini = "audio/music/Cassini.mp3"

define audio.tires = "audio/sfx/tire_screech.mp3"

define audio.windowcrash = "audio/sfx/window_smash.mp3"

define audio.deathfx = "audio/sfx/deathfx.mp3"

#TRANSITIONS
define slowDissolve = Dissolve (2.0)
