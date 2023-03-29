import numpy as np
import pandas as pd

# file name
FILENAME = 'data.csv'

# read from CSV file
matrix = np.genfromtxt(FILENAME, delimiter=',', dtype=None, encoding='utf-8')

# put data into a DataFrame + clean up + add headers
df = pd.DataFrame(data=matrix)
df = df.drop(df.columns[len(df.columns) - 1], axis=1)
df.columns = [    
    "Type", "sflow_agent_address", "inputPort", "outputPort", "src_MAC", "dst_MAC",
    "ethernet_type", "in_vlan", "out_vlan", "src_IP", "dst_IP", "IP_protocol", "ip_tos", "ip_ttl", 
    "udp_src_port/tcp_src_port/icmp_type", "udp_dst_port/tcp_dst_port/icmp_code",
    "tcp_flags", "packet_size", "IP_size", "sampling_rate"
]


# EXERCISE 4A: TOP TALKERS AND LISTENERS
print("\n===EXERCISE 4A===\nTOP 5 TALKERS")
senders_grouped = df.groupby('src_IP').size().reset_index(name='Count')
senders_grouped = senders_grouped.sort_values(['Count'], ascending=False)
top5_senders = senders_grouped.head(5)
print(top5_senders)

print("\nTOP 5 LISTENERS")
listeners_grouped = df.groupby('dst_IP').size().reset_index(name='Count')
listeners_grouped = listeners_grouped.sort_values(['Count'], ascending=False)
top5_listeners = listeners_grouped.head(5)
print(top5_listeners)


# EXERCISE 4B: TRANSPORT PROTOCOL PERCENTAGE BREAKDOWN
print("\nEXERCISE 4B: TRANSPORT PROTOCOL PERCENTAGE BREAKDOWN")
count_row = df.shape[0]
df_grouped = df.groupby('IP_protocol').size().reset_index(name='Count')
df_grouped = df_grouped.sort_values(['Count'], ascending=False)
df_grouped['Percentage'] = df_grouped['Count'] / count_row * 100
top5 = df_grouped.head(5)
print(top5)


# EXERCISE 4C: APPLICATIONS PROTOCOL
print("\nEXERCISE 4C: TOP 5 APPLICATIONS PROTOCOL")
df_grouped = df.groupby('udp_dst_port/tcp_dst_port/icmp_code').size().reset_index(name='Count')
df_grouped = df_grouped.sort_values(['Count'], ascending=False)
top5 = df_grouped.head(10)
print(top5)


# EXERCISE 4D: TRAFFIC INTENSITY
print("\nEXERCISE 4D: TRAFFIC INTENSITY")
total_packet_size = df["IP_size"].sum() / (8*1024**2)
print(f"Total traffic: {total_packet_size: .3f} MB")