import reflex as rx
import smtplib
from email.message import EmailMessage


class BookState(rx.State):
    name: str = ""
    phone: str = ""
    email: str = ""
    city: str = ""
    printertype: str = ""
    hours: str = ""
    problem: str = ""
    submit: str = "Submit"

    def book(self):
        self.submit = "Submitted!"
        msg = EmailMessage()
        msg.set_content(
            f"""
      Name: {self.name}
      Phone: {self.phone}
      Email:{self.email}
      City: {self.city}
      Printer Type: {self.printertype}
      Hours:{self.hours}
      Problem:{self.problem}
            """
        )
        msg["Subject"] = f"WR | New Booking from {self.name}"
        msg["From"] = "wjsobral1000@gmail.com"
        msg["To"] = "wjsobral1000@gmail.com"
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("wjsobral1000@gmail.com", "xokeperqawfclcjp ")
        s.send_message(msg)
        s.quit()


def book() -> rx.Component:
    return rx.box(
        rx.container(rx.heading("Request a consultation"), size="1", padding_left="0%"),
        rx.flex(
            rx.flex(
                rx.text.strong("Name", padding_bottom="2%", padding_top="2%"),
                rx.input(
                    placeholder="enter name...", required=True, value=BookState.name, on_change=BookState.set_name
                ),
                direction="column",
                width="50%",
            ),
            rx.flex(
                rx.text.strong("Phone", padding_bottom="2%", padding_top="2%"),
                rx.input(
                    placeholder="enter phone number...",
                    required=True,
                    value=BookState.phone,
                    on_change=BookState.set_phone,
                ),
                direction="column",
                width="50%",
            ),
            spacing="3",
            width="100%",
        ),
        rx.flex(
            rx.flex(
                rx.text.strong("Email", padding_bottom="2%", padding_top="2%"),
                rx.input(
                    placeholder="enter email...", required=True, value=BookState.email, on_change=BookState.set_email
                ),
                direction="column",
                width="50%",
            ),
            rx.flex(
                rx.text.strong("City", padding_bottom="2%", padding_top="2%"),
                rx.input(placeholder="enter city...", value=BookState.city, on_change=BookState.set_city),
                direction="column",
                width="50%",
            ),
            spacing="3",
            width="100%",
        ),
        rx.flex(
            rx.flex(
                rx.text.strong("3D printer type", padding_bottom="2%", padding_top="2%"),
                rx.input(
                    placeholder="enter printer type...",
                    required=True,
                    value=BookState.printertype,
                    on_change=BookState.set_printertype,
                ),
                direction="column",
                width="50%",
            ),
            rx.flex(
                rx.text.strong("Printer hours", padding_bottom="2%", padding_top="2%"),
                rx.input(
                    placeholder="how many hours on printer...", value=BookState.hours, on_change=BookState.set_hours
                ),
                direction="column",
                width="50%",
            ),
            spacing="3",
            width="100%",
        ),
        rx.flex(
            rx.text.strong("What seems to be the problem?", padding_bottom="2%", padding_top="2%"),
            rx.text_area(
                placeholder="enter brief description here...",
                width="100%",
                value=BookState.problem,
                on_change=BookState.set_problem,
            ),
            width="100%",
            direction="column",
        ),
        # Calender Select
        # rx.card(
        #    rx.grid(
        #        rx.foreach(
        #            rx.Var.range(20),
        #            lambda i: rx.button(
        #                rx.text.strong("1", size="9"),
        #                height="5vh",
        #            ),
        #        ),
        #    ),
        # )),
        # rx.script( src="https://js.stripe.com/v3/"),
        # rx.script( src="library/checkout.js"),
        # rx.html(""""""),
        # rx.html("""<h1>COCCCK</h1>"""),
        rx.spacer(direction="row", spacing="2"),
        rx.container(
            rx.button(BookState.submit, value=BookState.submit, on_click=BookState.book),
            padding_top="5%",
            padding_left="0%",
            padding_bottom="0%",
        ),
        width="100%",
        size="1",
        padding_bottom="0%",
        padding_top="0%",
    )
