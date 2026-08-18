# RouteMem: Graph Memory for Multi-Step Tool Agents

> **一句话闭环**：多步工具调用任务中，语言 Agent 容易重复已经失败的动作。RouteMem 将历史状态、动作和工具结果写入有向图记忆，并用语义相关性与历史 utility 联合检索。构造论文在两个小型基准上报告更高的任务成功率和更少的重复失败。

> **来源边界**：本笔记只使用 `paper-brief.md` 中的合成正文、公式和两张表。该示例没有完整附录、代码或超参数表。  
> **论文类型**：Empirical agent paper

## 0. 论文信息

| 项目 | 内容 |
|---|---|
| Title | RouteMem: Graph Memory for Multi-Step Tool Agents |
| Authors | A. Chen, B. Singh, C. Lee |
| Venue / Status | Synthetic Workshop Example |
| Year | 2026 |
| DOI / arXiv | 未提供 |
| Research Area | Tool-using language agents |
| Paper / Code / Project | 未提供 |
| Source Version | Synthetic paper brief |
| Citation / BibTeX | 未提供 |

## 1. 场景、问题与核心思路

### 1.1 Research Scenario

研究场景是多步工具调用。Agent 需要根据当前 observation 选择工具动作，并利用工具返回结果继续决策。输入是当前 observation \(o_t\) 和已有记忆，输出是动作 \(a_t\) 或终止信号 Finish。（Method）

### 1.2 Problem

ReAct 风格 Agent 在长任务中可能重复执行已经失败的动作。平铺文本记忆能保留历史，但缺少显式的状态转移关系和历史 utility。论文将“如何检索与当前决策有关的成功或失败轨迹”设为核心问题。（Abstract, Method）

### 1.3 Motivation

作者观察到重复失败会浪费有限的交互步数。历史记录需要同时表达“当前状态与过去状态是否相似”和“过去动作是否产生了有用结果”。这两个判断分别对应语义相似度和 utility。（Method, Eq. 1）

### 1.4 Proposed Method

RouteMem 维护一个有向图。每个节点存储状态摘要、动作、工具结果和 utility，相邻决策通过有向边连接。决策时，系统检索分数较高的节点，将其加入 planning context，再生成动作。（Method）

## 2. 关键术语与符号

### 2.1 Key Concepts and Terminology

#### Directed Memory Graph

- **Original term**：directed memory graph
- **Formal definition**：以历史决策节点为顶点、时间相邻关系为有向边的记忆结构。
- **Role in this paper**：保存动作结果和轨迹顺序。
- **Plain-language explanation**：它像一张带方向的操作记录图，能够显示某一步之后发生了什么。
- **Related concepts**：episodic memory、trajectory graph
- **Source anchor**：Method

#### Utility

- **Original term**：utility
- **Formal definition**：节点 \(m_i\) 的历史效用值 \(u_i\)。
- **Role in this paper**：参与检索分数计算，提升成功历史的优先级。
- **Plain-language explanation**：utility 表示这条历史经验过去是否有帮助。
- **Related concepts**：reward、value
- **Source anchor**：Method, Eq. 1

### 2.2 Notation

| Symbol | Meaning | Type / Shape | Pipeline Role | First Use |
|---|---|---|---|---|
| \(o_t\) | 第 \(t\) 步 observation | 未说明 | 形成检索 query | Method |
| \(q_t\) | 当前检索 query | 向量，维度未说明 | 与记忆表示计算相似度 | Method |
| \(m_i\) | 第 \(i\) 个记忆节点 | 结构化记录 | 存储历史状态、动作、结果和 utility | Method |
| \(h_i\) | 记忆节点表示 | 向量，维度未说明 | 语义检索 | Eq. 1 |
| \(u_i\) | 节点 utility | 标量 | 调整检索优先级 | Eq. 1 |
| \(\alpha\) | 两类分数的权重 | 标量 | 平衡相似度与 utility | Eq. 1 |
| \(a_t\) | 第 \(t\) 步动作 | 离散动作或工具调用 | 作用于工具或环境 | Method |
| \(r_t\) | 工具返回结果 | 未说明 | 形成下一步 observation 和新节点 | Method |
| \(R\) | 任务完成奖励 | \(\{0,1\}\) | 更新节点 utility | Method |

