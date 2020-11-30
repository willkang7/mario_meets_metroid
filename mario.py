import pygame
from pygame.sprite import Sprite


class Mario(Sprite):
	"""A class to manage mario."""

	def __init__(self, ai_game):
		"""Initialize mario and set his starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the mario image and get its rect.
		self.image = pygame.image.load('images/mario.bmp')
		self.rect = self.image.get_rect()

		# Start each new mario at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for mario's horizontal position.
		self.x = float(self.rect.x)

		# Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update mario's position based on movement flags."""
		# Update mario's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.mario_speed
			self.image = pygame.image.load('images/mario.bmp')
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.mario_speed
			self.image = pygame.image.load('images/mario_left.bmp')

		# Update rect object from self.x.
		self.rect.x = self.x

	def blitme(self):
		"""Draw mario at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_mario(self):
		"""Center mario on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
