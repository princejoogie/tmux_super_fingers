from typing import Optional
from dataclasses import dataclass

class MarkTarget:
    pass

@dataclass
class UrlTarget(MarkTarget):
    url: str

@dataclass
class TextFileTarget(MarkTarget):
    file_path: str
    line_number: Optional[int] = None

@dataclass
class Mark:
    start: int
    end: int
    mark_text: str
    target: Optional[MarkTarget] = None
    hint: Optional[str] = None