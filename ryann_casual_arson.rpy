
init python:
    ryann_did_arson = False # That variable name isn't incriminating at all...

label ryann_casual_arson_start:

menu:
    "He can’t be that dangerous.":
        pass

    "Yeah, let's go.":
        jump ryann_casual_arson_start_return

$ anna2mood -= 1
c "He can't be that dangerous."
An face c "What?"
c "I mean, you’re acting like he’s actually a threat, or that he’s dangerous to us, or something."
An disgust c "What? Are you saying you actually want him to catch us out here?"
c "I’m just saying, you’re acting like we need to leave immediately. Like something horrible’s going to happen if we get caught."
c "You even said he’s a senile has-been. What’s he gonna do? Yell at us?"
An face c "Oh, yeah. Just because he’s old means he can’t call the actual authorities. I forgot that part."
c "Look, I just meant-{w=0.5}{nw}"
"???" "HEY! WHAT IN THE HELL ARE YOU TWO DOIN' OM MY FARM?!" with vpunch
An "Dammit…"
$ renpy.pause (0.5)
scene black with dissolve
play sound "fx/bushes.ogg"
m "Suddenly, Anna grabbed my wrist and started running, dragging me through some shrubbery and into the forest next to the farm."
$ renpy.pause (2.5)
scene forestx 
show anna sad c flip
with dissolveslow
$ renpy.pause (0.5)
An "Okay. I think we lost him."
c "Well, that was… intense."
An disgust c flip "You’re one to talk. {i}He can't be that dangerous. What’s he gonna do?{/i}"
c "…"
$ renpy.pause (1.5)
if anna2mood < 1:
    An face c flip "We’ve wasted enough time here."
    jump ryann_casual_arson_start_return

else:
    show anna normal c flip with dissolve
    $ renpy.pause (1.0)
    An smirk c flip "You know what? If we’re almost going to get caught, why not make it something worth getting caught over? And we can get back at that old kook while we’re at it."
    c "What are you talking about?"
    An normal c flip "Well, while I was killing that mouflon, I saw a tiny storage shed near the outskirts of the field."
    An "It sure would be a shame if something were to happen to it."
    An smirk c flip "Something… {i}incendiary…{/i}"
    $ renpy.pause (0.5)
    menu: 
        "That’s too far.":
            c "Anna, come on. That’s too far."
            show anna normal c flip with dissolve
            c "He was yelling at us for killing his mouflon in the first place. I’m pretty sure what we did already outweighs him yelling."
            An "Alright, fine."
            An "Let’s get out of here then."
            jump ryann_casual_arson_start_return

        "It sure would be a shame.":
            pass

$ anna2mood += 1
c "It sure would be a shame if that happened…"
An "Good."
An normal c flip "Let's go see how flammable it really is."
$ renpy.pause (0.5)
scene black with dissolveslow
$ renpy.pause (1.5)
scene farm night with dissolveslow
$ renpy.pause (0.5)
show anna normal c at Position(xpos=0.85) with easeinright
$ renpy.pause (0.5)
show anna at Position(xpos=0.25) with ease
$ renpy.pause (1.5)
show anna normal c flip with dissolve

