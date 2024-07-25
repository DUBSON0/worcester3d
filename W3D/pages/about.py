"""The dashboard page."""

from W3D.templates import template

import reflex as rx


@template(route="/about", title="About")
def about() -> rx.Component:
    return rx.vstack(
        rx.heading("About", size="8"),
        rx.section(
        rx.heading("What we do"),
        rx.text("""Worcester 3D Robotics is a 3D printer repair business created to help small businsses and
                makers maintain their 3D printers. We offer comprehensive repair services for the majority of consumer
                3D printers."""), size="2"),
        rx.section(
        rx.heading("Philosophy"),
        rx.text(
            """We don't do \"band-aid\" patches. We will find the root cause of the issue and ensure that it
            won't be a recurrent issue. We'll go the extra mile and ensure that your machine is much better off
            than when we found it.""",
        ), size="2"),
        rx.section(
        rx.heading("Experience"),
        rx.text(
            """Our team has extensive experience in servicing all types of machines from industrial printers that are
            the size of a Corrolla to miniature toy printers like the M3D. We've serviced machines from LulzBot,
            Ultimaker, Makerbot, Prusa, Creality, Monoprice, and more.""",
        ), size="2"),
    )
