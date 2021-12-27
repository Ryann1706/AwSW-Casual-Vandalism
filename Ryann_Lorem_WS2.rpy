
label Ryann_Lorem_WSmash2:

m "Upon entering the store I realised that most of the windows were either missing or mostly broken."
m "Except one."
m "And with this store falling apart it wouldn't be that hard to find something to smash it with..."
menu:
    "[[Do nothing]":
        m "But I decided that I've learned from my past mistakes and grown as a person."

    "[[Smash the window... again.]":
        $ ryannwindowssmashed +=1
        m "It didn't take long to find a piece of rubble small enough to throw."
        play sound "fx/glassimpact2.ogg"
        $ renpy.pause (0.5)
        show lorem relieved with dissolve
        Lo "Really...? Again?"
        c "Well, no one owns it this time."
        Lo "Well yeah, but still, there has to be a better way for you to vent your frustrations."
        show lorem think with dissolve
        Lo "Or, for whatever other reason you're obsesed with smashing windows."
        Lo "Anyway lets get back on track before you bring the walls and ceiling down too."
                
Lo "..."

jump Ryann_Lorem_WSmash2_end



label Ryann_Lorem_LoBrivkLose:

Lo think "Wait a second..."
c "What is it?"
Lo relieved "Oh, I must have lost the brick you gave me in the store."
Lo think "It might have been when that shelf fell on me."
Lo sad "Uh, sorry about that [player_name]..."
c "It's alright Lorem, I was messing with you when I gave it to you, I dont really care you lost it."
Lo normal "Alright, I'll admit it, you got me good with that, {w}anyway."

jump Ryann_Lorem_LoBrivkLose_end
