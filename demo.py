import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample DataFrame creation for demonstration (replace this with your actual data loading step)
data = {
    'Months': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23', 'Sep-23', 'Oct-23', 
               'Nov-23', 'Dec-23', 'Jan-24', 'Feb-24', 'Mar-24', 'Apr-24', 'May-24', 'Jun-24', 'Jul-24', 'Aug-24', 
               'Sep-24', 'Oct-24', 'Nov-24'],
    'File Timings': ['7:40:00 AM', '7:13:00 AM', '7:57:00 AM', '7:09:00 AM', '7:00:00 AM', '7:01:00 AM', '7:13:00 AM', 
                     '7:01:00 AM', '7:13:00 AM', '7:40:00 AM', '7:13:00 AM', '7:57:00 AM', '7:09:00 AM', '7:01:00 AM', 
                     '7:13:00 AM', '7:31:00 AM', '7:49:00 AM', '7:13:00 AM', '7:01:00 AM', '7:13:00 AM', '7:31:00 AM', 
                     '7:49:00 AM', '7:13:00 AM'],
    'Expected Time': ['7:30:00 AM'] * 23,
    'File Timings2': ['7:57:00 AM', '7:09:00 AM', '7:13:00 AM', '7:57:00 AM', '7:13:00 AM', '7:31:00 AM', '7:49:00 AM', 
                      '7:13:00 AM', '7:09:00 AM', '7:01:00 AM', '7:13:00 AM', '7:13:00 AM', '7:09:00 AM', '7:01:00 AM', 
                      '7:13:00 AM', '7:09:00 AM', '7:01:00 AM', '7:31:00 AM', '7:49:00 AM', '7:49:00 AM', '7:13:00 AM', 
                      '7:01:00 AM', '7:01:00 AM'],
    'Expected Time2': ['9:30:00 AM'] * 23
}

df = pd.DataFrame(data)

# Convert time strings to datetime objects
df['File Timings'] = pd.to_datetime(df['File Timings'], format='%I:%M:%S %p').dt.time
df['Expected Time'] = pd.to_datetime(df['Expected Time'], format='%I:%M:%S %p').dt.time
df['File Timings2'] = pd.to_datetime(df['File Timings2'], format='%I:%M:%S %p').dt.time
df['Expected Time2'] = pd.to_datetime(df['Expected Time2'], format='%I:%M:%S %p').dt.time

# Convert time to total seconds since midnight for plotting
df['File Timings'] = df['File Timings'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)
df['Expected Time'] = df['Expected Time'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)
df['File Timings2'] = df['File Timings2'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)
df['Expected Time2'] = df['Expected Time2'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)

# Define the y-axis interval (in hours)
interval_hours = 2  # This variable controls the interval of the y-axis

# Create list of times from 5:00 AM to 11:00 AM in seconds since midnight
y_ticks_seconds = [(5 + i * interval_hours) * 3600 for i in range(4)]  # Adjust range as needed
y_tick_labels = ['05:00 AM', '07:00 AM', '09:00 AM', '11:00 AM']  # Corresponding human-readable labels

# Variables to adjust the graph's size
graph_width = 12  # Adjust the width here
graph_height = 8  # Adjust the height here

# Plotting
plt.figure(figsize=(graph_width, graph_height))  # Use variables to set graph size

# Plot the timings and expected times
plt.plot(df['Months'], df['File Timings'], label='File Timings', color='blue')
plt.plot(df['Months'], df['File Timings2'], label='File Timings2', color='green')

# Plot expected times as dotted lines
plt.plot(df['Months'], df['Expected Time'], label='Expected Time', color='blue', linestyle='dotted')
plt.plot(df['Months'], df['Expected Time2'], label='Expected Time2', color='green', linestyle='dotted')

# Formatting
plt.xlabel('Months')
plt.ylabel('Time of Day')
plt.title('File Timings vs Expected Time')

# Set y-axis ticks and labels
plt.yticks(y_ticks_seconds, y_tick_labels)

plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


