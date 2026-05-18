import pytest
import pandas as pd
import joblib
import os

def test_data_exists():
    """测试数据文件是否存在"""
    assert os.path.exists("winequality-red.csv"), "CSV文件不存在"

def test_model_exists():
    """测试模型文件是否存在"""
    assert os.path.exists("model.pkl"), "模型文件不存在"

def test_model_can_load():
    """测试模型能否正常加载"""
    model = joblib.load("model.pkl")
    assert model is not None

def test_data_has_12_columns():
    """测试数据是否有12列（11特征+1目标）"""
    df = pd.read_csv("winequality-red.csv")
    assert df.shape[1] == 12

def test_quality_column_exists():
    """测试是否有quality列"""
    df = pd.read_csv("winequality-red.csv")
    assert "quality" in df.columns