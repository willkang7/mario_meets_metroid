import pygame.font
from pygame.sprite import Group

from mario import Mario

class Scoreboard:
	"""A class to report scoring information."""

	def __init__(self, ai_game):
		"""Initialize scorekeeping attributes."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Font settings for scoring information.
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score images.
		self.prep_images()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score, -1)
		score_str = '{:,}'.format(rounded_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.settings.bg_color)

		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		rounded_high_score = round(self.stats.high_score, -1)
		high_score_str = '{:,}'.format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, self.settings.bg_color)

		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Turn the level into a rendered image."""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
			self.text_color, self.settings.bg_color)

		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_marios(self):
		"""Show how many marios are left."""
		self.marios = Group()
		for mario_number in range(self.stats.marios_left):
			mario = Mario(self.ai_game)
			mario.rect.x = 10 + mario_number * (mario.rect.width + 10)
			mario.rect.y = 10
			self.marios.add(mario)

	def prep_images(self):
		"""Prepare the initial score images."""
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_marios()

	def show_score(self):
		"""Draw scores, level and marios to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.marios.draw(self.screen)

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()
