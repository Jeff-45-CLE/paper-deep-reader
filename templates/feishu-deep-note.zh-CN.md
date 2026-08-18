# [论文标题]

> **一句话闭环**：[研究场景] 中存在 [具体问题]。作者提出 [方法名]，通过 [核心机制] 解决该问题，并在 [主要实验] 上取得 [量化结果或结论]。

> **来源边界**：已阅读 [正文/附录/补充材料/代码]；未覆盖 [缺失内容]。  
> **论文类型**：[Empirical / Theoretical / Systems / Survey / Position]

## 0. 论文信息

| 项目 | 内容 |
|---|---|
| Title | |
| Authors | |
| Venue / Status | |
| Year | |
| DOI / arXiv | |
| Research Area | |
| Paper / Code / Project | |
| Source Version | |
| Citation / BibTeX | |

## 1. 场景、问题与核心思路

### 1.1 Research Scenario

- 研究场景：
- 实际任务：
- 输入：
- 输出：
- 约束或假设：
- 证据位置：

### 1.2 Problem

- 现有路线：
- 具体限制：
- 作者希望解决的问题：
- 问题边界：
- 证据位置：

### 1.3 Motivation

- 作者观察：
- 观察如何导向方法设计：
- 仍未被直接证明的假设：
- 证据位置：

### 1.4 Proposed Method

- 方法名称：
- 核心思想：
- 与直接前序方法的差异：
- 预期作用：
- 证据位置：

## 2. 关键术语与符号

### 2.1 Key Concepts and Terminology

#### [Term 1]

- **Original term**：
- **Formal definition**：
- **Role in this paper**：
- **Plain-language explanation**：
- **Related concepts**：
- **Source anchor**：

#### [Term 2]

- **Original term**：
- **Formal definition**：
- **Role in this paper**：
- **Plain-language explanation**：
- **Related concepts**：
- **Source anchor**：

### 2.2 Notation

| Symbol | Meaning | Type / Shape | Pipeline Role | First Use |
|---|---|---|---|---|
| | | | | |

### 2.3 Notation Issues

- 符号复用：
- 定义不一致：
- 论文未说明的维度：
- 需要保留的原始缩写：

## 3. 方法与算法流程

### 3.1 Overall Pipeline

```text
[Input]
   ↓
[Initialization / Preprocessing]
   ↓
[Module or Step 1]
   ↓
[Intermediate State]
   ↓
[Module or Step 2]
   ↓
[Decision / Prediction / Generation]
   ↓
[Output]
```

### 3.2 Training and Inference

#### Training

```text
Training data → Objective → Parameter update → Trained model
```

- 训练输入：
- 监督信号或目标：
- 参数更新：
- 训练输出：
- 终止条件：

#### Inference

```text
Test input → Trained components → Inference rule → Final output
```

- 推理输入：
- 推理步骤：
- 推理输出：
- 是否访问标签、未来数据或外部工具：

### 3.3 Step-by-Step Algorithm

#### Step 1: [名称]

- **Input**：
- **Operation**：
- **Output**：
- **Purpose**：
- **Next consumer**：
- **Source anchor**：

#### Step 2: [名称]

- **Input**：
- **Operation**：
- **Output**：
- **Purpose**：
- **Next consumer**：
- **Source anchor**：

#### Termination and Final Output

- 停止条件：
- 最终输出：
- 输出如何用于任务评价：

### 3.4 Key Modules

#### [Module 1]

- 功能：
- 输入与输出：
- 内部机制：
- 存在原因：
- 与其他模块的关系：
- 可替换部分：
- 证据位置：

### 3.5 Key Equations

#### Equation 1: [作用]

$$
[Original equation]
$$

- **Symbols**：
- **What it computes**：
- **Why it is needed**：
- **Pipeline position**：
- **Plain-language intuition**：
- **Assumptions / Constraints**：
- **Source anchor**：

### 3.6 Complexity and Resource Cost

- 时间复杂度：
- 空间复杂度：
- 训练成本：
- 推理成本：
- 论文未报告的部分：

## 4. 构造实例：完整走一遍算法

> **说明**：以下数值为构造数据，只用于解释算法流程，不属于论文实验结果。

### 4.1 Input

- 输入样本：
- 初始状态：
- 参数：

### 4.2 Execution Trace

#### Step 1

- 计算：
- 中间结果：
- 含义：

#### Step 2

- 计算：
- 中间结果：
- 含义：

#### Final Step

- 最终输出：
- 输出解释：
- 与任务目标的关系：

### 4.3 Closure Check

- 每个中间结果是否被后续步骤使用：
- 是否覆盖初始化、更新和停止：
- 是否与论文算法顺序一致：

## 5. 实验设置与结果

### 5.1 Experimental Questions

- **RQ1**：
- **RQ2**：
- **RQ3**：

### 5.2 Experimental Setup

| Item | Setting |
|---|---|
| Dataset / Environment | |
| Task | |
| Protocol / Split | |
| Information Access / Leakage Risk | |
| Baselines | |
| Metrics | |
| Backbone / Model | |
| Training Setting | |
| Inference Setting | |
| Hyperparameters | |
| Seeds / Runs | |
| Compute | |

### 5.3 Main Experiments

#### Experiment 1: [名称]

- **Question**：
- **Setup**：
- **Comparison**：
- **Fairness / Confounders**：
- **Reported result**：
- **Interpretation**：
- **Supported claim**：
- **Source anchor**：

### 5.4 Ablation and Analysis

#### Ablation 1: [模块或因素]

- 删除或改变了什么：
- 结果：
- 说明：
- 是否存在混杂因素：
- 证据位置：

#### Additional Analysis

- 参数敏感性：
- 可视化：
- Case study：
- Error analysis：
- Statistical test：

### 5.5 Efficiency and Reproducibility

- 参数量：
- FLOPs：
- 训练时间：
- 推理延迟：
- 显存或内存：
- 代码与数据：
- 可复现性缺口：

## 6. Claim-Evidence Map

| Claim | Evidence | Reported Result | Support | Anchor |
|---|---|---|---|---|
| | | | Strong / Partial / Weak / Unverified | |

## 7. 贡献、优势与边界

### 7.1 Authors' Claimed Contributions

1.
2.
3.

### 7.2 Concrete Technical Contributions

1.
2.
3.

### 7.3 Strengths

- 方法：
- 实验：
- 表达或工程：

### 7.4 Limitations

#### Author-Stated Limitations

-

#### Research Interpretation

-

### 7.5 Failure Cases and Generalization Boundary

- 已展示的 failure cases：
- 可以从假设推断的风险：
- 未测试的数据分布或任务：
- 实际部署约束：

## 8. 研究脉络与可迁移启发

### 8.1 Relationship with Existing Work

```text
[Prior work]
   ↓ retained / changed
[This paper]
   ↓ enables
[New capability]
   ↓ leaves
[Remaining gap]
```

- 直接前序工作：
- 保留的部分：
- 修改的部分：
- 新增能力：
- 仍未解决的问题：

### 8.2 Transferable Research Insights

- Problem formulation：
- Method design：
- Model or agent architecture：
- Training strategy：
- Loss or objective：
- Experimental protocol：
- Evaluation method：

标注每一点属于 **Paper stated**、**Research interpretation** 或 **External context**。

## 9. 歧义与待核实点

- 论文未说明：
- 公式或符号歧义：
- 实验协议歧义：
- 需要查看代码或补充材料：
- 外部检索才能确认：
