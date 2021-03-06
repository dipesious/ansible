"""Completers for use with argcomplete."""
from __future__ import annotations

import argparse
import typing as t

from ..target import (
    find_target_completion,
)

from .argparsing.argcompletion import (
    OptionCompletionFinder,
)


def complete_target(completer: OptionCompletionFinder, prefix: str, parsed_args: argparse.Namespace, **_) -> t.List[str]:
    """Perform completion for the targets configured for the command being parsed."""
    matches = find_target_completion(parsed_args.targets_func, prefix, completer.list_mode)
    completer.disable_completion_mangling = completer.list_mode and len(matches) > 1
    return matches


def complete_choices(choices: t.List[str], prefix: str, **_) -> t.List[str]:
    """Perform completion using the provided choices."""
    matches = [choice for choice in choices if choice.startswith(prefix)]
    return matches
