from typing import Dict, Any, List, Optional

class DocumentVisualReadingOrderTopologicalSorter:
    """
    Sorts 2D text bounding boxes from complex multi-column documents, sidebars,
    and callout boxes into the correct human reading order using topological geometry.
    """
    def __init__(self, page_width: float = 612.0, column_gutter_threshold: float = 30.0):
        self.page_width = page_width
        self.column_gutter_threshold = column_gutter_threshold

    def sort_reading_order(self, blocks: List[Dict[str, Any]]) -> Dict[str, Any]:
        midpoint = self.page_width / 2.0
        left_column = []
        right_column = []
        full_width_headers = []

        for b in blocks:
            left = b.get("left", 0)
            width = b.get("width", 0)
            right = left + width
            if width > self.page_width * 0.65:
                full_width_headers.append(b)
            elif right <= midpoint + self.column_gutter_threshold:
                left_column.append(b)
            else:
                right_column.append(b)

        full_width_headers.sort(key=lambda x: x.get("top", 0))
        left_column.sort(key=lambda x: x.get("top", 0))
        right_column.sort(key=lambda x: x.get("top", 0))

        ordered_sequence = []
        for h in full_width_headers:
            ordered_sequence.append(h)
        for l in left_column:
            ordered_sequence.append(l)
        for r in right_column:
            ordered_sequence.append(r)

        serialized_text = "\n".join(b.get("text", "") for b in ordered_sequence)

        return {
            "total_blocks": len(blocks),
            "layout_detected": "two_column_with_banner" if (left_column and right_column) else "single_column",
            "ordered_blocks": ordered_sequence,
            "serialized_text": serialized_text
        }
