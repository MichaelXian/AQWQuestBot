# Helper Functions
def farm():
    type('5t4321xp')

def wait_click(image):
    try:
        wait(image, 10)
        click(image)
    except:
        print("Anti anti cheat")
        anti_anti_cheat()
        raise Exception("Anti-cheat hit, reset to beginning")

def try_click(region, image):
    try:
        farm()
        if region.exists(image, 0):
            region.click(image)
        return True
    except:
        return False

complete_region = Region(86,127,681,758)
turnin_region = Region(240,780,340,108)
close_region = Region(637,168,77,64)
quest_region = Region(1375,947,84,71)
open_quest_region = Region(1301,833,239,70)
empty_region = Region(479,489,190,210)
no_region = Region(886,506,350,176)

complete = Pattern("complete.png").similar(0.60)
close_button = "close_button.png"
turnin = Pattern("turnin.png").similar(0.95)
quest_button = Pattern("quest_button.png").similar(0.80)
open_quests_button = Pattern("open_quests_button.png").similar(0.80)
empty = "empty.png"
no_button = "no_button.png"
    
while True:
   try_click(quest_region, quest_button)
   try_click(open_quest_region, open_quests_button)
   try_click(complete_region, complete)
   try_click(empty_region, empty)
   try_click(no_region, no_button)
   try_click(turnin_region, turnin)
   try_click(close_region, close_button)
   
