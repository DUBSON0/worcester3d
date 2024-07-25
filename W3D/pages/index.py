"""The home page of the app."""

from W3D import styles
from W3D.templates import template
import sys

import reflex as rx


@template(route="/", title="Home")
def index() -> rx.Component:
    rx.html(
        """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4P2FLHP5ZQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-4P2FLHP5ZQ');
</script>"""
    )
    return rx.flex(
        rx.heading("3D Printer Repair and Consultation", size="8"),
        rx.divider(),
        rx.text(
            """Worcester 3D Robotics offers 3D printer repair services in
               Worcester, MA. We strive to provide top-notch repair and maintenance services for all of
               your 3D printing needs. Our team of experienced technicians is dedicated to ensuring
               that your 3D printer is running smoothly and efficiently so you can focus on what
               matters most. If you’re in need of a quick repair or a full maintenance check-up, we’ve
               got you covered."""
        ),
        rx.flex(
            rx.image(src="/titan.webp", alt="titan robotics 3d printer", width="30%", border_radius="10px"),
            rx.spacer(),
            rx.image(src="/mp.webp", alt="Monoprice select mini v2 3d printer", width="30%", border_radius="10px"),
            rx.spacer(),
            rx.image(src="/grover.webp", alt="gover robotics chassis model", width="30%", border_radius="10px"),
        ),
        rx.card(
            rx.heading("Let’s get your project going. ", rx.link("Schedule a consultation", href="start"), size="4"),
            bg="accent",
            color="accent",
        ),
        spacing="5",
        direction="column",
    )


# with open("README.md", encoding="utf-8") as readme:
#     content = readme.read()
# return rx.markdown(content, component_map=styles.markdown_style)
