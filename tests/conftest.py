from __future__ import absolute_import
import sys
from pathlib import Path
from typing import Optional

from _pytest.config import Config
from py import path as pypath
from typing_extensions import Final

# See https://github.com/HypothesisWorks/hypothesis/pull/2567
pytest_plugins = [u'hypothesis.extra.pytestplugin']

PYTHON_VERSION = (sys.version_info.major, sys.version_info.minor)
ENABLE_SINCE = {
    (3, 10): frozenset((
        Path(u'tests/test_examples/test_result/test_result_pattern_matching.py'),
        Path(u'tests/test_examples/test_maybe/test_maybe_pattern_matching.py'),
        Path(u'tests/test_examples/test_io/test_ioresult_container/test_ioresult_pattern_matching.py'),  # noqa: E501
    )),
}
PATHS_TO_IGNORE_NOW = frozenset(
    path.absolute()
    for since_python, to_ignore in ENABLE_SINCE.items()
    for path in to_ignore
    if PYTHON_VERSION < since_python
)


def pytest_ignore_collect(
    path,
    config,
):
    u"""
    Return True to prevent considering this path for collection.

    This hook is consulted for all files and directories prior to calling
    more specific hooks. Stops at first non-None result.
    """
    return Path(path) in PATHS_TO_IGNORE_NOW
