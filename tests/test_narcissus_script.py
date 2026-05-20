import importlib.util
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "5.py"


def load_script_module():
    spec = importlib.util.spec_from_file_location("narcissus_script", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def run_script(user_input: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=user_input,
        capture_output=True,
        text=True,
        check=False,
    )


class NarcissusScriptTests(unittest.TestCase):
    def test_module_is_import_safe_and_exposes_main(self) -> None:
        module = load_script_module()
        self.assertTrue(hasattr(module, "main"))
        self.assertTrue(module.is_narcissus_number(153))

    def test_153_is_narcissus_number(self) -> None:
        completed = run_script("153\n")
        self.assertEqual(completed.stdout.strip(), "是水仙花数")

    def test_123_is_not_narcissus_number(self) -> None:
        completed = run_script("123\n")
        self.assertEqual(completed.stdout.strip(), "不是水仙花数")

    def test_99_is_not_narcissus_number(self) -> None:
        completed = run_script("99\n")
        self.assertEqual(completed.stdout.strip(), "不是水仙花数")
