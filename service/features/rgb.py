import subprocess
import shutil


def detect_capabilities() -> dict:
    if shutil.which("openrgb"):
        try:
            res = subprocess.run(["openrgb", "--list-devices"], capture_output=True, text=True)
            if "No devices found" not in res.stdout and len(res.stdout.strip()) > 0:
                return {"supported": True, "partial": False, "reason": "OpenRGB devices found"}
            return {"supported": False, "partial": False, "reason": "OpenRGB installed but no devices found"}
        except Exception:
            return {"supported": False, "partial": False, "reason": "OpenRGB command failed"}
    return {"supported": False, "partial": False, "reason": "openrgb not installed"}


def set_rgb_mode(mode: str, color: str = None) -> bool:
    if not shutil.which("openrgb"):
        return False
    cmd = ["openrgb"]

    if mode == "off":
        cmd.extend(["-m", "off"])
    elif mode == "static" and color:
        cmd.extend(["-m", "static", "-c", color])
    elif mode == "breathing" and color:
        cmd.extend(["-m", "breathing", "-c", color])
    elif mode == "rainbow":
        cmd.extend(["-m", "rainbow"])
    else:
        cmd.extend(["-m", "static", "-c", "00FF00"])

    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
