import subprocess
import shutil


def detect_capabilities() -> dict:
    has_nvidia = shutil.which("nvidia-settings") is not None
    if has_nvidia:
        return {"supported": True, "partial": True, "reason": "Requires X11 and Coolbits enabled in xorg.conf"}
    return {"supported": False, "partial": False, "reason": "nvidia-settings not found"}


def set_gpu_clocks(core_offset: int, mem_offset: int) -> bool:
    if not shutil.which("nvidia-settings"):
        return False
    try:
        subprocess.run(["nvidia-settings", "-a", f"[gpu:0]/GPUGraphicsClockOffset[3]={core_offset}"], check=True)
        subprocess.run(["nvidia-settings", "-a", f"[gpu:0]/GPUMemoryTransferRateOffset[3]={mem_offset}"], check=True)
        return True
    except Exception:
        return False
