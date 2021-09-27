from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    name="Casual Vandalism"
    version="v1.0"
    author="Ryann1706"
    nsfw=False

    def mod_load(self):
       ml = modinfo.get_mods()["MagmaLink"].import_ml()

       ml.find_label("lorem3") \
        .search_say("Let's go, then.") \
        .hook_to("Ryann_Lorem_GetBrick") \
        .search_say("Here we are. The X on the map is right between these two buildings, so it must be around here somewhere.") \
        .link_from("Ryann_Lorem_GB_end")

       ml.find_label("lorem3") \
        .search_menu("Look inside the windows.").branch() \
        .search_say("As Lorem flew up to the windowsill with a few flaps of his wings, I turned to the right to look inside the windows of the administrative building") \
        .hook_to("Ryann_Lorem_Search") \
        .search_say("Nothing.") \
        .link_from("Ryann_Lorem_Ser_end")
        
       ml.find_label("lorem3") \
        .search_menu("Look inside the windows.").branch() \
        .search_say("The curtains were closed, but through a small gap, I could barely see inside.") \
        .link_from("Ryann_Lorem_NormalWindow")
        
       ml.find_label("lorem3") \
        .search_menu("Look inside the windows.").branch() \
        .search_say("Did you find anything?") \
        .hook_to("Ryann_Lorem_LoremBrick", condition="HasBrick == True")
    
       ml.find_label("lorem3searchmenu") \
        .search_say("Let's just look for the X.", depth=500) \
        .hook_to("Ryann_Lorem_WSmash2", condition="WindowSmashed == True") \
        .search_say("I nearly got sent back, by the way.", depth=600) \
        .link_from("Ryann_Lorem_WSmash2_end") 
    
       ml.find_label("c4resultscontinue") \
        .search_say("Loud bangs were heard from the area her body was found, and she has numerous wounds consistent with both the wounds of the previous victims and that other weapon he has.") \
        .hook_to("Ryann_Lorem_Comments", condition="WindowSmashed == True") \
        .search_say("A hatchery? Is that what this building is?") \
        .link_from("Ryann_Lorem_Coms_end") 
       
       ml.find_label("lorem4") \
        .search_say("So this is where you live.") \
        .hook_to("Ryann_Lorem_LoremComment", condition="WindowsSmashed2 == True") \
        .search_say("You already got a glimpse when you delivered Reza's letter, remember?") \
        .link_from("jump Ryann_Lorem_LoremComment_end")

    def mod_complete(self):
        pass
