
label Ryann_Lorem_WSmash2:

     m "Upon entering the store I realised that most of the windows were either missing or mostly broken."
     m "Except one."
     m "And with this store falling apart it wouldn't be that hard to find something to smash it with..."
     menu:
          "[[Do nothing]":
                $ WindowsSmashed2 = False
                m "But I decided that I've learned from my past mistakes and grown as a person."

          "[[Smash the window... again.]":
                $ WindowsSmashed2 = True
                m "It didnt take long to find a piece of rubble small enough to throw."
                play sound "fx/glassimpact2.ogg"
                $ renpy.pause (0.5)
                show lorem relieved with dissolve
                Lo "Really...? Again?"
                c "Well, no one owns it this time."
                Lo "Well yeah, but still, there has to be a better way for you to vent your frustrations."
                show lorem think with dissolve
                Lo "Or, for whatever other reason you're obbsesed with smashing windows."
                Lo "Anyway lets get back on track before you bring the walls and ceiling down too."
                Lo "..."

jump Ryann_Lorem_WSmash2_end
