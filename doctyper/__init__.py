"""Wrapper around Typer using Google-Doc strings for CLI descriptions."""

from shutil import get_terminal_size as get_terminal_size

from click.exceptions import Abort as Abort
from click.exceptions import BadParameter as BadParameter
from click.exceptions import Exit as Exit
from click.termui import clear as clear
from click.termui import confirm as confirm
from click.termui import echo_via_pager as echo_via_pager
from click.termui import edit as edit
from click.termui import getchar as getchar
from click.termui import pause as pause
from click.termui import progressbar as progressbar
from click.termui import prompt as prompt
from click.termui import secho as secho
from click.termui import style as style
from click.termui import unstyle as unstyle
from click.utils import echo as echo
from click.utils import format_filename as format_filename
from click.utils import get_app_dir as get_app_dir
from click.utils import get_binary_stream as get_binary_stream
from click.utils import get_text_stream as get_text_stream
from click.utils import open_file as open_file
from typer import __version__ as __version__
from typer import colors as colors
from typer.main import DocTyper as DocTyper
from typer.main import Typer as Typer
from typer.main import launch as launch
from typer.main import run as run
from typer.models import CallbackParam as CallbackParam
from typer.models import Context as Context
from typer.models import FileBinaryRead as FileBinaryRead
from typer.models import FileBinaryWrite as FileBinaryWrite
from typer.models import FileText as FileText
from typer.models import FileTextWrite as FileTextWrite
from typer.params import Argument as Argument
from typer.params import Option as Option