An "The wood is pretty flimsy, and bone dry."
c "What are you waiting for then?"
An "Well, as I said, my fire is made from two different components combining. And my body can’t produce enough to light the entire shed."
An "We need some sort of tinder, and kindling."
c "Would hay work?"
An smirk c flip "Not a bad idea."
An normal c flip "Wait here and act as a lookout. I saw some hay bales somewhere in the field."
c "What should I do if something happens?"
An face c flip "Obviously you should warn me. And don’t use my name when you do."
An normal c flip "I shouldn’t take too long."
$ renpy.pause (0.5)
hide anna with easeoutright
$ renpy.pause (3.0)
c "(Waiting Game 3: Return of the Boredom.)"
$ renpy.pause (3.0)
c "…"
$ renpy.pause (2.0)
c "(At least it’s a nice night, I guess…)"
$ renpy.pause (2.0)
m "Somehow without me noticing, one of those mouflons appeared right next to me, and it was staring right at me."
c "(What does this thing want?)"
m "It did nothing but stare with its glossed-over eyes, cliff-faced expression, and mind devoid of any and all thought."
$ renpy.pause (1.5)
menu:
    "[[Pet it.]":
        m "I had a strange urge to pet it, and unsure what it wanted from me, I gave in and began to pet it."
        $ renpy.pause (1.5)
        c "(Woah…)"
        m "I started petting it, and despite its looks, it was very soft and fluffy."
        m "Fortunately, it seemed to be enjoying it, as it pushed its head into the hand I was using to pet it."
        c "(Awww…)"
        $ renpy.pause (1.0)
        show anna normal c at Position(xpos=0.85) with easeinright
        $ renpy.pause (1.0)
        if anna2mood > 1:
            show anna smirk c with dissolve
            $ renpy.pause (0.5)
            An "You know, I would be annoyed that you’re not doing the one thing I asked you to do, but that’s adorable."
            c "It’s so fluffy…"
            An normal c "Yes. It’s a farm animal, meaning it’s reared for the specific animal products it produces, so they can be later harvested."

        else:
            An face c "Seriously? I asked you to do one thing, but you decided playing with {i}that thing{/i} is more important."
            An sad c "What are you even doing? Petting it?"
            c "It’s so fluffy…"
            An face c "Yes. It’s a farm animal. Meaning it’s raired for the specific animal products it produces, so they can be later harvested."

        c "Do you want to pet it?"
        An face c "Did you really just ask that?"
        c "Come on… You know you want to… What have you got to lose by petting it?"
        An sad c "…"
        if anna2mood > 2:
            An normal c "Fine. If it’ll get you to leave it alone."
            show anna at Position(xpos=0.65) with ease
            m "Anna walked up to the mouflon and also tried to pet it."
            $ renpy.pause (0.5)
            show anna smirk c with dissolve
            $ renpy.pause (1.0)
            m "But after a few seconds of doing so, it looked up at her, then ran away."
            show anna face c with dissolve
            $ renpy.pause (1.0)
            An "It should be scared of you… You’re the foreign creature here, not me."
            c "Well, you are still covered in basically its cousin's blood."
            An normal c "Fair."

        else:
            An disgust c "We are actively committing a serious felony with actual prison time, yet petting farm animals is your main priority?"
            c "…"
            c "So, I take it that you don’t want to."
            An face c "Yes. Leave the thing alone."
            $ renpy.pause (1.5)

    "[[Ignore it.]":
        $ anna2mood += 1
        m "I had no clue what it wanted, so I decided to just ignore it."
        $ renpy.pause (2.0)
        m "Yet it continued to stare straight into my soul…"
        $ renpy.pause (2.0)
        show anna normal c at Position(xpos=0.85) with easeinright
        $ renpy.pause (1.0)
        An "What is that thing doing?"
        c "I have no clue. It won’t leave me alone."
        m "Anna turned to face the mouflon."
        show anna at Position(xpos=0.65) with ease
        $ renpy.pause (0.5)
        An disgust c "Hey! Shoo! Get out of here before you end up like your cousin over there!"
        m "The mouflon proceeded to run away."
        show anna normal c with dissolve
        c "Wow. You really put that thing in its place. It won’t be forgetting that lesson anytime soon."
        An smirk c "Oh haha, smartass."


