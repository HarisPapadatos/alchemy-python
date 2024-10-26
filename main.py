# Alchemist Game Project
import time

list_of_recipes = [ ("air","fire","heat"), ("fire","fire","energy"), ("air","air","pressure"), ("earth", "earth","land"), ("fire", "earth","lava"),
                    ("water", "fire", "steam"), ("water", "heat","steam"), ("water", "water", "pond"), ("pond", "water", "lake"), ("pond", "pond", "lake"),
                    ("land", "earth", "hill"), ("land", "land", "hill"), ("lake", "lake", "sea"), ("lake", "pond", "sea"), ("lake","water", "sea"),
                    ("sea", "sea", "ocean"), ("sea", "lake", "ocean"), ("sea", "pond", "ocean"), ("sea" ,"water", "ocean"), ("continent", "continent", "planet"),
                    ("ocean", "planet", "planet earth"), ("lava", "earth", "volcano"), ("water", "earth", "mud"), ("lava", "air", "stone"), ("air","earth", "dust"),
                    ("dust", "fire", ""), ("gunpowder", "fire", "explosion"), ("air", "water", "cloud"), ("cloud", "water", "rain"),
                    ("rain","earth","plant"), ("plant", "rain", "tree"), ("stone", "fire", "metal"), ("stone", "air", "sand"), ("sand", "stone", "sandstone"),
                    ("lava", "lake", "lava lake"), ("lava", "pond", "lava lake"), ("continent", "lava", "tectonic plate"), ("earth", "energy", "earth quake"),
                    ("energy", "tectonic plate", "earth quake"), ("earth quake", "earth", "mountain"), ("hill", "hill", "continent"), ("hill", "land", "continent"), ("hill", "earth", "continent"),
                    ("earth", "steam", "geyser"), ("fire", "planet", "sun"), ("planet", "heat", "planet Venus"), ("planet", "sun", "solar system"), ("tree", "tree", "forest"),
                    ("forest", "forest", "jungle"), ("tree", "plant", "forest"), ("tree", "forest", "jungle"), ("forest", "rain", "rainforest"), ("jungle", "rain", "rainforest"),
                    ("sand", "mud", "clay"), ("mud", "dust", "clay"), ("mud", "fire", "brick"), ("clay", "fire", "pottery"), ("brick", "brick", "wall"),
                    ("stone", "brick", "stone brick"), ("stone brick", "stone  brick", "stone brick wall"), ("stone brick", "brick", "wall"), ("wall", "wall", "house"),
                    ("house", "house", "village"), ("village", "village", "town"), ("village", "house", "town"), ("town", "town", "city"), ("town", "village", "city"),
                    ("plant", "mud", "swamp"), ("energy", "metal", "electricity"), ("metal", "electricity", "wire"), ("lava", "water", "obsidian"), ("stone", "metal", "blade"),
                    ("blade", "blade", "scissors"), ("energy", "planet", "gravity"), ("energy", "sun", "heat"), ("solar system", "solar system", "galaxy"),
                    ("wire", "coil", "magnet"), ("magnet", "planet earth", "magnetic field"), ("magnetic field", "metal", "electric field"), ("metal", "blade", "sword"),
                    ("wire", "wire", "coil"), ("wire", "metal", "chain"), ("electricity", "metal", "machine"), ("machine", "explosion", "engine"),
                    ("engine", "explosion", "combustion engine"), ("machine", "steam", "engine"), ("machine", "energy", "engine"),  ("engine", "steam", "steam engine"),
                    ("engine", "electricity", "power generator"), ("swamp", "energy", "life"), ("stone", "planet", "moon"), ("stone", "stone", "rock"), ("rock", "rock", "boulder"),
                    ("rock", "stone", "boulder"), ("air", "planet", "atmosphere"), ("rain", "rain", "flood"), ("rain", "rain", "storm"), ("storm", "energy", "thunder"), ("thunder", "cloud", "lightning"),
                    ("thunder", "thunder", "lightning"), ("thunder", "rain", "lightning"),  ("tree", "rain", "flower"), ("energy", "sea", "premordial soup"),
                    ("energy", "ocean", "primordial soup"), ("primordial soup", "energy", "life"), ("galaxy", "galaxy", "galaxy claster"), ("galaxy cluster", "galaxy cluster", "universe"),
                    ("universe", "universe", "multiverse"), ("sun", "sun", "binary star"), ("cloud", "atmosphere", "sky"), ("cloud", "air", "sky"), ("sky", "sun", "day"),
                    ("sky", "moon", "night"), ("night", "day", "time"), ("sand", "fire", "glass"), ("glass", "sand", "hourglass"), ("glass", "glass", "glasses"),
                    ("sun", "glasses", "sunglasses"), ("water", "mountain", "river"), ("rain", "mountain", "river"), ("river", "mountain","waterfall"), ("water", "gravity", "waterfall"),
                    ("glass", "electricity", "light bulb"), ("lightbulb", "electrcity", "light"), ("sun", "atmosphere", "light"), ("fire", "night", "light"),
                    ("light", "rain", "rainbow"), ("rain", "sun", "rainbow"), ("rainbow", "rainbow", "double rainbow"), ("air", "energy", "wind"), ("wind", "stone", "sand"),
                    ("wind", "lava", "stone"), ("life", "stone", "egg"), ("life", "forest", "animal"), ("life", "mountain", "animal"), ("life", "ocean", "animal"), ("life", "sea", "animal"),
                    ("animal", "tree", "ape"), ("hourglass", "hourglass", "time"), ("time", "time", "future"), ("future", "time", "past"), ("animal", "forest", "wild animal"),
                    ("animal", "sea", "fish"), ("animal", "ocean", "fish"), ("animal", "lake", "fish"), ("sand", "sand", "desert"), ("stone wall", "stone wall", "castle"),
                    ("castle", "sand", "sand castle"), ("animal", "air", "bird"), ("bird", "bird", "bird swarm"), ("bird", "fish", "flying fish"), ("fish", "air", "dolphin"),
                    ("tree", "sun", "photosynthesis"), ("plant", "tree", "photosynthesis"), ("photosynthesis", "plant", "oxygen"), ("photosynthesis", "tree", "oxygen"),
                    ("oxygen", "life", "carbon dioxide"), ("oxygen", "animal", "carbon dioxide"), ("oxygen", "tree", "carbon dioxide"), ("oxygen", "plant", "carbon dioxide"),
                    ("plant", "sun", "flower"), ("flower", "rain", "fruit"), ("flower", "sun", "fruit"), ("fruit", "time", "wine"), ("fruit", "glass", "jam"),
                    ("carbon dioxide", "garbon dioxide", "green-house gas"), ("oxygen", "oxygen", "ozone"), ("ozone", "atmosphere", "ozone sphere"),
                    ("wind", "mountain", "cold"), ("air", "mountain", "cold"), ("cold", "water", "ice"), ("cold", "rain", "snow"), ("snow", "snow", "snowball"),
                    ("animal", "mountain", "goat"), ("wild animal", "mountain", "lion"), ("plant", "earth", "grass"), ("grass", "land", "grassland"), ("time", "ape", "human"),
                    ("animal", "grass", "ant"), ("ant", "hill", "anthill"), ("human", "wild animal", "domestication"), ("ape", "stone", "tool"), ("human", "stone", "tool"),
                    ("sea", "sand", "beach"), ("ocean", "sand", "beach"), ("sea", "land", "island"), ("ocean", "land", "island"), ("sea", "volcano", "island"), ("ocean", "volcano", "island"),
                    ("tool", "tree", "wood"), ("beach", "tree", "palm"), ("tree", "snow", "spruce"), ("tree", "mountain", "spruce"), ("wood", "house", "cabin"),
                    ("palm", "fruit", "banana"), ("banana", "planet", "moon"), ("banana", "animal", "ape"), ("fruit", "ape", "banana"), ("stone", "palm", "coconut"),
                    ("palm", "flower", "coconut"), ("night", "sky", "star"), ("solar system", "sky", "space"), ("sky", "space", "star"), ("sky", "star", "space"),
                    ("sun", "space", "star"), ("star", "star", "constellation"), ("glass", "sky", "telescope"), ("glass", "star", "telescope"), ("glass", "sky", "telescope"),
                    ("telescope", "telescope", "binoculars"), ("constellation", "human", "astrology"), ("telescope", "human", "science"), ("human", "human", "love"),
                    ("tool", "blade", "axe"), ("axe", "tree", "wood"), ("axe", "chain", "chainsaw"), ("chainsaw", "tree", "wood"), ("wood", "sea", "boat"),
                    ("cold", "human", "sickness"), ("sickness", "life", "bacteria"), ("bacteria", "sun", "photosynthesis"), ("star", "blade", "shuriken"),
                    ("shuriken", "human", "ninja"), ("sword", "ninja", "katana"), ("tool", "land", "farmland"), ("tool", "wood", "plow"), ("plow", "land", "farmland"),
                    ("plow", "earth", "farmland"), ("tool", "earth", "farmland"), ("farmland", "farmland", "field"), ("farmland", "earth", "field"), ("field", "tool", "plow"),
                    ("tree", "fruit", "fruit tree"), ("fruit tree", "fruit tree", "orchard"), ("animal", "field", "lifestock"), ("human", "field", "farmer"),
                    ("farmer", "animal", "domestication"), ("wild animal", "forest", "wolf"), ("wolf", "domestication", "dog"), ("wild animal", "domestication", "dog"),
                    ("animal", "domestication", "lifestock"), ("animal", "blade", "meat"), ("plant", "desert", "cactus"), ("bird", "night", "bat"),
                    ("sky", "rain", "rainbow"), ("continent", "ocean", "planet earth"), ("fire", "sky", "sun"), ("explosion", "sky", "fireworks"), ("explosion", "night", "fireworks"),
                    ("land", "sky", "heaven"), ("land", "volcano", "hell"), ("land", "fire", "hell"), ("stone", "water", "spring"), ("rock", "water", "spring"),
                    ("rock", "boulder", "rock & roll"), ("bird", "metal", "airplane"), ("bird", "human", "angel"), ("human", "sickness", "death"), ("life", "time", "death"),
                    ("angel", "death", "angel of death"), ("angel", "hell", "devil"), ("tree", "blade", "paper"), ("wood", "machine", "paper"), ("paper", "paper", "newspaper"),
                    ("paper", "day", "newspaper"), ("paper", "time", "newspaper"), ("grass", "sun", "hay"), ("grass", "farmer", "hay"), ("farmer", "tool", "pitchfork"),
                    ("farmer", "blade", "pitchfork"), ("pitchfork", "grass", "hay"), ("hay", "hay", "haybale"), ("lifestock", "hay", "horse"), ("animal", "hay", "horse"),
                    ("horse", "human", "knight"), ("human", "blade", "blood"), ("corpse", "corpse", "death"), ("animal", "machine", "leather"), ("lifestock", "machine", "leather"),
                    ("paper", "scissors", "hand craft"), ("paper", "leather", "book"), ("paper", "boat", "paper boat"), ("paper", "airplane", "paper plane"),
                    ("paper", "bird", "orginami"), ("wood", "fire", "campfire"), ("campfire", "campfire", "bonfire"), ("campfire", "time", "coal"), ("campfire", "human", "story"),
                    ("story", "paper", "book"), ("book", "book", "bookself"), ("book", "house", "school"), ("bookself", "house", "library"), ("book", "human", "education"),
                    ("story","time", "myth"), ("myth", "time", "legend"), ("human", "horse", "centaur"), ("glass", "lifestock", "cow"), ("cloud", "lifestock", "sheep"),
                    ("mud", "lifestock", "pig"), ("goat", "domestication", "sheep"), ("cow", "farmer", "milk"), ("scissors", "sheep", "wool"), ("cow", "tool", "milk"),
                    ("pig", "blade", "meat"), ("sheep", "tool", "wool"), ("cow", "blade", "meat"), ("sheep", "blade", "meat"), ("gunpowder", "metal", "bullet"),
                    ("bullet", "bullet", "gun magazine"), ("bullet", "metal", "gun"), ("gun magazine", "metal", "riffle"), ("gun", "gun","riffle"), ("gun", "human", "corpse"),
                    ("corpse", "life", "zombie"), ("bat", "human", "vampire"), ("blood", "human", "vampire"), ("combustion engine", "metal", "car"), ("wood", "tool", "wheel"),
                    ("wheel", "wood", "cart"), ("cart", "combustion engine", "car"), ("engine", "metal", "car"), ("cart", "engine", "car"), ("car", "wood", "cart"),
                    ("cart", "horse", "wagon"), ("wood", "horse", "trojan horse"), ("cow", "human", "minotaur"), ("human", "love", "family"), ("tool", "human", "blacksmith"),
                    ("blacksmith", "metal", "armor"), ("blacksmith", "blade", "sword"), ("blacksmith", "axe", "waraxe"), ("armor", "animal", "armadillo"), ("armor", "human", "warrior"),
                    ("waraxe", "human", "warrior"), ("human", "sword", "warrior"), ("warrior", "horse", "knight"), ("star", "pressure", "neutron star"), ("neutron star", "pressure", "blackhole"),
                    ("wool", "tool", "thread"), ("space", "time", "spacetime"), ("spacetime", "fabric", "fabric of spacetime"), ("thread", "machine", "fabric"),
                    ("wool", "machine", "thread"), ("thread", "tool", "fabric"), ("plant", "cloud", "cotton"), ("plant", "sun", "sunflower"), ("flower", "sun", "sunflower"),
                    ("wind", "sea", "wave"), ("wind", "ocean", "wave"), ("wave", "air", "sound"), ("sound", "human", "music"), ("music", "human", "musician"),
                    ("sound", "wave", "soundwave"), ("sound", "sound", "noise"), ("electricity", "field", "electric field"), ("wave", "spacetime", "gravitational wave"),
                    ("magnet", "field", "magnetic field"), ("magnetic field", "electric field", "electromagnetic field"), ("wave","electromagnetic field", "radiation"),
                    ("metal", "sun", "gold"), ("lightbulb", "human", "idea"), ("bird", "pond", "duck"), ("bird", "lake", "duck"), ("gold", "paper", "money"),
                    ("corpse", "time", "skeleton"), ("life", "death", "organic matter"), ("corpse", "earth", "grave"), ("grave", "stone", "gravestone"),
                    ("money", "house", "bank"), ("money", "pig", "piggy bank"), ("pig", "bank", "piggy bank"), ("grave", "grave", "graveyard"), ("grave", "house", "gravyard"),
                    ("grave", "land", "graveyard"), ("grave", "wood", "casket"), ("graveyard","house", "mausoleum"), ("graveyard", "human", "gravedigger"),
                    ("machine", "life", "robot"), ("robot", "human", "cyborg"), ("machine", "human", "robot"), ("glasses", "human", "nerd"), ("nerd", "machine", "computer"),
                    ("sword", "light", "lightsaber"), ("lightsaber", "human", "jedi"), ("sword", "stone", "excalibur"), ("sword", "rock", "excalibur"),
                    ("excalibur", "human", "monarch"), ("human", "castle", "monarch"), ("monarch", "house", "castle"), ("house", "sky", "skyscraper"), ("house", "tree", "treehouse"),
                    ("house", "bird", "nest"), ("wood", "nest", "birdhouse"), ("house", "dog", "doghouse"), ("milk", "bacteria", "cheece"), ("milk", "ice", "icecream"),
                    ("milk", "time", "yogurt"), ("goat", "tool", "milk"), ("goat", "human", "milk"), ("fabric", "human", "clothes"), ("thread", "human", "tailor"),
                    ("wolf", "house", "cave"), ("bat", "house", "cave"), ("cheece", "animal", "mouse"), ("farmer", "house", "farm"), ("lifestock", "house", "barn"),
                    ("tree", "wind", "leaf"), ("cow", "house", "barn"), ("goat", "house", "barn"), ("pig", "house", "barn"), ("horse", "house", "stable"), ("bird", "lifestock", "chicken"),
                    ("chicken", "house", "chicken coop"), ("chicken", "day", "rooster"), ("organic matter", "pressure", "diamond"), ("diamond", "gold", "ring"),
                    ("ring", "love", "marriage"), ("marriage", "house", "temple"), ("star", "fish", "starfish"), ("house", "barn", "farm"), ("farm", "hay", "cylo"),
                    ("house", "hay", "cylo"), ("car", "field", "tractor"), ("farm", "car", "tractor"), ("tractor", "house", "farm"), ("earth", "metal", "plow"),
                    ("bird", "farm", "chicken"), ("animal", "farm", "lifestock"), ("night", "graveyard", "ghost"), ("night", "grave", "ghost"), ("graveyard", "story", "ghost"),
                    ("horse", "rainbow", "unicorn"), ("horse", "bird", "pegasus"), ("horse", "story", "unicorn"), ("horse", "myth", "pegasus"), ("cave", "water", "spring"),
                    ("lava", "planet", "mantle"), ("mantle", "stone", "mineral"), ("mantle", "rock", "mineral"), ("lava", "planet earth", "mantle"), ("volcano", "earth", "mineral"),
                    ("human", "universe", "world"), ("human", "planet earth", "world"), ("human", "planet", "alien"), ("alien", "airplane", "u.f.o."), ("wave", "world", "hello world!"),
                    ("wind", "wind", "tornado"), ("thunder", "thunder", "thunderstorm"), ("storm", "thunder", "thunderstorm"), ("tornado", "atmosphere", "cyclone"), ("tornado", "tornado", "cyclone"),
                    ("lightning bolt", "sound", "thunderbolt"), ("thunder", "lightning", "lightning bolt"), ("explosion", "bullet", "rocket"), ("rocket", "gun", "rocket launcher"),
                    ("rainbow", "water", "color"), ("color", "water", "paint"), ("paint", "water", "waterpaint"), ("paint", "human", "painter"), ("paint", "tool", "paint brush"),
                    ("flower", "flower", "garden"), ("flower", "grass", "garden"), ("fruit", "heat", "sugar"), ("fruit", "fire", "sugar"), ("fruit", "sun", "sugar"),
                    ("animal", "flower", "bee"), ("bee", "house", "beehive"), ("beehive", "human", "beekeeper"), ("bee", "flower", "honey"), ("bee", "beehive", "wax"),
                    ("bee", "bee", "wax"), ("beehive", "wax", "honey"), ("beehive", "honey", "wax"), ("wax", "fire", "candle"), ("light", "tool", "flashlight"), ("lightbulb", "tool", "flashlight"),
                    ("electricity", "gun", "stungun"), ("egg", "fire", "omelette"), ("human", "idea", "philosophy"), ("idea", "story", "philosophy"), ("human", "house", "society"),
                    ("human", "village", "society"), ("human", "town", "society"), ("nerd", "house", "school"), ("school", "universe", "university"), ("school", "human", "education"),
                    ("education", "idea", "philosophy"), ("philosophy", "universe", "science"), ("philosophy", "world", "science"), ("lightbulb", "house", "lighthouse"), ("light", "house", "lighthouse"),
                    ("electricity", "flashlight", "light"), ("glass", "light", "prism"), ("tomb", "stone", "tombstone"), ("casket", "house", "tomb"), ("grave", "wall", "tomb"),
                    ("tomb", "desert", "pyramid"), ("tomb","sandstone","pyramid"), ("casket","pyramid","sarcophagus"), ("pyramid", "monarch", "pharaoh"), ("desert", "monarch", "pharaoh"),
                    ("pharaoh", "casket", "sarcophagus"), ("grave", "desert", "pyramid"), ("wind", "desert", "dune"), ("corpse", "pyramid", "mummy"), ("fabric","corpse","mummy"),
                    ("plant", "pond", "lilipad"), ("plant", "lake", "lilipad"), ("lilipad", "flower", "lotus flower"), ("flower", "love", "rose"), ("rose", "rose", "bouquete"),
                    ("pottery", "flower", "flower pot"), ("pottery", "rose", "vase"),



                    ]
