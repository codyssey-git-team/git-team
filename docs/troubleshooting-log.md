# Troubleshooting Log

Git 트러블슈팅 4종(amend · reset · revert · stash)의 실습 기록. 시나리오마다 참여자(이름+역할) · 상황(재현 가능한 설명) · 시도한 명령/절차(실제 출력) · 결과와 주의점(원격 히스토리·협업 영향) · 왜 이 방법을 선택했는가(Why)를 적는다.



## 시나리오: amend

<!-- TODO(@P516n): 참여자 / 상황 / 시도한 명령·절차 / 결과·주의점 / Why -->



## 시나리오: reset

<!-- TODO(@whoawoodev): 참여자 / 상황 / 시도한 명령·절차 / 결과·주의점 / Why -->



## 시나리오: revert

### 참여자
- 실행·기록: @sangwoo-codyssey — 도입 PR #39 (`feature/sangwoo-list-default-size`) 와 되돌린 PR #44 (`fix/sangwoo-revert-chunk-default`) 둘 다 작성자
- 리뷰어: @whoawoodev — PR #39 에서 위험을 라인 코멘트로 남기고 Approve, PR #44 에서 되돌린 결과를 검증하고 Approve

### 상황
- `chunk(items, size)` 는 #16 에서 `size <= 0` 이면 `ValueError` 로 즉시 실패(fail-fast)하기로 정했던 함수다.
- PR #39 (Issue #38, 커밋 `72106f0`): `size` 에 기본값 `0` 을 두고 "0 = 자르지 않고 통째로 반환" 이라는 의미를 부여했다. PR 본문에서 #16 결정을 뒤집는 것이 맞는지, `chunk([], 0)` 이 `[[]]` 인 것이 자연스러운지 리뷰어에게 결정을 요청했고, @whoawoodev 가 [L22 코멘트](https://github.com/codyssey-git-team/git-team/pull/39#discussion_r4033645868)로 "계산 결과로 `size` 가 0 이 되면 전에는 `ValueError` 로 잡혔는데 이제는 조용히 통과한다, `chunk([], 3)` 은 `[]` 인데 `chunk([], 0)` 은 `[[]]` 라 결과가 `size` 에 따라 달라진다" 는 위험을 남기고 Approve → 작성자 머지 `103473f` (2026-09-17 15:02).
- 머지 뒤 main `103473f` 에서 코멘트의 상황을 그대로 재현했다. 정수 나눗셈으로 `size` 가 0 이 되는 호출이 예외 없이 통과한다.

  ```
  scores=[88, 92, 75]  n_groups=10  size=len(scores)//n_groups=0
  chunk(scores, size) -> [[88, 92, 75]]   # 예외 없이 전체가 한 조각
  chunk(scores)       -> [[88, 92, 75]]   # size 를 빠뜨린 호출도 조용히 통과
  chunk([], 3)        -> []    vs   chunk([], 0) -> [[]]

  # 머지 전(00a7b04)에는 같은 호출이:
  chunk(scores, 0)    -> ValueError: size must be positive, got 0
  chunk(scores)       -> TypeError: chunk() missing 1 required positional argument: 'size'
  ```
