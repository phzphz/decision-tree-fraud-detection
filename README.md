# Decision Trees for Fraud Detection

**Coursework · Semester 6 · COMP2611 Artificial Intelligence · CW2 (course-provided scaffold)**

决策树分类课程实现：缺失值过滤、分层划分、剪枝与特征选择。

A scikit-learn coursework implementation covering CSV loading, removal of rows containing a `-99` sentinel, coefficient-of-variation statistics, stratified train/test splitting, decision-tree training, accuracy/recall, tree depth and cost-complexity pruning experiments.

## Run a synthetic demonstration

```bash
python -m pip install -r requirements.txt
python make_demo_data.py
python fraud_detection.py
```

The generator writes an explicitly synthetic 300-row `DT.csv` and refuses to overwrite an existing file. It demonstrates execution only. The original course dataset is excluded. To use a separately obtained permitted dataset, supply numeric feature columns followed by a binary target column; `-99` denotes missing values in this archived implementation.

## Methodological limits

The historical coursework functions select pruning parameters and features using the same test split later used for reporting. That is suitable for tracing the exercise but gives an optimistic model-selection estimate. A serious evaluation should use a separate validation split or cross-validation and a final untouched test set. No original accuracy, recall or grade is claimed here; synthetic results are not real fraud-detection performance.

The task-oriented source and references are preserved. [Publication details](PROVENANCE.md).
