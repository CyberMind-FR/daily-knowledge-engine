from __future__ import annotations

import base64
import os
from pathlib import Path
from typing import Optional


class ImageGenerationUnavailable(RuntimeError):
    """Raised when OpenAI image generation cannot run in the current environment."""


def generate_image_from_prompt(
    prompt: str,
    output_path: Path,
    *,
    model: str = "gpt-image-1",
    size: str = "1024x1536",
    quality: str = "medium",
    dry_run: bool = False,
) -> Optional[Path]:
    """Generate a final poster image with the OpenAI Images API.

    In dry-run mode, no network call is made. This keeps CI deterministic and safe.
    When dry_run is false, OPENAI_API_KEY must be present in the environment.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if dry_run:
        output_path.with_suffix(".prompt.txt").write_text(prompt, encoding="utf-8")
        return None

    if not os.getenv("OPENAI_API_KEY"):
        raise ImageGenerationUnavailable("OPENAI_API_KEY is missing. Use --image-dry-run in CI or configure a GitHub Actions secret.")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ImageGenerationUnavailable("The openai package is not installed. Run: pip install -e '.[image]' or '.[dev,image]'.") from exc

    client = OpenAI()
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )

    image_b64 = response.data[0].b64_json
    if not image_b64:
        raise ImageGenerationUnavailable("OpenAI response did not contain base64 image data.")

    output_path.write_bytes(base64.b64decode(image_b64))
    return output_path
