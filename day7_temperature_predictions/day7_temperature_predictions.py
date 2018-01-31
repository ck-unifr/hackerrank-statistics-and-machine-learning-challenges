#https://www.hackerrank.com/challenges/temperature-predictions/problem

# input
# 443
# yyyy	month	tmax	tmin
# 1908	January	5.0	-1.4
# 1908	February	7.3	1.9
# 1908	March	6.2	0.3
# 1908	April	Missing_1	2.1
# 1908	May	Missing_2	7.7
# 1908	June	17.7	8.7
# 1908	July	Missing_3	11.0
# 1908	August	17.5	9.7
# 1908	September	16.3	8.4
# 1908	October	14.6	8.0
# 1908	November	9.6	3.4
# 1908	December	5.8	Missing_4
# 1909	January	5.0	0.1
# 1909	February	5.5	-0.3
# 1909	March	5.6	-0.3
# 1909	April	12.2	3.3
# 1909	May	14.7	4.8
# 1909	June	15.0	7.5
# 1909	July	17.3	10.8
# 1909	August	18.8	10.7
# 1909	September	14.5	8.1
# 1909	October	12.9	6.9
# 1909	November	7.5	1.7
# 1909	December	5.3	0.4
# 1910	January	5.2	-0.5
# 1910	February	Missing_5	1.5
# 1910	March	9.1	Missing_6
# 1910	April	9.8	2.4
# 1910	May	14.3	Missing_7
# 1910	June	17.7	9.6
# 1910	July	17.0	9.8
# 1910	August	18.0	11.8
# 1910	September	15.0	8.5
# 1910	October	12.6	7.3
# 1910	November	5.5	-0.4
# 1910	December	8.0	3.6
# 1911	January	5.8	Missing_8
# 1911	February	6.9	1.3
# 1911	March	6.4	1.9
# 1911	April	10.0	3.9
# 1911	May	16.3	7.9
# 1911	June	17.8	9.0
# 1911	July	22.2	11.7
# 1911	August	21.6	Missing_9
# 1911	September	17.3	8.6
# 1911	October	11.4	5.6
# 1911	November	7.9	3.2
# 1911	December	8.2	3.3
# 1912	January	Missing_10	0.1
# 1912	February	6.6	Missing_11
# 1912	March	Missing_12	3.5
# 1912	April	12.4	3.4
# 1912	May	Missing_13	6.6
# 1912	June	Missing_14	9.9
# 1912	July	18.3	11.7
# 1912	August	15.1	9.2
# 1912	September	13.7	7.7
# 1912	October	11.6	4.2
# 1912	November	8.3	Missing_15
# 1912	December	8.9	2.4
# 1913	January	5.4	1.1
# 1913	February	Missing_16	1.2
# 1913	March	8.3	2.1
# 1913	April	10.6	3.8
# 1913	May	14.7	6.8
# 1913	June	17.4	9.5
# 1913	July	17.5	10.4
# 1913	August	18.5	Missing_17
# 1913	September	16.9	10.3
# 1913	October	12.7	Missing_18
# 1913	November	10.1	5.1
# 1913	December	6.8	2.3
# 1914	January	6.0	0.7
# 1914	February	9.5	3.5
# 1914	March	Missing_19	2.6
# 1914	April	14.1	4.4
# 1914	May	13.7	5.9
# 1914	June	18.4	9.1
# 1914	July	19.2	11.5
# 1914	August	19.7	11.1
# 1914	September	17.0	8.4
# 1914	October	Missing_20	7.2
# 1914	November	9.1	Missing_21
# 1914	December	6.4	1.7
# 1915	January	5.4	1.3
# 1915	February	6.3	0.8
# 1915	March	7.9	1.5
# 1915	April	10.9	3.5
# 1915	May	13.9	4.9
# 1915	June	18.6	8.2
# 1915	July	Missing_22	10.3
# 1915	August	18.3	10.2
# 1915	September	16.8	8.9
# 1915	October	Missing_23	5.1
# 1915	November	5.8	-0.6
# 1915	December	Missing_24	1.2
# 1916	January	9.7	4.4
# 1916	February	5.4	0.5
# 1916	March	4.4	Missing_25
# 1916	April	11.4	3.1
# 1916	May	14.8	6.3
# 1916	June	14.4	7.7
# 1916	July	Missing_26	11.1
# 1916	August	20.1	12.1
# 1916	September	Missing_27	8.9
# 1916	October	Missing_28	6.1
# 1916	November	8.8	4.1
# 1916	December	4.4	-0.6
# 1917	January	3.0	-0.5
# 1917	February	3.2	-2.3
# 1917	March	5.5	Missing_29
# 1917	April	8.3	0.8
# 1917	May	16.3	6.6
# 1917	June	Missing_30	9.4
# 1917	July	19.9	11.0
# 1917	August	18.1	11.9
# 1917	September	17.3	10.3
# 1917	October	10.2	3.6
# 1917	November	9.6	Missing_31
# 1917	December	4.5	-0.1
# 1918	January	6.1	0.2
# 1918	February	8.0	2.9
# 1918	March	8.2	2.0
# 1918	April	Missing_32	2.9
# 1918	May	16.9	7.3
# 1918	June	16.6	Missing_33
# 1918	July	Missing_34	10.5
# 1918	August	Missing_35	11.4
# 1918	September	Missing_36	8.1
# 1918	October	11.8	6.1
# 1918	November	7.9	1.7
# 1918	December	8.8	3.7
# 1919	January	Missing_37	0.1
# 1919	February	3.1	-1.4
# 1919	March	5.4	Missing_38
# 1919	April	10.1	Missing_39
# 1919	May	17.3	7.3
# 1919	June	17.7	9.4
# 1919	July	17.2	Missing_40
# 1919	August	18.9	10.5
# 1919	September	Missing_41	8.3
# 1919	October	11.1	3.1
# 1919	November	4.9	0.2
# 1919	December	7.2	2.0
# 1920	January	7.4	Missing_42
# 1920	February	8.3	Missing_43
# 1920	March	10.1	3.1
# 1920	April	9.7	4.0
# 1920	May	14.8	7.0
# 1920	June	17.5	9.0
# 1920	July	16.3	10.4
# 1920	August	16.4	9.7
# 1920	September	15.9	8.5
# 1920	October	12.7	6.8
# 1920	November	8.7	4.5
# 1920	December	6.2	1.7
# 1921	January	8.9	3.8
# 1921	February	6.4	1.9
# 1921	March	9.9	Missing_44
# 1921	April	11.5	Missing_45
# 1921	May	15.2	5.9
# 1921	June	18.6	8.6
# 1921	July	22.4	11.9
# 1921	August	Missing_46	11.5
# 1921	September	17.7	9.3
# 1921	October	16.2	8.8
# 1921	November	6.1	0.9
# 1921	December	9.0	3.3
# 1922	January	4.8	Missing_47
# 1922	February	6.1	0.5
# 1922	March	6.3	1.3
# 1922	April	8.6	0.7
# 1922	May	16.4	Missing_48
# 1922	June	17.0	8.6
# 1922	July	Missing_49	9.6
# 1922	August	16.1	9.9
# 1922	September	14.8	8.4
# 1922	October	Missing_50	4.9
# 1922	November	8.8	3.3
# 1922	December	7.5	3.3
# 1923	January	8.2	3.0
# 1923	February	6.2	1.9
# 1923	March	9.0	2.8
# 1923	April	9.8	3.2
# 1923	May	11.5	4.7
# 1923	June	Missing_51	8.3
# 1923	July	20.0	Missing_52
# 1923	August	17.5	10.7
# 1923	September	15.2	Missing_53
# 1923	October	11.6	6.5
# 1923	November	5.5	0.5
# 1923	December	Missing_54	0.5
# 1924	January	6.0	1.1
# 1924	February	5.2	Missing_55
# 1924	March	6.6	-1.3
# 1924	April	9.7	Missing_56
# 1924	May	13.8	7.0
# 1924	June	16.7	9.4
# 1924	July	18.0	10.9
# 1924	August	16.7	10.0
# 1924	September	Missing_57	10.2
# 1924	October	12.4	6.7
# 1924	November	8.9	4.5
# 1924	December	9.0	4.8
# 1925	January	7.3	2.2
# 1925	February	6.8	1.4
# 1925	March	7.3	1.8
# 1925	April	10.3	3.4
# 1925	May	14.6	7.2
# 1925	June	18.9	9.2
# 1925	July	20.8	12.1
# 1925	August	18.8	11.7
# 1925	September	14.3	7.5
# 1925	October	13.0	6.4
# 1925	November	5.8	-0.2
# 1925	December	4.6	-0.8
# 1926	January	6.7	1.5
# 1926	February	8.2	3.5
# 1926	March	8.5	3.1
# 1926	April	12.3	4.9
# 1926	May	Missing_58	4.6
# 1926	June	17.2	8.3
# 1926	July	20.2	Missing_59
# 1926	August	19.3	11.0
# 1926	September	17.1	Missing_60
# 1926	October	10.5	4.1
# 1926	November	7.7	2.2
# 1926	December	6.4	1.6
# 1927	January	6.7	1.9
# 1927	February	6.6	0.6
# 1927	March	9.5	3.5
# 1927	April	10.2	3.8
# 1927	May	13.9	5.5
# 1927	June	Missing_61	7.4
# 1927	July	18.7	11.6
# 1927	August	17.9	11.7
# 1927	September	15.0	9.2
# 1927	October	13.2	6.5
# 1927	November	8.0	2.8
# 1927	December	Missing_62	-0.5
# 1928	January	Missing_63	0.9
# 1928	February	7.7	2.3
# 1928	March	7.8	2.3
# 1928	April	11.1	3.3
# 1928	May	13.9	5.6
# 1928	June	15.4	7.8
# 1928	July	18.8	11.3
# 1928	August	18.6	11.0
# 1928	September	15.9	8.5
# 1928	October	12.4	6.1
# 1928	November	9.8	4.8
# 1928	December	5.7	-0.1
# 1929	October	12.0	5.2
# 1929	November	Missing_64	2.5
# 1929	December	7.2	2.4
# 1930	January	7.6	1.3
# 1930	February	3.8	-0.5
# 1930	March	Missing_65	1.0
# 1930	April	9.9	4.2
# 1930	May	13.7	5.7
# 1930	June	18.7	9.6
# 1930	July	17.5	Missing_66
# 1930	August	18.6	Missing_67
# 1930	September	15.7	9.9
# 1930	October	12.6	7.0
# 1930	November	8.5	Missing_68
# 1930	December	6.0	1.5
# 1931	January	5.5	0.0
# 1931	February	5.2	1.0
# 1931	March	6.4	-0.7
# 1931	April	Missing_69	3.8
# 1931	May	14.5	6.8
# 1931	June	16.7	9.8
# 1931	July	18.0	11.8
# 1931	August	Missing_70	9.9
# 1931	September	14.3	8.3
# 1931	October	12.2	4.6
# 1931	November	9.5	5.0
# 1931	December	7.3	2.4
# 1932	January	8.8	3.1
# 1932	February	5.8	0.4
# 1932	March	7.6	1.2
# 1932	April	9.5	2.4
# 1932	May	12.8	Missing_71
# 1932	June	17.8	8.8
# 1932	July	19.0	12.4
# 1932	August	19.6	12.4
# 1932	September	15.9	8.7
# 1932	October	11.4	4.7
# 1932	November	8.2	Missing_72
# 1932	December	7.3	3.6
# 1933	January	4.4	-0.3
# 1933	February	Missing_73	1.0
# 1933	March	10.1	2.1
# 1933	April	12.3	4.8
# 1933	May	15.6	7.7
# 1933	June	19.5	9.9
# 1933	July	21.4	12.4
# 1933	August	21.1	12.5
# 1933	September	18.9	Missing_74
# 1933	October	12.3	Missing_75
# 1933	November	7.6	3.2
# 1933	December	4.2	-0.1
# 1934	January	7.3	1.5
# 1934	February	7.0	1.5
# 1934	March	7.3	1.1
# 1934	April	10.7	3.9
# 1934	May	15.3	6.5
# 1934	June	18.3	9.5
# 1934	July	22.4	12.7
# 1934	August	18.6	10.7
# 1934	September	18.5	10.0
# 1934	October	12.6	7.4
# 1934	November	Missing_76	3.7
# 1934	December	9.3	5.2
# 1935	January	6.5	1.9
# 1935	February	7.5	2.7
# 1935	March	8.9	3.3
# 1935	April	10.7	3.9
# 1935	May	13.5	4.8
# 1935	June	18.7	10.3
# 1935	July	21.1	11.8
# 1935	August	Missing_77	11.4
# 1935	September	16.5	9.2
# 1935	October	11.8	6.1
# 1935	November	8.7	Missing_78
# 1935	December	4.5	Missing_79
# 1936	January	5.0	0.5
# 1936	February	3.9	-1.3
# 1936	March	8.8	3.2
# 1936	April	Missing_80	2.1
# 1936	May	14.5	6.4
# 1936	June	18.1	9.6
# 1936	July	18.4	11.6
# 1936	August	19.4	Missing_81
# 1936	September	17.1	11.2
# 1936	October	12.5	5.9
# 1936	November	7.9	Missing_82
# 1936	December	7.7	2.0
# 1937	January	6.9	1.7
# 1937	February	6.8	1.6
# 1937	March	5.0	-0.6
# 1937	April	11.4	5.0
# 1937	May	15.5	7.6
# 1937	June	17.1	Missing_83
# 1937	July	19.6	12.4
# 1937	August	Missing_84	11.7
# 1937	September	16.4	8.9
# 1937	October	12.8	7.0
# 1937	November	7.7	2.2
# 1937	December	4.5	0.3
# 1938	January	7.8	Missing_85
# 1938	February	6.7	2.3
# 1938	March	12.5	5.3
# 1938	April	11.3	3.5
# 1938	May	14.2	6.3
# 1938	June	17.4	10.1
# 1938	July	17.9	10.9
# 1938	August	19.3	11.8
# 1938	September	16.6	9.7
# 1938	October	12.4	7.1
# 1938	November	10.8	6.0
# 1938	December	6.1	1.2
# 1939	January	5.4	0.9
# 1939	February	7.6	2.4
# 1939	March	7.9	2.7
# 1939	April	Missing_86	4.1
# 1939	May	15.0	Missing_87
# 1939	June	18.1	8.8
# 1939	July	18.4	11.5
# 1939	August	19.3	12.4
# 1939	September	16.7	10.6
# 1939	October	10.9	4.8
# 1939	November	10.0	5.0
# 1939	December	5.2	1.4
# 1940	January	0.7	-4.9
# 1940	February	Missing_88	-1.6
# 1940	March	8.9	1.9
# 1940	April	10.4	3.6
# 1940	May	16.9	7.2
# 1940	June	21.8	10.6
# 1940	July	18.4	10.9
# 1940	August	18.5	10.5
# 1940	September	15.8	8.2
# 1940	October	11.7	6.2
# 1940	November	8.6	4.1
# 1940	December	6.0	1.5
# 1941	January	1.4	-2.3
# 1941	February	4.7	Missing_89
# 1941	March	Missing_90	0.9
# 1941	April	8.1	2.6
# 1941	May	12.3	Missing_91
# 1941	June	19.1	9.3
# 1941	July	22.2	12.5
# 1941	August	17.9	Missing_92
# 1941	September	17.6	11.2
# 1941	October	Missing_93	7.2
# 1941	November	8.6	3.0
# 1941	December	7.5	2.7
# 1942	January	2.8	-1.4
# 1942	February	2.1	Missing_94
# 1942	March	7.0	0.6
# 1942	April	12.2	3.9
# 1942	May	14.4	6.0
# 1942	June	18.5	8.9
# 1942	July	18.8	10.9
# 1942	August	19.1	12.7
# 1942	September	16.1	8.3
# 1942	October	12.8	7.0
# 1942	November	7.6	2.7
# 1942	December	8.7	3.7
# 1943	January	Missing_95	0.9
# 1943	February	8.5	3.0
# 1943	March	9.9	2.5
# 1943	April	13.8	6.1
# 1943	May	16.1	5.9
# 1943	June	17.7	9.8
# 1943	July	19.9	10.7
# 1943	August	18.0	11.3
# 1943	September	15.6	9.0
# 1943	October	13.2	6.0
# 1943	November	8.4	3.5
# 1943	December	6.0	1.2
# 1944	January	8.2	2.6
# 1944	February	Missing_96	0.6
# 1944	March	8.1	1.3
# 1944	April	12.6	5.4
# 1944	May	14.4	6.1
# 1944	June	16.0	8.7
# 1944	July	18.8	12.2
# 1944	August	19.4	11.9
# 1944	September	15.2	8.4
# 1944	October	11.0	5.9
# 1944	November	8.4	Missing_97
# 1944	December	6.5	1.3
# 1945	January	3.7	Missing_98
# 1945	February	9.6	3.4
# 1945	March	11.5	Missing_99
# 1945	April	13.3	4.7
# 1945	May	15.4	6.9
# 1945	June	17.7	9.8
# 1945	July	20.0	12.1
# 1945	August	18.9	Missing_100

