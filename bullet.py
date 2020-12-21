import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from mario."""

	def __init__(self, ai_game):
		"""Create a bullet object at mario's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Create a bullet rect at (0, 0) and then set correct position.
		self.image = pygame.image.load('images/fireball.png')
		self.rect = self.image.get_rect()
		self.rect.midtop = ai_game.mario.rect.midtop

		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.y -= self.settings.bullet_speed
		# Update the rect position.
		self.rect.y = self.y
