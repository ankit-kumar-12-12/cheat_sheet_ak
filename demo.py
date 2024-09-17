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