discovered_items = ["air", "earth", "fire", "water"]
listed_items = []
item_list = []
total_item_count = 4

def recipe_index(element1, element2):
    i = 0
    for e1, e2, res in list_of_recipes:
        if (element1 == e1 and element2 == e2) or (element1 == e2 and element2 == e1):
            return i
        i += 1
    return -1

def insert_item_alphabetically(lst, item):
    if item < lst[0]:
        lst.insert(0,item)
    elif item > lst[-1]:
        lst.append(item)
    else:
        for i in range(0,len(lst)-1):
            if item>lst[i] and item<lst[i+1]:
                lst.insert(i+1,item)
                return

def save_progress(item):
    with open("progress.txt", "w") as file:
        file.write("\n".join(discovered_items))

def load_progress():
    global discovered_items
    with open("progress.txt", "r") as file:
        contents = file.readlines()

    for i in range(len(contents)):
        contents[i] = contents[i].replace("\n", "")

    discovered_items = contents

def special_elements(itm):
    pass

def display_item_list():
    print("\n" * 90)
    for item in discovered_items:
        print(item.title())
    print("")
    print("Press Enter to continue")
    input()

############################################################
load_progress()

# count total items
for res in list_of_recipes:
    if res[2] not in item_list:
        item_list.append(res[2])
