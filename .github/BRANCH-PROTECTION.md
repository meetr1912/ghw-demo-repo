# Branch protection — `main`

This file documents the branch-protection rules that are applied to the `main`
branch of `ghw-demo-repo`. GitHub does **not** store these rules as a file in
the repository — they live in the repository's settings — so this document is
the human-readable record of what is configured.

> Apply the settings by hand on github.com following
> [`../../branch-protection-checklist.md`](../../branch-protection-checklist.md).
> That checklist is the exact click-path; this file is the summary.

## Repository visibility

| Setting | Value |
| --- | --- |
| Visibility | **Public** |
| Default branch | `main` |
| Social preview | `social-preview/social-preview.png` (1280×640) |

## Protected branch ruleset (`main`)

| Rule | Setting |
| --- | --- |
| Require a pull request before merging | ✅ on |
| → Required approvals | **1** |
| → Dismiss stale approvals on new commits | ✅ on |
| → Require review from Code Owners | ✅ on |
| → Require conversation resolution before merging | ✅ on |
| Require status checks to pass | ✅ on |
| → Required check | **CI / test** (from `.github/workflows/ci.yml`) |
| → Require branches to be up to date before merging | ✅ on |
| Require linear history | ✅ on |
| Do not allow bypassing the above settings | ✅ on |
| Allow force pushes | ❌ off |
| Allow deletions | ❌ off |

## Why each rule matters

- **Require a pull request** — nobody (not even the owner) pushes straight to
  `main`; every change is reviewable.
- **1 approval + Code Owners** — the owners in [`../CODEOWNERS`](../CODEOWNERS)
  must sign off on changes to their paths.
- **Status checks** — the CI workflow must be green before merge, so a broken
  build can never land on `main`.
- **Linear history** — merge commits are disallowed; history stays readable
  (squash or rebase merges only).
- **No force-push / no deletions** — `main` cannot be rewritten or removed.

## Code owners

Ownership is declared in [`../CODEOWNERS`](../CODEOWNERS). The catch-all rule
`* @meetr1912` means the repository owner is the default reviewer for every
change. CODEOWNERS only takes effect on branch protection once the referenced
users have **write** access to the repository.
