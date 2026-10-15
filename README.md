<div align="center">

# ghw-demo-repo

**A minimal, production-shaped Python starter — built for MLH Global Hack Week: Hacktoberfest 2026.**

[![CI](https://github.com/meetr1912/ghw-demo-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/meetr1912/ghw-demo-repo/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/meetr1912/ghw-demo-repo/pulls)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/meetr1912/ghw-demo-repo)

</div>

---

## Overview

`ghw-demo-repo` is a tiny but **complete** example of what a healthy open-source
repository looks like: a clear README, a continuous-integration workflow, a
pre-configured development container, code owners, and a one-command test suite.

It exists to demonstrate two things end to end:

1. **Repository management** — the settings and files that make a repo look
   legitimate and keep its default branch protected.
2. **Cloud development with Codespaces** — booting a reproducible dev
   environment straight from the repo and shipping a change from it.

## Features

- 🐍 Zero-dependency Python CLI (standard library only)
- ✅ Unit tests with `pytest`, run automatically in CI
- 🧪 GitHub Actions workflow on every push and pull request
- 📦 `.devcontainer/` so Codespaces and VS Code start ready to go
- 👤 `CODEOWNERS` so review requests are routed automatically
- 📄 MIT licensed and documented

## Quick start

```bash
# 1. Clone
git clone https://github.com/meetr1912/ghw-demo-repo.git
cd ghw-demo-repo

# 2. (optional) create a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# 3. Install dev dependencies
pip install -r requirements.txt

# 4. Run the app
python -m src.greeter Ada Lovelace

# 5. Run the tests
pytest -q
```

## Usage

```console
$ python -m src.greeter Ada
Hello, Ada! Welcome to Global Hack Week.

$ python -m src.greeter            # no name -> friendly default
Hello, world! Welcome to Global Hack Week.

$ python -m src.greeter Ada Grace   # multiple names
Hello, Ada! Welcome to Global Hack Week.
Hello, Grace! Welcome to Global Hack Week.
```

## Project layout

```text
ghw-demo-repo/
├── .devcontainer/
│   └── devcontainer.json     # Codespaces / VS Code dev environment
├── .github/
│   ├── BRANCH-PROTECTION.md  # notes on the protected main branch
│   └── workflows/ci.yml      # continuous integration
├── social-preview/           # repository social preview image (1280×640)
├── src/
│   └── greeter.py            # the application
├── tests/
│   └── test_greeter.py       # unit tests
├── CODEOWNERS                # who reviews what
├── LICENSE                   # MIT
├── README.md
└── requirements.txt
```

## Development

The fastest way to get a working environment is **GitHub Codespaces**:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/meetr1912/ghw-demo-repo)

The dev container installs `pytest` automatically and configures the editor, so
you can run `pytest -q` the moment the Codespace is ready. See
`.devcontainer/devcontainer.json` for the exact configuration.

## Contributing

Contributions are welcome! Please:

1. Fork the repository and create a feature branch
   (`git switch -c feat/my-change`).
2. Make your change and add or update tests.
3. Ensure `pytest -q` passes locally.
4. Open a pull request against `main`.

The `main` branch is protected and requires review from the owners listed in
[`CODEOWNERS`](./CODEOWNERS). Pull requests must pass the CI workflow before
they can be merged.

## License

This project is licensed under the **MIT License** — see the
[`LICENSE`](./LICENSE) file for the full text.

```text
MIT License

Copyright (c) 2026 Mit Patel
...
```

---

<div align="center">
<sub>Built for MLH Global Hack Week · Hacktoberfest 2026 · event 14553</sub>
</div>
