import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn as sns
from datetime import timedelta

def impute_missing_values(data, columns):
    data[columns] = data[columns].fillna("UNKNOWN")
    
    return data
    
def convert_date_to_days(data):
    data["date"] = data["date"].apply(pd.to_datetime)
    data['days'] = data["date"].dt.dayofweek
    
    DAYS_CONVERT = {
                0: "Senin",
                1: "Selasa",
                2: "Rabu",
                3: "Kamis",
                4: "Jum'at",
                5: "Sabtu",
                6: "Minggu"
               }
    
    data.replace({"days": DAYS_CONVERT}, inplace=True)
    
    return data
    
    
def get_hours(data):
    data['start_stream'] = pd.to_datetime(data['start_stream']).dt.time
    data["hours"] = pd.to_datetime(data['start_stream'], format='%H:%M:%S').dt.hour
    
    return data
    
def plot_count_days(data, username):
    plt.figure(figsize=(12,9))
    plt.title(f"Hari ketika {username} melakukan Livestream selama 3 bulan")
    ax = sns.countplot(data['days'], alpha=0.8, order = data['days'].value_counts().index)
    ax.bar_label(ax.containers[0])
    plt.show()
    
def plot_avg_days_views(data, var_name, username):
    plt.figure(figsize=(12,9))
    ax = sns.barplot(var_name.index, var_name.values, alpha=0.8)
    ax.bar_label(ax.containers[0])
    plt.xlabel("Days")
    plt.ylabel("Views")
    plt.title(f"{username} Views Average by Days in 3 months")
    plt.show()
    
def plot_count_hours(data, username):
    plt.figure(figsize=(12,9))
    plt.title(f"Jam ketika {username} melakukan stream selama 3 bulan")
    ax = sns.countplot(data['hours'], alpha=0.8)
    ax.bar_label(ax.containers[0])
    plt.show()
    
def plot_trend_views(data, username, max_limit):
    plt.figure(figsize=(20,9))
    ax = sns.lineplot(x = "date", y = "views", data=data, marker='o', ci=None)
    plt.ylim(0, max_limit)
    plt.title(f'{username} Trend Views in 3 months', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Views', fontsize=12)
    date_form = DateFormatter("%m-%d-%y")
    ax.xaxis.set_major_formatter(date_form)
    plt.show()
    
def plot_distribution(data, col):
    plt.figure(figsize=(12,9))
    plt.title(f'{col} distribution')
    sns.distplot(data[col])
    plt.show()
    
def plot_avg_views_hours(data, var_name, username):
    plt.figure(figsize=(12,9))
    ax = sns.barplot(var_name.index, var_name.values, alpha=0.8)
    ax.bar_label(ax.containers[0])
    plt.xlabel("Hours")
    plt.ylabel("Views")
    plt.title(f"{username} Views based on Hours Livestream in 3 Months")
    plt.show()
    
def convert_timestamp_to_minutes(data):
    data['duration'] = data['duration'].astype('str') 

    convert_data = []
    for duration in data['duration']:
        delta = timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1]), seconds=int(duration.split(':')[2]))
        minutes = delta.total_seconds()/60
        convert_data.append(round(minutes,2))
        
    data['convert_duration_minutes'] = convert_data
    
    return data

def plot_avg_duration_stream_days(data, var_name, username):
    plt.figure(figsize=(12,9))
    ax = sns.barplot(var_name.index, var_name.values, alpha=0.8)
    ax.bar_label(ax.containers[0])
    plt.xlabel("Days")
    plt.ylabel("Average Live Stream Duration")
    plt.xticks(fontsize=14)
    plt.title(f"{username} Livestream Durations Average (in hours) by Days in 3 Months")
    plt.show()
    
def plot_correlation(data):
    plt.figure(figsize=(12,9))
    plt.title("Correlation Between Views and Live Stream Durations")
    sns.scatterplot(y='views', x='convert_duration_minutes', data=data)
    plt.show()

def plot_livestream_topic(data, col_name, username):
    plt.figure(figsize=(12,9))
    plt.title(f'{username} Live Stream Topics in 3 months')
    ax = sns.countplot(data[col_name], alpha=0.8)
    ax.bar_label(ax.containers[0])
    plt.show()