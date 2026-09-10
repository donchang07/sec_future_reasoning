# Prediction result publication — Plan

2026-09-11. User authorizes ongoing GitHub publication of generated results, beginning with today's Daily.

Publish every registered public v2 live_forward system journal and its existing explainability report to docs/predictions/YYYY-MM-DD/run_id/. Backfill existing registered results. Keep raw bundles, outer shadow/human records, credentials and private data local. Publish immutable linked public Outcome records when available. The original prediction must never be rewritten.

Use a separate publication package/task outside the frozen operations manifest. Poll every five minutes, retry failed publication without rerunning prediction, and leave the existing 07:00 task/model unchanged. Never force-push or include unrelated changes. Pre-existing local changes must remain untouched.

Success: today's report reachable on GitHub; autonomous task installed after tests/CI; exact journal seal preserved; repeat publication idempotent; safe staged scope; interrupted/network-failed pushes retry; old replay hashes unchanged; permanent project rule updated. Follow Plan → Design → Do → Check/Act and publish phase documents.
