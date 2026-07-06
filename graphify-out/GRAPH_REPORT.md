# Graph Report - .  (2026-07-06)

## Corpus Check
- Corpus is ~19,658 words - fits in a single context window. You may not need a graph.

## Summary
- 67 nodes · 113 edges · 10 communities (6 shown, 4 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_React Component Management|React Component Management]]
- [[_COMMUNITY_DOM Template Parsing|DOM Template Parsing]]
- [[_COMMUNITY_Runtime Engine Initialization|Runtime Engine Initialization]]
- [[_COMMUNITY_Document Bootstrapping and Decoding|Document Bootstrapping and Decoding]]
- [[_COMMUNITY_Asset Bundler Toolchain|Asset Bundler Toolchain]]
- [[_COMMUNITY_Path Resolution and Script Loading|Path Resolution and Script Loading]]
- [[_COMMUNITY_CSS Style Transformation|CSS Style Transformation]]
- [[_COMMUNITY_Template Compilation|Template Compilation]]
- [[_COMMUNITY_Type Verification Utilities|Type Verification Utilities]]
- [[_COMMUNITY_Web Presentation Layer|Web Presentation Layer]]

## God Nodes (most connected - your core abstractions)
1. `walkChildren()` - 7 edges
2. `walk()` - 7 edges
3. `createRuntime()` - 7 edges
4. `compileAttr()` - 6 edges
5. `collectProps()` - 6 edges
6. `boot()` - 5 edges
7. `resolve()` - 5 edges
8. `walkComponent()` - 5 edges
9. `walkXImport()` - 5 edges
10. `walkElement()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Unpack Script (unpack.py)` --conceptually_related_to--> `Asset Bundler System`  [INFERRED]
  unpack.py → pack.py

## Communities (10 total, 4 thin omitted)

### Community 1 - "DOM Template Parsing"
Cohesion: 0.36
Nodes (11): collectProps(), compileAttr(), contentKey(), walk(), walkChildren(), walkComponent(), walkElement(), walkFor() (+3 more)

### Community 2 - "Runtime Engine Initialization"
Cohesion: 0.20
Nodes (10): createComponentFactory(), createExternalModules(), createHelmetManager(), createPseudoSheet(), createRegistry(), createRuntime(), createStreamTracker(), evalDcLogic() (+2 more)

### Community 3 - "Document Bootstrapping and Decoding"
Cohesion: 0.25
Nodes (8): boot(), dcNameFromPath(), getReactDOM(), parseDataProps(), parseDcDocument(), parseDcText(), rootNameForDocument(), safeDecode()

### Community 4 - "Asset Bundler Toolchain"
Cohesion: 0.29
Nodes (3): Asset Bundler System, Pack Script (pack.py), Unpack Script (unpack.py)

### Community 5 - "Path Resolution and Script Loading"
Cohesion: 0.33
Nodes (6): findTopLevelEquality(), loadReactUmd(), loadScript(), parensWrapWhole(), resolve(), resolvePath()

### Community 6 - "CSS Style Transformation"
Cohesion: 0.67
Nodes (3): cssToObj(), hostPositionStyle(), kebabToCamel()

## Knowledge Gaps
- **3 isolated node(s):** `src/index.html`, `React Component Architecture`, `Mateo Trans & Cars Web Application`
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `src/index.html`, `React Component Architecture`, `Mateo Trans & Cars Web Application` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `React Component Management` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._