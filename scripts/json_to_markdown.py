#!/usr/bin/env python3
"""Convert extracted PPT JSON to markdown for RAG ingestion"""
import json
import os
from pathlib import Path

def json_to_markdown(json_path: str) -> str:
    """Convert PPT JSON to structured markdown"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    source = data.get('source_file', Path(json_path).stem)
    total_slides = data.get('total_slides', 0)

    lines = [
        f"# {source}",
        f"**Total Slides:** {total_slides}",
        "",
    ]

    for slide in data.get('slides', []):
        slide_num = slide.get('slide_number', 0)
        title = slide.get('title', '').strip()
        body = slide.get('body_text', [])
        tables = slide.get('tables', [])

        # Skip empty slides
        if not title and not body and not tables:
            continue

        lines.append(f"## Slide {slide_num}")
        if title:
            lines.append(f"### {title}")

        # Body text
        for text in body:
            if text.strip():
                lines.append(text.strip())

        # Tables - convert to markdown tables with context
        for tbl_idx, table in enumerate(tables):
            rows = table.get('data', [])
            if not rows:
                continue

            lines.append("")
            lines.append(f"**Table {tbl_idx + 1}:**")

            # Header row
            if rows:
                header = rows[0]
                lines.append("| " + " | ".join(str(c).replace('\n', ' ').replace('|', '/') for c in header) + " |")
                lines.append("| " + " | ".join("---" for _ in header) + " |")

                # Data rows
                for row in rows[1:]:
                    lines.append("| " + " | ".join(str(c).replace('\n', ' ').replace('|', '/') for c in row) + " |")

            lines.append("")

        lines.append("")

    return "\n".join(lines)


def main():
    # Paths
    base = Path("/home/guilinzhang/allProjects/mfg-ai-platform")
    json_dir = base / "data" / "extracted"
    output_dir = base / "prototype" / "data" / "ppt_extracted"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all JSON files
    json_files = list(json_dir.glob("*.json"))
    print(f"Found {len(json_files)} JSON files")

    for json_file in json_files:
        if json_file.name == "extraction_summary.json":
            continue

        print(f"Converting: {json_file.name}")
        try:
            md_content = json_to_markdown(str(json_file))

            # Output filename
            out_name = json_file.stem + ".md"
            out_path = output_dir / out_name

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            print(f"  -> {out_path.name}")
        except Exception as e:
            print(f"  Error: {e}")

    print(f"\nDone! Markdown files written to: {output_dir}")


if __name__ == "__main__":
    main()
