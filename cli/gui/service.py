"""D-Bus client wrapper for talking to vantageservice.

Falls back to "limited mode" if the service is unavailable, letting the
GUI open but disabling all hardware-control actions.
"""

try:
    import dbus
    _DBUS_AVAILABLE = True
except ImportError:
    _DBUS_AVAILABLE = False


class VantageService:
    def __init__(self):
        self.iface = None
        self.limited = False
        if not _DBUS_AVAILABLE:
            self.limited = True
            return
        try:
            bus = dbus.SystemBus()
            obj = bus.get_object("org.lenovo.Vantage", "/org/lenovo/Vantage")
            self.iface = dbus.Interface(obj, "org.lenovo.Vantage")
        except dbus.exceptions.DBusException:
            self.limited = True

    def _safe(self, method_name, *args, default=None):
        if self.limited or self.iface is None:
            return default
        try:
            return getattr(self.iface, method_name)(*args)
        except Exception:
            return default