import numpy as np
from sklearn import ensemble

def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

# def sin_func(x, p1, p2, p3):
#   return p1 * np.sin(p2*x + p3) + 10

month_dict={"January":0,
   "February":1,
   "March":2,
   "April":3,
   "May":4,
   "June":5,
   "July":6,
   "August":7,
   "September":8,
   "October":9,
   "November":10,
   "December":11}

n = int(input())
input()
MIN = []
MAX = []
X_train = []
X_test = []

for i in range(n):
    line = input().split('\t')
    MAX.append(float(line[2]) if is_float(line[2]) else None)
    MIN.append(float(line[3]) if is_float(line[3]) else None)
    if is_float(line[2]) and is_float(line[3]):
        X_train.append([int(line[0]), month_dict[line[1]]])
    else:
        X_test.append([int(line[0]), month_dict[line[1]]])

Y_train = ([(x + y)/2 for x, y in zip(MAX, MIN) if x is not None and y is not None])

model = ensemble.GradientBoostingRegressor()
model.fit(X_train, Y_train)

Y_test = list(model.predict(X_test))

for i in range(n):
    if MIN[i] == None:
        print(round(2 * Y_test.pop(0) - MAX[i], 1))
    if MAX[i] == None:
        print(round(2 * Y_test.pop(0) - MIN[i], 1))

