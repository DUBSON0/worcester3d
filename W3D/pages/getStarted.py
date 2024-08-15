"""The dashboard page."""
from W3D.templates import template
from W3D.components.book import book
import reflex as rx


@template(route="/start", title="Getting Started")
def start() -> rx.Component:
    return rx.vstack(
        rx.heading("Get Started", size="7"),
        rx.hstack(
            rx.vstack(
                rx.container(
                    rx.card(
                        rx.heading("1. On-boarding", size="4"),
                        rx.text(
                            """Book a 20 minute on-boarding consulation to get started. We will discuss the issue
                    your printer is having and what steps we can take to resolve it."""
                        ),
                    ),
                    size="1",
                ),
                rx.container(
                    rx.card(
                        rx.heading("2. Prognosis", size="4"),
                        rx.text(
                            """After on-boarding our team will compile a comprehensive list of the possible root causes and the procedures
                        required to fix each of them."""
                        ),
                    ),
                    size="1",
                ),
                rx.container(
                    rx.card(
                        rx.heading("3. Repair", size="4"),
                        rx.text(
                            """You can choose to ship or drop off your printer at our location at your cost and
                        we'll repair it for a flat fee."""
                        ),
                    ),
                    size="1",
                ),
                spacing="1",
            ),
            rx.container(
                rx.card(
                    book(),
                ),
                size="1",
            ),
        ),
        rx.divider(),
        rx.container(
            rx.section(
                rx.heading("Pricing", size="4"),
                rx.text(
                    """The on-boarding consulation is free. After consulation we will provide a quote
                    for a flat repair fee. For standard printers the repair fee is typically
                    between $65-$125 including the part costs."""
                ),
                size="1",
            ),
            rx.section(
                rx.heading("Our Guarantee", size="4"),
                rx.text(
                    """We are confident we can repair your printer, we can't guarantee it. In the
                    case we can't repair your printer you won't pay a penny beyond what is fair."""
                ),
                size="1",
            ),
            size="1",
        ),
    )
