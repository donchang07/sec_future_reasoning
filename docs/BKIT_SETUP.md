# bkit-codex setup

This repository pins bkit-codex as a Git submodule at `.bkit-codex`.

After cloning, initialize submodules and run the project setup script for your operating system. The setup creates or refreshes `.agents/skills` from the pinned bkit-codex skills and ensures the PDCA document directories exist.

Prerequisites: OpenAI Codex CLI v0.100.0 or later, Node.js v20+, and Git.

Verification in Codex: start Codex in the repository and check PDCA status. The bkit MCP server is configured in `.codex/config.toml`.

The project-specific `AGENTS.md` intentionally preserves the SEC Future Reasoning architecture rules while bkit-codex supplies PDCA, context engineering, skills, and MCP state management.
