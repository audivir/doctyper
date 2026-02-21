"""Wrapper around Typer using Google-Doc strings for CLI descriptions."""

from typer import DocTyper as DocTyper
from typer import Typer as Typer
from typer import run as run

SlimTyper = DocTyper
