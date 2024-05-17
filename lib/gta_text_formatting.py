"""
This module defines constant values related to GTA formatting for better organization
and readability of the code.
    HUD_COLORS (dict): A dictionary containing RGBA values for various HUD colors used in the game.
    FORMAT_REPLACEMENT_TABLE (list): A list of replacement rules used to map formatting tags to their corresponding HUD color tags.
    TEXT_FORMATTING_REGEX (str): A regular expression pattern for detecting various text formatting tags in GTA strings.
"""
HUD_COLORS = {
    "HUD_COLOUR_PURE_WHITE": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_WHITE": "rgba(240, 240, 240, 255)",
    "HUD_COLOUR_BLACK": "rgba(0, 0, 0, 255)",
    "HUD_COLOUR_GREY": "rgba(155, 155, 155, 255)",
    "HUD_COLOUR_GREYLIGHT": "rgba(205, 205, 205, 255)",
    "HUD_COLOUR_GREYDARK": "rgba(77, 77, 77, 255)",
    "HUD_COLOUR_RED": "rgba(224, 50, 50, 255)",
    "HUD_COLOUR_REDLIGHT": "rgba(240, 153, 153, 255)",
    "HUD_COLOUR_REDDARK": "rgba(112, 25, 25, 255)",
    "HUD_COLOUR_BLUE": "rgba(93, 182, 229, 255)",
    "HUD_COLOUR_BLUELIGHT": "rgba(174, 219, 242, 255)",
    "HUD_COLOUR_BLUEDARK": "rgba(47, 92, 115, 255)",
    "HUD_COLOUR_YELLOW": "rgba(240, 200, 80, 255)",
    "HUD_COLOUR_YELLOWLIGHT": "rgba(254, 235, 169, 255)",
    "HUD_COLOUR_YELLOWDARK": "rgba(126, 107, 41, 255)",
    "HUD_COLOUR_ORANGE": "rgba(255, 133, 85, 255)",
    "HUD_COLOUR_ORANGELIGHT": "rgba(255, 194, 170, 255)",
    "HUD_COLOUR_ORANGEDARK": "rgba(127, 66, 42, 255)",
    "HUD_COLOUR_GREEN": "rgba(114, 204, 114, 255)",
    "HUD_COLOUR_GREENLIGHT": "rgba(185, 230, 185, 255)",
    "HUD_COLOUR_GREENDARK": "rgba(57, 102, 57, 255)",
    "HUD_COLOUR_PURPLE": "rgba(132, 102, 226, 255)",
    "HUD_COLOUR_PURPLELIGHT": "rgba(192, 179, 239, 255)",
    "HUD_COLOUR_PURPLEDARK": "rgba(67, 57, 111, 255)",
    "HUD_COLOUR_PINK": "rgba(203, 54, 148, 255)",
    "HUD_COLOUR_RADAR_HEALTH": "rgba(53, 154, 71, 255)",
    "HUD_COLOUR_RADAR_ARMOUR": "rgba(93, 182, 229, 255)",
    "HUD_COLOUR_RADAR_DAMAGE": "rgba(235, 36, 39, 255)",
    "HUD_COLOUR_NET_PLAYER1": "rgba(194, 80, 80, 255)",
    "HUD_COLOUR_NET_PLAYER2": "rgba(156, 110, 175, 255)",
    "HUD_COLOUR_NET_PLAYER3": "rgba(255, 123, 196, 255)",
    "HUD_COLOUR_NET_PLAYER4": "rgba(247, 159, 123, 255)",
    "HUD_COLOUR_NET_PLAYER5": "rgba(178, 144, 132, 255)",
    "HUD_COLOUR_NET_PLAYER6": "rgba(141, 206, 167, 255)",
    "HUD_COLOUR_NET_PLAYER7": "rgba(113, 169, 175, 255)",
    "HUD_COLOUR_NET_PLAYER8": "rgba(211, 209, 231, 255)",
    "HUD_COLOUR_NET_PLAYER9": "rgba(144, 127, 153, 255)",
    "HUD_COLOUR_NET_PLAYER10": "rgba(106, 196, 191, 255)",
    "HUD_COLOUR_NET_PLAYER11": "rgba(214, 196, 153, 255)",
    "HUD_COLOUR_NET_PLAYER12": "rgba(234, 142, 80, 255)",
    "HUD_COLOUR_NET_PLAYER13": "rgba(152, 203, 234, 255)",
    "HUD_COLOUR_NET_PLAYER14": "rgba(178, 98, 135, 255)",
    "HUD_COLOUR_NET_PLAYER15": "rgba(144, 142, 122, 255)",
    "HUD_COLOUR_NET_PLAYER16": "rgba(166, 117, 94, 255)",
    "HUD_COLOUR_NET_PLAYER17": "rgba(175, 168, 168, 255)",
    "HUD_COLOUR_NET_PLAYER18": "rgba(232, 142, 155, 255)",
    "HUD_COLOUR_NET_PLAYER19": "rgba(187, 214, 91, 255)",
    "HUD_COLOUR_NET_PLAYER20": "rgba(12, 123, 86, 255)",
    "HUD_COLOUR_NET_PLAYER21": "rgba(123, 196, 255, 255)",
    "HUD_COLOUR_NET_PLAYER22": "rgba(171, 60, 230, 255)",
    "HUD_COLOUR_NET_PLAYER23": "rgba(206, 169, 13, 255)",
    "HUD_COLOUR_NET_PLAYER24": "rgba(71, 99, 173, 255)",
    "HUD_COLOUR_NET_PLAYER25": "rgba(42, 166, 185, 255)",
    "HUD_COLOUR_NET_PLAYER26": "rgba(186, 157, 125, 255)",
    "HUD_COLOUR_NET_PLAYER27": "rgba(201, 225, 255, 255)",
    "HUD_COLOUR_NET_PLAYER28": "rgba(240, 240, 150, 255)",
    "HUD_COLOUR_NET_PLAYER29": "rgba(237, 140, 161, 255)",
    "HUD_COLOUR_NET_PLAYER30": "rgba(249, 138, 138, 255)",
    "HUD_COLOUR_NET_PLAYER31": "rgba(252, 239, 166, 255)",
    "HUD_COLOUR_NET_PLAYER32": "rgba(240, 240, 240, 255)",
    "HUD_COLOUR_SIMPLEBLIP_DEFAULT": "rgba(159, 201, 166, 255)",
    "HUD_COLOUR_MENU_BLUE": "rgba(140, 140, 140, 255)",
    "HUD_COLOUR_MENU_GREY_LIGHT": "rgba(140, 140, 140, 255)",
    "HUD_COLOUR_MENU_BLUE_EXTRA_DARK": "rgba(40, 40, 40, 255)",
    "HUD_COLOUR_MENU_YELLOW": "rgba(240, 160, 0, 255)",
    "HUD_COLOUR_MENU_YELLOW_DARK": "rgba(240, 160, 0, 255)",
    "HUD_COLOUR_MENU_GREEN": "rgba(240, 160, 0, 255)",
    "HUD_COLOUR_MENU_GREY": "rgba(140, 140, 140, 255)",
    "HUD_COLOUR_MENU_GREY_DARK": "rgba(60, 60, 60, 255)",
    "HUD_COLOUR_MENU_HIGHLIGHT": "rgba(30, 30, 30, 255)",
    "HUD_COLOUR_MENU_STANDARD": "rgba(140, 140, 140, 255)",
    "HUD_COLOUR_MENU_DIMMED": "rgba(75, 75, 75, 255)",
    "HUD_COLOUR_MENU_EXTRA_DIMMED": "rgba(50, 50, 50, 255)",
    "HUD_COLOUR_BRIEF_TITLE": "rgba(95, 95, 95, 255)",
    "HUD_COLOUR_MID_GREY_MP": "rgba(100, 100, 100, 255)",
    "HUD_COLOUR_NET_PLAYER1_DARK": "rgba(93, 39, 39, 255)",
    "HUD_COLOUR_NET_PLAYER2_DARK": "rgba(77, 55, 89, 255)",
    "HUD_COLOUR_NET_PLAYER3_DARK": "rgba(124, 62, 99, 255)",
    "HUD_COLOUR_NET_PLAYER4_DARK": "rgba(120, 80, 80, 255)",
    "HUD_COLOUR_NET_PLAYER5_DARK": "rgba(87, 72, 66, 255)",
    "HUD_COLOUR_NET_PLAYER6_DARK": "rgba(74, 103, 83, 255)",
    "HUD_COLOUR_NET_PLAYER7_DARK": "rgba(60, 85, 88, 255)",
    "HUD_COLOUR_NET_PLAYER8_DARK": "rgba(105, 105, 64, 255)",
    "HUD_COLOUR_NET_PLAYER9_DARK": "rgba(72, 63, 76, 255)",
    "HUD_COLOUR_NET_PLAYER10_DARK": "rgba(53, 98, 95, 255)",
    "HUD_COLOUR_NET_PLAYER11_DARK": "rgba(107, 98, 76, 255)",
    "HUD_COLOUR_NET_PLAYER12_DARK": "rgba(117, 71, 40, 255)",
    "HUD_COLOUR_NET_PLAYER13_DARK": "rgba(76, 101, 117, 255)",
    "HUD_COLOUR_NET_PLAYER14_DARK": "rgba(65, 35, 47, 255)",
    "HUD_COLOUR_NET_PLAYER15_DARK": "rgba(72, 71, 61, 255)",
    "HUD_COLOUR_NET_PLAYER16_DARK": "rgba(85, 58, 47, 255)",
    "HUD_COLOUR_NET_PLAYER17_DARK": "rgba(87, 84, 84, 255)",
    "HUD_COLOUR_NET_PLAYER18_DARK": "rgba(116, 71, 77, 255)",
    "HUD_COLOUR_NET_PLAYER19_DARK": "rgba(93, 107, 45, 255)",
    "HUD_COLOUR_NET_PLAYER20_DARK": "rgba(6, 61, 43, 255)",
    "HUD_COLOUR_NET_PLAYER21_DARK": "rgba(61, 98, 127, 255)",
    "HUD_COLOUR_NET_PLAYER22_DARK": "rgba(85, 30, 115, 255)",
    "HUD_COLOUR_NET_PLAYER23_DARK": "rgba(103, 84, 6, 255)",
    "HUD_COLOUR_NET_PLAYER24_DARK": "rgba(35, 49, 86, 255)",
    "HUD_COLOUR_NET_PLAYER25_DARK": "rgba(21, 83, 92, 255)",
    "HUD_COLOUR_NET_PLAYER26_DARK": "rgba(93, 98, 62, 255)",
    "HUD_COLOUR_NET_PLAYER27_DARK": "rgba(100, 112, 127, 255)",
    "HUD_COLOUR_NET_PLAYER28_DARK": "rgba(120, 120, 75, 255)",
    "HUD_COLOUR_NET_PLAYER29_DARK": "rgba(152, 76, 93, 255)",
    "HUD_COLOUR_NET_PLAYER30_DARK": "rgba(124, 69, 69, 255)",
    "HUD_COLOUR_NET_PLAYER31_DARK": "rgba(10, 43, 50, 255)",
    "HUD_COLOUR_NET_PLAYER32_DARK": "rgba(95, 95, 10, 255)",
    "HUD_COLOUR_BRONZE": "rgba(180, 130, 97, 255)",
    "HUD_COLOUR_SILVER": "rgba(150, 153, 161, 255)",
    "HUD_COLOUR_GOLD": "rgba(214, 181, 99, 255)",
    "HUD_COLOUR_PLATINUM": "rgba(166, 221, 190, 255)",
    "HUD_COLOUR_GANG1": "rgba(29, 100, 153, 255)",
    "HUD_COLOUR_GANG2": "rgba(214, 116, 15, 255)",
    "HUD_COLOUR_GANG3": "rgba(135, 125, 142, 255)",
    "HUD_COLOUR_GANG4": "rgba(229, 119, 185, 255)",
    "HUD_COLOUR_SAME_CREW": "rgba(252, 239, 166, 255)",
    "HUD_COLOUR_FREEMODE": "rgba(45, 110, 185, 255)",
    "HUD_COLOUR_PAUSE_BG": "rgba(0, 0, 0, 186)",
    "HUD_COLOUR_FRIENDLY": "rgba(93, 182, 229, 255)",
    "HUD_COLOUR_ENEMY": "rgba(194, 80, 80, 255)",
    "HUD_COLOUR_LOCATION": "rgba(240, 200, 80, 255)",
    "HUD_COLOUR_PICKUP": "rgba(114, 204, 114, 255)",
    "HUD_COLOUR_PAUSE_SINGLEPLAYER": "rgba(114, 204, 114, 255)",
    "HUD_COLOUR_FREEMODE_DARK": "rgba(22, 55, 92, 255)",
    "HUD_COLOUR_INACTIVE_MISSION": "rgba(154, 154, 154, 255)",
    "HUD_COLOUR_DAMAGE": "rgba(194, 80, 80, 255)",
    "HUD_COLOUR_PINKLIGHT": "rgba(252, 115, 201, 255)",
    "HUD_COLOUR_PM_MITEM_HIGHLIGHT": "rgba(252, 177, 49, 255)",
    "HUD_COLOUR_SCRIPT_VARIABLE": "rgba(0, 0, 0, 255)",
    "HUD_COLOUR_YOGA": "rgba(109, 247, 204, 255)",
    "HUD_COLOUR_TENNIS": "rgba(241, 101, 34, 255)",
    "HUD_COLOUR_GOLF": "rgba(214, 189, 97, 255)",
    "HUD_COLOUR_SHOOTING_RANGE": "rgba(112, 25, 25, 255)",
    "HUD_COLOUR_FLIGHT_SCHOOL": "rgba(47, 92, 115, 255)",
    "HUD_COLOUR_NORTH_BLUE": "rgba(93, 182, 229, 255)",
    "HUD_COLOUR_SOCIAL_CLUB": "rgba(234, 153, 28, 255)",
    "HUD_COLOUR_PLATFORM_BLUE": "rgba(11, 55, 123, 255)",
    "HUD_COLOUR_PLATFORM_GREEN": "rgba(146, 200, 62, 255)",
    "HUD_COLOUR_PLATFORM_GREY": "rgba(234, 153, 28, 255)",
    "HUD_COLOUR_FACEBOOK_BLUE": "rgba(66, 89, 148, 255)",
    "HUD_COLOUR_INGAME_BG": "rgba(0, 0, 0, 186)",
    "HUD_COLOUR_DARTS": "rgba(114, 204, 114, 255)",
    "HUD_COLOUR_WAYPOINT": "rgba(164, 76, 242, 255)",
    "HUD_COLOUR_MICHAEL": "rgba(101, 180, 212, 255)",
    "HUD_COLOUR_FRANKLIN": "rgba(171, 237, 171, 255)",
    "HUD_COLOUR_TREVOR": "rgba(255, 163, 87, 255)",
    "HUD_COLOUR_GOLF_P1": "rgba(240, 240, 240, 255)",
    "HUD_COLOUR_GOLF_P2": "rgba(235, 239, 30, 255)",
    "HUD_COLOUR_GOLF_P3": "rgba(255, 149, 14, 255)",
    "HUD_COLOUR_GOLF_P4": "rgba(246, 60, 161, 255)",
    "HUD_COLOUR_WAYPOINTLIGHT": "rgba(210, 166, 249, 255)",
    "HUD_COLOUR_WAYPOINTDARK": "rgba(82, 38, 121, 255)",
    "HUD_COLOUR_PANEL_LIGHT": "rgba(0, 0, 0, 77)",
    "HUD_COLOUR_MICHAEL_DARK": "rgba(72, 103, 116, 255)",
    "HUD_COLOUR_FRANKLIN_DARK": "rgba(85, 118, 85, 255)",
    "HUD_COLOUR_TREVOR_DARK": "rgba(127, 81, 43, 255)",
    "HUD_COLOUR_OBJECTIVE_ROUTE": "rgba(240, 200, 80, 255)",
    "HUD_COLOUR_PAUSEMAP_TINT": "rgba(0, 0, 0, 215)",
    "HUD_COLOUR_PAUSE_DESELECT": "rgba(100, 100, 100, 127)",
    "HUD_COLOUR_PM_WEAPONS_PURCHASABLE": "rgba(45, 110, 185, 255)",
    "HUD_COLOUR_PM_WEAPONS_LOCKED": "rgba(240, 240, 240, 191)",
    "HUD_COLOUR_END_SCREEN_BG": "rgba(0, 0, 0, 186)",
    "HUD_COLOUR_CHOP": "rgba(224, 50, 50, 255)",
    "HUD_COLOUR_PAUSEMAP_TINT_HALF": "rgba(0, 0, 0, 215)",
    "HUD_COLOUR_NORTH_BLUE_OFFICIAL": "rgba(0, 71, 133, 255)",
    "HUD_COLOUR_SCRIPT_VARIABLE_2": "rgba(0, 0, 0, 255)",
    "HUD_COLOUR_H": "rgba(33, 118, 37, 255)",
    "HUD_COLOUR_HDARK": "rgba(37, 102, 40, 255)",
    "HUD_COLOUR_T": "rgba(234, 153, 28, 255)",
    "HUD_COLOUR_TDARK": "rgba(225, 140, 8, 255)",
    "HUD_COLOUR_HSHARD": "rgba(20, 40, 0, 255)",
    "HUD_COLOUR_CONTROLLER_MICHAEL": "rgba(48, 255, 255, 255)",
    "HUD_COLOUR_CONTROLLER_FRANKLIN": "rgba(48, 255, 0, 255)",
    "HUD_COLOUR_CONTROLLER_TREVOR": "rgba(176, 80, 0, 255)",
    "HUD_COLOUR_CONTROLLER_CHOP": "rgba(127, 0, 0, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_VIDEO": "rgba(53, 166, 224, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_AUDIO": "rgba(162, 79, 157, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_TEXT": "rgba(104, 192, 141, 255)",
    "HUD_COLOUR_HB_BLUE": "rgba(29, 100, 153, 255)",
    "HUD_COLOUR_HB_YELLOW": "rgba(234, 153, 28, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_SCORE": "rgba(240, 160, 1, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_AUDIO_FADEOUT": "rgba(59, 34, 57, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_TEXT_FADEOUT": "rgba(41, 68, 53, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_SCORE_FADEOUT": "rgba(82, 58, 10, 255)",
    "HUD_COLOUR_HEIST_BACKGROUND": "rgba(37, 102, 40, 186)",
    "HUD_COLOUR_VIDEO_EDITOR_AMBIENT": "rgba(240, 200, 80, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_AMBIENT_FADEOUT": "rgba(80, 70, 34, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_AMBIENT_DARK": "rgba(255, 133, 85, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_AMBIENT_LIGHT": "rgba(255, 194, 170, 255)",
    "HUD_COLOUR_VIDEO_EDITOR_AMBIENT_MID": "rgba(255, 133, 85, 255)",
    "HUD_COLOUR_LOW_FLOW": "rgba(240, 200, 80, 255)",
    "HUD_COLOUR_LOW_FLOW_DARK": "rgba(126, 107, 41, 255)",
    "HUD_COLOUR_G1": "rgba(247, 159, 123, 255)",
    "HUD_COLOUR_G2": "rgba(226, 134, 187, 255)",
    "HUD_COLOUR_G3": "rgba(239, 238, 151, 255)",
    "HUD_COLOUR_G4": "rgba(113, 169, 175, 255)",
    "HUD_COLOUR_G5": "rgba(160, 140, 193, 255)",
    "HUD_COLOUR_G6": "rgba(141, 206, 167, 255)",
    "HUD_COLOUR_G7": "rgba(181, 214, 234, 255)",
    "HUD_COLOUR_G8": "rgba(178, 144, 132, 255)",
    "HUD_COLOUR_G9": "rgba(0, 132, 114, 255)",
    "HUD_COLOUR_G10": "rgba(216, 85, 117, 255)",
    "HUD_COLOUR_G11": "rgba(30, 100, 152, 255)",
    "HUD_COLOUR_G12": "rgba(43, 181, 117, 255)",
    "HUD_COLOUR_G13": "rgba(233, 141, 79, 255)",
    "HUD_COLOUR_G14": "rgba(137, 210, 215, 255)",
    "HUD_COLOUR_G15": "rgba(134, 125, 141, 255)",
    "HUD_COLOUR_ADVERSARY": "rgba(109, 34, 33, 255)",
    "HUD_COLOUR_DEGEN_RED": "rgba(255, 0, 0, 255)",
    "HUD_COLOUR_DEGEN_YELLOW": "rgba(255, 255, 0, 255)",
    "HUD_COLOUR_DEGEN_GREEN": "rgba(0, 255, 0, 255)",
    "HUD_COLOUR_DEGEN_CYAN": "rgba(0, 255, 255, 255)",
    "HUD_COLOUR_DEGEN_BLUE": "rgba(0, 0, 255, 255)",
    "HUD_COLOUR_DEGEN_MAGENTA": "rgba(255, 0, 255, 255)",
    "HUD_COLOUR_STUNT_1": "rgba(38, 136, 234, 255)",
    "HUD_COLOUR_STUNT_2": "rgba(224, 50, 50, 255)",
    "HUD_COLOUR_SPECIAL_RACE_SERIES": "rgba(154, 178, 54, 255)",
    "HUD_COLOUR_SPECIAL_RACE_SERIES_DARK": "rgba(93, 107, 45, 255)",
    "HUD_COLOUR_CS": "rgba(206, 169, 13, 255)",
    "HUD_COLOUR_CS_DARK": "rgba(103, 84, 6, 255)",
    "HUD_COLOUR_TECH_GREEN": "rgba(0, 151, 151, 255)",
    "HUD_COLOUR_TECH_GREEN_DARK": "rgba(5, 119, 113, 255)",
    "HUD_COLOUR_TECH_RED": "rgba(151, 0, 0, 255)",
    "HUD_COLOUR_TECH_GREEN_VERY_DARK": "rgba(0, 40, 40, 255)",
    "HUD_COLOUR_PLACEHOLDER_01": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_02": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_03": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_04": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_05": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_06": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_07": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_08": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_09": "rgba(255, 255, 255, 255)",
    "HUD_COLOUR_PLACEHOLDER_10": "rgba(255, 255, 255, 255)"
}

