import re
import shutil
import tempfile
import unittest
from pathlib import Path
from build import ROOT, read_copy, render_pages, rich_text


class CopyEditingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for folder in ("content", "templates"):
            shutil.copytree(ROOT / folder, self.root / folder)

    def tearDown(self):
        self.temp.cleanup()

    def test_user_can_edit_home_and_project_without_html(self):
        home = self.root / "content/홈페이지.md"
        home.write_text(re.sub(r"(## 소개 · 이름\n).*?(?=\n## |\Z)", r"\1문구 수정 확인\n", home.read_text(), flags=re.S))
        project = self.root / "content/ARMIGO.md"
        project.write_text(re.sub(r"(## 1쪽 · 제목\n).*?(?=\n## |\Z)", r"\1새 프로젝트 소개\n", project.read_text(), flags=re.S))
        pages = render_pages(self.root)
        self.assertIn('id="intro-title">문구 수정 확인</h1>', pages["index.html"])
        self.assertIn("새 프로젝트 소개</h1>", pages["armigo.html"])
        self.assertIn('href="assets/armigo-teaching.mp4"', pages["armigo.html"])

    def test_missing_or_renamed_heading_stops_build(self):
        path = self.root / "content/홈페이지.md"
        path.write_text(path.read_text().replace("## 소개 · 이름", "## 잘못 바꾼 제목"))
        with self.assertRaisesRegex(ValueError, "제목을 찾을 수 없습니다"):
            render_pages(self.root)

    def test_duplicate_heading_stops_build(self):
        path = self.root / "content/홈페이지.md"
        path.write_text(path.read_text() + "\n## 소개 · 이름\n중복\n")
        with self.assertRaisesRegex(ValueError, "중복"):
            read_copy(path)

    def test_copy_is_text_and_links_keep_safe_attributes(self):
        result = rich_text('회로 & 제어\n**강조** <script>alert(1)</script> [코드](https://github.com/PjongB)')
        self.assertIn("회로 &amp; 제어<br/><strong>강조</strong>", result)
        self.assertNotIn("<script>", result)
        self.assertIn('rel="noopener noreferrer"', result)
        with self.assertRaises(ValueError):
            rich_text("[링크](javascript:alert)")

    def test_all_seven_pages_render(self):
        pages = render_pages(self.root)
        self.assertEqual(len(pages), 7)
        self.assertFalse(any("{{rich|" in page or "{{plain|" in page for page in pages.values()))


if __name__ == "__main__":
    unittest.main()
