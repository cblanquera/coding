#!/usr/bin/env python3
"""Run a docs preview command with a localhost bind and optional build step."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run an optional docs build command, then exec a preview server "
            "command with HOST and PORT set for localhost browser QA."
        )
    )
    parser.add_argument(
        "--cwd",
        default=".",
        help="Working directory for the build and serve commands. Defaults to the current directory.",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind the preview server to. Defaults to 127.0.0.1.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=4173,
        help="Port to bind the preview server to. Defaults to 4173.",
    )
    parser.add_argument(
        "--build",
        help="Optional build command to run before starting the preview server.",
    )
    parser.add_argument(
        "--serve",
        required=True,
        help="Preview server command to exec after build completes.",
    )
    return parser.parse_args()


def run_shell(command: str, *, cwd: str, env: dict[str, str], shell: str) -> None:
    subprocess.run([shell, "-lc", command], cwd=cwd, env=env, check=True)


def main() -> int:
    args = parse_args()
    shell = os.environ.get("SHELL", "/bin/sh")
    cwd = str(Path(args.cwd).expanduser().resolve())

    env = os.environ.copy()
    env["HOST"] = args.host
    env["PORT"] = str(args.port)

    if args.build:
        print(f"[localhost-preview] build: {args.build}", flush=True)
        run_shell(args.build, cwd=cwd, env=env, shell=shell)

    print(f"[localhost-preview] url: http://{args.host}:{args.port}", flush=True)
    print(f"[localhost-preview] serve: {args.serve}", flush=True)

    os.chdir(cwd)
    os.execvpe(shell, [shell, "-lc", args.serve], env)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        print(
            f"[localhost-preview] command failed with exit code {error.returncode}",
            file=sys.stderr,
        )
        raise SystemExit(error.returncode)
