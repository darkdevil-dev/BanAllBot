import os

class Config:
    API_ID = 24401427
    API_HASH = "7d93af9ff00f5ccb053dbacc3064a1c0"
    TOKEN = "7605194933:AAEPUlTxK0X6LLd5x3RgnN9dQic-aYXzpGc"
    SUDO_RAW = os.environ.get("SUDO", "7086277926")  # Default value
    SUDO = [int(i) for i in SUDO_RAW.replace(",", " ").split() if i.strip().isdigit()]
    START_IMG = "https://telegra.ph/file/52fefb8bd51289a83a49b.jpg"
    BOT_ID = 7605194933
    BOT_USERNAME = "Musical_asj_bot"
    BOT_NAME = "完美世界 石昊"
