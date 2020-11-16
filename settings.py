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

		# Alien settings
		self.alien_speed = 0.2
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
