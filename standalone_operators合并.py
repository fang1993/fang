
import json
import copy
from copy import deepcopy

dict1=json.load(open('bb.json',encoding='utf-8'))
# print(dict1)
dict2=json.load(open('bb2.json',encoding='utf-8'))
# print(dict2)



dict3=copy.copy(dict1)
# print(dict2['preprocess']['subcategory']['1111'])
# dict3["model"]["subcategory"]["default"]["operators"].append(dict2["model"]["subcategory"]["default"]["operators"][1])

# 模型管理
dict3["model"]["subcategory"]["default"]["operators"].append({
                        "name": "ModelExportPMMLFile",
                        "description": "模型导出-PMML文件",
                        "ports": {},
                        "params": {}
                    })

# 样本数据
dict3["sample_data"]["subcategory"]["sampledatacommon"]={
                "index": 1,
                "description": "通用",
                "operators":[

                ]
            }
dict3["sample_data"]["subcategory"]["sampledataenergy"]={
                "index": 2,
                "description": "能源",
                "operators": [
                    {
                        "name": "GasWellProductionOp",
                        "description": "气井产量预测",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "GasWellPressureMeasure",
                        "description": "气井压力虚拟计量",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "GasWellSandOp",
                        "description": "气井出砂预测",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "TreeHeightOp",
                        "description": "采油树高度预测",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "FluidChangeOp",
                        "description": "信流体组分的动态变化预测",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "GasWellTemperatureOp",
                        "description": "气井温度分析预测",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "GasPressureRecoverOP",
                        "description": "气藏压力与采收率预测",
                        "ports": {},
                        "params": {}
                    }
                ]
            }

# 特征工程
aa=[{
                        "name": "CharacteristicsDiscrete",
                        "description": "特征离散",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "HotCoding",
                        "description": "独热编码",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "SortCoding",
                        "description": "排序编码",
                        "ports": {},
                        "params": {}
                    }]
dict3["feature_engineering"]["subcategory"]["default"]["operators"].extend(aa)

aa1=[{
                        "name": "Chi-squareFeatureSelection",
                        "description": "卡方特征选择",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "RecursiveFeatureElimination",
                        "description": "递归特征消除",
                        "ports": {},
                        "params": {}
                    }]

dict3["feature_engineering"]["subcategory"]["feature_importance"]["operators"].extend(aa1)


dict3["feature_engineering"]["subcategory"]["characteristic_derivative"]={
                "index": 3,
                "description": "特征衍生",
                "operators": [
                    {
                        "name": "WindowStatistical",
                        "description": "时间窗口统计",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "CrossoverOperation",
                        "description": "交叉运算",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "LongTOWide",
                        "description": "长表转宽表",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "FeatureCartesian",
                        "description": "特征组合-笛卡尔积",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "FeatureTree",
                        "description": "特征组合-决策树",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "FeatureXqboost",
                        "description": "特征组合-Xgboost",
                        "ports": {},
                        "params": {}
                    }
                ]
            }

# 机器学习模型
bb=[{
                        "name": "SVM",
                        "description": "SVM",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "KNN",
                        "description": "KNN",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "NaiveBayes",
                        "description": "朴素贝叶斯",
                        "ports": {},
                        "params": {}
                    }]
dict3["machine_learning_algorithm"]["subcategory"]["classification"]["operators"].extend(bb)

bb0=[{
                        "name": "RidgeRegression",
                        "description": "岭回归",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "lassoRegression",
                        "description": "lasso回归",
                        "ports": {},
                        "params": {}
                    }]
dict3["machine_learning_algorithm"]["subcategory"]["regression"]["operators"].extend(bb0)

bb1=[{
                        "name": "DensityClusteringDBSCAN",
                        "description": "密度聚类（DBSCAN）",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "HierarchicalClustering",
                        "description": "层次聚类（Hierarchical Clustering）",
                        "ports": {},
                        "params": {}
                    }]
dict3["machine_learning_algorithm"]["subcategory"]["cluster"]["operators"].extend(bb1)

bb2=[{
                        "name": "LRClassification",
                        "description": "LR多分类",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "RFClassification",
                        "description": "RF多分类",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "xgboostClassification",
                        "description": "xgboost多分类",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "SVNClassification",
                        "description": "SVM多分类",
                        "ports": {},
                        "params": {}
                    }]
dict3["machine_learning_algorithm"]["subcategory"]["muticlassification"]["operators"].extend(bb2)

dict3["machine_learning_algorithm"]["subcategory"]["CorrelationAnalysis"]={
                "index": 4,
                "description": "关联分析",
                "operators": [
                    {
                        "name": "apriori",
                        "description": "apriori",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "FP-tree",
                        "description": "FP-tree",
                        "ports": {},
                        "params": {}
                    }
                ]
            }
dict3["machine_learning_algorithm"]["subcategory"]["TimeSeriesAnalysis"]={
                "index": 6,
                "description": "时间序列分析",
                "operators": [
                    {
                        "name": "VectorAutoregression",
                        "description": "向量自回归",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "ExponentialSmoothing",
                        "description": "指数平滑",
                        "ports": {},
                        "params": {}
                    }
                ]
            }
dict3["machine_learning_algorithm"]["subcategory"]["DeepLearning"]={
                "index": 7,
                "description": "深度学习",
                "operators": [
                    {
                        "name": "tensorflow",
                        "description": "tensorflow",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "pytorch",
                        "description": "pytorch",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "caffe",
                        "description": "caffe",
                        "ports": {},
                        "params": {}
                    }
                ]
            }

# 数据IO
dict3["dataio"]["subcategory"]["default"]["operators"].append({
                        "name": "PredictDataSaveOp",
                        "description": "数据保存",
                        "ports": {
                            "in": {},
                            "out": {
                                "outp": {
                                    "type": "DataFrame"
                                }
                            }
                        },
                        "params": {
                            "path": {
                                "name": "path",
                                "docstring": "输入csv文件路径",
                                "tips": "",
                                "hint": "",
                                "required": true,
                                "default": "",
                                "type": "Unicode",
                                "conditions": {
                                    "enum": null
                                },
                                "theme": "TextBox",
                                "combination_struct": null
                            }
                        }
                    })

# 预处理
dict3["preprocess"]["subcategory"]["statisticalanalysis"]={
                "index": 3,
                "description": "统计分析",
                "operators": [
                    {
                        "name": "StatisticalDescription",
                        "description": "统计描述",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "ExperienceDensity ",
                        "description": "经验概率密度图",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "CoefficientMatrix",
                        "description": "相关系数矩阵",
                        "ports": {},
                        "params": {}
                    },
                    {
                        "name": "HypothesisTesting",
                        "description": "假设检验",
                        "ports": {},
                        "params": {}
                    }
                ]
            }

dict3=json.dumps(dict3,ensure_ascii=False,sort_keys=False, indent=4, separators=(',', ': '))

with open('bb3.json','w',encoding='utf-8') as f:
    f.write(dict3)

