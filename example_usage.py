import json
from client import DocumentVisualReadingOrderTopologicalSorter

def main():
    sorter = DocumentVisualReadingOrderTopologicalSorter(page_width=600)
    blocks = [
        {"id": "header", "text": "GLOBAL QUARTERLY REPORT", "top": 20, "left": 50, "width": 500, "height": 30},
        {"id": "col1_para1", "text": "North America recorded 18% growth...", "top": 80, "left": 50, "width": 220, "height": 60},
        {"id": "col2_para1", "text": "Europe operations remained steady...", "top": 80, "left": 320, "width": 220, "height": 60},
        {"id": "col1_para2", "text": "Supply chain friction eased in Q3...", "top": 150, "left": 50, "width": 220, "height": 60}
    ]
    result = sorter.sort_reading_order(blocks)
    print("Topological Reading Order:")
    print(json.dumps(result, indent=2))
    assert result["ordered_blocks"][0]["id"] == "header"
    assert result["ordered_blocks"][1]["id"] == "col1_para1"
    assert result["ordered_blocks"][2]["id"] == "col1_para2"
    assert result["ordered_blocks"][3]["id"] == "col2_para1"
    print("Topological reading order sorter verification: PASS")

if __name__ == "__main__":
    main()
