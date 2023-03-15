# Here’s some more info about the project.

# The ship’s starting coordinates are (0, 0), which is on Earth.
# The ship’s destination is (0, 250), which is on the moon.
# The ship will be controlled over a CLI using a standard keyboard as follows:

# The ship starts at (0, 0) at 0 speed, i.e. at complete rest.
# The ship only moves when a valid key is pressed.
# Pressing W increases the ship’s speed and then moves it forward by speed units.
# The ship’s maximum speed is 5.
# Pressing S decreases the ship’s speed and then moves it forward by speed units.
# The ship’s minimum speed is 0.
# After launch, the ship cannot go below speed 1, i.e. it always moves forward until it reaches the moon.
# Pressing A and D move the ship left and right by one unit respectively.
# The ship also moves forward by speed units.
# Write a CLI program in your preferred language to simulate the above spacecraft. Display output as follows:

# Begin with (0, 0) ready for launch.
# After every movement, display the updated position.
# If the ship goes more than 5 points to the left/right, display wrong trajectory.
# If the ship tries to decrease the speed below 1, display minimum speed.
# If the ship tries to increase the speed over 5, display maximum speed.
# When the ship reaches (0, 250) display on the moon.
# If the ship goes beyond 250 on the y-axis, display contact lost.

import sys 
from dataclasses import dataclass

@dataclass
class SpaceShip:
    speed:int = 0
    position: tuple[int,int] = (0,0)

    def interpret_command(self, command:str):
        if command == 'w':
            self.update_speed(1)
        if command == 's':
            self.update_speed(-1)
        if command == 'a':
            self.update_heading(-1)
        if command == 'd':
            self.update_heading(1)

    def update_speed(self,speed:int):
        if speed > 0 and self.speed < 5:
            self.speed += 1
            print(self.speed)
        if speed < 0 and self.speed > 1:
            self.speed -= 1
            print(self.speed)
            
    def update_heading(self, position:int):
        new_position_x = self.position[0] + position
        self.position = (new_position_x, self.position[1])
        print(position)
        if abs(new_position_x) > 5:
            print("wrong trajectory")
    
    def update_position(self, command:str):
        self.interpret_command(command)
        new_position_y = self.position[1] + self.speed
        self.position = (self.position[0], new_position_y)
        if self.position == (0,250):
             print("on the moon")

if __name__ == "__main__":
    # initialize spaceship
    apollo = SpaceShip()

    for line in sys.stdin:
        if 'w' == line.rstrip():
            print("up")
            apollo.update_position("w")
        if 's' == line.rstrip():
            print("down")
            apollo.update_position('s')
        if 'a' == line.rstrip():
            print("left")
            apollo.update_position('a')
        if 'd' == line.rstrip():
            apollo.update_position('d')
        