
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "Casual Arson"
    version = "1.0"
    author = "Ryann1706"
    dependencies = ["MagmaLink", "?BangOk"]

    def mod_load(self):
        ml.find_label("anna2") \
            .search_say("We should probably leave before that senile has-been wakes up from his evening nap.", depth=1300) \
            .hook_to("ryann_casual_arson_start")

        ml.find_label("c3cont") \
            .search_say("Sebastian, you can finish up here and go to the Ministry when you're done. We'll probably have to make some arrangements after this meeting.") \
            .hook_to("ryann_casual_arson_chapter3", condition="ryann_did_arson == True") \
            .search_say("Let's go then, shall we?") \
            .link_from("ryann_casual_arson_chapter3_return1")

    def mod_complete(self):
        pass

