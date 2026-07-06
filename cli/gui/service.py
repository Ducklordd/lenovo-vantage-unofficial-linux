"""D-Bus client wrapper for talking to vantageservice.

If the service is not running, the wrapper falls back to a "limited mode"
that lets the GUI open but disables all hardware-control actions.
"""

try:
    import dbus
    _DBUS_AVAILABLE = True
except ImportError:
    _DBUS_AVAILABLE = False


class VantageService:
    """Thin wrapper around the org.lenovo.Vantage D-Bus interface.

    On success, ``self.iface`` is a live dbus.Interface and
    ``self.limited`` is False.  If the service is unreachable,
    ``self.iface`` is None and ``self.limited`` is True — the GUI
    can still open but all hardware calls are no-ops.
    """

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