### 2.3 Notation Issues

论文摘要没有说明 \(q_t\) 和 \(h_i\) 的编码器、维度和归一化方式。utility 的具体更新公式也未给出。

## 3. 方法与算法流程

### 3.1 Overall Pipeline

```text
当前 observation o_t
   ↓
编码为 query q_t
   ↓
对每个记忆节点计算 retrieval score s_i
   ↓
选取 top-k 节点
   ↓
把节点内容加入 planning context
   ↓
策略生成动作 a_t
   ↓
工具返回 r_t
   ↓
写入新节点并连接有向边
   ↓
Finish 或达到 15 步时终止
```

### 3.2 Training and Inference

#### Training

合成正文没有说明参数训练过程。可以确认的更新只包括任务结束后使用 \(R\in\{0,1\}\) 更新节点 utility。更新公式和参数学习方式均未提供。（Method）

#### Inference

推理阶段重复执行检索、规划、工具调用和写入记忆。系统在 Agent 输出 Finish 或交互达到 15 步时停止。（Method）

### 3.3 Step-by-Step Algorithm

#### Step 1: Query Construction

- **Input**：当前 observation \(o_t\)
- **Operation**：将 observation 编码为 \(q_t\)
- **Output**：检索 query \(q_t\)
- **Purpose**：表示当前决策需求
- **Next consumer**：retrieval score
- **Source anchor**：Method

#### Step 2: Memory Retrieval

- **Input**：\(q_t\)、节点表示 \(h_i\)、utility \(u_i\)
- **Operation**：计算 \(s_i=\alpha\cos(q_t,h_i)+(1-\alpha)u_i\)
- **Output**：每个节点的检索分数
- **Purpose**：同时考虑状态相关性和历史效用
- **Next consumer**：top-\(k\) 选择
- **Source anchor**：Eq. 1

#### Step 3: Context-Augmented Planning

- **Input**：top-\(k\) 记忆节点与当前 observation
- **Operation**：将历史节点加入 planning context，策略生成动作
- **Output**：动作 \(a_t\)
- **Purpose**：利用相关历史调整当前动作
- **Next consumer**：工具或环境
- **Source anchor**：Method

#### Step 4: Memory Update

- **Input**：状态摘要、\(a_t\)、工具结果 \(r_t\)
- **Operation**：创建新节点，并从上一个节点连接有向边
- **Output**：更新后的 memory graph
- **Purpose**：保存当前交互和轨迹顺序
- **Next consumer**：下一步检索
- **Source anchor**：Method

#### Termination and Final Output

Agent 输出 Finish 或达到 15 步时停止。最终输出是任务答案或失败状态。（Method）

### 3.4 Key Modules

#### Retrieval Scorer

检索器接收 \(q_t\)、\(h_i\) 和 \(u_i\)，输出 \(s_i\)。语义相似度选择状态相关的经验，utility 提升历史有效节点的排序。Table 2 中移除 utility 后，ToolBench-Lite 成功率从 61.2 降到 57.8。（Table 2）

#### Directed Graph Memory

图边记录时间相邻关系。移除图边后，成功率从 61.2 降到 58.6。该结果支持轨迹结构对决策有帮助，但没有单独比较其他图结构。（Table 2）

### 3.5 Key Equations

#### Equation 1: Retrieval Score

$$
s_i=\alpha\cos(q_t,h_i)+(1-\alpha)u_i
$$

- **Symbols**：\(s_i\) 是节点分数，\(\cos(q_t,h_i)\) 是语义相似度，\(u_i\) 是 utility，\(\alpha\) 是权重。
- **What it computes**：计算第 \(i\) 个历史节点对当前决策的优先级。
- **Why it is needed**：单独使用语义相似度无法表达历史动作是否有效。
- **Pipeline position**：query 构造之后，top-\(k\) 选择之前。
- **Plain-language intuition**：一个节点更接近当前状态，同时过去更有用，它会获得更高排序。
- **Assumptions / Constraints**：正文没有说明 \(u_i\) 的范围。两项量纲是否一致也未说明。
- **Source anchor**：Eq. 1

