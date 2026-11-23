#!/usr/bin/env python3
"""Dependency-free structural check for a PPTX file.

Usage:
    python validate_pptx.py <path-to-pptx>

Exit code 0 means no errors, 1 means errors were found, 2 means bad usage.
"""

import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def slide_number(name):
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def validate(path):
    report = {
        "file": str(path),
        "slides": 0,
        "images": 0,
        "errors": [],
        "warnings": [],
    }

    if not path.exists():
        report["errors"].append("file not found")
        return report

    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            slides = sorted(
                [name for name in names if re.match(r"ppt/slides/slide\d+\.xml$", name)],
                key=slide_number,
            )
            report["slides"] = len(slides)
            report["images"] = len([name for name in names if name.startswith("ppt/media/")])

            if not slides:
                report["errors"].append("no slides found")

            for name in slides:
                index = slide_number(name)
                root = ET.fromstring(archive.read(name))
                runs = [(node.text or "") for node in root.iter(A + "t")]
                full_text = "".join(runs).strip()

                if not full_text:
                    report["errors"].append(f"slide {index}: no text found")
                if any(len(run) > 120 for run in runs):
                    report["warnings"].append(
                        f"slide {index}: text run over 120 chars, check for overflow"
                    )

                placeholders = [node.get("type") for node in root.iter(P + "ph")]
                if not any(kind in ("title", "ctrTitle") for kind in placeholders):
                    report["warnings"].append(f"slide {index}: no title placeholder")

                if len(runs) > 40:
                    report["warnings"].append(
                        f"slide {index}: more than 40 text runs, likely too dense"
                    )
    except zipfile.BadZipFile as exc:
        report["errors"].append(f"not a valid pptx zip: {exc}")
    except ET.ParseError as exc:
        report["errors"].append(f"malformed slide xml: {exc}")

    return report


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_pptx.py <path-to-pptx>")
        return 2

    report = validate(Path(sys.argv[1]))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
