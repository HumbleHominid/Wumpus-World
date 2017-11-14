import random

class Room(object):
   def  __init__(self, attributes = '.'):
        self.attributes = attributes
        self.visited = False

   def describe_room(self):
       for type in self.attributes:
            print(ROOM_DESCRIPTIONS[type])

ROOM_DESCRIPTIONS = {
        'p': "",
        'x': "The room has already been visited",
        '.': "The room is baren",
        'o': "You fall into the pit of dispair never to come back out",
        '~': "You feel a faint breeze on your cheek",
        'w': "You freeze in your steps at the sight of the Wumpus and are powerless while you watch it consume you",
        's': "A foul odor comes over you",
        'g': "A faint shimmer passed before your eyes as you lay sight on the treasure. Gold"
}

class Cave(object):
    def __init__(self, size = 5):
        self.cave = []
        self.size = size
        
        for i in range(size):
            self.cave.append([])

            for j in range(size):
                self.cave[i].append(Room())

        wumpus_x = 0
        wumpus_y = 0

        while wumpus_x == 0 and wumpus_y == 0: 
            wumpus_x = random.randrange(size)
            wumpus_y = random.randrange(size)

        self.cave[wumpus_x][wumpus_y].attributes += 'w'

        self.wumpus_x = wumpus_x
        self.wumpus_y = wumpus_y
        
        gold_x = random.randrange(size)
        gold_y = random.randrange(size)

        self.cave[gold_x][gold_y].attributes += 'g'

        self.gold_x = gold_x
        self.gold_y = gold_y

        for i in [1, -1]:
            new_x = wumpus_x + i
            new_y = wumpus_y + i

            if new_x in range(size):
                self.cave[new_x][wumpus_y].attributes += 's'

            if new_y in range(size):
                self.cave[wumpus_x][new_y].attributes += 's'

        for i in range(size):
            for j in range(size):
                if random.random() < 0.1:
                    self.cave[i][j].attributes += 'o'

                    for k in [1, -1]:
                        new_x = i + k
                        new_y = j + k

                        if new_x in range(size):
                            self.cave[new_x][j].attributes += 's'
                        
                        if new_y in range(size):
                            self.cave[i][new_y].attributes += 's'

class Player(object):
    player_x = 0
    player_y = 0

    def __init__(self):
        pass

    def move(self, dir = ' '):
        dir = dir.lower()
       
        if dir == 'd':
            self.player_y += 1
            print("You take a step to the North")
        elif dir == 'a':
            self.player_x -= 1
            print("You take a step to the West")
        elif dir == 's':
            self.player_y -= 1
            print("You take a step to the South")
        elif dir == 'h':
            self.player_x += 1
            print("You take a step to the East")

def player_commands():
    print("Use d, h, s, or a to move North, East, South, and West respectively")
    print("Usse i to get info on your tile")

cave = Cave()
player = Player()

player_commands()

while (player.player_x != cave.gold_x and player.player_y != cave.gold_y or
        player.player_x != cave.wumpus_x and player.player_y != cave.wumpus_y):
    # prints room description
    cave.cave[player.player_x][player.player_y].describe_room()
    
    p_input = input()

    if p_input in "dash":
        player.move(p_input)