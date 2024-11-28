PLAYER1_COLOUR: tuple[int, int, int] = (190, 0, 0)
PLAYER2_COLOUR: tuple[int, int, int] = (190, 190, 0)
BACKGROUND_COLOUR: tuple[int, int, int] = (200, 200, 200)
FRAME_COLOUR: tuple[int, int, int] = (50, 50, 200)
TRANSPARENT_COLOUR: tuple[int, int, int] = (0, 0, 0, 0)

FPS: int = 60

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
# PLAYER1_COLOUR: tuple[int, int, int] = (190, 0, 0)
# PLAYER2_COLOUR: tuple[int, int, int] = (190, 190, 0)
# BACKGROUND_COLOUR: tuple[int, int, int] = (200, 200, 200)
# FRAME_COLOUR: tuple[int, int, int] = (50, 50, 200)
# TRANSPARENT_COLOUR: tuple[int, int, int] = (0, 0, 0, 0)

# FRAME_FEET_WIDTH: int = 40
# FRAME_FEET_HEIGHT: int = 40
# FRAME_MARGIN: int = 25

# CIRCLE_DIAMETER: int = 100
# CIRCLE_PADDING: int = 10

# columnBoundaries: dict[int, tuple[int, int]] = { }
# for i in range(7):
#     columnBoundaries[i] = (25 + (110 * i)), 125 + (110 * i)