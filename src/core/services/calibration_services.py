import subprocess
from pathlib import Path


class CalibrationServices:
    def __init__(self):
        self.tools_path = (
            Path(__file__).resolve().parent.parent.parent / "tools"
        )

    def open_color_coordinate_capture(self):
        exe = self.tools_path / "CapturadorCoordenadasCor.exe"
        subprocess.Popen([str(exe)])

    def open_calibrator(self):
        exe = self.tools_path / "Calibrador.exe"
        subprocess.Popen([str(exe)])

if __name__ == "__main__":
    calibration_services = CalibrationServices()
    calibration_services.open_calibrator()
    calibration_services.open_color_coordinate_capture()