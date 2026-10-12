# Portfolio editing

- User-editable copy is authoritative in `content/*.md`. Preserve its Korean section headings; templates refer to those exact headings.
- Change layout in `templates/*.html` and `style.css`. Do not reintroduce generated HTML in the repository root or edit `_site/` directly.
- Run `python3 -m unittest discover -s tools -p 'test_*.py'` and `python3 tools/build.py` after relevant changes. Preview `_site/` locally.
- Keep all videos and reference files visible as large `.resource-file` buttons. Do not hide them behind a disclosure menu.
- Keep project case studies at two A4 landscape sheets; the resource section is web-only. Validate print layout when changing page content or print CSS.
- ARMIGO: team leader, hardware design and multi-motor control. The user did not perform 3D printing fabrication.
- Smart plant is ongoing. Personal role: team leader/PM and control planning, website creation, system-wide implementation guidance and technical support, hardware configuration and production support. The user specifically proposed hardware configuration, host communication methods and using four ArUco markers. Describe this as concrete technical direction, while distinguishing it from personally implementing all teammates’ device code. Do not invent protocols, marker geometry or measured improvements.
- Publishing uses `.github/workflows/pages.yml` with GitHub Pages Actions. Deploy only `_site`; never upload source resumes or unrelated local files.
