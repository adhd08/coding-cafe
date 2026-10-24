import arcade
import random

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Arcade Dino Runner"

# Physics Settings
GRAVITY = 0.8
JUMP_SPEED = 14
DINO_GROUND_Y = 40

# Colors (Arcade uses normalized tuples or its own color constants)
BG_COLOR = arcade.color.ALABASTER
DINO_COLOR = arcade.color.CHARCOAL
CACTUS_COLOR = arcade.color.FOREST_GREEN

class Dinosaur(arcade.SpriteSolidColor):
    def __init__(self):
        # Create a solid rectangle sprite for the Dino
        super().__init__(width=40, height=50, color=DINO_COLOR)
        self.center_x = 100
        self.center_y = DINO_GROUND_Y + (self.height / 2)

        # Physics vectors
        self.change_y = 0
        self.is_jumping = False

    def update(self):
        # Apply Gravity if in the air
        if self.center_y > DINO_GROUND_Y + (self.height / 2) or self.change_y > 0:
            self.change_y -= GRAVITY

        # Update vertical position
        self.center_y += self.change_y

        # Ground boundary landing check
        min_y = DINO_GROUND_Y + (self.height / 2)
        if self.center_y <= min_y:
            self.center_y = min_y
            self.change_y = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.change_y = JUMP_SPEED
            self.is_jumping = True


class Cactus(arcade.SpriteSolidColor):
    def __init__(self, speed):
        # Vary cactus sizes slightly for erratic patterns
        # FIX: random.choice() needs a sequence to pick from — it was
        # being called with no arguments at all.
        width = random.choice([15, 20, 25, 30])
        height = random.choice([30, 40, 50])
        super().__init__(width=width, height=height, color=CACTUS_COLOR)

        # Position right off-screen
        self.center_x = SCREEN_WIDTH + random.randint(50, 300)
        self.center_y = DINO_GROUND_Y + (self.height / 2)
        self.change_x = -speed

    def update(self):
        self.center_x += self.change_x


class DinoGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BG_COLOR)

        # Game state tracking
        self.game_over = False
        self.score = 0
        self.obstacle_speed = 6

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()

        # Instantiate entities
        self.dino = Dinosaur()
        self.player_list.append(self.dino)

        # Spawn initial obstacle
        self.spawn_obstacle()

    def spawn_obstacle(self):
        cactus = Cactus(self.obstacle_speed)

        # Ensure we don't spawn cacti directly on top of each other
        if len(self.obstacle_list) > 0:
            # FIX: `[-]` is invalid syntax — needed `[-1]` to get the last sprite.
            last_cactus = self.obstacle_list[-1]
            if cactus.center_x < last_cactus.center_x + 250:
                cactus.center_x = last_cactus.center_x + random.randint(250, 450)

        self.obstacle_list.append(cactus)

    def on_draw(self):
        # Standard clear-frame render pass
        self.clear()

        # Draw the solid Ground terrain line
        arcade.draw_line(0, DINO_GROUND_Y, SCREEN_WIDTH, DINO_GROUND_Y, arcade.color.GRAY, 3)

        # Render active game loops
        self.player_list.draw()
        self.obstacle_list.draw()

        # Render Score Overlay Text
        arcade.draw_text(
            f"Score: {int(self.score)}",
            15, SCREEN_HEIGHT - 35,
            arcade.color.CHARCOAL,
            font_size=18, font_name="Kenney Future"
        )

        # Draw Game Over overlay if triggered
        if self.game_over:
            arcade.draw_text(
                "GAME OVER",
                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20,
                arcade.color.CRIMSON, font_size=32,
                anchor_x="center", anchor_y="center"
            )
            arcade.draw_text(
                "Press ENTER to Restart",
                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20,
                arcade.color.CHARCOAL, font_size=16,
                anchor_x="center", anchor_y="center"
            )

    def on_update(self, delta_time):
        if self.game_over:
            return

        # Update entity positions
        self.player_list.update()
        self.obstacle_list.update()

        # Score increases progressively over time
        self.score += delta_time * 10

        # Gradually speed up game dynamically as the score scales up
        self.obstacle_speed = 6 + (int(self.score) // 100)

        # Recycle off-screen obstacles and manage clean spawning loops
        # FIX: iterate over a copy (list(...)) instead of the live SpriteList,
        # since remove_from_sprite_lists() mutates the list mid-iteration and
        # would otherwise cause elements to be silently skipped.
        for cactus in list(self.obstacle_list):
            if cactus.center_x < -50:
                cactus.remove_from_sprite_lists()

        if len(self.obstacle_list) < 3:
            self.spawn_obstacle()

        # Native multi-entity AABB collision checker
        if arcade.check_for_collision_with_list(self.dino, self.obstacle_list):
            self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE or key == arcade.key.UP:
            if not self.game_over:
                self.dino.jump()

        if key == arcade.key.ENTER and self.game_over:
            # RESET/RESTART standard states
            self.game_over = False
            self.score = 0
            self.obstacle_speed = 6
            self.obstacle_list.clear()
            self.dino.center_y = DINO_GROUND_Y + (self.dino.height / 2)
            self.dino.change_y = 0
            self.spawn_obstacle()


if __name__ == "__main__":
    game = DinoGame()
    arcade.run()