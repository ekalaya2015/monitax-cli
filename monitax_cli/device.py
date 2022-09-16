import json
from typing import Optional

import requests
import typer
from rich.console import Console

from . import config

app = typer.Typer(help="Device command interface")
setting = config.Setting()
console = Console()


@app.command(help="My device")
def me():
    try:
        with console.status("Wait...", spinner="arrow3") as stat:
            url = f"{setting.baseurl}/devices/me"
            headers = {
                "Authorization": f"Bearer {setting.token}",
                "Access-Control-Allow-Origin": "*",
            }
            session = requests.Session()
            response = session.get(url=url, headers=headers)
            if response.status_code == 200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
    except Exception:
        console.print_exception()


@app.command(help="List device")
def list(
    status: Optional[str] = typer.Option(
        "active",
        "--status",
        "-s",
        help="Device status (active|inactive|created|on|off)",
    )
):
    try:
        with console.status("Wait...", spinner="arrow3") as stat:
            url = f"{setting.baseurl}/devices/"
            headers = {
                "Authorization": f"Bearer {setting.token}",
                "Access-Control-Allow-Origin": "*",
            }
            params = {"limit": 10, "offset": 0, "status": status.title()}
            session = requests.Session()
            response = session.get(url=url, params=params, headers=headers)
            if response.status_code == 200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
    except Exception:
        console.print_exception()


@app.command(help="Create new device")
def create(
    name: str = typer.Option(..., "--name", "-n", help="Device name"),
    serial_num: str = typer.Option(
        ..., "--serialnum", "-s", help="Device serial number"
    ),
    description: str = typer.Option(..., "--desc", "-d", help="Device description"),
):
    try:
        with console.status("Wait...", spinner="arrow3") as status:
            url = f"{setting.baseurl}/devices/"
            headers = {
                "Authorization": f"Bearer {setting.token}",
                "Access-Control-Allow-Origin": "*",
            }
            data = {"name": name, "serial_num": serial_num, "description": description}
            session = requests.Session()
            response = session.post(url=url, json=data, headers=headers)
            if response.status_code == 200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
    except Exception:
        console.print_exception()


@app.command()
def delete(id: str = typer.Option(..., "--id", help="Device id")):
    """Delete device by id"""
    try:
        with console.status("Wait...", spinner="arrow3") as status:
            url = f"{setting.baseurl}/devices/{id}"
            headers = {
                "Authorization": f"Bearer {setting.token}",
                "Access-Control-Allow-Origin": "*",
            }
            session = requests.Session()
            response = session.delete(url=url, headers=headers)
            if response.status_code == 200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
    except Exception:
        console.print_exception()


@app.command(help="Assign device to a registered user")
def assign(
    deviceid: str = typer.Option(..., "--deviceid", help="Device ID"),
    userid: str = typer.Option(..., "--userid", help="User ID"),
    lat: float = typer.Option(..., "--lat", help="Device latitude coordinate"),
    lon: float = typer.Option(..., "--lon", help="Device longitude coordinate"),
):
    try:
        with console.status("Wait...",spinner="arrow3") as status:
            url = f"{setting.baseurl}/devices/{deviceid}/{userid}"
            headers = {
                "Authorization": f"Bearer {setting.token}",
                "Access-Control-Allow-Origin": "*",
            }
            session = requests.Session()
            data = {"lat": lat, "lon": lon}
            response = session.put(url=url, json=data, headers=headers)
            if response.status_code == 200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
    except Exception:
        console.print_exception()


@app.command(help="Update device profile")
def update(
    deviceid: str = typer.Option(..., "--deviceid", help="Device ID"),
    lat: float = typer.Option(..., "--lat", help="Device latitude coordinate"),
    lon: float = typer.Option(..., "--lon", help="Device longitude coordinate"),
):
    try:
        with console.status("Wait...",spinner="arrow3") as status:
            url = f"{setting.baseurl}/devices/{deviceid}"
            headers = {
                "Authorization": f"Bearer {setting.token}",
                "Access-Control-Allow-Origin": "*",
            }
            session = requests.Session()
            data = {"lat": lat, "lon": lon}
            response = session.patch(url=url, json=data, headers=headers)
            if response.status_code == 200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
                            
    except Exception:
        console.print_exception()


if __name__ == "__main__":
    app()
