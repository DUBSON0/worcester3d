"""Sidebar component for the app."""

from W3D import styles

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.color_mode_cond(
            rx.image(src="/w3d_logo_black.png", height="3em"),
            rx.image(src="/w3d_logo_white.png", height="3em"),
        ),
        rx.spacer(),
        # Link to Reflex GitHub repo.
        rx.link(
            rx.center(
                rx.image(
                    src="/black_heart.png",
                    height="3em",
                    padding="0.5em",
                ),
                box_shadow=styles.box_shadow,
                bg="transparent",
                border_radius=styles.border_radius,
                _hover={
                    "bg": styles.accent_color,
                },
            ),
            href="start",
        ),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.link(
            rx.text("Docs"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            style=styles.link_style,
        ),
        rx.link(
            rx.text("Blog"),
            href="https://reflex.dev/blog/",
            style=styles.link_style,
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )


def sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == f"/{text.lower()}") | ((rx.State.router.page.path == "/") & text == "Home")

    return rx.link(
        rx.hstack(
            rx.text(
                text,
                align="center",
            ),
            bg=rx.cond(
                active,
                styles.accent_color,
                "transparent",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            align="center",
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
            padding_y="1em",
        ),
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                sidebar_item("Home", "/"),
                sidebar_item("Get Started", "/start"),
                sidebar_item("About", "/about"),
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.spacer(),
            sidebar_footer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