FORMAT_REPLACEMENT_TABLE = [
    [r"~r~", '~HUD_COLOUR_RED~'],
    [r"~g~", '~HUD_COLOUR_GREEN~'],
    [r"~b~", '~HUD_COLOUR_BLUE~'],
    [r"~f~", '~HUD_COLOUR_FRIENDLY~'],
    [r"~y~", '~HUD_COLOUR_YELLOW~'],
    [r"~c~", '~HUD_COLOUR_MENU_GREY~'],
    [r"~t~", '~HUD_COLOUR_MENU_GREY~'],
    [r"~o~", '~HUD_COLOUR_ORANGE~'],
    [r"~p~", '~HUD_COLOUR_PURPLE~'],
    [r"~q~", '~HUD_COLOUR_PINK~'],
    [r"~m~", '~HUD_COLOUR_MID_GREY_MP~'],
    [r"~l~", '~HUD_COLOUR_BLACK~'],
    [r"~d~", '~HUD_COLOUR_BLUEDARK~'],
    [r"~s~", '~HUD_COLOUR_GREYLIGHT~']
]

LONG_TEXT_FORMATTING_REGEX = r"~h~|~n~|~bold~|~italic~|\(C\)|\(\/C\)|~HUD_COLOUR_.+?~|~HC_.+?~|~CC_[0-9]{1,3}_[0-9]{1,3}_[0-9]{1,3}~"