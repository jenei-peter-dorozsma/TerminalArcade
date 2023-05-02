'''Ascii art for dice faces'''

DICE_ART = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    7: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    8: [
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ●   ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ],
    9: [
        "┌─────────┐",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "│  ● ● ●  │",
        "└─────────┘",
    ],
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "