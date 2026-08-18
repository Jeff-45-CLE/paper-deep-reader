# Synthetic Paper Brief

This file describes a fictional paper created only to demonstrate the skill.

## Metadata

- Title: RouteMem: Graph Memory for Multi-Step Tool Agents
- Authors: A. Chen, B. Singh, C. Lee
- Venue: Synthetic Workshop Example
- Year: 2026
- Type: Empirical agent paper

## Abstract

Tool-using language agents often repeat failed actions during long tasks. RouteMem stores past action outcomes in a directed memory graph. At each decision step, the agent retrieves relevant memory nodes, scores them by semantic similarity and historical utility, and revises its next action. Experiments on ToolBench-Lite and WebShop-Mini report higher task success and fewer repeated failures than a ReAct-style baseline.

## Method

The agent observes state \(o_t\) and forms query \(q_t\). Each memory node \(m_i\) stores a state summary, action, tool result, and utility \(u_i\). Retrieval uses:

\[
s_i = \alpha \cos(q_t, h_i) + (1-\alpha)u_i.
\]

The top \(k\) nodes are added to the planning context. The policy generates action \(a_t\), receives tool result \(r_t\), and adds a new node. A directed edge links the previous node to the new node. Utility is updated after task completion using success reward \(R \in \{0,1\}\).

The loop stops when the agent emits Finish or reaches 15 steps.

## Experiments

- ToolBench-Lite: 500 tasks.
- WebShop-Mini: 300 tasks.
- Baselines: ReAct, ReAct with flat text memory.
- Backbone: same language model for all methods.
- Metric: task success rate and repeated-failure count.
- Three random seeds.

### Table 1

| Method | ToolBench-Lite Success | WebShop-Mini Success |
|---|---:|---:|
| ReAct | 52.0 | 46.7 |
| Flat Memory | 56.4 | 49.3 |
| RouteMem | 61.2 | 55.0 |

### Table 2

| Variant | ToolBench-Lite Success |
|---|---:|
| RouteMem | 61.2 |
| Without utility score | 57.8 |
| Without graph edges | 58.6 |

The paper reports 18% fewer repeated failed actions than ReAct. Runtime increases by 7%. No cross-model evaluation is included.
