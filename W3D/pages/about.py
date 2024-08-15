"""The dashboard page."""

from W3D.templates import template

import reflex as rx


@template(route="/about", title="About")
def about() -> rx.Component:
    return rx.vstack(
        rx.heading("About", size="8"),
        rx.section(
            rx.heading("What we do"),
            rx.text(
                """Worcester 3D Robotics is a 3D printer service that helps businesses and
                makers get the most out of their 3D printers. We offer comprehensive repair services
                for the most types of 3D printers. From a faulty thermister, broken belt, or buggy firmware, we're here to
                keep your printer operational with expediance and high quality repairs."""
            ),
            size="2",
        ),
        rx.section(
            rx.heading("Philosophy"),
            rx.text(
                """We're not mechanics; we do not put a \"band-aid\" and call it good. High quality service is at the core
                of what we do and we will find the root cause of the problem to ensure it won't be a
                recurrent an issue. If you work with us, your machine will be better off
            than when we found it.""",
            ),
            size="2",
        ),
        rx.section(
            rx.heading("Experience"),
            rx.text(
                """Our team has extensive experience in servicing all types of machines from
                industrial 3D printers the size of a Corrolla to desktop printers like the Taz or
                Creality CR10. We've serviced machines from LulzBot,
            Ultimaker, Makerbot, Prusa, Creality, Monoprice, and more.""",
            ),
            size="2",
        ),
    )
