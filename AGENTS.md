# Portfolio editing

- User-editable copy is authoritative in `content/*.md`. Preserve its Korean section headings; templates refer to those exact headings.
- Change layout in `templates/*.html` and `style.css`. Do not reintroduce generated HTML in the repository root or edit `_site/` directly.
- Run `python3 -m unittest discover -s tools -p 'test_*.py'` and `python3 tools/build.py` after relevant changes. Preview `_site/` locally.
- Keep all videos and reference files visible as large `.resource-file` buttons. Do not hide them behind a disclosure menu.
- Keep project case studies at two A4 landscape sheets; the resource section is web-only. Validate print layout when changing page content or print CSS.
- ARMIGO: team leader, hardware design and multi-motor control. The user did not perform 3D printing fabrication.
- Smart plant is ongoing. Updated by the user on 2026-10-20: personal role is team leader/PM and host control development, including the host control web UI and API. Use the public role label “호스트 관제 개발”; omit “전담” per the user’s wording preference. Also retain system-wide technical guidance, hardware configuration/production support and the proposed use of four ArUco markers. Device-level robot/arm code is divided among teammates. Distinguish implemented UI/API from ongoing physical integration; do not invent measured outcomes or claim teammates' device code.
- Publishing uses `.github/workflows/pages.yml` with GitHub Pages Actions. Deploy only `_site`; never upload source resumes or unrelated local files.

- Smart plant case-study body: omit jig-improvement images/descriptions and model training/success-rate sections at the user’s request. The second sheet now focuses on the latest host control screenshot, personal implementation and state/command validation. Current host site: https://7s-fa.github.io/host_web/control.html. Public screenshots show devices disconnected and must be labeled accordingly.
