import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)
from src.loader import SlackDataLoader  # Adjust the import based on your project structure

def plot_top_users_with_highest_replies(data):
    sorted_data = data.sort_values(by='reply_count', ascending=False)
    top_users = sorted_data.head(3)

    st.title('Users with Highest Replies')

    fig, ax = plt.subplots(figsize=(15, 7.5))
    ax.bar(top_users['sender_name'], top_users['reply_count'], color='blue')

    ax.set_xlabel('User')
    ax.set_ylabel('Number of Replies')

    st.pyplot(fig)

def draw_df(data):
    st.title('Usernames with Highest Replies')
    users = data.sort_values(by='reply_count', ascending=False).head(10)
    users_replies = users[['sender_name', 'reply_count']]
    
    st.table(users_replies.reset_index(drop=True))

def draw_message_with_replies(data):
    st.title('Messages with Highest Replies')
    df = data.sort_values(by='reply_count', ascending=False).head(10)
    channels_replies = df[['channel', 'reply_count']]
    
    st.table(channels_replies.reset_index(drop=True))

def draw_reply_per_user_per_channel(data):
    st.title('Plot of Number of Replies per User per Channel')
    grouped_df = data.groupby(['channel', 'sender_name'])['reply_count'].sum().unstack()

    grouped_df = data.groupby(['channel', 'sender_name'])['reply_count'].sum().unstack()
    sorted_df = grouped_df.sum(axis=1).sort_values(ascending=False)
    top_7_channels = sorted_df.head(7)

    fig, ax = plt.subplots(figsize=(15, 7.5))
    top_7_channels.plot(kind='bar', ax=ax, stacked=True)

    plt.xlabel('Channel')
    plt.ylabel('Total Reply Count')
    plt.legend(title='Sender Name', bbox_to_anchor=(1, 1))

    st.pyplot(fig)

if __name__ == '__main__':
    sl = SlackDataLoader('../../data/anonymized/')
    df = sl.create_dataframe()

    
    plot_top_users_with_highest_replies(df)
    draw_df(df)

    draw_message_with_replies(df)
    draw_reply_per_user_per_channel(df)
