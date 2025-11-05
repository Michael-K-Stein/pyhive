#!/usr/bin/env python3
"""Generate supported API versions file"""
from pathlib import Path
import tomllib

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """Occurs immediately before each build."""

        pyproject = tomllib.loads(Path("pyproject.toml").read_text())
        versions = pyproject["tool"]["api_versions"]["supported"]

        dst = Path("pyhive/src/_generated_versions.py")
        dst.write_text(
            "SUPPORTED_API_VERSIONS = " + repr(versions) + "\n"
            "MIN_API_VERSION = SUPPORTED_API_VERSIONS[0]\n"
            "LATEST_API_VERSION = SUPPORTED_API_VERSIONS[-1]\n"
        )

        print(f"+ Generated {dst}")
