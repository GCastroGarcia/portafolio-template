import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    icon_elem = (
        rx.box(class_name=f"devicon-{icon}-plain", font_size="1.2em")
        if icon in ["github", "linkedin"] or "devicon" in icon
        else rx.icon(icon)
    )
    return rx.link(
        rx.button(
            icon_elem,
            text,
            variant="solid" if solid else "surface"
        ),
        href=url,
        is_external=True
    )
