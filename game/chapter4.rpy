label chapter4:
    scene black_bg with pixellate
    q "\"Hey, he's barely breathing.\""
    q "\"Come on, let's hurry.\""
    q "\"Amazing, I've never seen the program act like this before.\""
    q "\"Vitals are steadily declining.\""
    q "\"We can't just pull him out.\""
    q "\"His body seems unresponsive, but we're still seeing brain activity in the program.\""
    q "\"Let's test this out.\""
    q "\"Can you hear us?\""
    menu:
        "..."
        "Yes.":
            q"\"We've got a response.\""
    q "\"I'm gonna be straight with you because we don't have the time.\""
    q "\"Your body's damaged.\""
    q "\"Badly.\""
    q "\"If we pull you out now, you'll lose all your memories.\""
    q "\"We'll lose the data from your memories as well, including this \"Anna\".\""
    q "\"The other option is we upload all this data to the network.\""
    q "\"The problem with that is that your body will die, but you'll stay in the program.\""
    q "\"What do you want us to do?\""
    menu:
        "..."
        "Pull me out.":
            call rw_ending from _call_rw_ending
        "I'll stay here.":
            call sim_ending from _call_sim_ending
    return

# label alt_scene4:
#     scene room night with pixellate
#     show anna smile at truecenter with dissolve
#     a "Hey."
#     show anna talk with dissolve
#     a "I'm actually pretty scared of falling asleep."
#     show anna thinking with dissolve
#     a "I don't know what might happen."
#     show anna smile with dissolve
#     a "Time just passes."
#     show anna talk with dissolve
#     a "Every second that you're here is a second closer to your death."
#     show anna smile with dissolve
#     a "Every second that you're here is a second closer to my death."
#     show anna annoyed with dissolve
#     a "Even if help arrives, you would still have to go."
#     show anna mad with dissolve
#     a "And I don't want that."
#     show anna annoyed with dissolve
#     a "And I hate that all I can do is wait."
#     show anna mad with dissolve
#     a "Wait for you to pass."
#     show anna annoyed with dissolve
#     a "Wait for you to leave."
#     show anna mad with dissolve
#     a "In the end, I'm just here."
#     show anna talk with dissolve
#     a "Lines of code written."
#     show anna smile with dissolve
#     a "Never waking up."
#     show anna smug with dissolve
#     a "A memory to you, just like how I always wanted."
#     show anna smile with dissolve
#     a "And it sucks."
#     return
