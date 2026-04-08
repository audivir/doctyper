"""Build doctyper package."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar

import libcst as cst
from libcst.metadata import MetadataWrapper, ParentNodeProvider

if TYPE_CHECKING:
    from pdm.backend.hooks.base import Context

    ModuleNameT = TypeVar("ModuleNameT", cst.Attribute, cst.Name, None)


class ReplacePackageTransformer(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (ParentNodeProvider,)

    def __init__(self, src: str, target: str, wrapper: MetadataWrapper) -> None:
        self.src = src
        self.target = target
        self.wrapper = wrapper

    def leave_Name(self, original_node: cst.Name, updated_node: cst.Name) -> cst.Name:
        parent = self.get_metadata(ParentNodeProvider, original_node)
        # only change the final value of an attribute chain
        if isinstance(parent, cst.Attribute) and original_node != parent.value:
            return updated_node
        if updated_node.value == self.src:
            updated_node = updated_node.with_changes(value=self.target)
        return updated_node

    def leave_Attribute(
        self, original_node: cst.Attribute, updated_node: cst.Attribute
    ) -> cst.Attribute:
        if not isinstance(updated_node.value, cst.Name):
            return updated_node
        if updated_node.value.value == self.src:
            updated_node = updated_node.with_changes(
                value=updated_node.value.with_changes(value=self.target)
            )
        return updated_node


def adjust_file(file: Path, src: str, target: str) -> None:
    """Replace the calls/imports to `src` with `target`."""
    if file.suffix not in {".py", ".pyi"}:
        return
    content = file.read_text()
    if src not in content:
        return

    # custom fix
    template = '"Annotated[int, {}.Argument()]"'
    content = content.replace(template.format(src), template.format(target))

    tree = cst.parse_module(content)
    wrapper = MetadataWrapper(tree)
    new_tree = wrapper.visit(ReplacePackageTransformer(src, target, wrapper))
    file.write_text(new_tree.code)


def pdm_build_initialize(context: Context) -> None:
    """Copy code to doctyper directory and fix imports/calls to typer."""
    if context.target == "sdist":
        return
    root: Path = Path()  # context.root
    src = root / "typer"
    dest = root / "doctyper"

    # clean target
    if dest.is_dir():
        shutil.rmtree(dest)
    elif dest.exists():
        dest.unlink()

    # copy source code
    shutil.copytree(src, dest)

    # patch imports
    for f in dest.iterdir():
        adjust_file(f, "typer", "doctyper")
