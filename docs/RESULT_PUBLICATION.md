# 결과 자동 게시

공개 Prediction Journal과 설명 보고서는 [결과 목록](predictions/README.md)에 자동 게시한다. 날짜는 Prediction timestamp의 KST 날짜이며, 각 run_id는 별도 디렉터리다. 전문 한국어 `briefing.md`가 네이비 헤더, 오늘의 결론, 기간별 주요 예측, 방향·타이밍·정렬·유동성 해설과 데이터 한계를 먼저 보여준다. 전체 기여도 감사는 `explainability.md`, 봉인 원본은 `journal.json`에서 확인한다. Journal은 봉인된 원본과 같은 바이트로 저장하며, 이후 공개 Outcome은 해당 디렉터리의 outcomes/에 별도 추가한다.

`SEC-Frozen-Forward-Publish` 작업이 매일 07:15 KST에 새 결과를 확인하고 origin/main으로 push한다. 정상적으로 완료된 07:00 Daily 결과는 약 15분 뒤 같은 날 게시된다. 07:15 이후 완료된 Daily/Event 결과는 수동 게시하지 않는 한 다음 날 07:15에 게시된다. 예측 실행과 분리되어 있으므로 게시 실패가 새 Prediction을 만들지 않는다. 기존 07:00 예측 작업·코드·Replay manifest를 변경하지 않는다. 현재 PC와 사용자 로그인 세션, GitHub 연결이 필요하다.

GitHub 게시가 성공하면 같은 작업이 활성화일 이후의 새 `official_preopen` Daily를 전문 이메일로 1회 전달한다. 이메일은 네이비 헤더, 오늘의 결론, 1주·1개월·1년 주요 예측, 의사결정 게이트, 데이터 신뢰도, 전체 공개 브리핑 링크를 포함한다. 문구와 숫자는 봉인된 Journal에서 결정론적으로 렌더링하며 Gmail 연결은 전송만 담당한다. Event/Human/Shadow/held/private 결과와 활성화 이전 날짜는 발송하지 않는다.

수신 주소, 활성화일, Codex 실행 경로, Gmail message ID와 전송 envelope/result는 `artifacts/local/publication/`에만 저장하고 Git에 게시하지 않는다. Gmail OAuth 토큰이나 SMTP 비밀번호는 코드와 로컬 설정에 저장하지 않으며 설치된 Gmail 플러그인의 연결을 사용한다. 로컬 ledger와 Gmail Sent 사전 확인으로 재시도 중 중복 발송을 방지한다.

Windows에서는 publisher가 모든 `git.exe` subprocess를 `CREATE_NO_WINDOW`로 실행하므로 Git 확인·commit·push 과정에서 콘솔 창을 표시하지 않는다.

```powershell
.venv/Scripts/python.exe -m publication
./scripts/install-result-publication.ps1 -Recipient '<approved local recipient>'
Get-ScheduledTaskInfo -TaskName SEC-Frozen-Forward-Publish
```

최초 설치에는 `-Recipient`가 필요하고 이후 재등록은 로컬 설정을 재사용한다. Gmail 플러그인 연결이 만료되면 다시 연결한 뒤 수동 publication 명령으로 재시도한다. 메일만 일시 중지하려면 로컬 `email-config.json`의 `enabled`를 `false`로 바꾼다. 수신 주소는 문서나 명령 기록에 남기지 않는다.

네트워크 오류로 commit만 만들어지고 push가 실패한 경우 다음 날 07:15 실행이 해당 게시 commit을 재시도한다. GitHub 게시가 끝났지만 Gmail 전달이 실패한 경우 public 결과는 그대로 유지하고 메일만 다음 invocation에서 재시도한다. 즉시 재시도가 필요하면 `.venv/Scripts/python.exe -m publication`을 수동 실행한다. 다른 작업의 staged 변경이나 미게시 commit, 원격과의 분기가 있으면 안전하게 보류하며 강제 push나 자동 merge를 하지 않는다. 정상 작업·동기화 후 다음 실행에서 다시 시도한다.

원본 raw snapshot, 자격증명, 개인 보유정보, Human Forecast와 외부 Shadow 입력은 게시하지 않는다. 공개 System Journal만 허용하며 모르는 필드/Source나 비공개 값은 거절한다. 오류와 게시 commit 기록은 로컬 `artifacts/local/publication/`에 저장한다. 비정상 종료로 lock이 남았다면 실행 중인 publisher가 없는지 확인한 후 그 lock 파일만 정리한다.

처음 활성화할 때 등록된 기존 공개 결과도 소급 게시하지만, 예측 시각이나 판단을 다시 계산하지 않는다. 기존 Journal과 설명 보고서의 내용이 다른 파일을 발견하면 덮어쓰지 않고 오류로 기록한다.