---------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Sample DataFrame creation for demonstration (replace this with your actual data loading step)
data = {
    'Months': ['Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23', 'Sep-23', 'Oct-23', 
               'Nov-23', 'Dec-23', 'Jan-24', 'Feb-24', 'Mar-24', 'Apr-24', 'May-24', 'Jun-24', 'Jul-24', 'Aug-24', 
               'Sep-24', 'Oct-24', 'Nov-24'],
    'File Timings': ['7:40:00 AM', '7:13:00 AM', '7:57:00 AM', '7:09:00 AM', '7:00:00 AM', '7:01:00 AM', '7:13:00 AM', 
                     '7:01:00 AM', '7:13:00 AM', '7:40:00 AM', '7:13:00 AM', '7:57:00 AM', '7:09:00 AM', '7:01:00 AM', 
                     '7:13:00 AM', '7:31:00 AM', '7:49:00 AM', '7:13:00 AM', '7:01:00 AM', '7:13:00 AM', '7:31:00 AM', 
                     '7:49:00 AM', '7:13:00 AM'],
    'Expected Time': ['7:30:00 AM'] * 23,
    'File Timings2': ['7:57:00 AM', '7:09:00 AM', '7:13:00 AM', '7:57:00 AM', '7:13:00 AM', '7:31:00 AM', '7:49:00 AM', 
                      '7:13:00 AM', '7:09:00 AM', '7:01:00 AM', '7:13:00 AM', '7:13:00 AM', '7:09:00 AM', '7:01:00 AM', 
                      '7:13:00 AM', '7:09:00 AM', '7:01:00 AM', '7:31:00 AM', '7:49:00 AM', '7:49:00 AM', '7:13:00 AM', 
                      '7:01:00 AM', '7:01:00 AM'],
    'Expected Time2': ['9:30:00 AM'] * 23
}

df = pd.DataFrame(data)

# Convert time strings to datetime objects
df['File Timings'] = pd.to_datetime(df['File Timings'], format='%I:%M:%S %p').dt.time
df['Expected Time'] = pd.to_datetime(df['Expected Time'], format='%I:%M:%S %p').dt.time
df['File Timings2'] = pd.to_datetime(df['File Timings2'], format='%I:%M:%S %p').dt.time
df['Expected Time2'] = pd.to_datetime(df['Expected Time2'], format='%I:%M:%S %p').dt.time

# Convert time to total seconds since midnight for plotting
df['File Timings'] = df['File Timings'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)
df['Expected Time'] = df['Expected Time'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)
df['File Timings2'] = df['File Timings2'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)
df['Expected Time2'] = df['Expected Time2'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second)

# Define the start and end time for the y-axis in 'HH:MM' format
start_time = "06:30 AM"
end_time = "09:30 AM"
interval_hours = 0.5  # This variable controls the interval of the y-axis in hours

# Convert start and end times to datetime objects
start_time_dt = datetime.strptime(start_time, '%I:%M %p')
end_time_dt = datetime.strptime(end_time, '%I:%M %p')

# Generate the y-ticks (in seconds since midnight) and corresponding time labels
y_ticks = []
y_tick_labels = []
current_time = start_time_dt

while current_time <= end_time_dt:
    # Convert current time to seconds since midnight
    seconds_since_midnight = current_time.hour * 3600 + current_time.minute * 60
    y_ticks.append(seconds_since_midnight)
    y_tick_labels.append(current_time.strftime('%I:%M %p'))  # Convert time back to 'HH:MM AM/PM' format
    # Increment the current time by the interval
    current_time += timedelta(hours=interval_hours)

# Variables to adjust the graph's size
graph_width = 12  # Adjust the width here
graph_height = 8  # Adjust the height here

# Plotting
plt.figure(figsize=(graph_width, graph_height))  # Use variables to set graph size

# Plot the timings and expected times
plt.plot(df['Months'], df['File Timings'], label='File Timings', color='blue')
plt.plot(df['Months'], df['File Timings2'], label='File Timings2', color='green')

# Plot expected times as dotted lines
plt.plot(df['Months'], df['Expected Time'], label='Expected Time', color='blue', linestyle='dotted')
plt.plot(df['Months'], df['Expected Time2'], label='Expected Time2', color='green', linestyle='dotted')

# Formatting
plt.xlabel('Months')
plt.ylabel('Time of Day')
plt.title('File Timings vs Expected Time')

# Set y-axis ticks and labels
plt.yticks(y_ticks, y_tick_labels)

plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

-----------------------------------------




import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import datetime

# Step 1: Create sample data
data = {
    'Months': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01',
                              '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01',
                              '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01',
                              '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01',
                              '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-01']),
    'Timings': ['06:52:00', '05:31:00', '05:35:00', '06:10:00', '05:45:00', '06:00:00',
                '05:08:00', '04:58:00', '05:20:00', '05:15:00', '05:50:00', '06:05:00',
                '05:30:00', '05:25:00', '05:40:00', '05:35:00', '05:55:00', '05:45:00',
                '05:08:00', '04:58:00']
}

df = pd.DataFrame(data)

# Step 2: Ensure 'Timings' is handled as time
df['Timings'] = pd.to_datetime(df['Timings'], format='%H:%M:%S').dt.time

# Step 3: Convert 'Timings' to seconds from midnight for plotting
df['Timings_in_seconds'] = df['Timings'].apply(lambda t: t.hour * 3600 + t.minute * 60 + t.second)

# Step 4: Set dynamic start time, end time, and interval
start_time = datetime.time(3, 0)  # Dynamic start time
end_time = datetime.time(11, 0)   # Dynamic end time
interval_minutes = 60  # Dynamic interval in minutes (e.g., 60 minutes = 1 hour)

