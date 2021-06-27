EXERCISE 2
With faang, use type conversion to change the date column to datetime and the volume column to integers. Then, sort by date and ticker.

In [3]:
faang = faang.assign(
    date=lambda x: pd.to_datetime(x.date),
    volume=lambda x: x.volume.astype(int)
).sort_values(
    ['date', 'ticker']
)

faang.head()
Out[3]:
ticker	date	high	low	open	close	volume
0	AAPL	2018-01-02	43.075001	42.314999	42.540001	43.064999	102223600
0	AMZN	2018-01-02	1190.000000	1170.510010	1172.000000	1189.010010	2694500
0	FB	    2018-01-02	181.580002	177.550003	177.679993	181.419998	18151900
0	GOOG	2018-01-02	1066.939941	1045.229980	1048.339966	1065.000000	1237600
0	NFLX	2018-01-02	201.649994	195.419998	196.100006	201.070007	10966900
EXERCISE 3
Find the 7 rows with the lowest value for volume.

In [4]:
faang.nsmallest(7, 'volume')
Out[4]:
ticker	date	high	low	open	close	volume
126	GOOG	2018-07-03	1135.819946	1100.020020	1135.819946	1102.890015	679000
226	GOOG	2018-11-23	1037.589966	1022.398987	1030.000000	1023.880005	691500
99	GOOG	2018-05-24	1080.469971	1066.150024	1079.000000	1079.239990	766800
130	GOOG	2018-07-10	1159.589966	1149.589966	1156.979980	1152.839966	798400
152	GOOG	2018-08-09	1255.541992	1246.010010	1249.900024	1249.099976	848600
159	GOOG	2018-08-20	1211.000000	1194.625977	1205.020020	1207.770020	870800
161	GOOG	2018-08-22	1211.839966	1199.000000	1200.000000	1207.329956	887400

EXERCISE 4
Right now, the data is somewhere between long and wide format. Use melt() to make it completely long format.

In [5]:
melted_faang = faang.melt(
    id_vars=['ticker', 'date'], 
    value_vars=['open', 'high', 'low', 'close', 'volume']
)
melted_faang.head()
Out[5]:
ticker	date	variable	value
0	AAPL	2018-01-02	open	42.540001
1	AMZN	2018-01-02	open	1172.000000
2	FB	2018-01-02	open	177.679993
3	GOOG	2018-01-02	open	1048.339966
4	NFLX	2018-01-02	open	196.100006

EXERCISE 5
Suppose we found out there was a glitch in how the data was recorded on July 26, 2018. How should we handle this?

Given that this is a large data set (~ 1 year), we would be tempted to just drop that date and interpolate. However, some preliminary research on that date for the FAANG stocks reveals that FB took a huge tumble that day. If we had interpolated, we would have missed the magnitude of the drop.

EXERCISE 6
The European Centre for Disease Prevention and Control (ECDC) provides an open dataset on COVID-19 cases called, daily number of new reported cases of COVID-19 by country worldwide. This dataset is updated daily, but we will use a snapshot that contains data from January 1, 2020 through September 18, 2020. Clean and pivot the data so that it is in wide format:

Read in the covid19_cases.csv file.
Create a date column using the data in the dateRep column and the pd.to_datetime() function.
Set the date column as the index and sort the index.
Replace occurrences of United_States_of_America and United_Kingdom with USA and UK, respectively.
Using the countriesAndTerritories column, filter the data down to Argentina, Brazil, China, Colombia, India, Italy, Mexico, Peru, Russia, Spain, Turkey, the UK, and the USA.
Pivot the data so that the index contains the dates, the columns contain the country names, and the values are the case counts in the cases column. Be sure to fill in NaN values with 0.
In [6]:
covid = pd.read_csv('../../ch_03/exercises/covid19_cases.csv').assign(
    date=lambda x: pd.to_datetime(x.dateRep, format='%d/%m/%Y')
).set_index('date').replace(
    'United_States_of_America', 'USA'
).replace('United_Kingdom', 'UK').sort_index()

covid[
    covid.countriesAndTerritories.isin([
        'Argentina', 'Brazil', 'China', 'Colombia', 'India', 'Italy', 
        'Mexico', 'Peru', 'Russia', 'Spain', 'Turkey', 'UK', 'USA'
    ])
].reset_index().pivot(index='date', columns='countriesAndTerritories', values='cases').fillna(0)
Out[6]:
countriesAndTerritories	Argentina	Brazil	China	Colombia	India	Italy	Mexico	Peru	Russia	Spain	Turkey	UK	USA
date													
2020-01-01	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
2020-01-02	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
2020-01-03	0.0	0.0	17.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
2020-01-04	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
2020-01-05	0.0	0.0	15.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...
2020-09-14	10778.0	14768.0	29.0	7355.0	92071.0	1456.0	4408.0	6787.0	5449.0	27404.0	1527.0	3330.0	33871.0
2020-09-15	9056.0	15155.0	22.0	5573.0	83809.0	1008.0	3335.0	4241.0	5509.0	9437.0	1716.0	2621.0	34841.0
2020-09-16	9908.0	36653.0	24.0	6698.0	90123.0	1229.0	4771.0	4160.0	5529.0	11193.0	1742.0	3103.0	51473.0
2020-09-17	11893.0	36820.0	7.0	7787.0	97894.0	1452.0	4444.0	6380.0	5670.0	11291.0	1771.0	3991.0	24598.0
2020-09-18	11674.0	36303.0	44.0	7568.0	96424.0	1583.0	3182.0	5698.0	5762.0	14389.0	1648.0	3395.0	43567.0
262 rows × 13 columns

EXERCISE 7
In order to determine the case totals per country efficiently, we need the aggregation skills we will learn in Chapter 4, Aggregating DataFrames, so the ECDC data in the covid19_cases.csv file has been aggregated for us and saved in the covid19_total_cases.csv file. It contains the total number of case per country. Use this data to find the 20 countries with the largest COVID-19 case totals. Hints:

When reading in the CSV file, pass in index_col='cases'.
Note that it will be helpful to transpose the data before isolating the countries.
In [7]:
pd.read_csv('../../ch_03/exercises/covid19_total_cases.csv', index_col='index')\
    .T.nlargest(20, 'cases').sort_values('cases', ascending=False)
Out[7]:
index	cases
USA	            6724667
India	        5308014
Brazil	        4495183
Russia	        1091186
Peru	        756412
Colombia	    750471
Mexico	        688954
South_Africa	657627
Spain	        640040
Argentina	    601700
Chile	        442827
France	        428696
Iran	        416198
UK	            385936
Bangladesh	    345805
Saudi_Arabia	328720
Iraq	        311690
Pakistan	    305031
Turkey	        299810
Italy	        294932