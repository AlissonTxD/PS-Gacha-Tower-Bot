import logging
from pathlib import Path
from threading import Event
from time import sleep

from playsound import playsound

from src.core.config.config_controller import ConfigController
from src.core.models.crystal_cracker_model import CrystalCrackerModel
from src.core.models.gacha_model import GachaModel
from src.core.models.grinder_model import GrinderModel
from src.core.models.pego_model import PegoModel
from src.core.models.render_station_model import RenderStationModel
from src.core.models.teleport_model import TeleportModel
from src.core.models.trap_model import TrapModel
from src.core.services.calibration_services import CalibrationServices


class GachaBotViewModel:
    def __init__(self):
        self.stop_event = Event()
        self.load_config()

    # Main functions
    def start_bot_trap(self) -> None:
        """
        Starts the gacha bot feeding with traps
        """
        try:
            self.stop_event.clear()
            self.load_config()
            self.play_start_sound()
            if not self.__wait(5):
                return
            self.render_station.leave_bed()
            if self.stop_event.is_set():
                return
            self.__collect_crystals()
            if self.stop_event.is_set():
                return
            self.__rest()
            while not self.stop_event.is_set():
                self.__feed_all_gachas()
                if self.stop_event.is_set():
                    return
                self.__collect_crystals()
                if self.stop_event.is_set():
                    return
                self.__rest(3)
        except Exception as e:  # noqa: BLE001
            #record
            logging.warning(e)  # noqa: LOG015

    def __collect_crystals(self) -> None:
        pego = 1
        while pego <= self.qtd_pego:
            if self.stop_event.is_set():
                return
            self.teleporter.teleport(f"pego{pego:02d}")
            if self.stop_event.is_set():
                return
            self.pego.collect_crystals()
            if self.stop_event.is_set():
                return
            self.teleporter.teleport("open crystal")
            if self.stop_event.is_set():
                return
            self.cracker.crack_crystals()
            if self.stop_event.is_set():
                    return
            self.teleporter.teleport("grinder")
            if self.stop_event.is_set():
                return
            self.grinder.grind_items()
            pego += 1

    def test_gachas(self):
        sleep(5)
        gacha = 1
        self.render_station.leave_bed()
        while gacha <= self.qtd_gacha:
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.test_gachas()
            gacha += 1

    def __feed_all_gachas(self):
        gacha = 1
        trap = 1
        while gacha <= self.qtd_gacha:
            if self.stop_event.is_set():
                return
            self.teleporter.teleport(f"trap{trap:02d}")
            if self.stop_event.is_set():
                return
            self.trap.get_trap()
            if self.stop_event.is_set():
                return
            self.teleporter.teleport(f"gt{gacha:02d}")
            if self.stop_event.is_set():
                return
            self.gacha.feed_gacha_pair_trap()
            if self.stop_event.is_set():
                return
            gacha += 1
            trap += 1
            if trap > self.qtd_trap:
                trap = 1

    def __rest(self, time: float = 0) -> None:

        self.teleporter.teleport("start")
        self.render_station.join_bed()
        if not self.__wait(time):
            return
        self.render_station.leave_bed()

    def stop_bot(self):
        print(">>> F10: solicitando STOP")
        self.stop_event.set()
        print(">>> F10: STOP enviado")

    def load_config(self):
        self.config = ConfigController()
        self.tools = CalibrationServices()
        self.general_config = self.config.load_config()
        self.qtd_gacha = self.general_config["quantities"]["gacha_boxes"]
        self.qtd_pego = self.general_config["quantities"]["pego_boxes"]
        self.qtd_trap = self.general_config["quantities"]["trap_boxes"]
        self.render_station = RenderStationModel(self.general_config, self.stop_event)
        self.teleporter = TeleportModel(self.general_config, self.stop_event)
        self.pego = PegoModel(self.general_config, self.stop_event)
        self.cracker = CrystalCrackerModel(self.general_config, self.stop_event)
        self.gacha = GachaModel(self.general_config, self.stop_event)
        self.trap = TrapModel(self.general_config, self.stop_event)
        self.grinder = GrinderModel(self.general_config, self.stop_event)

    def __wait(self, seconds: float) -> bool: 
        """ Waits for the specified time. Returns False if the bot was stopped during the wait. """ 
        return not self.stop_event.wait(seconds)

    def play_start_sound(self):
        sound_path = Path(__file__).resolve().parent.parent.parent / "sounds" / "bombardo.mp3"
        print(str(sound_path))
        playsound(str(sound_path))