# Convert times to seconds for y-axis limits
start_seconds = start_time.hour * 3600 + start_time.minute * 60
end_seconds = end_time.hour * 3600 + end_time.minute * 60

# Step 5: Create y-ticks dynamically based on the interval
yticks = list(range(start_seconds, end_seconds + 1, interval_minutes * 60))  # Generate ticks every interval
yticklabels = [str(datetime.timedelta(seconds=t))[:-3] for t in yticks]  # Format y-tick labels as HH:MM

# Step 6: Plot the data
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data using 'Months' and 'Timings_in_seconds'
ax.plot(df['Months'], df['Timings_in_seconds'])

# Step 7: Set the y-axis with dynamic limits and intervals
ax.set_ylim([start_seconds, end_seconds])  # Set dynamic y-axis range
ax.set_yticks(yticks)  # Set y-ticks dynamically
ax.set_yticklabels([datetime.time(t // 3600, (t % 3600) // 60).strftime('%I:%M %p') for t in yticks])  # Set y-tick labels dynamically

# Step 8: Customize x-ticks to show months in the format Jan-23, Feb-23, ...
ax.xaxis.set_major_locator(mdates.MonthLocator())  # Set major x-ticks for every month
ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))  # Format x-ticks as Jan-23, Feb-23, etc.

# Rotate x-axis labels to prevent overlapping
plt.xticks(rotation=45)

# Set axis labels and title
plt.xlabel('Month')
plt.ylabel('Time')
plt.title('Months vs Time with Dynamic Y-Axis')

# Step 9: Show the plot
plt.tight_layout()
plt.show()


-----------------------------------------------------------------------------------------------------------------


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import datetime

# Step 1: Create sample data
data = {
    'Months': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01',
                              '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01',
                              '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01',
                              '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01',
                              '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-01']),
    'Timings': ['06:52:00', '05:31:00', '05:35:00', '06:10:00', '05:45:00', '06:00:00',
                '05:08:00', '04:58:00', '05:20:00', '05:15:00', '05:50:00', '06:05:00',
                '05:30:00', '05:25:00', '05:40:00', '05:35:00', '05:55:00', '05:45:00',
                '05:08:00', '04:58:00']
}

df = pd.DataFrame(data)

# Step 2: Ensure 'Timings' is handled as time
df['Timings'] = pd.to_datetime(df['Timings'], format='%H:%M:%S').dt.time

# Step 3: Convert 'Timings' to seconds from midnight for plotting
df['Timings_in_seconds'] = df['Timings'].apply(lambda t: t.hour * 3600 + t.minute * 60 + t.second)

# Step 4: Set dynamic start time, end time, and interval for y-axis
start_time = datetime.time(3, 0)  # Start time
end_time = datetime.time(11, 0)   # End time
interval_minutes = 60  # Interval in minutes

# Convert times to seconds for y-axis limits
start_seconds = start_time.hour * 3600 + start_time.minute * 60
end_seconds = end_time.hour * 3600 + end_time.minute * 60

# Create y-ticks dynamically based on the interval
yticks = list(range(start_seconds, end_seconds + 1, interval_minutes * 60))  # Generate ticks every interval
yticklabels = [datetime.time(t // 3600, (t % 3600) // 60).strftime('%I:%M %p') for t in yticks]  # Format y-tick labels dynamically

# Step 5: Set graph height, width, and x-axis range dynamically
graph_width = 12  # Width of the graph
graph_height = 6  # Height of the graph
start_month = pd.to_datetime('2023-01-01')  # Dynamic start of the x-axis
end_month = pd.to_datetime('2024-08-01')  # Dynamic end of the x-axis
x_tick_interval = 2  # Custom x-tick interval (e.g., every 2 months)

# Step 6: Plot the data
fig, ax = plt.subplots(figsize=(graph_width, graph_height))

# Plot the data using 'Months' and 'Timings_in_seconds'
ax.plot(df['Months'], df['Timings_in_seconds'])

# Set the y-axis with dynamic limits and intervals
ax.set_ylim([start_seconds, end_seconds])  # Set dynamic y-axis range
ax.set_yticks(yticks)  # Set y-ticks dynamically
ax.set_yticklabels([datetime.time(t // 3600, (t % 3600) // 60).strftime('%I:%M %p') for t in yticks])  # Set y-tick labels dynamically

# Step 7: Customize x-ticks with dynamic intervals
ax.set_xlim([start_month, end_month])  # Set dynamic x-axis range
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=x_tick_interval))  # Set custom x-tick interval (every 2 months)
ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))  # Format x-ticks as Jan-23, Feb-23, etc.

# Rotate x-axis labels to prevent overlapping
plt.xticks(rotation=45)

# Set axis labels and title
plt.xlabel('Month')
plt.ylabel('Time')
plt.title(f'Months vs Time (Custom Dimensions: {graph_width}x{graph_height})')

# Step 8: Show the plot
plt.tight_layout()
plt.show()


