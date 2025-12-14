#!/usr/bin/env bash

set -e
set -x

mypy doctyper
ruff check doctyper tests docs_src scripts
ruff format doctyper tests docs_src scripts --check
