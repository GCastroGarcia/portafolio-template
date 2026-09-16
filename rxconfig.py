import os
import reflex as rx

patch_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".npm_patch.js")).replace("\\", "/")
if os.path.exists(patch_path):
    os.environ["NODE_OPTIONS"] = f"--require {patch_path}"

config = rx.Config(
    app_name="portafolio",
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="grass",
                radius="full",
            )
        ),
        rx.plugins.SitemapPlugin(),
    ],
)
