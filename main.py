"""food-picture-01 entry: put the food picture in the output directory.

The finished picture is committed beside this file as ``entry.png`` (a
1024x683 PNG of a wood-fired margherita pizza slice with a mozzarella
cheese pull, chosen by a pairwise tournament over 12 generated candidates;
see tournament.md). The program's whole job is to place those exact bytes
at ``<output>/entry.png``, where ``<output>`` is ``/output`` in the
grading sandbox, or ``$MAKEFUN_OUTPUT_DIR`` when that variable is set
(the kit's local runs set it). On success it prints a short confirmation
line with the written path and byte size so a run log shows exactly what
landed. Standard library only, no network.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.png")


def digest(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    dest = output_path()
    shutil.copyfile(SOURCE, dest)
    # The entry is graded on the exact bytes written, and the program is
    # run twice and must produce identical output: verify the copy landed
    # whole (sha256 of the written file matches the source) rather than
    # trusting the copy call. After that check passes, print a short
    # confirmation line with the written path and byte size.
    if digest(dest) != digest(SOURCE):
        print("error: output does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