total_item_count += len(item_list)
item_list = []

# load available recipes
for item in discovered_items:
    i = 0
    while i < len(list_of_recipes):
        if list_of_recipes[i][2] == item:
            del list_of_recipes[i]
            i -= 1
        i += 1

# load listed items
for item in discovered_items:
    remove_item = True
    for recipe in list_of_recipes:
        if recipe[0] == item or recipe[1] == item:
            remove_item = False
    if remove_item == False:
        listed_items.append(item)

while True:
    print("\n" * 90)
    for item in listed_items:
        print(item.title())
    print("")
    print("Enter two items you want to combine ")
    print(f"(Type 'SEE ALL' to see a list of all your elements) {len(discovered_items)}/{total_item_count}")
    element1 = input("1: ").lower().strip()
    if element1 == 'see all':
        display_item_list()
        continue

    element2 = input("2: ").lower().strip()

    # SEE ALL entry
    # incorect item entry
    if element1 not in listed_items or element2 not in listed_items:
        print("You can't combine items that you don't have")
        time.sleep(2)
        continue

    index = recipe_index(element1, element2)

    if index != -1:
        new_item = list_of_recipes[index][2]
        insert_item_alphabetically(discovered_items, new_item)
        insert_item_alphabetically(listed_items, new_item)
        print("You have discovered " + new_item.title() + "!")

        # checking for discovery of special elements
        special_elements(new_item)

        # deleting recipes that result in the same item
        i = 0
        while i < len(list_of_recipes):
            if list_of_recipes[i][2] == new_item:
                del list_of_recipes[i]
                i -= 1
            i += 1

        # deleting elements if they have no more use
            # Element 1
        read_time = 0
        delete_item = True
        i = 0
        while i < len(list_of_recipes):
            if list_of_recipes[i][0] == element1 or list_of_recipes[i][1] == element1:
                delete_item = False
                break
            i += 1

        if delete_item:
            print("There is nothing more to create with " + element1.title())
            listed_items.remove(element1)
            read_time = 0.5

            # Element 2
        if element2 in listed_items:
            delete_item = True
            i = 0
            while i < len(list_of_recipes):
                if list_of_recipes[i][0] == element2 or list_of_recipes[i][1] == element2:
                    delete_item = False
                    break
                i += 1

            if delete_item:
                print("There is nothing more to create with " + element2.title())
                read_time += 0.5
                listed_items.remove(element2)

        if new_item in listed_items:
            delete_item = True
            i = 0
            while i < len(list_of_recipes):
                if list_of_recipes[i][0] == new_item or list_of_recipes[i][1] == new_item:
                    delete_item = False
                    break
                i += 1

            if delete_item:
                read_time += 0.5
                listed_items.remove(new_item)

        # saving on a file
        save_progress(new_item)

        print("\n\n\n")
        time.sleep(1.5 + read_time)
    else:
        print("Nothing new came out\n\n\n")
        time.sleep(1.5)
