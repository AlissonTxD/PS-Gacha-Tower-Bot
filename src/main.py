from src.views.gacha_bot_view import GachaBotView

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def start():
    view = GachaBotView()
    view.menu()