- 문제 커밋은 이미 **원격 `main` 에 머지돼 있고**, 그 위에 다른 PR(#43 CODEOWNERS, `e1594d1`)까지 쌓인 상태였다. 팀원이 이미 pull 했을 수 있는 커밋이다. Issue #42 를 등록하고 되돌리기로 했다.

### 시도한 명령/절차
- 최신 main 에서 되돌리기용 브랜치를 따고, **머지 커밋**을 `-m 1` 로 revert 했다.

  ```
  $ git switch main && git pull --ff-only
  $ git log --oneline -1
  103473f Merge pull request #39 from codyssey-git-team/feature/sangwoo-list-default-size
  $ git switch -c fix/sangwoo-revert-chunk-default

  $ git revert -m 1 103473f --no-edit
  [fix/sangwoo-revert-chunk-default af2012f] Revert "Merge pull request #39 from codyssey-git-team/feature/sangwoo-list-default-size"
   2 files changed, 7 insertions(+), 12 deletions(-)

  $ git show --stat HEAD
  af2012f Revert "Merge pull request #39 from codyssey-git-team/feature/sangwoo-list-default-size"
      This reverts commit 103473f17cbaf5e52e0c9fa08ead7112e07c0fc1, reversing
      changes made to 00a7b042fb6a6e5d81fd5783c0b4d61c0bb4f59d.
   README.md               |  2 +-
   src/utils/list_utils.py | 17 ++++++-----------
  ```
- `-m 1` 의 의미: 머지 커밋 `103473f` 는 부모가 둘이다 — 첫 번째 `00a7b04`(main 쪽), 두 번째 `72106f0`(브랜치 쪽). `-m 1` 은 "첫 번째 부모를 기준으로" 라는 뜻이라, 브랜치가 main 에 가져온 변경만 정확히 취소된다.
- 되돌린 결과를 브랜치에서 검증했다.

  ```
  $ python3 -m doctest src/utils/list_utils.py -v | tail -3
  3 passed and 0 failed.
  $ python3 -c "from src.utils.list_utils import chunk; chunk([88, 92, 75], 0)"
  ValueError: size must be positive, got 0
  $ git diff 00a7b04 HEAD --stat
  (출력 없음 — main 쪽 부모와 파일 내용이 완전히 같음 = #39 변경만 정확히 되돌아감)
  ```
- push → PR #44 (Closes #42, 리뷰어 @whoawoodev) → Approve ("`git diff 00a7b04 HEAD` 가 비어 있는 것 확인했습니다. #39 이전 상태로 돌아갔습니다.") → 작성자 머지 `d65177e` (15:20) + 브랜치 삭제 → Issue #42 자동 close.
- 명령·출력 전문: [evidence/pr39-revert-2026-09-17.txt](evidence/pr39-revert-2026-09-17.txt)

### 결과
- main `d65177e` 에서 `chunk(scores, 0)` 이 다시 `ValueError`, doctest 3 passed. `git diff 00a7b04 main --stat` 에는 그 사이 머지된 `.github/CODEOWNERS` 만 나오고 `list_utils.py`·`README.md` 는 차이 없음.
- 히스토리에는 도입(`103473f`)과 취소(`af2012f` → 머지 `d65177e`)가 **둘 다 남는다**. 지워진 커밋은 없다.

  ![revert 커밋 af2012f](evidence/pr44-revert-commit-2026-09-17.jpg)
  ![PR #44](evidence/pr44-revert-pr-2026-09-17.jpg)
  ![main Commits — 도입과 취소가 나란히](evidence/pr44-main-commits-2026-09-17.jpg)
- 주의할 점 (원격 히스토리 · 협업 영향):
  - 원격 `main` 은 보호 규칙(force push 금지, PR 필수)이라 `reset` 으로 커밋을 지울 수 없다. 지울 수 있는 상황이었더라도 이미 pull 한 팀원의 로컬 히스토리와 어긋나 그쪽에서 다시 문제가 된다.
  - 머지 커밋은 `-m` 을 지정하지 않으면 revert 가 거부된다. 부모 번호를 잘못 고르면(`-m 2`) main 쪽 변경이 되돌아가므로, 끝나고 `git diff <main 쪽 부모> HEAD` 가 비는지 반드시 확인한다.
  - 되돌린 뒤 같은 브랜치의 커밋 `72106f0` 을 다시 머지해도 변경이 들어오지 않는다 — git 은 이미 히스토리에 있는 커밋으로 본다. main `34383fc` 에서 확인:

    ```
    $ git merge 72106f0
    Already up to date.
    $ git merge-base --is-ancestor 72106f0 main && echo ancestor
    ancestor
    ```
    같은 변경을 다시 넣으려면 revert 커밋을 revert 하거나 새 커밋으로 만들어야 한다.
  - revert 도 일반 변경과 똑같이 PR 과 리뷰를 거쳤다 (#44). 되돌리는 것 자체가 팀이 확인해야 할 변경이다.
- 관련: Issue #38 · PR #39 (머지 `103473f`) · Issue #42 · PR #44 (커밋 `af2012f`, 머지 `d65177e`) · 팀장·P516n 의 앞선 사례 PR #18 (`35fc0ea`)

### 왜 이 방법을 선택했는가(Why)
- **revert 는 되돌렸다는 사실 자체가 커밋으로 남는다.** `103473f` 를 왜 취소했는지가 `af2012f` 의 메시지(`This reverts commit 103473f…`)와 PR #44 · Issue #42 에 그대로 이어지고, `git log` 만 봐도 "넣었다가 뺐다" 는 흐름이 보인다. `reset` 으로 지우면 실수가 있었다는 기록과 그 이유가 함께 사라진다.
- 커밋이 **이미 원격 `main` 에 있고 그 위에 #43 이 쌓인 뒤**였다. `reset` + force push 는 보호 규칙이 막기도 하지만, 허용됐더라도 이미 pull 한 팀원의 로컬은 지워진 커밋을 그대로 갖고 있어 다음 push 때 다시 살아나거나 충돌한다. 혼자 쓰는 브랜치가 아니면 히스토리를 지우는 방식은 선택지에서 빠진다.
- 손으로 `list_utils.py` 와 `README.md` 를 고쳐 새 커밋을 만들 수도 있었지만, 그러면 "#39 이전과 정확히 같은가" 를 사람이 보장해야 한다. `git revert -m 1` 은 머지 커밋이 가져온 diff 를 기계적으로 뒤집으므로 `git diff 00a7b04 HEAD` 가 비는 것으로 정확성을 검증할 수 있었다.
- revert 도 PR 로 올려 리뷰를 받은 이유: 되돌리는 것도 main 에 들어가는 변경이고, 도입 PR 에서 위험을 지적했던 리뷰어(@whoawoodev)가 "정확히 이전 상태로 돌아갔는지" 를 확인하는 것이 가장 자연스러운 검증이었다.



## 시나리오: stash

<!-- TODO(@Jeong-Yun-Choi): 참여자 / 상황 / 시도한 명령·절차 / 결과·주의점 / Why -->
