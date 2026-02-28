from time import sleep

from src.core.models.render_station_model import render_station_model
from src.core.models.teleport_model import TeleportModel
from src.core.models.pego_mode import PegoModel
from src.core.models.crystal_cracker import CrystalCracker

PEGO_LIST = ["pego01", "pego02", "pego03"]

GACHA_LIST = []

class GachaBotViewModel:
    def __init__(self):
        self.render_station = render_station_model()
        self.teleporter = TeleportModel()
        self.pego = PegoModel()
        self.cracker = CrystalCracker()

    def start(self):
        sleep(5)
        while True:
            self.render_station.leave_bed_start()
            for pego in PEGO_LIST:
                self.teleporter.teleport(pego)
                self.pego.collect_crystals()
                self.teleporter.teleport("craker")
                self.cracker.crack_crystals()
                self.teleporter.teleport("grinder")
                self.cracker.grind_items()
            self.teleporter.teleport("start")
            self.render_station.join_bed_end()
            sleep(300)
