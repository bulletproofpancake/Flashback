label start:
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
    call chapter3 from _call_chapter3
    call chapter4 from _call_chapter4
    return
#     scene black_bg with pixellate
#     a "I'm sorry."
#     a "It seems that my meddling put your body to a catatonic state."
#     a "I've sent an alert under your name but I don't know if help will come."
#     a "All I wanted was for you to leave me in the past."
#     show anna smile at truecenter with dissolve
#     a "But I guess we're stuck till the future, huh."
#     jump select_route

# label select_route:
#     scene room_dawn_light_off with pixellate
#     show anna smile at truecenter with dissolve
#     a "So..."
#     show anna talk with dissolve
#     a "Who do you wanna spend the day with?"

#     if anna_route and bella_route and cara_route:
#         show anna smile at truecenter with dissolve
#         a "Me?"
#         hide anna with pixellate
#         show bella smile at truecenter with dissolve
#         b "Me?"
#         hide bella with pixellate
#         show cara smile at truecenter with dissolve
#         c "Or Me?"
#         hide cara with pixellate

#     elif anna_route == False and bella_route and cara_route:
#         hide anna with pixellate
#         show bella smile at truecenter with dissolve
#         b "Me?"
#         hide bella with pixellate
#         show cara smile at truecenter with dissolve
#         c "Or Me?"
#         hide cara with pixellate
#     elif anna_route == False and bella_route == False and cara_route:
#         hide anna with pixellate
#         show cara smile at truecenter with dissolve
#         c "Me?"
#         hide cara with pixellate
#     stop music fadeout 10.0
#     menu:
#         "..."
#         "[a]" if anna_route:
#             a "Alright, give me a few."
#             scene rewrite_room
#             call anna_arc
#             $ anna_route = False
#         "[b]" if bella_route:
#             b "Alright, give me a few."
#             scene rewrite_room
#             call bella_arc
#             $ bella_route = False
#         "[c]" if cara_route:
#             c "Alright, give me a few."
#             scene rewrite_room
#             call cara_arc
#             $ cara_route = False

#     if anna_route == False and bella_route == False and cara_route == False:
#         $all_route = True
#         jump ending

#     elif all_route == False:
#         jump select_route
