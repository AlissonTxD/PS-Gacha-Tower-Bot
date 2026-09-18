import pygetwindow as gw


class WindowServices:
    def focus_ark(self) -> bool:
        windows = gw.getWindowsWithTitle("ArkAscended")
        if not windows:
            return False
        window = windows[0]
        if window.isMinimized:
            window.restore()
        window.activate()
        return True
