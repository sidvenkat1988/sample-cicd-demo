# CI/CD Demo - Local vs CI Failure

This demo shows a common scenario where code works locally but fails in CI/CD.

## The Issue

- **Local**: Has PostgreSQL development libraries (libpq-dev) installed
- **CI/CD**: Clean Ubuntu container without system libraries
- **Result**: `psycopg2` installation fails in CI/CD

## Test Locally

```bash
# If you have PostgreSQL installed locally, this will work
pip install -r requirements.txt
pytest -v
```

All tests will pass locally if you have libpq-dev installed.

## Push to GitHub

When you push this to GitHub, the CI/CD workflow will fail with:

```
Error: pg_config executable not found
error: command 'gcc' failed: No such file or directory
```

## The Fix

Either:
1. Install system dependencies in CI workflow:
```yaml
- name: Install system dependencies
  run: sudo apt-get install -y libpq-dev
```

2. Or use psycopg2-binary (pre-compiled):
```
psycopg2-binary==2.9.9
```
