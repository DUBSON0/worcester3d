"""The dashboard page."""

from W3D.templates import template
from W3D.components.accountAccess import create_account
import reflex as rx


class Redirect(rx.State):
    def go_back(self, route: str):
        return rx.redirect(route)


@template(route="/create-account", title="Create Account")
def createAccount() -> rx.Component:
    return rx.vstack(create_account(), align="center")
