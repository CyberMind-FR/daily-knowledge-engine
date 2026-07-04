from pathlib import Path

from dke.openai_image import generate_image_from_prompt


def test_image_dry_run_writes_prompt(tmp_path: Path):
    result = generate_image_from_prompt("poster prompt", tmp_path / "poster.png", dry_run=True)
    assert result is None
    assert (tmp_path / "poster.prompt.txt").read_text(encoding="utf-8") == "poster prompt"
