import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams['font.family'] = ['SimSun', 'Times New Roman']

def visualize_alerts(df, base_force, thresholds):
    plt.figure(figsize=(12, 6))

    # 画基准线和预警线
    plt.axhline(y=base_force, color='black', linestyle='--', label='基准反力')
    level3 = base_force * (1 - thresholds['normal'])
    level2 = base_force * (1 - thresholds['level3'])
    level1 = base_force * (1 - thresholds['level2'])

    plt.axhline(y=level3, color='blue', linestyle='-', label='三级预警线')
    plt.axhline(y=level2, color='orange', linestyle='-', label='二级预警线')
    plt.axhline(y=level1, color='red', linestyle='-', label='一级预警线')

    # 所有数据点及预警点
    plt.plot(df['Timestamp'], df['BearingForce'], color='black', linewidth=1, alpha=0.3)

    color_map = {'三级预警': 'blue', '二级预警': 'orange', '一级预警': 'red'}
    for level, color in color_map.items():
        points = df[df['AlertLevel'] == level]
        plt.scatter(points['Timestamp'], points['BearingForce'], color=color, marker='*', s=80, label=f'{level}点')

    plt.title('支座脱空预警', fontsize=14)
    plt.xlabel('时间', fontsize=14)
    plt.ylabel('支座反力 (kN)', fontsize=14)
    plt.xticks(rotation=45, fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n%H:%M'))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper right', fontsize=10)
    plt.tight_layout()
    plt.show()
