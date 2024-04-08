from turtle import *
from time import *

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x} {self.y}"
    def __eq__(self,pt):
        return self.x == pt.x and self.y == pt.y

def ptlist(x,y):
    lst = []
    for a,b in zip(x,y):
        lst.append(Point(a,b))
    return lst

def drawsect(pts,outline="black",fill=""):
    color(outline)
    penup()
    setpos(pts[0].x/1.25,pts[0].y/1.25)
    begin_fill()
    pendown()
    for i in range(1,len(pts)):
        goto(pts[i].x/1.25,pts[i].y/1.25)
    fillcolor(fill)
    end_fill()

speed(1)

def printround(x,y):
    print("[",end="")
    for p in x:
        print(f"{round(p)}",end=", ")
    print("\b\b]\n")

    print("[",end="")
    for p in y:
        print(f"{round(p)}",end=", ")
    print("\b\b]")

x_beak = [86,78,67,56,44,32,15,0,-14,-33,-48,-66,-90,-105,-120,-130,-140,-154,-167,-172,-170,-165,-157,-148,-136,-125,-123,-107,-98,-79,-67,-54,-38,-27,-13,0,15,30,53,67,104,115,120,120,116,111,108,96,84,69,53,38,23,6,-14,-41,-59,-73,-90,-103,-118,-134,-149,-165,-167]

y_beak = [325,322,312,302,293,284,275,268,263,259,256,254,254,257,264,270,278,286,288,292,307,323,334,344,353,364,367,380,386,394,398,401,402,401,398,392,384,376,366,360,350,342,330,312,293,279,275,269,265,258,246,235,224,215,207,201,201,203,211,220,238,259,275,285,288]

x_righteye = [53,30,22,18,18,22,32,43,63,75,85,92,92,88,79,67,53]

y_righteye = [366,376,388,401,423,435,448,456,456,449,440,422,399,387,375,368,366]

x_lefteye = [-97,-107,-123,-129,-136,-143,-148,-152,-152,-148,-143,-136,-122,-114,-107,-103,-99,-96,-95,-97]

y_lefteye = [386,380,367,370,376,383,393,404,426,440,448,453,453,449,441,436,428,414,393,386]

x_body = [426,421,412,410,400,390,387,372,370,353,350,335,330,319,310,304,291,290,277,270,266,256,250,248,241,235,231,230,228,227,226,225,225,225,225,223,221,217,212,210,204,194,190,182,170,167,150,149,130,124,110,90,70,50,30,10,0,-10,-30,-50,-70,-90,-98,-110,-129,-130,-150,-165,-170,-177,-186,-190,-192,-196,-198,-200,-201,-201,-201,-201,-200,-199,-199,-197,-197,-195,-193,-192,-190,-191,-197,-209,-210,-226,-230,-244,-250,-262,-270,-279,-290,-295,-310,-323,-330,-333,-340,-343, -345,-346,-348,-350,-356,-361,-373,-403,-421,-429,-433,-434,-435,-433,-431,-429,-425,-425, -414, -402, -378, -366, -351, -336, -322, -306, -285, -270, -255, -242, -227, -210,-182,-167,-153,-146,-146,-151,-159,-176,-196,-243,-271,-289,-303,-322,-322,-320,-316,-309,-299,-288,-279,-269,-258,-248,-249,-228,-230,-228,-224,-217,-209,-202,-185,-172,-161,-153,-150, -149, -165, -167, -172, -171, -165, -157, -148, -136, -126, -107, -98, -80, -67, -54, -38, -27, -13, 0, 15, 30, 53, 67, 104, 115, 120, 120, 116, 111, 111, 118, 127, 144, 163, 178, 187, 192, 196, 213, 228, 245, 260, 271, 278, 280, 278, 274, 271, 275, 283, 288, 284, 283, 282, 283, 287, 296, 305, 321, 336, 354, 372, 393, 411, 426, 437, 446, 452, 454, 461, 467, 472, 478, 478, 476, 472, 467, 459, 451, 444, 435, 426]

y_body = [0,10,30,33,50,66,70,90,92,110,114,130,137,150,163,170,190,191,210,223,230,250,265,270,290,310,330,334,350,370,390,410,430,450,470,490,510,530,550,555,570,590,597,610,627,630,649,650,666,670,679,690,697,703,707,709,709,709,708,706,701,694,690,683,670,669,650,630,623,610,590,574,570,550,530,510,490,470,450,430,410,390,370,350,330,310,290,270,250,230,210,190,189,170,166,150,143,130,121,110,97,90,70,50,36,30,10,0,-4,-11,-19,-26,-45,-61,-88,-150,-186,-202,-215,-225,-244,-257,-264,-270,-277,-278, -267, -261, -260, -265, -276, -292, -310, -333, -364, -387, -413, -435, -460, -483,-486,-482,-473,-456,-439,-423,-411,-392,-375,-338,-315,-299,-286,-267,-241,-218,-189,-149,-115,-82,-60,-40,-19,0,0,32,44,59,80,102,118,130,155,174,194,217,274, 275, 285, 288, 293, 307, 324, 334, 344, 353, 364, 380, 386, 394, 398, 401, 402, 401, 398, 392, 384, 376, 366, 360, 350, 342, 330, 312, 292, 279, 279, 265, 241, 206, 168, 132, 100, 77, 57, 38, 17, -13, -48, -92, -126, -184, -219, -264, -287, -288, -289, -291, -301, -314, -330, -343, -355, -368, -375, -381, -384, -385, -381, -372, -361, -348, -336, -323, -311, -302, -302, -284, -265, -232, -186, -169, -144, -119, -88, -65, -42, -17, 0]

