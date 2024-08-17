"""The dashboard page."""
from W3D.templates import template
from W3D.components.book import book
import reflex as rx
from datetime import datetime


class User(rx.Model, table=True):
    first_name: str
    last_name: str
    email: str
    password: str
    # data: dict[str]


class Login(rx.State):
    logged_in: bool = False
    user_id: int
    login_message: str
    # Temp vars
    first_name: str
    last_name: str
    email: str
    form_data: dict

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        print(type(self.form_data))
        # self.attempt_login()

    def attempt_login(self):
        with rx.session() as session:
            user = session.exec(User.select().where(User.email == self.form_data["email"])).first()
            if user != None:
                if user.password == self.form_data["password"]:
                    self.logged_in = True
                    self.user_id = user.id
                    self.first_name = user.first_name
                    self.last_name = user.last_name
                    self.email = user.email
                    self.login_message = "Successfully signed in!"
                else:
                    self.logged_in = False
                    self.login_message = "Incorrect password. Try again"
            else:
                self.login_message = "Username or E-mail not found"
                self.logged_in = False


def login() -> rx.Component:
    return rx.box(
        rx.match(
            Login.logged_in,
            (
                False,
                rx.box(
                    rx.heading("Sign In"),
                    rx.form(
                        rx.vstack(
                            rx.text(),
                            rx.text("Username or E-mail", size="2"),
                            rx.input(name="email", required=True),
                            rx.text("Password", size="2"),
                            rx.input(name="password", type="password", required=True),
                            rx.button("Login", type="submit"),
                            spacing="3",
                        ),
                        on_submit=Login.handle_submit,
                        reset_on_submit=True,
                    ),
                    rx.text(Login.login_message),
                ),
            ),
            (True, rx.heading("You're logged in as " + Login.first_name)),
        )
    )


class CreateAccount(rx.State):
    form_message: str

    def handle_submit(self, form_data: dict):
        if form_data["password"] == form_data["passwordcheck"]:
            with rx.session() as session:
                user = session.exec(User.select().where(User.email == form_data["email"])).all()
            if user == None or user == []:
                with rx.session() as session:
                    session.add(
                        User(
                            first_name=form_data["first_name"],
                            last_name=form_data["last_name"],
                            email=form_data["email"],
                            password=form_data["password"],
                        )
                    )
                    session.commit()
                self.form_message = "Success!"
            else:
                self.form_message = """An account with that email already exists, please reset your password or try a
            different email."""
        else:
            self.form_message = "Passwords do not match, try again"


def create_account() -> rx.Component:
    return rx.box(
        rx.match(
            Login.logged_in,
            (
                False,
                rx.vstack(
                    rx.heading("Create Account"),
                    rx.form(
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(
                                    rx.text("First Name", size="2"),
                                    rx.input(name="first_name", required=True),
                                ),
                                rx.vstack(
                                    rx.text("Last Name", size="2"),
                                    rx.input(name="last_name", required=True),
                                ),
                            ),
                            rx.vstack(
                                rx.text("E-mail", size="2"),
                                rx.input(name="email", required=True, type="email", width="380px"),
                            ),
                            rx.vstack(
                                rx.text("Password", size="2"),
                                rx.hstack(
                                    rx.input(name="password", type="password", required=True),
                                    rx.input(
                                        placeholder="Confirm Password...",
                                        name="passwordcheck",
                                        type="password",
                                        required=True,
                                    ),
                                ),
                            ),
                            rx.button("Sign Up", type="submit"),
                            spacing="3",
                            width="100%",
                        ),
                        on_submit=CreateAccount.handle_submit,
                        reset_on_submit=True,
                    ),
                    rx.text(CreateAccount.form_message),
                ),
            ),
            (True, rx.heading("You're logged in as " + Login.first_name)),
        ),
    )
