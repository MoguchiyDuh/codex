---
tags: [theory, architecture, pipelining, hazards]
status: stub
---

# Pipelining

> Overlapping instruction execution — while one instruction executes, the next is being decoded.

## The idea

### Assembly line analogy

### Classic 5-stage pipeline: IF → ID → EX → MEM → WB

## Throughput vs latency

### Pipeline improves throughput, not latency of a single instruction

## Hazards — what breaks the pipeline

### Structural hazard — two instructions need the same hardware

### Data hazard — instruction depends on result not yet written

#### RAW (Read After Write) — the most common

#### WAR, WAW

#### Solution: forwarding/bypassing, stalling (bubble insertion)

### Control hazard — branch target not known until execute

#### Branch prediction — static vs dynamic

#### Speculative execution

#### Branch misprediction penalty

## Out-of-order execution

## Superscalar — multiple pipelines in parallel

## See also

- [[CPU Architecture]]
- [[Instruction Set Architecture]]
- [[Memory Hierarchy]]
