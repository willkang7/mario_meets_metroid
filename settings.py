class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (160,172,254)

		# Ship settings
		self.ship_speed = 0.5

		# Bullet settings
		self.bullet_speed = 0.4
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (252,85,18)
		self.bullets_allowed = 3
