# Narcissus Structure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refactor `5.py` into an import-safe script with a `main()` entry point while preserving the existing three-digit narcissus-number behavior.

**Architecture:** Keep the current boolean helper for the three-digit check, add a separate `main()` that performs input and output, and protect execution with the standard `if __name__ == "__main__"` guard. Extend tests with one import-based unit test plus the existing subprocess black-box checks.

**Tech Stack:** Python standard library, `unittest`, `importlib.util`, `subprocess`

---

### Task 1: Add an import-safe structure test

**Files:**
- Modify: `tests/test_narcissus_script.py`
- Modify: `5.py`

**Step 1: Write the failing test**

```python
def test_module_is_import_safe_and_exposes_main(self) -> None:
    module = load_script_module()
    self.assertTrue(hasattr(module, "main"))
    self.assertTrue(module.is_narcissus_number(153))
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest discover -s tests -p "test_narcissus_script.py" -v`
Expected: FAIL because importing the current script triggers top-level input instead of exposing an import-safe module.

**Step 3: Write minimal implementation**

```python
def main() -> None:
    number = int(input())
    print(IS_NARCISSUS_TEXT if is_narcissus_number(number) else IS_NOT_NARCISSUS_TEXT)


if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest discover -s tests -p "test_narcissus_script.py" -v`
Expected: PASS

**Step 5: Commit**

```bash
git add 5.py tests/test_narcissus_script.py docs/plans/2026-04-08-narcissus-structure-design.md docs/plans/2026-04-08-narcissus-structure-plan.md
git commit -m "refactor: add main entry point to narcissus script"
```

### Task 2: Re-run the black-box behavior checks

**Files:**
- Modify: `tests/test_narcissus_script.py`
- Modify: `5.py`

**Step 1: Keep the existing subprocess tests unchanged**

```python
def test_153_is_narcissus_number(self) -> None:
    completed = run_script("153\n")
    self.assertEqual(completed.stdout.strip(), "是水仙花数")
```

**Step 2: Run the full test file**

Run: `python -m unittest discover -s tests -p "test_narcissus_script.py" -v`
Expected: PASS with both the new import-safe test and the existing subprocess behavior tests.

**Step 3: Commit**

```bash
git add 5.py tests/test_narcissus_script.py
git commit -m "test: verify import-safe narcissus script structure"
```
