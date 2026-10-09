# 박종빈 포트폴리오

**[포트폴리오 바로가기 → https://pjongb.github.io/](https://pjongb.github.io/)**

## 홈페이지 문구 직접 수정하기

아래의 **수정하기**를 누르면 GitHub 편집 화면이 열립니다. HTML이나 코드를 수정할 필요 없이, 한글 제목 아래의 문장만 바꾸면 됩니다.

| 수정할 곳 | 들어 있는 내용 | 편집 화면 |
| --- | --- | --- |
| 홈페이지 | 첫 화면 소개글, 기술스택, 경력 내역, 수상 내역, 프로젝트 카드 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/%ED%99%88%ED%8E%98%EC%9D%B4%EC%A7%80.md) |
| 스마트플랜트 | 진행 상태, PM·팀장 역할, 기술 지원 내용 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/%EC%8A%A4%EB%A7%88%ED%8A%B8%ED%94%8C%EB%9E%9C%ED%8A%B8.md) |
| 스마트도서관 | RFID·통신·기판 제작과 문제 해결 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/%EC%8A%A4%EB%A7%88%ED%8A%B8%EB%8F%84%EC%84%9C%EA%B4%80.md) |
| ARMIGO | 하드웨어 설계, 다중 모터 제어와 문제 해결 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/ARMIGO.md) |
| 세이프킥 | 센서 보정, 구동 제어와 문제 해결 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/%EC%84%B8%EC%9D%B4%ED%94%84%ED%82%A5.md) |
| 음주컷 | 하드웨어, 상태 제어와 문제 해결 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/%EC%9D%8C%EC%A3%BC%EC%BB%B7.md) |
| PLC | 자동 적재 프로젝트 설명과 협업 경험 | [수정하기](https://github.com/PjongB/pjongb.github.io/edit/main/content/PLC.md) |

## 수정 순서

1. 위 표에서 원하는 페이지의 **수정하기**를 누릅니다. 본인 GitHub 계정으로 로그인하세요.
2. `## 소개 · 인사말` 같은 제목 아래에서 문장을 수정합니다. **`##`로 시작하는 항목 제목은 그대로 둡니다.**
3. 오른쪽 위 **Commit changes…**를 누릅니다. 변경 내용은 `소개글 수정`처럼 적고, **Commit directly to the main branch**를 선택해 저장합니다.
4. [Actions의 ‘문구 수정 자동 배포’](https://github.com/PjongB/pjongb.github.io/actions/workflows/pages.yml)에 초록색 체크가 뜨면 사이트를 새로고침합니다. 반영까지 보통 1~2분 정도 걸립니다.

### 수정 예시

`홈페이지.md`에서 아래 제목 밑의 문장만 원하는 소개글로 바꾸세요.

```markdown
## 소개 · 인사말
회로와 코드를 함께 이해하고,
센서·모터 제어와 장치 통신을 구현합니다.
```

- 줄을 바꾸면 화면에서도 줄이 바뀝니다. `**강조할 내용**`은 굵게 표시됩니다.
- `[프로젝트 코드](https://github.com/...)` 형태는 링크입니다. 문장만 바꿀 때는 주소를 유지하세요.
- 메인의 프로젝트 카드와 상세 페이지는 각각의 파일에서 수정합니다.
- 상세 페이지는 A4 가로 2쪽에 맞춘 구성입니다. 설명을 많이 늘렸다면 사이트의 **PDF / 인쇄**에서 분량을 확인하세요.
- 문구를 잘못 바꿨다면 파일의 **History**에서 이전 내용을 확인할 수 있습니다. 배포 검사에서 오류가 나면 기존 공개 사이트는 유지됩니다.
- 첨부된 발표 PDF는 원본 파일입니다. 이 문구 파일을 바꿔도 첨부 PDF 내부 글자는 바뀌지 않습니다. 사이트의 **PDF / 인쇄**에는 수정한 문구가 반영됩니다.

## 파일 구성

- `content/*.md`: 직접 수정하는 글자들 — **문구의 기준 파일**
- `templates/*.html`: 화면 구성과 글자 위치
- `assets/`: 사진, 도면, 영상, 첨부 PDF
- `style.css`: 디자인과 인쇄 규격
- `tools/build.py`: 문구와 화면 구성을 합쳐 사이트 생성
- `.github/workflows/pages.yml`: 저장 후 자동 검사·배포

개발용 미리보기:

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/build.py
python3 -m http.server 4173 --directory _site
```

`_site/`는 자동 생성 결과이므로 직접 수정하거나 커밋하지 않습니다. GitHub Pages는 GitHub Actions 방식으로 배포합니다.
