"""The dashboard page."""
from W3D.templates import template
from W3D.components.book import book
import reflex as rx
from datetime import datetime
from W3D.components.accountAccess import login


class MultipageFormControl(rx.State):  # For use with the match component. Must set control max for any given element.
    control = 0
    control_min: int = 0
    control_max: int = 5
    continue_to_next: bool = True

    def control_add(self):
        self.control += 1

    def control_sub(self):
        self.control -= 1


def form_navigation_buttons(manipulated_class) -> rx.Component:
    return rx.flex(
        rx.cond(
            Login.logged_in == True,
            rx.hstack(
                rx.cond(
                    MultipageFormControl.control > MultipageFormControl.control_min,
                    rx.button(rx.icon("move-left"), on_click=MultipageFormControl.control_sub),
                ),
                rx.spacer(),
                rx.cond(
                    MultipageFormControl.control < MultipageFormControl.control_max,
                    rx.button(
                        rx.icon("move-right"),
                        on_click=MultipageFormControl.control_add,
                    ),
                ),
                rx.cond(
                    MultipageFormControl.control == MultipageFormControl.control_max,
                    rx.button("Submit", on_click=manipulated_class.submit),
                ),
                width="100%",
            ),
        ),
        width="100%",
    )


class Inquiry(rx.State):
    printer_brand: str
    printer_model: str
    printer_hours: int
    problem_type: str
    problem_desc: str
    service_type: str
    user_comments: str
    our_notes: str
    problem_type_ops: list[str] = [
        "Print quality",
        "Extrusion/hotend",
        "Bed adheasion",
        "Electrical",
        "Mechanical",
        "Firmware/Software",
        "Other",
    ]
    service_type_ops: list[str] = ["In-person dropoff", "Ship remotely", "Virtual meeting"]
    printer_brand_ops: list[str] = [
        "Anycubic",
        "Artillery",
        "BCN3D",
        "Creality",
        "Dremel",
        "ELEGOO",
        "FLSUN",
        "FlashForge",
        "LulzBot",
        "MakerBot",
        "M3D",
        "Monoprice",
        "Prusa",
        "Qidi",
        "Raise3D",
        "SeeMeCNC",
        "Tevo",
        "Ultimaker",
        "Voron",
        "Wanhao",
        "Other",
    ]

    def compile_inquiry(self):
        compiled_inquiry = {
            "datetime": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            "form type": "Onboarding Form",
            " printer_brand": self.printer_brand,
            " printer_model": self.printer_model,
            " printer_hours": self.printer_hours,
            " problem_type ": self.problem_type,
            " problem_desc ": self.problem_desc,
            " service_type ": self.service_type,
            " user_comments": self.user_comments,
            " our_notes": self.our_notes,
        }
        print(compiled_inquiry)

    def submit(self):  # This method is required to interface with the submit button in the case left right switches.
        print(self.compile_inquiry())


def CreateInquiry(manipulated_class) -> rx.Component:
    MultipageFormControl.control_max = 3
    return rx.card(
        rx.vstack(
            rx.match(
                Login.logged_in,
                (False, rx.vstack(login(), rx.text("Don't have an account? ", rx.link("Sign Up")))),
                (
                    True,
                    rx.match(
                        MultipageFormControl.control,
                        (
                            0,
                            rx.box(
                                rx.vstack(
                                    rx.heading(f"Hi, {Login.first_name}.", size="5"),
                                    rx.heading("Tell us about your 3D printer."),
                                    rx.text("What brand is it?"),
                                    rx.select(
                                        Inquiry.printer_brand_ops,
                                        value=Inquiry.printer_brand,
                                        on_change=Inquiry.set_printer_brand,
                                        placeholder="Brand...",
                                        required=True,
                                    ),
                                    rx.text("What model?"),
                                    rx.input(
                                        placeholder="...",
                                        value=Inquiry.printer_model,
                                        on_change=Inquiry.set_printer_model,
                                        required=True,
                                    ),
                                    rx.text("Printer Hours"),
                                    rx.text(
                                        """Approximately, how many hours worth of 3D printing have you
                                        done?""",
                                        size="1",
                                        margin="none",
                                        padding="none",
                                    ),
                                    rx.input(
                                        placeholder="...",
                                        value=Inquiry.printer_hours,
                                        on_change=Inquiry.set_printer_hours,
                                        required=True,
                                    ),
                                ),
                                width="400px",
                            ),
                        ),
                        (
                            1,
                            rx.box(
                                rx.vstack(
                                    rx.heading("Tell us what we can do for you."),
                                    rx.text("What type of problem is it?"),
                                    rx.select(
                                        Inquiry.problem_type_ops,
                                        value=Inquiry.problem_type,
                                        on_change=Inquiry.set_problem_type,
                                        placeholder="Select...",
                                        required=True,
                                    ),
                                    rx.text("Describe the problem you're experiencing"),
                                    rx.text_area(
                                        placeholder="The more detailed, the better...",
                                        value=Inquiry.problem_desc,
                                        on_change=Inquiry.set_problem_desc,
                                        width="100%",
                                        height="150px",
                                    ),
                                ),
                                width="400px",
                            ),
                        ),
                        (
                            2,
                            rx.box(
                                rx.vstack(
                                    rx.heading("What service type works best?"),
                                    rx.text("Select a service type"),
                                    rx.select(
                                        Inquiry.service_type_ops,
                                        value=Inquiry.service_type,
                                        on_change=Inquiry.set_service_type,
                                        placeholder="Select...",
                                        required=True,
                                    ),
                                    rx.card(
                                        rx.text(
                                            """Please Note: The customer is reponsible for all shipping expenses if
                    incurred.""",
                                        ),
                                    ),
                                ),
                                width="400px",
                            ),
                        ),
                        (
                            3,
                            rx.box(
                                rx.vstack(
                                    rx.heading("One last thing."),
                                    rx.text("Do you have any additional comments?"),
                                    rx.text_area(
                                        placeholder="Type here...",
                                        value=Inquiry.user_comments,
                                        on_change=Inquiry.set_user_comments,
                                        width="100%",
                                    ),
                                ),
                                width="400px",
                            ),
                        ),
                    ),
                ),
            ),
            form_navigation_buttons(manipulated_class),
            align="center",
        ),
        width="100%",
        height="40%",
        align="center",
    )
