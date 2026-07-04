from __future__ import annotations

from datetime import date
from pathlib import Path

import typer

from dke.sample_data import build_sample_dko
from dke.verify import enforce_publication_rules
from skills.les_cimes import LesCimesSkill

app = typer.Typer(help="Daily Knowledge Engine CLI")


@app.command()
def run(publication: str = "les-cimes", date_: str = typer.Option(None, "--date"), out: Path = Path("dist")) -> None:
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
    typer.echo(f"Generated {out}/les-cimes.md, .html and image prompt")


if __name__ == "__main__":
    app()
