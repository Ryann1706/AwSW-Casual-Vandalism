
label Ryann_Lorem_WSmash2:

     m "Upon entering the store I realised that most of the windows were either missing or mostly broken."
     m "Except one."
     m "And with this store falling apart it would be that hart to find something to smash it with..."
     menu:
          "[[Do nothing]":
                m "But I decided that ive learned from my past mistakes and grown as a person."

          "[[Smash the window... again.]":
                $ WindowsSmashed2 = True
                m "I didnt take longh to find a peice of rubble small enough to throw."
                play sound "fx/glassimpact2.ogg"
                show lorem relieved with dissolve
                lo "Really...? Again?"
                c "Well, no one owns it this time."
                lo "Well yeah, but still, there has to be a better way for you to vent your frustrations."
                show lorem think with dissolve
                lo "Or, for whatever other reason you're obbsesed with smashing windows."
                lo "Anyway lets get back on track before you bring the walls and ceiling down too."
                lo "..."

jump Ryann_Lorem_WSmash2_end
