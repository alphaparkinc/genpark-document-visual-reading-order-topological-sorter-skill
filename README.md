# GenPark AI Agent Skill - Visual Reading Order Topological Sorter

Converts multi-column newspaper layouts and asymmetric bounding box geometries into serialized natural reading sequences.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Spatial Bboxes with Coordinates] --> B[Gutter & Margin Segmentation]
    B --> C{Span Across Multiple Columns?}
    C -->|Yes| D[Classify as Header / Banner]
    C -->|No| E[Bucket into Left / Right Column Queues]
    D --> F[Topological Y-Axis Sorter]
    E --> F
    F --> G[Serialized Linear Reading Order Stream]
```

## Features
- **Multi-Column Columnar Disentanglement**: Prevents horizontal cross-column word interleaving errors.
- **Zero Third-Party Dependencies**: Pure Python 3.9+ standard library.
