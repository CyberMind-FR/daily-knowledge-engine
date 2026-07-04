from __future__ import annotations

from datetime import date
from pathlib import Path

import typer

from dke.openai_image import ImageGenerationUnavailable, generate_image_from_prompt
from dke.sample_data import build_sample_dko
from dke.verify import enforce_publication_rules
from skills.les_cimes import LesCimesSkill

app = typer.Typer(help="Daily Knowledge Engine CLI")


@app.command()
def run(
    publication: str = "les-cimes",
    date_: str = typer.Option(None, "--date"),
    out: Path = Path("dist"),
    image: bool = typer.Option(False, "--image", help="Generate the final poster image with the OpenAI Images API."),
    image_dry_run: bool = typer.Option(False, "--image-dry-run", help="Write the image prompt without calling OpenAI."),
    image_model: str = typer.Option("gpt-image-1", "--image-model"),
    image_size: str = typer.Option("1024x1536", "--image-size"),
    image_quality: str = typer.Option("medium", "--image-quality"),
) -> None:
    publication_date = date.fromisoformat(date_ or date.today().isoformat())
    dko = enforce_publication_rules(build_sample_dko(publication_date))
    out.mkdir(parents=True, exist_ok=True)

    if publication != "les-cimes":
        raise typer.BadParameter("Only 'les-cimes' is implemented in this starter kit.")

    skill = LesCimesSkill()
    md = skill.render_markdown(dko)
    html = skill.render_html(dko)
    prompt = skill.render_image_prompt(dko)

    (out / "les-cimes.md").write_text(md, encoding="utf-8")
    (out / "les-cimes.html").write_text(html, encoding="utf-8")
    (out / "les-cimes-image-prompt.txt").write_text(prompt, encoding="utf-8")

    if image or image_dry_run:
        try:
            generated = generate_image_from_prompt(
                prompt,
                out / "les-cimes-poster.png",
                model=image_model,
                size=image_size,
                quality=image_quality,
                dry_run=image_dry_run,
            )
            if generated:
                typer.echo(f"Generated image: {generated}")
            else:
                typer.echo(f"Image dry-run prompt: {out / 'les-cimes-poster.prompt.txt'}")
        except ImageGenerationUnavailable as exc:
            raise typer.BadParameter(str(exc)) from exc

    typer.echo(f"Generated {out}/les-cimes.md, .html and image prompt")


if __name__ == "__main__":
    app()
