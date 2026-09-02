from time import sleep

from src.core.models.render_station_model import render_station_model
from src.core.models.teleport_model import TeleportModel
from src.core.models.pego_model import PegoModel
from src.core.models.crystal_cracker_model import CrystalCracker
from src.core.models.iguano_model import IguanoModel
from src.core.models.gacha_model import GachaModel
from src.core.models.berrys_model import BerrysModel
from src.core.models.trap_model import TrapModel
from src.core.ctypes_utils import CtypesUtils


PEGO_LIST = ["pego01", "pego02", "pego03", "pego04", "pego05", "pego06", "pego07", "pego08", "pego09", "pego10"]
QTD_GACHA = 40

GACHA_LIST_1 = [{"tpname": "gt01"},
              {"tpname": "gt02"},
              {"tpname": "gt03"},
              {"tpname": "gt04"},
              {"tpname": "gt05"},
              {"tpname": "gt06"},
              {"tpname": "gt07"},
              {"tpname": "gt08"},
              {"tpname": "gt09"},
              {"tpname": "gt10"},
              {"tpname": "gt11"},
              {"tpname": "gt12"},
              {"tpname": "gt13"},
              {"tpname": "gt14"},
              {"tpname": "gt15"},
              {"tpname": "gt16"},
              {"tpname": "gt17"},
              {"tpname": "gt18"},
              {"tpname": "gt19"},
              {"tpname": "gt20"},
              ]

GACHA_LIST_2 = [{"tpname": "gt21"},
                {"tpname": "gt22"},
                {"tpname": "gt23"},
                {"tpname": "gt24"},
                {"tpname": "gt25"},
                {"tpname": "gt26"},
                {"tpname": "gt27"},
                {"tpname": "gt28"},
                {"tpname": "gt29"},
                {"tpname": "gt30"},
                {"tpname": "gt31"},
                {"tpname": "gt32"},
                {"tpname": "gt33"},
                {"tpname": "gt34"},
                {"tpname": "gt35"},
                {"tpname": "gt36"},
                {"tpname": "gt37"},
                {"tpname": "gt38"},
                {"tpname": "gt39"},
                {"tpname": "gt40"},]

GACHA_TEST_LIST = [
                   {"tpname": "gt25"},
                   {"tpname": "gt25"},
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
        self.trap = TrapModel()

    def start(self, start_type: str = None):
        try:
            if start_type == "normal":
                print("startando normal")
                self.gacha.first_time = False
            sleep(30)
            self.render_station.leave_bed_start()
            self.__collect_crystals()
            while True:
                self.__feed_gachas_1()
                self.__collect_crystals()
                self.teleporter.teleport("start")
                self.render_station.join_bed_end()
                sleep(30)
                self.render_station.leave_bed_start()
                self.__feed_gachas_2()
                self.__collect_crystals()
                self.teleporter.teleport("start")
                self.render_station.join_bed_end()
                sleep(30)
                self.render_station.leave_bed_start()
                self.gacha.first_time = False
        except Exception as e:
            #self.ctype.combo("leftalt","f10")
            print(f"Erro salvo: {e}")

    def start_trap(self):
        try:
            sleep(5)
            self.render_station.leave_bed_start()
            self.__collect_crystals()
            self.teleporter.teleport("start")
            self.render_station.join_bed_end()
            self.render_station.leave_bed_start()
            while True:
                self.__feed_all_gachas()
                self.__collect_crystals()
                self.teleporter.teleport("start")
                self.render_station.join_bed_end()
                sleep(3)
                self.render_station.leave_bed_start()
        except Exception as e:
            self.record_replay()
            print(f"Erro salvo: {e}")

    def __collect_crystals(self):
            for pego in PEGO_LIST:
                self.teleporter.teleport(pego)
                self.pego.collect_crystals()
                self.teleporter.teleport("open crystal")
                self.cracker.crack_crystals()
                self.teleporter.teleport("grinder")
                self.cracker.grind_items()

    def __feed_gachas_1(self):
         for gacha_pair in GACHA_LIST_1:
            self.teleporter.teleport("gtberry")
            self.berrys.get_berrys()
            self.teleporter.teleport("iguano")
            self.iguano.get_seeds_w_berry()
            self.teleporter.teleport(gacha_pair["tpname"])
            self.gacha.feed_gacha(side="left")
            self.teleporter.teleport("iguano")
            self.iguano.get_seeds_w_no_berrys()
            self.teleporter.teleport(gacha_pair["tpname"])
            self.gacha.feed_gacha(side="right")

    def __feed_gachas_2(self):
         for gacha_pair in GACHA_LIST_2:
            self.teleporter.teleport("gtberry")
            self.berrys.get_berrys()
            self.teleporter.teleport("iguano")
            self.iguano.get_seeds_w_berry()
            self.teleporter.teleport(gacha_pair["tpname"])
            self.gacha.feed_gacha(side="left")
            self.teleporter.teleport("iguano")
            self.iguano.get_seeds_w_no_berrys()
            self.teleporter.teleport(gacha_pair["tpname"])
            self.gacha.feed_gacha(side="right")
    
    def test_gachas(self):
        sleep(5)
        gacha = 25
        self.render_station.leave_bed_start()
        while gacha <= QTD_GACHA:
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.test_gachas()
            gacha += 1

    def __feed_all_gachas(self):
        gacha = 1
        trap = 1
        while gacha <= QTD_GACHA:
            self.teleporter.teleport(f"trap{trap:02d}")
            self.trap.get_trap()
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.feed_gacha_pair_trap()
            gacha += 1
            trap = 3 - trap

    def record_replay(self):
        self.ctype.key_down("leftalt")
        sleep(0.5)
        self.ctype.key_down("f10")
        sleep(0.5)
        self.ctype.key_up("f10")
        self.ctype.key_up("leftalt")