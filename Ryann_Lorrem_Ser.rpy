
label Ryann_Lorem_Search:
m "I looked at the window and took a moment to appreciate how unbroken it was."
if HasBrick == True: 
 m "I suddenly remembered the brick I'd picked up earlier." 
 menu:
     "[[Do nothing.]":
               $ WindowSmashed = False
               $ WindowsSmashed2 = False
               m "Then I realised smashing a window with a brick wouldnt be my smartest idea."
               jump Ryann_Lorem_NormalWindow

     "[[Smash the window.]":
               $ HasBrick = False
               $ WindowSmashed = True
               play sound "fx/glassimpact2.ogg"
               m "I threw the brick I had through the window."
               show lorem think with dissolve
               Lo "[player_name] I heard glass breaking are-"
               m "Lorem looked at the ground and saw no glass on our side of the now broken window."
               Lo "Wait... {w}Did you do that?"
               c "Yeah..."
               Lo relieved "But... Why? Why did you just smash some random window?"
               c "I dont know... Just felt like it, I guess..."
               Lo "But why would you..."
               m "Lorem, at a loss for words, stared back and forward between me and the broken window in stunned bewilderment for a few seconds."
               show lorem relieved at right with move
               show sebastian normal b flip at Position (xpos = 0.05) with easeinleft
               Sb "[player_name], there you are, where's Reza?"
               c "Uh... What do you mean?"
               Sb "We got a call about a human from this building."
               Sb "So we assumed it was Reza and ran here immedediately."
               m "Bryce rounded the and looked around, confused."
               show bryce brow b flip at Position (xpos = 0.2) behind sebastian
               with easeinleft
               Br "Where's Reza?"
               Br "Also, [player_name], what are you doing here?"
               c "Reza's not here."
               Br "But we got a call about a human who broke a window, and I'm assuming it's him."
               m "He guestured towards the building with the window I had smashed."
               m "I only then noticed a dragon on the other side who had a distraught look on their face."
               Br "But if Reza's not here, then who...?"
               c "I... Uhh... {w}I smashed the window..."
               Sb disapproval b flip "Wait... Really?"
               Br "But why would you do that?"
               c "I don't really know..."
               Br angry old b flip "Dammit [player_name]!"
               Br brow b flip "You know the situation with Reza and you know we dont have the time to spare with false alarms like this!"
               m "Bryce sighed."
               Br "You're lucky you have your diplomatic immunity and you're our only connection to Reza, or else you'd be arrested right now."
               Br "Dont think this is over, [player_name]. We're gonna talk about this later."
               Lo think "Wait, whats going on with Reza?"
               Sb "Nothing for you to worry about."
               Br "Sebastian, clear everything up here, I'll head back to the station."
               Sb normal b flip "Got it Cheif."
               Br "You two go back to whatever you were doing. [player_name], you better not do anything stupid."
               $ renpy.pause (0.5)
               
               show bryce brow b old
               $ renpy.pause (0.2)
               hide bryce with easeoutleft

               $ renpy.pause (0.5)

               hide sebastian with easeoutright

               m "I felt like I was a child who'd just gotten caught doing something they shouldn't have."
               Lo sad "Uh... Let's just forget about that and get back to what we were doing..."
               c "Yeah..."
               Lo "Also, did you actually find anything here?"


 jump Ryann_Lorem_Ser_end

else:
 $ WindowSmashed = False
 $ WindowsSmashed2 = False
 m "I looked for a few more seconds before remembering what I was doing."
 jump Ryann_Lorem_NormalWindow