### 3.6 Complexity and Resource Cost

若 memory graph 含 \(N\) 个节点，直接计算全部检索分数需要 \(N\) 次相似度计算。合成正文没有给出近似检索、缓存和内存上限。实验报告运行时间增加 7%。（Experiments）

## 4. 构造实例：完整走一遍算法

> **说明**：以下数值为构造数据，只用于解释算法流程，不属于论文实验结果。

### 4.1 Input

当前任务是“查询某商品库存，然后提交可购买商品”。Agent 在第 4 步收到 observation：“商品 A 缺货，商品 B 状态未知”。

记忆中有两个节点：

- \(m_1\)：曾再次查询商品 A，工具返回缺货，\(u_1=0.1\)
- \(m_2\)：曾查询替代商品 B，工具返回有货，\(u_2=0.9\)

设 \(\alpha=0.6\)，语义相似度分别为 0.9 和 0.7。

### 4.2 Execution Trace

#### Step 1

系统形成 query \(q_t\)，表达“当前需要避开缺货商品并查询替代商品”。

#### Step 2

\[
s_1=0.6\times0.9+0.4\times0.1=0.58
\]

\[
s_2=0.6\times0.7+0.4\times0.9=0.78
\]

\(m_2\) 的状态相似度较低，utility 更高，因此最终分数更高。

#### Step 3

系统将 \(m_2\) 加入 planning context。策略生成动作“查询商品 B 库存”，记为 \(a_t\)。

#### Step 4

工具返回“商品 B 有货”，记为 \(r_t\)。系统创建新节点，保存当前状态、动作和结果，并从前一个节点连接到新节点。

#### Final Step

Agent 提交商品 B 并输出 Finish。该例覆盖 query、检索、规划、工具反馈、记忆写入和终止。

### 4.3 Closure Check

每个中间结果都被后续步骤使用。流程覆盖初始化输入、分数计算、动作决策、环境反馈、记忆更新和停止条件。

## 5. 实验设置与结果

### 5.1 Experimental Questions

- **RQ1**：RouteMem 是否提高多步工具任务成功率？
- **RQ2**：utility score 是否有效？
- **RQ3**：有向图边是否有效？
- **RQ4**：性能收益带来多少运行开销？

### 5.2 Experimental Setup

| Item | Setting |
|---|---|
| Dataset / Environment | ToolBench-Lite 500 tasks；WebShop-Mini 300 tasks |
| Task | 多步工具调用 |
| Protocol / Split | 未说明 |
| Information Access / Leakage Risk | 未说明；无法判断是否使用跨任务记忆 |
| Baselines | ReAct；ReAct with flat text memory |
| Metrics | task success rate；repeated-failure count |
| Backbone / Model | 所有方法使用相同语言模型 |
| Training Setting | 未说明 |
| Inference Setting | 最多 15 步 |
| Hyperparameters | \(\alpha\)、\(k\) 未给出 |
| Seeds / Runs | 3 seeds |
| Compute | 未说明 |

### 5.3 Main Experiments

#### Experiment 1: Task Success

- **Question**：RouteMem 是否提高任务成功率？
- **Setup**：在 ToolBench-Lite 和 WebShop-Mini 上比较 ReAct、Flat Memory 和 RouteMem。
- **Comparison**：所有方法使用相同 backbone。
- **Fairness / Confounders**：记忆容量和 prompt 是否匹配未说明。
- **Reported result**：ToolBench-Lite 上为 61.2，对比 ReAct 的 52.0；WebShop-Mini 上为 55.0，对比 ReAct 的 46.7。
- **Interpretation**：两个基准的平均成功率均更高。论文没有报告方差或统计检验。
- **Supported claim**：RouteMem 在给定基准和 backbone 下提高成功率。
- **Source anchor**：Table 1

