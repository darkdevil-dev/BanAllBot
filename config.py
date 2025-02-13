import os

class Config:
    API_ID = 
    API_HASH = ""
    TOKEN = ""
    SUDO_RAW = os.environ.get("SUDO", "7644357019,7263027158")  # Default value
    SUDO = [int(i) for i in SUDO_RAW.replace(",", " ").split() if i.strip().isdigit()]
    START_IMG = "https://telegra.ph/file/52fefb8bd51289a83a49b.jpg"
    BOT_ID = 7880134209
    BOT_USERNAME = "Musics_ProRobot"
    BOT_NAME = "完美世界 石昊"
