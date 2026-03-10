from time import sleep

from src.core.models.render_station_model import render_station_model
from src.core.models.teleport_model import TeleportModel
from src.core.models.pego_model import PegoModel
from src.core.models.crystal_cracker_model import CrystalCracker
from src.core.models.iguano_model import IguanoModel
from src.core.models.gacha_model import GachaModel
from src.core.models.berrys_model import BerrysModel
from src.core.ctypes_utils import CtypesUtils


PEGO_LIST = ["pego01", "pego02", "pego03", "pego04", "pego05", "pego06"]

GACHA_LIST = [{"yaw": "left", "tpname": "gacha01"},
              {"yaw": "left", "tpname": "gacha02"},
              {"yaw": "left", "tpname": "gacha03"},
              {"yaw": "left", "tpname": "gacha04"},
              {"yaw": "left", "tpname": "gacha05"},
              {"yaw": "left", "tpname": "gacha06"},
              {"yaw": "left", "tpname": "gacha07"},
              {"yaw": "left", "tpname": "gacha08"},
              {"yaw": "left", "tpname": "gacha09"},
              {"yaw": "left", "tpname": "gacha10"},
              {"yaw": "left", "tpname": "gacha11"},
              {"yaw": "left", "tpname": "gacha12"},
              {"yaw": "right", "tpname": "gacha13"},
              {"yaw": "right", "tpname": "gacha14"},
              {"yaw": "right", "tpname": "gacha15"},
              {"yaw": "right", "tpname": "gacha16"},
              {"yaw": "right", "tpname": "gacha17"},
              {"yaw": "right", "tpname": "gacha18"},
              {"yaw": "right", "tpname": "gacha19"},
              {"yaw": "right", "tpname": "gacha20"},
              {"yaw": "right", "tpname": "gacha21"},
              {"yaw": "right", "tpname": "gacha22"},
              {"yaw": "right", "tpname": "gacha23"},
              {"yaw": "right", "tpname": "gacha24"}
              ]

class GachaBotViewModel:
    def __init__(self):
        self.render_station = render_station_model()
        self.teleporter = TeleportModel()
        self.pego = PegoModel()
        self.cracker = CrystalCracker()
        self.iguano = IguanoModel()
        self.gacha = GachaModel()
        self.berrys = BerrysModel()
        self.ctype = CtypesUtils()

    def start(self, start_type: str = None):
        try:
            if start_type == "normal":
                print("startando normal")
                self.gacha.first_time = False
            sleep(30)
            while True:
                self.render_station.leave_bed_start()
                self.__collect_crystals()
                self.__feed_gachas()
                self.__collect_crystals()
                self.teleporter.teleport("start")
                self.render_station.join_bed_end()
                self.gacha.first_time = False
                sleep(900)
        except Exception as e:
            self.ctype.combo("leftalt","f10")
            print(f"Erro salvo: {e}")

    def __collect_crystals(self):
            for pego in PEGO_LIST:
                self.teleporter.teleport(pego)
                self.pego.collect_crystals()
                self.teleporter.teleport("craker")
                self.cracker.crack_crystals()
                self.teleporter.teleport("grinder")
                self.cracker.grind_items()

    def __feed_gachas(self):
         for gacha_pair in GACHA_LIST:
            self.teleporter.teleport("gtberry")
            self.berrys.get_berrys()
            self.teleporter.teleport("iguano")
            self.iguano.get_seeds_w_berry()
            self.teleporter.teleport(gacha_pair["tpname"])
            self.gacha.feed_gacha(yaw=gacha_pair["yaw"], side="left")
            self.teleporter.teleport("iguano")
            self.iguano.get_seeds_w_no_berrys()
            self.teleporter.teleport(gacha_pair["tpname"])
            self.gacha.feed_gacha(yaw=gacha_pair["yaw"], side="right")
    