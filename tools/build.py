#!/usr/bin/env python3
"""Build static pages from the Korean copy files; no third-party packages needed."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"\{\{(plain|rich)\|([^|{}]+)\|([^{}]+)\}\}")
INLINE = re.compile(r"\*\*(.+?)\*\*|\[([^\]\n]+)\]\(([^\s)]+)\)")


def read_copy(path):
    fields, key, lines = {}, None, []
    def save():
        if key is None:
            return
        value = "\n".join(lines).strip()
        if not value:
            raise ValueError(f"{path.name}: '{key}'의 문장이 비어 있습니다.")
        fields[key] = value
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            save()
            key, lines = line[3:].strip(), []
            if key in fields:
                raise ValueError(f"{path.name}: '{key}' 제목이 중복되었습니다.")
        elif key is not None:
            lines.append(line)
    save()
    return fields


def rich_text(value):
    """Allow bold and links, escape raw HTML, and retain intentional line breaks."""
    pieces, position = [], 0
    for match in INLINE.finditer(value):
        pieces.append(html.escape(value[position:match.start()]))
        bold, label, url = match.groups()
        if bold is not None:
            pieces.append("<strong>" + html.escape(bold) + "</strong>")
        else:
            parsed = urlsplit(url)
            if parsed.scheme not in ("https", "http", "mailto") or (parsed.scheme in ("https", "http") and not parsed.netloc):
                raise ValueError(f"지원하지 않는 링크 주소입니다: {url}")
            pieces.append('<a href="' + html.escape(url, quote=True) + '" rel="noopener noreferrer" target="_blank">' + html.escape(label) + '</a>')
        position = match.end()
    pieces.append(html.escape(value[position:]))
    return "".join(pieces).replace("\n", "<br/>")


def render_pages(root=ROOT):
    manifest = json.loads((root / "content/pages.json").read_text(encoding="utf-8"))
    copies = {name: read_copy(root / "content" / f"{name}.md") for name in manifest.values()}
    used = {name: set() for name in copies}
    pages = {}
    for filename in manifest:
        template = (root / "templates" / filename).read_text(encoding="utf-8")
        def replace(match):
            kind, name, key = match.groups()
            if name not in copies or key not in copies[name]:
                raise ValueError(f"{name}.md: '{key}' 제목을 찾을 수 없습니다. ## 제목을 원래대로 복원하세요.")
            used[name].add(key)
            value = copies[name][key]
            return html.escape(" ".join(value.split()), quote=True) if kind == "plain" else rich_text(value)
        pages[filename] = TOKEN.sub(replace, template)
    for name, fields in copies.items():
        unknown = set(fields) - used[name]
        if unknown:
            raise ValueError(f"{name}.md: 연결되지 않은 제목: {', '.join(sorted(unknown))}. ## 제목은 바꾸지 마세요.")
    return pages


def build(root=ROOT, output=None):
    output = output or root / "_site"
    pages = render_pages(root)  # Validate all copy before replacing an existing build.
    output.mkdir(parents=True, exist_ok=True)
    for filename in ("style.css", "script.js", ".nojekyll"):
        shutil.copy2(root / filename, output / filename)
    shutil.copytree(root / "assets", output / "assets", dirs_exist_ok=True)
    for filename, text in pages.items():
        # Asset revisions keep the design current after each edit without disabling caching.
        for asset in ("style.css", "script.js"):
            version = hashlib.sha256((root / asset).read_bytes()).hexdigest()[:12]
            text = re.sub(re.escape(asset) + r"\?v=[^\"']+", asset + "?v=" + version, text)
        (output / filename).write_text(text, encoding="utf-8")
    print(f"완료: 문구 파일 {len(pages)}개 → {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        build(output=args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f"문구 수정 확인이 필요합니다: {error}\n")
