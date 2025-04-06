# Contributing

## Setup

  ```bash
  make -f Makefile.win setup
  make -f Makefile.unix setup
  ```

## Common Commands

- Run server:  
  ```bash
  python manage.py runserver
  ```

- Run tests:  
  ```bash
  pytest
  ```

- Format code:  
  ```bash
  make -f Makefile.win format
  make -f Makefile.unix format
  ```

- Lint code:  
  ```bash
  make -f  Makefile.{os_name} lint
  ```

- CI check:  
  ```bash
  make -f  Makefile.{os_name} check
  ```

## Cleanup (optional)
- Remove caches and `.pyc` files:
  ```bash
  make -f  Makefile.{os_name} clean-cache
  ```
- Remove the entire conda environment:
  ```bash
    make -f  Makefile.{os_name} clean-env
  ```

## Notes

- Code checks apply to `core/` only  
- Run `make format` and `make lint` before pushing  
- Make sure all tests pass
