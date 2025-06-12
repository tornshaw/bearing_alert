def print_alert_statistics(df):
    try:
        from tabulate import tabulate
    except ImportError:
        print("\n未安装 tabulate 库，使用普通格式打印。")
        tabulate = None

    print("\n===== 各级预警统计信息 =====")
    for level in ['三级预警', '二级预警', '一级预警']:
        subset = df[df['AlertLevel'] == level]
        if not subset.empty:
            print(f"\n【{level}】 (数量: {len(subset)})")
            if tabulate:
                rows = [[row['Timestamp'].strftime('%Y-%m-%d %H:%M'), row['BearingForce']] for _, row in subset.iterrows()]
                print(tabulate(rows, headers=['时间点', '支座反力 (kN)'], tablefmt='pretty'))
            else:
                for _, row in subset.iterrows():
                    print(f"时间点：{row['Timestamp'].strftime('%Y-%m-%d %H:%M')}, 反力：{row['BearingForce']}")
