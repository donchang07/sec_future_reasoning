#!/usr/bin/env bash
set -euo pipefail
git submodule update --init --recursive
mkdir -p .agents/skills docs/01-plan/features docs/02-design/features docs/03-analysis docs/04-report
for skill in .bkit-codex/.agents/skills/*/; do
  name="$(basename "$skill")"
  rm -rf ".agents/skills/$name"
  cp -R "$skill" ".agents/skills/$name"
done
echo "bkit-codex project setup complete. Start Codex in this repository and check PDCA status."
