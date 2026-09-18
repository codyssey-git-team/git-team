# Submission Index

## Team

- 팀명: git-team
- 저장소: https://github.com/codyssey-git-team/git-team (GitHub Organization `codyssey-git-team`, public)
- 결과물: (A) 유틸 함수 모음 (`src/utils/`)

| 역할 | GitHub | 트러블슈팅 담당 | 충돌 실습 역할 | 유틸 함수 |
|---|---|---|---|---|
| 팀장 | @Jeong-Yun-Choi | stash · revert | 충돌 #1 — 먼저 머지되는 쪽 (#32) | `clamp` (#25) |
| 팀원 | @P516n | amend (+ rebase -i squash) | 충돌 #1 — 해결하는 쪽 (#28) | `to_snake_case` · `to_camel_case` · `to_pascal_case` (#19) |
| 팀원 | @whoawoodev | reset --soft | 충돌 #2 — 먼저 머지되는 쪽 (#31) | `days_between` (#13) |
| 팀원 | @sangwoo-codyssey | revert | 충돌 #2 — 해결하는 쪽 (#33) | `chunk` (#16) |

빠른 검색: `is:pr author:<아이디>` · `is:pr reviewed-by:<아이디>` · `is:issue author:<아이디>`

## Member Contributions

PR 옆 해시는 main 의 머지 커밋. 리뷰 반영 옆 해시는 리뷰 코멘트를 반영한 커밋.

### 팀장 — @Jeong-Yun-Choi

