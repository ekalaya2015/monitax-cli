import typer

from . import configure, device, invoice, user

app = typer.Typer()
app.add_typer(configure.app, name="configure")
app.add_typer(device.app, name="device")
app.add_typer(user.app, name="user")
app.add_typer(invoice.app, name="invoice")

if __name__ == "__main__":
    app()
