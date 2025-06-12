from bearing_alert import analyze_bearing_data, print_alert_statistics, visualize_alerts

def main():
    input_file = 'datasets/bearing_data.csv'
    base_force = 1000  # kN
    thresholds = {
        'normal': 0.05,
        'level3': 0.10,
        'level2': 0.15
    }

    df = analyze_bearing_data(input_file, base_force, thresholds)
    print_alert_statistics(df)
    visualize_alerts(df, base_force, thresholds)

if __name__ == '__main__':
    main()
