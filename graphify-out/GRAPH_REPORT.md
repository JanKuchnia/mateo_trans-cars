# Graph Report - .  (2026-07-06)

## Corpus Check
- Corpus is ~5,740 words - fits in a single context window. You may not need a graph.

## Summary
- 58 nodes · 50 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Astro Content Schema Types|Astro Content Schema Types]]
- [[_COMMUNITY_Project Dependency & Deployment|Project Dependency & Deployment]]
- [[_COMMUNITY_User Interface Pages|User Interface Pages]]
- [[_COMMUNITY_Package Build Scripts|Package Build Scripts]]
- [[_COMMUNITY_Astro Local Settings|Astro Local Settings]]

## God Nodes (most connected - your core abstractions)
1. `scripts` - 4 edges
2. `Deploy to GitHub Pages Workflow` - 4 edges
3. `_variables` - 2 edges
4. `Build Job` - 2 edges
5. `Deploy Job` - 2 edges
6. `dev` - 1 edges
7. `build` - 1 edges
8. `preview` - 1 edges
9. `astro` - 1 edges
10. `RenderResult` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (10 total, 1 thin omitted)

### Community 0 - "Astro Content Schema Types"
Cohesion: 0.07
Nodes (29): AllValuesOf, AnyEntryMap, CollectionEntry, CollectionKey, ContentCollectionKey, ContentConfig, ContentEntryMap, DataCollectionKey (+21 more)

### Community 1 - "Project Dependency & Deployment"
Cohesion: 0.25
Nodes (7): dependencies, astro, name, type, Build Job, Deploy Job, Deploy to GitHub Pages Workflow

### Community 2 - "User Interface Pages"
Cohesion: 0.29
Nodes (6): button, faqs, icon, isOpen, reviews, wrapper

### Community 3 - "Package Build Scripts"
Cohesion: 0.50
Nodes (4): scripts, build, dev, preview

## Knowledge Gaps
- **42 isolated node(s):** `name`, `type`, `dev`, `build`, `preview` (+37 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `scripts` connect `Package Build Scripts` to `Project Dependency & Deployment`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **What connects `name`, `type`, `dev` to the rest of the system?**
  _42 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Astro Content Schema Types` be split into smaller, more focused modules?**
  _Cohesion score 0.06666666666666667 - nodes in this community are weakly interconnected._