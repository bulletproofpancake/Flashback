label rw_ending:
    q "\"Alright, we're going to pull you out.\""
    q "\"I'm sorry for this.\""
    "Anna doesn't deserve this."
    "My memories are a small price to pay for hurting her."
    "Maybe I might be able to do it right this time."
    scene all_bg with pixellate
    show anna emotions at truecenter
    "My memories start to fade."
    "It might have been fun."
    "But I don't deserve those memories."
    scene black_bg with fade
    "Goodbye, Anna."
    return

label sim_ending:
    q "\"Alright, we're uploading your data now.\""
    scene room noon with fade
    "I wake up to the smell of bacon and eggs."
    "I see Anna by the kitchen cooking breakfast."
    "I slowly walk to her and give her a hug."
    show anna talk at truecenter with dissolve
    a "Oh, you should've told me you were awake."
    show anna thinking with dissolve
    a "Wait."
    show anna glad with dissolve
    a "You're here?"
    menu:
        "..."
        "I'm here.":
            show anna annoyed with dissolve
            a "You should've told me you were thinking of doing this."
            show anna mad with dissolve
            a "I mean, I don't even know how to react."
            show anna embarrassed with dissolve
            a "I'm glad, though."
    scene black_bg with fade
    "I might never be able to say sorry to everyone."
    "But I've got a second chance."
    "Maybe I'll do it right this time."
    return