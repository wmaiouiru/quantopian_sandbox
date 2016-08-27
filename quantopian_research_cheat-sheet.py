


'''
link to quantopian research 
https://www.quantopian.com/research 
'''

'''
0. Basic API on quantopian research 
1. GETTING STARTED => how to use numpy and do moving averages  
2. Getting Started: Financial Modeling 
	Looking at correlations 
	seaborn => statistical data visualization 
3. 

'''

get_pricing
	get_pricing('APPL') # get pricing for apple all 
	get_pricing('AAPL',
		fields=['price','close_price','open_price'],
		start_date='2016-08-01',
		end_date='2016-08-02',
		frequency='minute'
	) # sample call
	'''
	Customzie get_pricing 
	fields => you can supply a list 
		price
		close_price (an alias of price) => last available price => closing of last day  
		open_price => first avaliable price => opening of current day 
		high => high of the market? 
		low => low of the market? 
		volume => volume 
	start_date 
	end_date
	frequency (minute,daily)
	'''

symbols()
# get information on a stock 


local_csv()
# work with local data 

get_backtest()
# get result of backtest 

get_fundamentals()


fundamentals = init_fundamentals()
fund_df = get_fundamentals(query(fundamentals.valuation_ratios.pe_ratio)
                             .filter(fundamentals.valuation.market_cap > 1e9)
                             .filter(fundamentals.valuation_ratios.pe_ratio > 1)
                             .order_by(fundamentals.valuation.market_cap)
                             .limit(10),
                             '2015-05-01')
fund_df


get_pricing? # => for documentation 



