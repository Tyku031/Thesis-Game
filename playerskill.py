import pygame
from pygame.locals import *


playerskills = [
	("Strenth", 0),
	("Dexterity", 1),
	("Physical Resistance", 2),
	("Magic Resistance", 3),
	("Agility", 4),
	("Dodge", 5)
]


class Playerskill:
	def __init__(self, name, iden=-1, level=0, xp=0, xpn=10):
		"""
		:param str name: The name of the skill
		:param int iden: The ID of the skill
		:param int level: The level of the skill
		:param int xp: The experience points of the skill
		:param int xpn: The experience needed for levelup
		"""
		self.name = name
		self.id = iden
		self.level = level
		self.xp = xp
		self.xp_needed = xpn
		# Does nothing at the moment
		# TODO: do something with a good formula to change needed xp per level per skill
		self.xp_formula = "x = x + 10"


# Returns a list of player skills
def init():
	"""
	:return: Returns a list with all player skills
	"""
	tmp = []
	for i in range(len(playerskills)):
		# Create new Baseskill(name, id) object
		tmp.append(Playerskill(playerskills[i][0], playerskills[i][1]))
	return tmp
