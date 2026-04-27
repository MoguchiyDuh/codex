from __future__ import annotations

import html as html_mod
import re
from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render(self, title: str, body: str) -> str: ...


class FileNamer(ABC):
    @abstractmethod
    def build_filename(self, title: str) -> str: ...


class MetadataFormatter(ABC):
    @abstractmethod
    def format_metadata(self, author: str) -> str: ...


def _slugify(title: str, separator: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"\s+", separator, slug.strip())
    return slug or "untitled"


class HtmlRenderer(Renderer):
    def render(self, title: str, body: str) -> str:
        t = html_mod.escape(title)
        b = html_mod.escape(body)
        return (
            f"<!DOCTYPE html>\n<html>\n<head><title>{t}</title></head>\n"
            f"<body>\n  <h1>{t}</h1>\n  <p>{b}</p>\n</body>\n</html>"
        )


class HtmlFileNamer(FileNamer):
    def build_filename(self, title: str) -> str:
        return f"{_slugify(title, '-')}.html"


class HtmlMetadataFormatter(MetadataFormatter):
    def format_metadata(self, author: str) -> str:
        a = html_mod.escape(author, quote=True)  # quote=True escapes " inside attrs
        return f'<meta name="author" content="{a}">'


class MarkdownRenderer(Renderer):
    def render(self, title: str, body: str) -> str:
        return f"# {title}\n\n{body}"


class MarkdownFileNamer(FileNamer):
    def build_filename(self, title: str) -> str:
        return f"{_slugify(title, '_')}.md"


class MarkdownMetadataFormatter(MetadataFormatter):
    def format_metadata(self, author: str) -> str:
        return f"_Author: {author}_"


class PlainTextRenderer(Renderer):
    def render(self, title: str, body: str) -> str:
        border = "=" * len(title)
        return f"{border}\n{title}\n{border}\n\n{body}"


class TextFileNamer(FileNamer):
    def build_filename(self, title: str) -> str:
        return f"{_slugify(title, '_')}.txt"


class TextMetadataFormatter(MetadataFormatter):
    def format_metadata(self, author: str) -> str:
        return f"Author: {author}"


def create_renderer(format: str) -> Renderer:
    match format:
        case "html":
            return HtmlRenderer()
        case "md":
            return MarkdownRenderer()
        case "txt":
            return PlainTextRenderer()
        case _:
            raise ValueError(f"Unknown format: {format!r}. Expected one of: html, md, txt")


class ExportFactory(ABC):
    @abstractmethod
    def create_renderer(self) -> Renderer: ...

    @abstractmethod
    def create_file_namer(self) -> FileNamer: ...

    @abstractmethod
    def create_metadata_formatter(self) -> MetadataFormatter: ...


class HtmlExportFactory(ExportFactory):
    def create_renderer(self) -> Renderer:
        return HtmlRenderer()

    def create_file_namer(self) -> FileNamer:
        return HtmlFileNamer()

    def create_metadata_formatter(self) -> MetadataFormatter:
        return HtmlMetadataFormatter()


class MarkdownExportFactory(ExportFactory):
    def create_renderer(self) -> Renderer:
        return MarkdownRenderer()

    def create_file_namer(self) -> FileNamer:
        return MarkdownFileNamer()

    def create_metadata_formatter(self) -> MetadataFormatter:
        return MarkdownMetadataFormatter()


class TextExportFactory(ExportFactory):
    def create_renderer(self) -> Renderer:
        return PlainTextRenderer()

    def create_file_namer(self) -> FileNamer:
        return TextFileNamer()

    def create_metadata_formatter(self) -> MetadataFormatter:
        return TextMetadataFormatter()


def export_report(
    factory: ExportFactory,
    title: str,
    body: str,
    author: str,
) -> dict[str, str]:
    return {
        "filename": factory.create_file_namer().build_filename(title),
        "metadata": factory.create_metadata_formatter().format_metadata(author),
        "content": factory.create_renderer().render(title, body),
    }


if __name__ == "__main__":
    TITLE = "Q2 Performance Report"
    BODY = "Revenue grew 18% YoY. Margins held steady despite supply chain headwinds."
    AUTHOR = "Kirill"

    # direct usage
    renderer = create_renderer("md")
    print(renderer.render(TITLE, BODY))

    # wrong format test
    try:
        create_renderer("pdf")
    except ValueError as e:
        print(f"\nExpected error: {e}")

    # using factory
    factories: list[tuple[str, ExportFactory]] = [
        ("HTML", HtmlExportFactory()),
        ("Markdown", MarkdownExportFactory()),
        ("Text", TextExportFactory()),
    ]

    for label, factory in factories:
        print("-" * 50)
        print(label)
        bundle = export_report(factory, TITLE, BODY, AUTHOR)
        print(f"filename : {bundle['filename']}")
        print(f"metadata : {bundle['metadata']}")
        print(f"content  :\n{bundle['content']}")
