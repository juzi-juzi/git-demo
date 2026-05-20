# Narcissus Program Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a small Python script that reads one integer from stdin and prints whether it is a three-digit narcissus number.

**Architecture:** Keep the program as a single script in `5.py`. Add one black-box test that runs the script in a subprocess, sends stdin, and asserts stdout. Implement only the minimal numeric decomposition logic needed for the required three-digit behavior.

**Tech Stack:** Python standard library, `unittest`, `subprocess`

---

### Task 1: Add the first failing behavior test

**Files:**
- Create: `tests/test_narcissus_script.py`
- Modify: `5.py`

**Step 1: Write the failing test**

```python
def test_153_is_narcissus_number():
    completed = run_script("153\n")
    assert completed.stdout.strip() == "是水仙花数"
```

**Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_narcissus_script -v`
Expected: FAIL because the script currently produces no matching output.

**Step 3: Write minimal implementation**

```python
n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
print("是水仙花数" if 100 <= n <= 999 and a ** 3 + b ** 3 + c ** 3 == n else "不是水仙花数")
```

**Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_narcissus_script -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/test_narcissus_script.py 5.py docs/plans/2026-04-07-narcissus-design.md docs/plans/2026-04-07-narcissus-program.md
git commit -m "feat: add three-digit narcissus number script"
```

### Task 2: Cover the non-narcissus and non-three-digit cases

**Files:**
- Modify: `tests/test_narcissus_script.py`
- Modify: `5.py`

**Step 1: Write failing tests**

```python
def test_123_is_not_narcissus_number():
    completed = run_script("123\n")
    assert completed.stdout.strip() == "不是水仙花数"

def test_non_three_digit_number_is_not_narcissus_number():
    completed = run_script("99\n")
    assert completed.stdout.strip() == "不是水仙花数"
```

**Step 2: Run tests to verify they fail if behavior is missing**

Run: `python -m unittest tests.test_narcissus_script -v`
Expected: the new assertions fail until the script handles both cases correctly.

**Step 3: Write minimal implementation**

```python
if not 100 <= n <= 999:
    print("不是水仙花数")
else:
    ...
```

**Step 4: Run tests to verify they pass**

Run: `python -m unittest tests.test_narcissus_script -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/test_narcissus_script.py 5.py
git commit -m "test: cover non-narcissus cases"
```
