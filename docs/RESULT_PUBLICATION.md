# 결과 자동 게시

공개 Prediction Journal과 설명 보고서는 [결과 목록](predictions/README.md)에 자동 게시한다. 날짜는 Prediction timestamp의 KST 날짜이며, 각 run_id는 별도 디렉터리다. Journal은 봉인된 원본과 같은 바이트로 저장한다. 이후 공개 Outcome은 해당 디렉터리의 outcomes/에 별도 추가한다.

`SEC-Frozen-Forward-Publish` 작업이 5분마다 새 결과를 확인하고 origin/main으로 push한다. 예측 실행과 분리되어 있으므로 게시 실패가 새 Prediction을 만들지 않는다. 기존 07:00 예측 작업·코드·Replay manifest를 변경하지 않는다. 현재 PC와 사용자 로그인 세션, GitHub 연결이 필요하다.

```powershell
.venv/Scripts/python.exe -m publication
./scripts/install-result-publication.ps1
Get-ScheduledTaskInfo -TaskName SEC-Frozen-Forward-Publish
```

네트워크 오류로 commit만 만들어지고 push가 실패한 경우 다음 실행이 해당 게시 commit을 재시도한다. 다른 작업의 staged 변경이나 미게시 commit, 원격과의 분기가 있으면 안전하게 보류하며 강제 push나 자동 merge를 하지 않는다. 정상 작업·동기화 후 다음 주기에 다시 시도한다.

원본 raw snapshot, 자격증명, 개인 보유정보, Human Forecast와 외부 Shadow 입력은 게시하지 않는다. 공개 System Journal만 허용하며 모르는 필드/Source나 비공개 값은 거절한다. 오류와 게시 commit 기록은 로컬 `artifacts/local/publication/`에 저장한다. 비정상 종료로 lock이 남았다면 실행 중인 publisher가 없는지 확인한 후 그 lock 파일만 정리한다.

처음 활성화할 때 등록된 기존 공개 결과도 소급 게시하지만, 예측 시각이나 판단을 다시 계산하지 않는다. 기존 Journal과 설명 보고서의 내용이 다른 파일을 발견하면 덮어쓰지 않고 오류로 기록한다.
