# git-team

Codyssey 10 · 3~5인 팀 GitHub 협업 실습. 결과물은 코드가 아니라 **협업 과정의 기록**(브랜치·PR·리뷰·이슈·충돌·트러블슈팅)이다.

## 프로젝트 소개

4인 팀이 GitHub Flow 로 협업하면서 아래를 **전원 수행**하고 기록으로 남겼다.

- Issue → `feature/<name>-<topic>` 브랜치 → PR → 리뷰(라인 코멘트·답글·반영) → 승인 1명 → 머지 → 브랜치 삭제
- 의도적으로 만든 충돌 2회(같은 hunk · 파일 이동 vs 수정)와 그 해결 과정
- Git 트러블슈팅 4종(amend · reset · revert · stash) 실습과 재현 가능한 기록
- 결과물은 (A) 팀원별 유틸 함수 모음 — 사용 예시는 각 함수 docstring 의 doctest

브랜치 전략·커밋 컨벤션·PR/리뷰 규칙은 [협업 가이드](docs/CONTRIBUTING.md), 제출물 인덱스는 [SUBMISSION.md](SUBMISSION.md).

## 폴더 구조

```
.
├── .github/
│   ├── CODEOWNERS               # 경로별 리뷰 오너 — 기본 팀장 · .github/ sangwoo · docs/ 팀장+sangwoo · 함수 파일은 작성자
│   ├── ISSUE_TEMPLATE/task.md   # 작업 이슈 템플릿 (Why / What / Done when)
│   └── PULL_REQUEST_TEMPLATE.md # Closes # / What / Why / How / 리뷰어에게
├── docs/
│   ├── CONTRIBUTING.md          # 협업 가이드
│   ├── conflict-resolution.md   # 충돌 해결 기록 (#1 · #2)
│   ├── troubleshooting-log.md   # amend · reset · revert · stash 기록
│   ├── git-history.txt          # git log --oneline --graph --decorate --all
│   └── evidence/                # 캡처·로그 증빙
├── src/utils/
│   ├── string_utils.py          # to_snake_case · to_camel_case · to_pascal_case
│   ├── list_utils.py            # chunk
│   ├── date_utils.py            # days_between
│   ├── math_utils.py            # clamp
│   ├── formatters.py            # format_price · format_percent (충돌 #1 실습 파일)
│   └── greeting.py              # greet · farewell · welcome_team (충돌 #2 실습 파일)
├── README.md
└── SUBMISSION.md                # 제출물 인덱스
```

검증: `python3 -m doctest src/utils/<파일>.py -v`

## 팀

| 역할 | GitHub |
|---|---|
| 팀장 | @Jeong-Yun-Choi |
| 팀원 | @P516n |
| 팀원 | @whoawoodev |
| 팀원 | @sangwoo-codyssey |

## 유틸 함수 목록

| 함수 | 파일 | 작성자 |
|---|---|---|
| `to_snake_case` | `src/utils/string_utils.py` | @P516n |
| `to_camel_case` | `src/utils/string_utils.py` | @P516n |
| `to_pascal_case` | `src/utils/string_utils.py` | @P516n |
| `chunk(items, size)` | `src/utils/list_utils.py` | @sangwoo-codyssey |
| `days_between(d1, d2)` | `src/utils/date_utils.py` | @whoawoodev |
| `clamp(value, low, high)` | `src/utils/math_utils.py` | @Jeong-Yun-Choi |

## 문서

- [협업 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [트러블슈팅 기록](docs/troubleshooting-log.md)