x_booty = [210,207,204,199,192,189,186,186,187,189,192,192,180,160,140,120,100,80,60,40,20,0,-20,-40,-60,-80,-100,-120,-140,-148,-148,-146,-144,-144,-145,-147,-151,-155,-160,-166,-166,-160,-140,-120,-100,-80,-60,-40,-20,0,20,40,60,80,100,120,140,160,180,200,210]

y_booty = [-436,-460,-480,-520,-560,-580,-600,-630,-640,-650,-660,-660,-657,-652,-647,-643,-640,-636,-634,-632,-630,-628,-627,-627,-628,-629,-631,-634,-637,-638,-638,-630,-620,-600,-590,-580,-570,-560,-550,-541,-541,-544,-554,-561,-567,-571,-574,-575,-574,-572,-568,-563,-556,-546,-535,-521,-505,-487,-468,-448,-436]

x_leftflipper = [-148,-152,-158,-166,-173,-182,-197,-214,-229,-256,-271,-294,-338,-380,-421,-469,-521,-570,-583,-594,-600,-600,-590,-578,-573,-571,-574,-578,-578,-574,-566,-554,-537,-520,-503,-483,-470,-459,-449,-437,-425,-412,-401,-379,-367,-351,-340,-332,-312,-283,-236,-210,-198,-184,-166,-160,-155,-151,-147,-145,-144,-144,-146,-148]

y_leftflipper = [-638,-649,-661,-674,-682,-690,-700,-706,-711,-710,-707,-698,-680,-667,-658,-647,-632,-617,-611,-602,-589,-572,-551,-524,-500,-474,-441,-413,-389,-369,-355,-347,-343,-342,-344,-340,-337,-329,-317,-298,-277,-267,-261,-261,-266,-276,-287,-298,-323,-368,-446,-483,-500,-518,-541,-550,-560,-570,-580,-590,-600,-620,-630,-638]

x_rightflipper = [273, 263, 253, 248, 234, 225, 220, 217, 213, 210, 209, 211, 211, 210,207,204,199,192,189,186,186,187,189,192,192,197,208,224,256,276,302,329,358,368,379,392,408,425,446,463,483,499,520,541,560,580,592,600,600,595,588,575,562,550,539,528,519,511,502,498,495,495,494,491,487,481,475,466,460]

y_rightflipper = [-287, -286, -285, -284, -285, -287, -290, -293, -299, -307, -335, -371, -406, -436,-460,-480,-520,-560,-580,-600,-630,-640,-650,-660,-660,-668,-682,-694,-706,-710,-710,-702,-686,-678,-667,-655,-640,-626,-610,-599,-588,-580,-570,-560,-548,-533,-519,-504,-489,-480,-471,-462,-452,-444,-434,-424,-416,-407,-394,-383,-374,-360,-348,-334,-325,-316,-310,-305,-302]

x_righteyewhite = [98, 107, 112, 118, 121, 121, 116, 112, 104, 95, 88, 75, 62, 42, 33, 22, 12, 4, -4, -9, -14, -14, -10, -6, 1, 15, 30, 53, 75, 98]

y_righteyewhite = [353, 362, 372, 387, 397, 437, 454, 465, 479, 491, 497, 504, 508, 508, 506, 501, 493, 485, 476, 463, 451, 423, 414, 407, 392, 385, 377, 366, 358, 352]

x_lefteyewhite = [-85, -91, -97, -104, -115, -123, -134, -147, -151, -159, -165, -169, -171, -171, -168, -165, -157, -148, -133, -123, -113, -102, -93, -87, -81, -75, -71, -71, -77, -85]

y_lefteyewhite = [392, 389, 387, 382, 375, 368, 355, 347, 352, 363, 376, 395, 418, 454, 463, 474, 485, 493, 499, 498, 495, 487, 478, 470, 459, 443, 423, 412, 404, 392]

drawsect(ptlist(x_rightflipper,y_rightflipper),"black","yellow")

drawsect(ptlist(x_body,y_body),"black","black")

drawsect(ptlist(x_beak,y_beak),"black","orange")

drawsect(ptlist(x_righteyewhite,y_righteyewhite),"black","white")

drawsect(ptlist(x_righteye,y_righteye),"black","black")

drawsect(ptlist(x_lefteyewhite,y_lefteyewhite),"black","white")

drawsect(ptlist(x_lefteye,y_lefteye),"black","black")

drawsect(ptlist(x_booty,y_booty),"black","black")

drawsect(ptlist(x_leftflipper,y_leftflipper),"black","yellow")

hideturtle()

Screen().exitonclick()