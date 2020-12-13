import pygame
from pygame.sprite import Sprite
import math


class Mario(Sprite):
	"""A class to manage mario."""

	def __init__(self, ai_game):
		"""Initialize mario and set his starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the mario images and get their rect.
		self._prep_images()
		self.image = self.right[0]
		self.rect = self.image.get_rect()
		self.frame = 0
		self.last_move = 'right'

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
			self.image = self.right[math.floor(self.frame)]
			self.last_move = 'right'
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.mario_speed
			self.image = self.left[math.floor(self.frame)]
			self.last_move = 'left'

		# Update rect object from self.x.
		self.rect.x = self.x

		# Update frame.
		self._update_frame()

	def _update_frame(self):
		"""Update mario's image based on movement flags."""
		if not self.moving_left and not self.moving_right:
			if self.last_move == 'right':
				self.frame = 0
				self.image = self.right[self.frame]
			elif self.last_move == 'left':
				self.frame = 0
				self.image = self.left[self.frame]
		else:
			if self.frame < 3.9:
				self.frame += 0.02
			else:
				self.frame = 0

	def blitme(self):
		"""Draw mario at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_mario(self):
		"""Center mario on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

	def _prep_images(self):
		"""Prepare the mario images."""
		self.right = [
			pygame.image.load('images/right_0.png'),
			pygame.image.load('images/right_1.png'),
			pygame.image.load('images/right_0.png'),
			pygame.image.load('images/right_2.png'),
			]
		self.left = [
			pygame.image.load('images/left_0.png'),
			pygame.image.load('images/left_1.png'),
			pygame.image.load('images/left_0.png'),
			pygame.image.load('images/left_2.png'),
			]
