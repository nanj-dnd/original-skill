#!/usr/bin/env python3
"""Turn an /original run record (markdown) into a PDF.

Usage: python3 export_pdf.py <run.md> [out.pdf]
Default output: ~/Downloads/originals/<same name>.pdf

Standard library only. Handles the markdown subset run records use: headings,
paragraphs, bullet and numbered lists (one level of nesting), bold, italic,
inline code, links, block quotes, fenced code and horizontal rules. Prints with
headless Chrome.
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]

CSS = """
@page { size: A4; margin: 18mm 18mm 20mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.5 -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif;
       color: #1a1a1a; margin: 0; }
h1 { font-size: 19pt; line-height: 1.2; margin: 0 0 4pt; }
h1 + p { color: #666; margin-top: 0; }
h2 { font-size: 12.5pt; margin: 18pt 0 6pt; padding-bottom: 3pt;
     border-bottom: 1px solid #ddd; break-after: avoid; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; }
li { margin: 0 0 3pt; }
li > ul, li > ol { margin: 3pt 0 0; }
blockquote { margin: 0 0 8pt; padding: 4pt 10pt; border-left: 3px solid #ccc; color: #444; }
code { font: 9.5pt ui-monospace, Menlo, monospace; background: #f3f3f3;
       padding: 0 3px; border-radius: 3px; }
pre { background: #f6f6f6; padding: 8pt; border-radius: 4px; white-space: pre-wrap;
      font: 9pt/1.4 ui-monospace, Menlo, monospace; }
pre code { background: none; padding: 0; }
hr { border: 0; border-top: 1px solid #ddd; margin: 14pt 0; }
a { color: #1a1a1a; }
li, blockquote, pre { break-inside: avoid; }
"""


def inline(text: str) -> str:
    codes = []

    def stash(m):
        codes.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


LIST_RE = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")


def convert(md: str) -> str:
    lines = md.splitlines()
    out, para, quote = [], [], []
    stack = []  # (indent, tag)
    i = 0

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_quote():
        if quote:
            out.append(f"<blockquote>{inline(' '.join(quote))}</blockquote>")
            quote.clear()

    def close_lists(to_indent=-1):
        while stack and stack[-1][0] > to_indent:
            out.append(f"</li></{stack.pop()[1]}>")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_para(); flush_quote(); close_lists()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(body))}</code></pre>")
            i += 1
            continue

        if not stripped:
            flush_para(); flush_quote()
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            flush_para(); flush_quote(); close_lists()
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            flush_para(); flush_quote(); close_lists()
            out.append("<hr>")
            i += 1
            continue

        if stripped.startswith(">"):
            flush_para(); close_lists()
            quote.append(stripped.lstrip("> ").rstrip())
            i += 1
            continue

        m = LIST_RE.match(line)
        if m:
            flush_para(); flush_quote()
            indent = len(m.group(1).expandtabs(4))
            tag = "ol" if m.group(2)[0].isdigit() else "ul"
            if stack and indent < stack[-1][0]:
                close_lists(indent)
            if stack and indent == stack[-1][0] and tag != stack[-1][1]:
                out.append(f"</li></{stack.pop()[1]}>")
            if not stack or indent > stack[-1][0]:
                out.append(f"<{tag}><li>{inline(m.group(3))}")
                stack.append((indent, tag))
            else:
                out.append(f"</li><li>{inline(m.group(3))}")
            i += 1
            continue

        if stack and line.startswith(" "):
            # continuation line of a list item
            out[-1] += " " + inline(stripped)
            i += 1
            continue

        close_lists()
        para.append(stripped)
        i += 1

    flush_para(); flush_quote(); close_lists()
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1]).expanduser().resolve()
    if len(sys.argv) > 2:
        dest = Path(sys.argv[2]).expanduser().resolve()
    else:
        dest = Path.home() / "Downloads" / "originals" / (src.stem + ".pdf")
    dest.parent.mkdir(parents=True, exist_ok=True)

    md = src.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+)$", md, re.M)
    title = html.escape(title_m.group(1) if title_m else src.stem)
    page = (f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>"
            f"<style>{CSS}</style></head><body>{convert(md)}</body></html>")

    chrome = next((c for c in CHROME_CANDIDATES if Path(c).exists()), None)
    if not chrome:
        sys.exit("No Chrome/Chromium/Edge found to print the PDF.")

    with tempfile.TemporaryDirectory() as tmp:
        page_path = Path(tmp) / "run.html"
        page_path.write_text(page, encoding="utf-8")
        result = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--user-data-dir={tmp}/profile", f"--print-to-pdf={dest}",
             page_path.as_uri()],
            capture_output=True, text=True, timeout=120,
        )
    if result.returncode != 0 or not dest.exists():
        sys.exit(f"Chrome failed ({result.returncode}):\n{result.stderr[-2000:]}")
    print(dest)


if __name__ == "__main__":
    main()
