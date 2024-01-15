import random
class Warrior:
    def __init__ (self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self,opponent):
        opponent.get_damage(self)
    def get_damage(self,opponent):
         self.health-=opponent.damage
         
class Battle:
     @staticmethod
     def battle(player1:Warrior,player2:Warrior):
         while True: 
             if player1.health<=0:
                 print(player2.name,'победил')
                 break 
             if player2.health<=0:
                 print(player1.name,'победил')
                 break 
             who_beat=random.randint(0,1)
             if who_beat==0:
                 player1.attack(player2)
                 print(player1.name,'attack',player1.name,'hp',player2.health) 
             else: 
                 player2.attack(player1)
                 print(player2.name,'attack',player1.name,'hp',player1.health)
                
chan=Warrior( 'Jackie chan',500,150)
terminator=Warrior('Terminator',350,200)
Battle.battle(chan,terminator)     
            