#### Experiment 2: Repeated Failures and Runtime

- **Question**：方法是否减少重复失败，代价是多少？
- **Reported result**：重复失败动作减少 18%，运行时间增加 7%。
- **Interpretation**：结果符合记忆检索的设计目标。正文没有给出绝对计数和硬件设置。
- **Supported claim**：RouteMem 减少重复失败，同时引入额外开销。
- **Source anchor**：Experiments

### 5.4 Ablation and Analysis

移除 utility score 后，ToolBench-Lite 成功率为 57.8。移除 graph edges 后为 58.6。两项结果都低于完整方法的 61.2。（Table 2）

消融只覆盖一个数据集。正文没有给出 \(\alpha\)、\(k\)、记忆规模和步数上限的敏感性分析。

### 5.5 Efficiency and Reproducibility

论文报告运行时间增加 7%，没有给出硬件、绝对延迟、token 数、参数量或内存占用。代码和数据链接未提供。

## 6. Claim-Evidence Map

| Claim | Evidence | Reported Result | Support | Anchor |
|---|---|---|---|---|
| RouteMem 提高任务成功率 | 两个基准的主表 | 61.2 vs 52.0；55.0 vs 46.7 | Partial | Table 1 |
| utility score 有效 | 移除 utility 的消融 | 61.2 降到 57.8 | Partial | Table 2 |
| graph edges 有效 | 移除边的消融 | 61.2 降到 58.6 | Partial | Table 2 |
| 方法减少重复失败 | repeated-failure 统计 | 减少 18% | Weak | Experiments |
| 运行开销可控 | runtime 统计 | 增加 7% | Weak | Experiments |

## 7. 贡献、优势与边界

### 7.1 Authors' Claimed Contributions

1. 提出面向工具 Agent 的有向图记忆。
2. 将语义相似度与历史 utility 联合用于检索。
3. 在两个合成基准上报告成功率提升和重复失败下降。

### 7.2 Concrete Technical Contributions

1. 将单步记忆节点组织为带方向的轨迹结构。
2. 用一个可解释的加权分数融合状态相关性与历史效用。
3. 通过两项组件消融验证 utility 和图边的作用。

### 7.3 Strengths

方法流程清楚，memory retrieval 与在线写入形成闭环。主实验保持相同 backbone，减少了模型规模差异带来的混杂。两项消融直接对应核心组件。

### 7.4 Limitations

#### Author-Stated Limitations

合成正文明确说明没有跨模型评价。

#### Research Interpretation

实验规模较小，协议和数据划分未说明。结果没有方差、置信区间或统计检验。utility 更新公式、检索超参数和内存管理策略缺失。

### 7.5 Failure Cases and Generalization Boundary

方法依赖历史中存在可迁移经验。新任务或持续分布变化可能降低检索质量。记忆规模增长会增加检索和存储成本。当前证据只覆盖两个小型任务集和一个 backbone。

## 8. 研究脉络与可迁移启发

### 8.1 Relationship with Existing Work

```text
ReAct
   ↓ 加入 flat memory
ReAct with flat text memory
   ↓ 加入有向轨迹结构与 utility-aware retrieval
RouteMem
   ↓ 仍需验证
跨模型、长时记忆和大规模任务
```

### 8.2 Transferable Research Insights

- **Paper stated**：将语义相关性和历史效用组合成检索分数。
- **Research interpretation**：对 Agent memory 的评价可以同时观察最终成功率、重复失败和运行开销。
- **Research interpretation**：图结构组件需要与等容量的非图记忆进行受控比较。
- **Research interpretation**：utility 更新和 memory pruning 会直接影响长期部署。

## 9. 歧义与待核实点

- \(q_t\) 和 \(h_i\) 的编码器与维度。
- \(\alpha\) 和 \(k\) 的具体取值。
- utility 更新公式。
- 数据划分和三次运行的统计方式。
- repeated-failure count 的定义。
- runtime 的硬件和绝对数值。
- 图边在检索时的具体使用方式。
