import os
import pandas as pd

# Folder containing temperature CSV files
FOLDER = r".\temperatures"

# Australian seasons
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

#Calculate seasonal averages
def calculate_seasonal_averages(all_data):
    seasonal_totals = {s: [] for s in SEASONS}

    for _, row in all_data.iterrows():
        for season, months in SEASONS.items():
            values = row[months].values
            values = [v for v in values if pd.notna(v)]
            if values:
                seasonal_totals[season].extend(values)

    seasonal_averages = {}
    for season, temps in seasonal_totals.items():
        if temps:
            seasonal_averages[season] = pd.Series(temps).mean()
        else:
            seasonal_averages[season] = None

    with open("average_temp.txt", "w", encoding="utf-8") as f:
        for season, avg in seasonal_averages.items():
            if avg is not None:
                f.write(f"{season}: {avg:.1f}°C\n")
    print("Saved seasonal averages to average_temp.txt")


# Function 2: Largest temperature range per station
def calculate_largest_range(all_data):
    try:
        station_summary = {}

        for _, row in all_data.iterrows():
            station = row["STATION_NAME"]
            temps = row.drop(labels=["STATION_NAME", "STN_ID", "LAT", "LON"]).values
            temps = [v for v in temps if pd.notna(v)]

            if temps:
                
                max_temp = pd.Series(temps).max()
                min_temp = pd.Series(temps).min()
                temp_range = max_temp - min_temp
                station_summary[station] = (max_temp, min_temp, temp_range)

        max_range = max(v[2] for v in station_summary.values())
        largest_range_stations = [s for s, v in station_summary.items() if v[2] == max_range]

        with open("largest_temp_range_station.txt", "w", encoding="utf-8") as f:
            for station in largest_range_stations:
                max_temp, min_temp, temp_range = station_summary[station]
                f.write(f"{station}: Range {temp_range:.1f}°C (Max: {max_temp:.1f}°C, Min: {min_temp:.1f}°C)\n")
        print("Saved largest temp range stations to largest_temp_range_station.txt")
    except Exception as e:
        print(f"Error calculating largest temperature range: {e}")


# Function 3: Temperature stability (using pandas std)
def calculate_temperature_stability(all_data):
    try: 
        station_std = {}

        for _, row in all_data.iterrows():
            station = row["STATION_NAME"]
            temps = row.drop(labels=["STATION_NAME", "STN_ID", "LAT", "LON"]).values
            temps = [v for v in temps if pd.notna(v)]

            if temps:
                series = pd.Series(temps)
                std_dev = series.std(ddof=0)  # population standard deviation
                station_std[station] = std_dev

        min_std = min(station_std.values())
        max_std = max(station_std.values())

        most_stable = [s for s, std in station_std.items() if std == min_std]
        most_variable = [s for s, std in station_std.items() if std == max_std]

        with open("temperature_stability_stations.txt", "w", encoding="utf-8") as f:
            for station in most_stable:
                f.write(f"Most Stable: {station}: StdDev {min_std:.1f}°C\n")
            for station in most_variable:
                f.write(f"Most Variable: {station}: StdDev {max_std:.1f}°C\n")
        print("Saved stability results to temperature_stability_stations.txt")
    except Exception as e:
        print(f"Error calculating temperature stability: {e}")



# Main function
def main():
    all_files = [os.path.join(FOLDER, f) for f in os.listdir(FOLDER) if f.endswith(".csv")]
    if not all_files:
        print("No CSV files found in the folder!")
        return

    all_data = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

    # Run all tasks
    calculate_seasonal_averages(all_data)
    calculate_largest_range(all_data)
    calculate_temperature_stability(all_data)


if __name__ == "__main__":
    main()
