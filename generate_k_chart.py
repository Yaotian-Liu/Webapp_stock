import os
import time
import shutil
import mplfinance as mpf
import pandas as pd
from tqdm import tqdm


def get_kchart(src):
    src = src[:-4]
    df = pd.read_csv(f'./stock_data/{src}.csv')
    data = df.drop(columns='code')
    data.index = pd.DatetimeIndex(data['date'])

    save = dict(fname=f'./static/k_chart/{src}.png', dpi=80, pad_inches=0.25)
    mpf.plot(data.tail(60), type='candle',
             volume=True, savefig=save, style='yahoo')


def clear_kchart_buffers():
    path = './static/k_chart'
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)

def print_kchart():
    clear_kchart_buffers()
    src_path = './stock_data'
    src_list = os.listdir(src_path)
    
    pbar = tqdm(src_list)
    for src in pbar:
        pbar.set_description('Printing ' + src)
        get_kchart(src)


if __name__ == '__main__':
    print_kchart()
    
        
    # time_start = time.time()
    # clear_kchart_buffers()

    # src_path = './stock_data'
    # src_list = os.listdir(src_path)
    # for src in src_list:
    #     get_kchart(src)
    #     print(f"Printing the k_chart of {src}")
    # print('-----------------------------------')
    # time_end = time.time()
    # time_duration = round(time_end - time_start, 2)
    # print(f"Takes up {time_duration} s to complete printing.")
