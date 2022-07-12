from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN

from .span_panel import SpanPanel

def panel_to_device_info(panel: SpanPanel):
   return DeviceInfo(
            identifiers={(DOMAIN, panel.serial_number)},
            manufacturer="Span",
            model=f"Span Panel ({panel.model()})",
            name="Span Panel",
            sw_version=panel.firmware_version(),
            configuration_url=f"http://{panel.host}",
        )