c "Anyway, did you get that hay?"
show anna smirk c with dissolve
m "She gestured to the loose hay pile by her feet."
c "I’ll take that as a yes."
show anna normal c with dissolve
m "Anna walked back over to the shed as I grabbed the hay pile and followed."
show anna at Position(xpos=0.25) with ease
$ renpy.pause (0.5)
play sound "fx/door/creaky.wav"
m "Anna opened the worn, aged door, and I loosely packed the hay inside."
$ renpy.pause (1.0)
An smirk c "Stand back."
m "As instructed, I took a good few steps back."
show anna normal c with dissolve
$ renpy.pause (1.0)
play sound "fx/firex.ogg"
$ renpy.pause (0.5)
An smirk c "Come on. Let’s go."
$ renpy.pause (0.5)
stop sound fadeout 2.5
scene black with dissolve
play soundloop "fx/run.ogg" 
$ renpy.pause (1.5)
"???" "HEY! YOU CURSED HOOLIGANS! GET BACK HERE NOW!" with vpunch

$ ryann_did_arson = True
$ renpy.pause (2.0)
stop soundloop fadeout 1.5
m "After running for what felt like minutes, we got to what felt like a safe enough distance away that we wouldn’t be found."
$ renpy.pause (0.5)
scene forestx 
show anna normal c
with dissolvemed
$ renpy.pause (0.5)
c "(Phew…)"
c "Well… That was… definitely a unique experience."
An smirk c "I bet you’ve never done anything like that on a date before."
c "It may be a shock to hear, but no, I haven’t."
$ renpy.pause (1.5)
c "How come you’re so… casual and nonchalant about committing crimes like this?"
An sad c "Well, when you’re in… my kind of situation for long enough, you tend to not be too fond of authority figures. Especially when most of them are idiots."
An smirk c "Plus, having some excitement like this is always welcome."
c "You’re not too fond of authority figures, yet you dated a police officer?"
An normal c "Well, there are obviously exceptions. But yes, I’ll admit you got me there."
c "So, how often do you commit crimes like this? Whenever you feel like it too?"
An face c "No. I don’t do things like this whenever I feel like it."
An normal c "I only do stuff like this very occasionally, and I’d only do something insignificant or inconsequential. Like, kill a single mouflon, or burn an old run-down shed full of rusty tools."
An smirk c "I’ve come here before. I know who the farmer is, and he’s loaded. If anything, we did him a favor by not charging a demolition fee to get rid of that pile of scrap wood."
c "And you’re not worried about getting found out at all?"
An normal c "It’s too dark out to recognize anyone. You won’t say anything because you're my accomplice. I’m fine."
c "Fair enough."
An "Anyway, let’s get out of here."

jump ryann_casual_arson_start_return



label ryann_casual_arson_chapter3:

Sb "Sure thing, Chief. Though there’s one other thing I was informed about."
Br "What is it?"
Sb "There was also a suspected arson attack recently."
c "O-Oh… Well, what do you know about it…?"
Sb "It’s not Reza if that’s what has you so nervous."
Sb "The victim is the owner of a farm and reported seeing the silhouettes of two people, one being a runner. They said it was too dark to see any more details or clearly see the silhouette of the other."
Sb "How should we proceed with this, Chief?"
Br "…"
Br "We won’t."
show sebastian shy b flip with dissolve
c "(Phew…)"
Sb normal b flip "What do mean we won’t do anything?"
Br "We don’t have the resources or people to spare until we find Reza, and by that point, it’ll be too late to catch the culprits."
Sb drop b flip "I see…"
c "So, I guess you could say this arson thing has to be… put on the {i}backburner{/i} for now."
show sebastian smile b flip
show bryce brow b
with dissolve
$ renpy.pause (0.5)
Br "[player_name], while I appreciate the attempt to lift the mood, now isn’t the best time for jokes."
c "Right, sorry."
$ renpy.pause (1.5)
Sb "I’ll go back to finishing up here."
$ renpy.pause (0.5)
show sebastian normal b
$ renpy.pause (0.3)
hide sebastian with easeoutleft
$ renpy.pause (0.5)
Br stern b "Anyway, let’s get back on topic. Emera is waiting for us."

jump ryann_casual_arson_chapter3_return1