- Issues: #10, #17, #20, #22, #29, #52
- PRs (머지 6): [#14](https://github.com/codyssey-git-team/git-team/pull/14) `8b3c5f4` 브랜치 전략 · [#18](https://github.com/codyssey-git-team/git-team/pull/18) `dca7855` #14 revert · [#21](https://github.com/codyssey-git-team/git-team/pull/21) `804eeec` 브랜치 전략 재PR · [#25](https://github.com/codyssey-git-team/git-team/pull/25) `b7f260e` clamp · [#32](https://github.com/codyssey-git-team/git-team/pull/32) `95755ec` format_price 반올림 · [#54](https://github.com/codyssey-git-team/git-team/pull/54) `6a4aa8d` stash 기록
- Reviews: #8, #13, #24, #33, #41, #46, #48, #50, #53
- 리뷰 반영: #21 (P516n 의 `hotfix/` 규칙 제안 → #14 revert 후 재PR 로 반영) · #25 `a2150c6` (whoawoodev 의 `low > high` 지적 → `ValueError` + doctest)
- 트러블슈팅: revert — #14 를 되돌린 #18 (Issue #17) 실행 ([PR #14 Revert 버튼](docs/evidence/pr14-revert-button-2026-09-16.png) · [revert 브랜치 체크아웃 `35fc0ea`](docs/evidence/pr18-revert-branch-checkout-2026-09-16.png)) · stash — [docs/troubleshooting-log.md › 시나리오: stash](docs/troubleshooting-log.md#시나리오-stash) (#54)

### 팀원 — @P516n

- Issues: #5, #11, #26, #37, #51
- PRs (머지 5): [#6](https://github.com/codyssey-git-team/git-team/pull/6) `1009c99` 커밋 컨벤션 · [#19](https://github.com/codyssey-git-team/git-team/pull/19) `9700c86` string_utils · [#28](https://github.com/codyssey-git-team/git-team/pull/28) `6404a49` format_price 천 단위 쉼표 (충돌 #1 해결 `f254ca2`) · [#41](https://github.com/codyssey-git-team/git-team/pull/41) `715bb24` 충돌 #1 기록 · [#53](https://github.com/codyssey-git-team/git-team/pull/53) `d8fd36d` amend 기록 (#3 은 닫음)
- Reviews: #14, #16, #18, #21, #31, #43, #50
- 리뷰 반영: #6 `213dbdf` (금지 예시 추가) · #19 `ca4af78` `8a04190` `d3a6544` (README 충돌·백틱·선행 밑줄 보존) · #53 `f3d28a3` `57951b3` (squash 후 해시 병기)
- 트러블슈팅: amend — `docs/troubleshooting-log.md` "시나리오: amend" (#53) · revert 참여 — #14 에 Revert 버튼 `35fc0ea`, #18 리뷰·머지
- 보너스: `git rebase -i` squash — [pr19-2 squash 수행 log.txt](docs/evidence/pr19-2%20squash%20%EC%88%98%ED%96%89%20log.txt) · [pr19-2 squash 수행.png](docs/evidence/pr19-2%20squash%20%EC%88%98%ED%96%89.png) (전/후 `git log --graph`)

### 팀원 — @whoawoodev

- Issues: #4, #12, #30, #40, #49
- PRs (머지 5): [#9](https://github.com/codyssey-git-team/git-team/pull/9) `9157387` PR·리뷰 규칙 · [#13](https://github.com/codyssey-git-team/git-team/pull/13) `104e68c` date_utils · [#31](https://github.com/codyssey-git-team/git-team/pull/31) `5946b60` helpers → utils/greeting 이동 · [#43](https://github.com/codyssey-git-team/git-team/pull/43) `e1594d1` CODEOWNERS · [#50](https://github.com/codyssey-git-team/git-team/pull/50) `e440890` reset 기록
- Reviews: #6, #25, #33, #35, #39, #44, #48
- 리뷰 반영: #9 `78ddcd3` (리뷰 제출 형식·답글 규칙) · #13 `33cc40a` (역순 입력 docstring) · #50 `227465c` (reflog 보관 기간 정정)
- 트러블슈팅: reset — `docs/troubleshooting-log.md` "시나리오: reset" (#50, 실습은 #13 직전 `ffa1ad8` push 거부 → `reset --soft`; `ffa1ad8` 는 reset 으로 사라진 로컬 커밋이라 [캡처](docs/evidence/pr13-reset-01-push-rejected-2026-09-16.png) 에만 남음)
- 보너스: `.github/CODEOWNERS` (#43)

### 팀원 — @sangwoo-codyssey

- Issues: #1, #7, #15, #23, #27, #34, #38, #42, #45, #47, #55 (#36 은 범위 밖으로 닫음)
- PRs (머지 10): [#2](https://github.com/codyssey-git-team/git-team/pull/2) `a37249d` 이슈·PR 템플릿 (보호 규칙 설정 전 인프라 PR, 리뷰 없이 머지) · [#8](https://github.com/codyssey-git-team/git-team/pull/8) `6389106` 충돌 대응 흐름 · [#16](https://github.com/codyssey-git-team/git-team/pull/16) `bfa4787` list_utils · [#24](https://github.com/codyssey-git-team/git-team/pull/24) `75bcafc` 브랜치 삭제 규칙 · [#33](https://github.com/codyssey-git-team/git-team/pull/33) `3e6e237` greet 빈 이름 검증 (충돌 #2 해결 `1e37419`) · [#35](https://github.com/codyssey-git-team/git-team/pull/35) `00a7b04` 충돌 #2 기록 · [#39](https://github.com/codyssey-git-team/git-team/pull/39) `103473f` chunk 기본 size · [#44](https://github.com/codyssey-git-team/git-team/pull/44) `d65177e` #39 revert · [#46](https://github.com/codyssey-git-team/git-team/pull/46) `34383fc` troubleshooting-log 뼈대 · [#48](https://github.com/codyssey-git-team/git-team/pull/48) `75b6470` revert 기록
- Reviews: #9, #19, #28, #32, #50, #53, #54
- 리뷰 반영: #8 `3ef6f45` (해결 주체 근거) · #24 `55dbdf2` (삭제 주체 명시) · #35 `f8b08af` (rename 감지 설명 정정) · #48 `089d3f3` (재머지 실제 출력)
- 트러블슈팅: revert — #39 머지 `103473f` → 부작용 재현 Issue #42 → `git revert -m 1` `af2012f` → #44 · 기록 `docs/troubleshooting-log.md` "시나리오: revert" (#48)
- 인프라: Organization·저장소 생성, 팀원 write 권한, Branch Protection, 이슈·PR 템플릿 (#2)

## Key Docs

- Contributing: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) — 브랜치 전략(#14·#21) · 커밋 컨벤션(#6) · PR·리뷰 규칙(#9) · 충돌 대응 흐름(#8) · 브랜치 삭제 규칙(#24)
- Conflict log: [docs/conflict-resolution.md](docs/conflict-resolution.md) — 충돌 #1 같은 hunk (팀장 ↔ P516n, #32/#28, 기록 #41) · 충돌 #2 파일 이동 vs 수정 (whoawoodev ↔ sangwoo, #31/#33, 기록 #35)
- Troubleshooting: [docs/troubleshooting-log.md](docs/troubleshooting-log.md) — amend/P516n (#53) · reset/whoawoodev (#50) · revert/sangwoo (#48) · stash/팀장 (#54)
- Code owners: [.github/CODEOWNERS](.github/CODEOWNERS) (#43)

## Evidence

- Git history: [docs/git-history.txt](docs/git-history.txt) — `git log --oneline --graph --decorate --all` (#54 머지 후 2026-09-17 생성)
- Branch protection: [docs/evidence/branch-protection-2026-09-16.txt](docs/evidence/branch-protection-2026-09-16.txt) — admin 의 main 직접 push 가 `GH006` 으로 거부된 로그 · 설정 화면 [① PR 필수 · 승인 1 · conversation resolution](docs/evidence/branch-protection-settings-1-pr-approvals-2026-09-17.jpg) · [② 관리자 bypass 금지 · force push · deletions 금지](docs/evidence/branch-protection-settings-2-bypass-force-push-2026-09-17.jpg)
- CODEOWNERS 적용: [docs/evidence/pr46-codeowners-timeline-2026-09-17.txt](docs/evidence/pr46-codeowners-timeline-2026-09-17.txt) (리뷰어 미지정 PR #46 에 팀장 자동 요청) · [pr46-codeowners-auto-request-2026-09-17.jpg](docs/evidence/pr46-codeowners-auto-request-2026-09-17.jpg) · [pr46-codeowners-tooltip-2026-09-17.png](docs/evidence/pr46-codeowners-tooltip-2026-09-17.png) ("is a code owner" 툴팁)
- 충돌: [pr28-1 비자명 충돌 발생.png](docs/evidence/pr28-1%20%EB%B9%84%EC%9E%90%EB%AA%85%20%EC%B6%A9%EB%8F%8C%20%EB%B0%9C%EC%83%9D.png) (충돌 #1) · [pr33-conflict-2026-09-17.png](docs/evidence/pr33-conflict-2026-09-17.png) (충돌 #2)
- 트러블슈팅:
  - amend (#53): [amend 수행.png](docs/evidence/pr-19-1%20%EC%BB%A4%EB%B0%8B%20%EB%A9%94%EC%8B%9C%EC%A7%80%20%EC%98%A4%ED%83%88%EC%9E%90%20amend%20%EC%88%98%ED%96%89.png) · [amend 수행 log.txt](docs/evidence/pr19-1%20%EC%BB%A4%EB%B0%8B%20%EB%A9%94%EC%8B%9C%EC%A7%80%20%EC%98%A4%ED%83%88%EC%9E%90%20amend%20%EC%88%98%ED%96%89%20log.txt) / squash: [squash 수행 log.txt](docs/evidence/pr19-2%20squash%20%EC%88%98%ED%96%89%20log.txt) · [squash 수행.png](docs/evidence/pr19-2%20squash%20%EC%88%98%ED%96%89.png)
  - reset (#50): [01 push 거부](docs/evidence/pr13-reset-01-push-rejected-2026-09-16.png) · [02 `--soft` 후 status](docs/evidence/pr13-reset-02-soft-status-2026-09-16.png) · [03 브랜치 재커밋](docs/evidence/pr13-reset-03-branch-recommit-2026-09-16.png)
  - revert (#48): [pr39-revert-2026-09-17.txt](docs/evidence/pr39-revert-2026-09-17.txt) · [revert 커밋](docs/evidence/pr44-revert-commit-2026-09-17.jpg) · [PR #44](docs/evidence/pr44-revert-pr-2026-09-17.jpg) · [main Commits](docs/evidence/pr44-main-commits-2026-09-17.jpg) / revert #14→#18 (팀장): [PR #14 Revert 버튼](docs/evidence/pr14-revert-button-2026-09-16.png) · [revert 브랜치 체크아웃](docs/evidence/pr18-revert-branch-checkout-2026-09-16.png)
  - stash (#54): [troubleshooting-log › 시나리오: stash](docs/troubleshooting-log.md#시나리오-stash) 에 `git pull` 거부 · `stash push` · `stash pop` CONFLICT · `stash drop` 출력 인라인 · [stash-choi-2026-09-17.txt](docs/evidence/stash-choi-2026-09-17.txt) 은 명령 이력만 (PowerShell transcript 가 git 출력 미포함)
