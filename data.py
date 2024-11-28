BLACK: tuple[int, int, int] = (0, 0, 0)

PLAYER1_COLOUR: tuple[int, int, int] = (190, 0, 0)
PLAYER2_COLOUR: tuple[int, int, int] = (190, 190, 0)
BACKGROUND_COLOUR: tuple[int, int, int] = (200, 200, 200)
FRAME_COLOUR: tuple[int, int, int] = (50, 50, 200)
TRANSPARENT_COLOUR: tuple[int, int, int] = (0, 0, 0, 0)

BUTTON_FONT_COLOUR: tuple[int, int, int] = (0, 0, 0)
BUTTON_MENU_COLOUR: tuple[int, int, int] = (150, 150, 255)
BUTTON_MENU_HOVER_COLOUR: tuple[int, int, int] = (100, 100, 200)
BUTTON_MENU_SHADOW_COLOUR: tuple[int, int, int, int] = (0, 0, 0, 50)



FPS: int = 60

BUTTON_OUTLINE_WIDTH: int = 3
BUTTON_FONT_SIZE: int = 25
BUTTON_SHADOW_OFFSET: int = 15
BUTTON_BORDER_RADIUS: int = 18

RECTANGLE_BORDER_RADIUS: int = 50

WINDOWS_WIDTH: int = 810
WINDOWS_HEIGHT: int = 740

FRAME_FEET_WIDTH: int = 40
FRAME_FEET_HEIGHT: int = 40
FRAME_MARGIN: int = 25

CIRCLE_DIAMETER: int = 100
CIRCLE_PADDING: int = 10

columnBoundaries: dict[int, tuple[int, int]] = { }
for i in range(7):
    columnBoundaries[i] = (FRAME_MARGIN + ((CIRCLE_DIAMETER + CIRCLE_PADDING) * i)), (
                            FRAME_MARGIN + CIRCLE_DIAMETER) + ((CIRCLE_DIAMETER + CIRCLE_PADDING) * i)




#![ DONT CHANGE ]
# DEFAULTS
# BLACK: tuple[int, int, int] = (0, 0, 0)

# PLAYER1_COLOUR: tuple[int, int, int] = (190, 0, 0)
# PLAYER2_COLOUR: tuple[int, int, int] = (190, 190, 0)
# BACKGROUND_COLOUR: tuple[int, int, int] = (200, 200, 200)
# FRAME_COLOUR: tuple[int, int, int] = (50, 50, 200)
# TRANSPARENT_COLOUR: tuple[int, int, int] = (0, 0, 0, 0)

# BUTTON_FONT_COLOUR: tuple[int, int, int] = (0, 0, 0)
# BUTTON_MENU_COLOUR: tuple[int, int, int] = (230, 230, 230)
# BUTTON_MENU_HOVER_COLOUR: tuple[int, int, int] = (120, 120, 120)
# BUTTON_MENU_SHADOW_COLOUR: tuple[int, int, int, int] = (0, 0, 0, 50)



# FPS: int = 60

# BUTTON_OUTLINE_WIDTH: int = 3
# BUTTON_FONT_SIZE: int = 25
# BUTTON_SHADOW_OFFSET: int = 15
# BUTTON_BORDER_RADIUS: int = 18

# RECTANGLE_BORDER_RADIUS: int = 50

# WINDOWS_WIDTH: int = 810
# WINDOWS_HEIGHT: int = 740

# FRAME_FEET_WIDTH: int = 40
# FRAME_FEET_HEIGHT: int = 40
# FRAME_MARGIN: int = 25

# CIRCLE_DIAMETER: int = 100
# CIRCLE_PADDING: int = 10

# columnBoundaries: dict[int, tuple[int, int]] = { }
# for i in range(7):
#     columnBoundaries[i] = (FRAME_MARGIN + ((CIRCLE_DIAMETER + CIRCLE_PADDING) * i)), (
#                             FRAME_MARGIN + CIRCLE_DIAMETER) + ((CIRCLE_DIAMETER + CIRCLE_PADDING) * i)