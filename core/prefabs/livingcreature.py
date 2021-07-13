class LivingCreature:
	def __init__(self, game, hp, max_hp, armor, speed):
		# Get the game's object so we can interact with the world
		self.game = game

		# LivingCreature Base
		self.hp = hp
		self.max_hp = max_hp
		self.armor = armor
		self.speed = speed
