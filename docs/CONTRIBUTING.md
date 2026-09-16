# Contributing Guide

## 브랜치 전략 / 네이밍 규칙

TODO(@Jeong-Yun-Choi)



## 커밋 메시지 컨벤션

TODO(@P516n)



## PR 규칙 / 코드 리뷰 규칙

TODO(@whoawoodev)



## 충돌 대응 흐름

충돌은 "같은 파일의 같은 부분을 두 브랜치가 다르게 고쳤다"는 신호일 뿐, 사고가 아니다.
아래 순서대로 처리하고 반드시 기록을 남긴다.

1. **발견** — PR 화면에 `This branch has conflicts` 가 뜨거나, `git merge` / `git pull` 결과에
   `CONFLICT (content): Merge conflict in <파일>` 이 찍히면 충돌이다.
2. **공유** — 해결하기 전에 팀 채널에 먼저 알린다. 어떤 PR 과 어떤 PR 이 어느 파일에서 부딪혔는지
   한 줄이면 된다. 상대 브랜치 작성자에게 "누가 해결할지" 를 정한다.
3. **해결** — 원칙은 **나중에 머지하려는 PR 의 작성자가 자기 브랜치에서** 해결한다.
   "먼저 발견한 사람" 으로 정하면 발견한 사람과 그 브랜치를 실제로 고칠 사람이 달라질 수 있어
   역할이 애매해지기 때문이다. `main` 이나 상대 브랜치를 직접 고치지 않는다.
   ```bash
   git switch feature/<내-브랜치>
   git fetch origin
   git merge origin/main          # 충돌 마커(<<<<<<< ======= >>>>>>>) 가 파일에 생긴다
   # 파일을 열어 마커를 지우며 최종 내용을 정한다 (keep both / choose one / refactor)
   git add <해결한 파일>
   git commit                     # 머지 커밋 메시지는 기본값 그대로 둬도 된다
   git push origin feature/<내-브랜치>
   ```
   해결 전략을 고를 때는 "상대 변경의 의도를 살리는가" 를 먼저 본다. 확신이 없으면 상대에게 묻고 정한다.
   공유 브랜치에서 `rebase` / `push --force` 는 쓰지 않는다.
4. **기록** — 해결한 사람이 `docs/conflict-resolution.md` 에 항목을 추가한다.
   참여자(작성자/상대), 상황(브랜치·파일), 충돌 마커 원문, 선택한 전략과 이유, 실제 실행한 명령, 결과(PR 링크), 배운 점을 적는다.
   기록은 **같은 PR 에 커밋으로 포함하거나** 별도 `docs:` PR 로 올린다.
5. **리뷰 재요청** — 충돌 해결 커밋이 push 되면 리뷰어에게 재리뷰를 요청한다.
   리뷰어는 머지 커밋의 diff 에서 "충돌 해결 부분만" 다시 본다.
