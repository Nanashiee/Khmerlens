"""Export result rows in a spreadsheet friendly CSV format."""

import csv
import io


FIELDS = ["position", "text", "type", "definition"]


def _safe_cell(value: str) -> str:
    # Spreadsheet programs can execute formulas in downloaded CSV files.
    return "'" + value if value.lstrip().startswith(("=", "+", "-", "@")) else value


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows({key: _safe_cell(value) for key, value in row.items()} for row in rows)
    return output.getvalue().encode("utf-8-sig")
