#!/usr/bin/env python3
"""Entry point for running SSS straight from a checkout or submodule.

Usage from a target repo root:  python3 .sss/tool/sss.py <command> [args]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import yaml  # noqa: F401
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "SSS needs PyYAML. Install it with:  python3 -m pip install pyyaml\n"
    )
    sys.exit(2)

from sss.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
