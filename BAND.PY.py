import pandas as pd
import psutil
import time
import seaborn as sns
import matplotlib.pyplot as plt
class Bandwidth:

    rcv_bytes=psutil.net_io_counters().bytes_recv
    sent_bytes=psutil.net_io_counters().bytes_sent
    total_bytes=rcv_bytes+sent_bytes
    print(f"{rcv_bytes/1024/1024:.2f} MB and {sent_bytes/1024/1024:.2f} MB then {total_bytes/1024/1024:.2f} MB")
    io_bytes=psutil.net_io_counters()
    data=[]
    while True:
        bytes_sent=psutil.net_io_counters().bytes_sent
        bytes_recv=psutil.net_io_counters().bytes_recv
        print(bytes_sent,bytes_recv)
        total_bytes1=bytes_sent+bytes_recv
        new_sent=bytes_sent-sent_bytes
        new_recv=bytes_recv-rcv_bytes
        new_total = total_bytes1 - total_bytes
        mb_new_sent=new_sent/1024/1024
        mb_new_recv=new_recv/1024/1024
        mb_total=new_total/1024/1024
        print(
            f"{mb_new_recv:.2f} MB and {mb_new_sent:.2f} MB then {mb_total :.2f} MB")
        data.append({
            'Byte_sent':io_bytes.bytes_sent,
            'Byte_recv':io_bytes.bytes_recv,
            'Pack_sent':io_bytes.packets_sent,
            'pack_recv':io_bytes.packets_recv,
            'pkt_dropin':io_bytes.dropin,
            'pkt_dropout':io_bytes.dropout,
            'error_in':io_bytes.errin,
            'error_out':io_bytes.dropout
        })
        df=pd.DataFrame(data)
        time.sleep(1)
        # sns.lineplot(data=df)
        # plt.show()
        print(df)
bandwidth=Bandwidth()
bandwidth()