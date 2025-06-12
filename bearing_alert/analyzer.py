import pandas as pd

def classify_alert_level(ratio, threshold_normal, threshold_level3, threshold_level2):
    if ratio < threshold_normal:
        return '正常'
    elif ratio < threshold_level3:
        return '三级预警'
    elif ratio < threshold_level2:
        return '二级预警'
    else:
        return '一级预警'

def analyze_bearing_data(input_file, base_force, thresholds):
    df = pd.read_csv(input_file, header=1, encoding='utf-8-sig')
    if df.shape[1] < 2:
        raise ValueError("CSV文件格式错误，至少包含两列（时间戳、支座反力）")

    df.columns = ['Timestamp', 'BearingForce']
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['BearingForce'] = pd.to_numeric(df['BearingForce'], errors='coerce')
    df = df.dropna(subset=['BearingForce'])

    df['DecreaseRatio'] = (base_force - df['BearingForce']) / base_force
    df['AlertLevel'] = df['DecreaseRatio'].apply(
        lambda r: classify_alert_level(r, thresholds['normal'], thresholds['level3'], thresholds['level2'])
    )
    return df
