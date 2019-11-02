#!/usr/bin/env python
# coding: utf-8

# In[1]:


import krakenex
import time

def login():
	k = krakenex.API()
	k.load_key('kraken.key')
	return k

def get_balance(k):
	result = k.query_private('Balance')['result']
	XXBTBal = result['XXBT']
	XETHBal = result['XETH']
	return [XXBTBal, XETHBal]

def get_max_purchase(assetPair, balance):
	result = k.query_public('Ticker', {'pair': assetPair})
	BTCForOneETH = result["result"]['XETHXXBT']['b'][0]
	max_buy = balance / float(BTCForOneETH) 
	return(max_buy-0.001) #accounts for some amount of fees and shit


def tradeBot(marginToSeek, stopLoss):
	# Buy Max ETH
	XXBTBal = float(get_balance()[0])
	TargetValue = XXBTBal
	max_buy = get_max_purchase('ETHXBT', XXBTBal)
	print(max_buy)
	response = k.query_private('AddOrder',
	                                    {'pair': 'ETHXBT',
	                                     'type': 'buy',
	                                     'ordertype': 'market',
	                                     'volume': (max_buy)})
	print(response)


# In[ ]:




