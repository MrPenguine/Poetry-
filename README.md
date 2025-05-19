# Poetry Lock Diff GitHub Action

A GitHub Action that posts a summary of all changes within the `poetry.lock` file to a pull request.

## Features

- Automatically detects changes in your Poetry lockfile
- Posts a clear summary comment on your pull request
- Shows added, removed, and updated dependencies with their versions
- Updates existing comments instead of creating new ones for each change

## Usage

### Basic Setup

Add this GitHub Action to your repository by creating a workflow file at `.github/workflows/poetry-lock-diff.yml`:

```yaml
name: Poetry Lock Diff

on:
  pull_request:
    paths:
      - 'poetry.lock'

jobs:
  diff-poetry-lock:
    runs-on: ubuntu-latest
    name: Diff poetry.lock
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Diff poetry.lock
        uses: ./
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Custom Lockfile Path

If your Poetry lockfile is not in the default location, you can specify a custom path:

```yaml
- name: Diff poetry.lock
  uses: ./
  with:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    lockfile_path: "custom/path/to/poetry.lock"
```

## How It Works

When a pull request is opened or updated that includes changes to the `poetry.lock` file, this action:

1. Fetches the lockfile from both the base branch and the PR branch
2. Compares the dependencies between the two versions
3. Generates a summary of added, removed, and updated packages
4. Posts this summary as a comment on the PR
5. Updates the comment if the PR is updated with new changes

## Example Output

```
### Detected 3 changes to dependencies in Poetry lockfile

Added pydantic (1.10.6)
Added typing-extensions (4.5.0)
Updated urllib3 (1.26.14 -> 1.26.15)

(2 added, 0 removed, 1 updated, 4 not changed)
```

## Development

### Prerequisites

- Python 3.8+
- Poetry

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/diff-poetry-lock.git
cd diff-poetry-lock

# Install dependencies
pnpm install
```

### Testing

```bash
pytest
```

## License

MIT
