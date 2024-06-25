import numpy as np
from obspy import UTCDateTime, Trace, Stream

# 生成随机地震波形数据
sampling_rate = 100.0  # 采样率（Hz）
npts = 1000  # 数据点数
data_bhz = np.random.randn(npts)
data_bhe = np.random.randn(npts)
data_bhn = np.random.randn(npts)

# 创建Trace对象
trace_bhz = Trace(data=data_bhz, header={
    'network': 'XX',
    'station': 'XYZ',
    'location': '00',
    'channel': 'BHZ',
    'starttime': UTCDateTime(2024, 4, 22, 12, 0, 0),
    'sampling_rate': sampling_rate,
    'units': 'counts'
})

trace_bhe = Trace(data=data_bhe, header={
    'network': 'XX',
    'station': 'XYZ',
    'location': '00',
    'channel': 'BHE',
    'starttime': UTCDateTime(2024, 4, 22, 12, 0, 0),
    'sampling_rate': sampling_rate,
    'units': 'counts'
})

trace_bhn = Trace(data=data_bhn, header={
    'network': 'XX',
    'station': 'XYZ',
    'location': '00',
    'channel': 'BHN',
    'starttime': UTCDateTime(2024, 4, 22, 12, 0, 0),
    'sampling_rate': sampling_rate,
    'units': 'counts'
})

# 创建Stream对象并添加Trace
stream = Stream(traces=[trace_bhz, trace_bhe, trace_bhn])

# 写入MiniSEED文件
stream.write('three_channel_counts_example.mseed', format='MSEED')


#%% 读取数据验证
import matplotlib.pyplot as plt
from obspy import read
# 读取MiniSEED文件
stream = read('three_channel_counts_example.mseed')

# 获取三个通道的数据
trace_bhz = stream.select(channel='BHZ')[0]
trace_bhe = stream.select(channel='BHE')[0]
trace_bhn = stream.select(channel='BHN')[0]

# 获取时间轴
times = trace_bhz.times()

# 绘制地震波形
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(times, trace_bhz.data, 'k')
plt.title('BHZ Channel')
plt.xlabel('Time (s)')
plt.ylabel('Counts')

plt.subplot(3, 1, 2)
plt.plot(times, trace_bhe.data, 'r')
plt.title('BHE Channel')
plt.xlabel('Time (s)')
plt.ylabel('Counts')

plt.subplot(3, 1, 3)
plt.plot(times, trace_bhn.data, 'b')
plt.title('BHN Channel')
plt.xlabel('Time (s)')
plt.ylabel('Counts')

plt.tight_layout()
plt.show()



