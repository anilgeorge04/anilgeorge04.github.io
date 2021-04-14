---
title: Exploring Bitcoin and Cryptocurrencies
excerpt: Just how big is it?
header:
  teaser: /assets/images/explorecrypto_files/crypto-istock.jpg
  overlay_image: /assets/images/explorecrypto_files/crypto-istock.jpg
  overlay_filter: 0.5
  caption: iStock Photo
nbviewer: https://bit.ly/32cevY3
mathjax: true
tags:
  - insights
  - howstuffworks
  - finance
  - blockchain
---
{% include /notebooks/datacamp.html %}

## 1. Bitcoin and Cryptocurrencies: Import Data
<p>Since the <a href="https://newfronttest.bitcoin.com/bitcoin.pdf">launch of Bitcoin in 2008</a>, hundreds of projects based on the blockchain technology have emerged. These are called cryptocurrencies (also coins or cryptos in the Internet slang). Some are extremely valuable nowadays, and others may have the potential to become extremely valuable in the future<sup>1</sup>. In fact, on the 6th of December of 2017, Bitcoin had a <a href="https://en.wikipedia.org/wiki/Market_capitalization">market capitalization</a> above $200 billion. </p>
<p><center>
<img src="https://assets.datacamp.com/production/project_82/img/bitcoint_market_cap_2017.png" style="width:500px"> <br> 
<em>The astonishing increase of Bitcoin market capitalization in 2017.</em></center></p>
<p>*<sup>1</sup> <strong>WARNING</strong>: The cryptocurrency market is exceptionally volatile and any money you put in might disappear into thin air.  Cryptocurrencies mentioned here <strong>might be scams</strong> similar to <a href="https://en.wikipedia.org/wiki/Ponzi_scheme">Ponzi Schemes</a> or have many other issues (overvaluation, technical, etc.). <strong>This is definitely NOT investment advice</strong>. *</p>

<p><strong>Dataset:</strong> In this notebook, we will use a CSV downloaded on 6th of December of 2017 using the coinmarketcap API (NOTE: The public API went private in 2020 and is no longer available) named <code>datasets/coinmarketcap_06122017.csv</code>. </p>

    DATASET CHECK
    Rows and Columns: (1326, 16)
    Sample rows of Data:
       Unnamed: 0  24h_volume_usd  available_supply            id  last_updated  \
    0           0    9.007640e+09      1.672352e+07       bitcoin    1512549554   
    1           1    1.551330e+09      9.616537e+07      ethereum    1512549553   
    2           2    1.111350e+09      1.684044e+07  bitcoin-cash    1512549578   
    3           3    2.936090e+09      2.779530e+09          iota    1512549571   
    4           4    2.315050e+08      3.873915e+10        ripple    1512549541   
    
       market_cap_usd    max_supply          name  percent_change_1h  \
    0    2.130493e+11  2.100000e+07       Bitcoin               0.12   
    1    4.352945e+10           NaN      Ethereum              -0.18   
    2    2.529585e+10  2.100000e+07  Bitcoin Cash               1.65   
    3    1.475225e+10  2.779530e+09          IOTA              -2.38   
    4    9.365343e+09  1.000000e+11        Ripple               0.56   
    
       percent_change_24h  percent_change_7d  price_btc     price_usd  rank  \
    0                7.33              17.45   1.000000  12739.500000     1   
    1               -3.93              -7.33   0.036177    452.652000     2   
    2               -5.51              -4.75   0.120050   1502.090000     3   
    3               83.35             255.82   0.000424      5.307460     4   
    4               -3.70             -14.79   0.000019      0.241754     5   
    
      symbol  total_supply  
    0    BTC  1.672352e+07  
    1    ETH  9.616537e+07  
    2    BCH  1.684044e+07  
    3  MIOTA  2.779530e+09  
    4    XRP  9.999309e+10  
    
    Coin ID and Market Cap in USD
    id                1326
    market_cap_usd    1031
    dtype: int64


## 2. Discard cryptocurrencies without a market capitalization
<p>The <code>count()</code> for <code>id</code> and <code>market_cap_usd</code> differs above. It is because some cryptocurrencies listed in coinmarketcap.com have no known market capitalization. This is represented by <code>NaN</code> in the data, and <code>NaN</code>s are not counted by <code>count()</code>. These cryptocurrencies are of little interest to us in this analysis, so they are safe to remove.</p>

    id                1031
    market_cap_usd    1031
    dtype: int64


## 3. How big is Bitcoin compared with the rest of the cryptocurrencies?
<p>At the time of writing, Bitcoin is under serious competition from other projects, but it is still dominant in market capitalization. Let's plot the market capitalization for the top 10 coins as a barplot to better visualize this.</p>




    Text(0.5, 0, 'Cryptocurrency')




    
![svg](/assets/images/explorecrypto_files/explorecrypto_5_1.svg)
    


## 4. Making the plot easier to read and more informative
<p>While the plot above is informative enough, it can be improved. Bitcoin is too big, and the other coins are hard to distinguish because of this. Instead of the percentage, let's use a log<sup>10</sup> scale of the "raw" capitalization. Plus, let's use color to group similar coins and make the plot more informative<sup>1</sup>. </p>
<p>For the colors rationale: bitcoin-cash and bitcoin-gold are forks of the bitcoin <a href="https://en.wikipedia.org/wiki/Blockchain">blockchain</a><sup>2</sup>. Ethereum and Cardano both offer Turing Complete <a href="https://en.wikipedia.org/wiki/Smart_contract">smart contracts</a>. Iota and Ripple are not minable. Dash, Litecoin, and Monero get their own color.</p>
<p><sup>1</sup> <em>This coloring is a simplification. There are more differences and similarities that are not being represented here.</em></p>
<p><sup>2</sup> <em>The bitcoin forks are actually <strong>very</strong> different. Please do your own research to understand it better.</em></p>




    Text(0.5, 0, '')




    
![svg](/assets/images/explorecrypto_files/explorecrypto_7_1.svg)
    


## 5. What is going on? Volatility in cryptocurrencies
<p>The cryptocurrencies market has been spectacularly volatile since the first exchange opened. This notebook started with a big, bold warning for a reason. Let's explore this volatility a bit more! We will begin by selecting and plotting the 24 hours and 7 days percentage change, which we already have available.</p>

                   percent_change_24h  percent_change_7d
    id                                                  
    flappycoin                 -95.85             -96.61
    credence-coin              -94.22             -95.31
    coupecoin                  -93.93             -61.24
    tyrocoin                   -79.02             -87.43
    petrodollar                -76.55             542.96


## 6. Well, we can already see that things are *a bit* crazy
<p>It seems you can lose a lot of money quickly on cryptocurrencies. Let's plot the top 10 biggest gainers and top 10 losers in market capitalization.</p>


    
![svg](/assets/images/explorecrypto_files/explorecrypto_11_0.svg)
    


## 7. Ok, that is just wild! What about weekly change?
<p>800% daily increase?! Why are we doing this tutorial and not buying random coins?<sup>1</sup></p>
<p>After calming down, let's reuse the function defined above to see what is going weekly instead of daily.</p>
<p><em><sup>1</sup> Please take a moment to understand the implications of the red plots on how much value some cryptocurrencies lose in such short periods of time</em></p>


    
![svg](/assets/images/explorecrypto_files/explorecrypto_13_0.svg)
    


## 8. How small is small?
<p>The names of the cryptocurrencies above are quite unknown, and there is a considerable fluctuation between the 1 and 7 days percentage changes. As with stocks, and many other financial products, the smaller the capitalization, the bigger the risk and reward. Smaller cryptocurrencies are less stable projects in general, and therefore even riskier investments than the bigger ones<sup>1</sup>. Let's classify our dataset based on Investopedia's capitalization <a href="https://www.investopedia.com/video/play/large-cap/">definitions</a> for company stocks. </p>
<p><sup>1</sup> <em>Cryptocurrencies are a new asset class, so they are not directly comparable to stocks. Furthermore, there are no limits set in stone for what a "small" or "large" stock is. Finally, some investors argue that bitcoin is similar to gold, this would make them more comparable to a <a href="https://www.investopedia.com/terms/c/commodity.asp">commodity</a> instead.</em></p>

    All largecap cryptocurrencies with a market cap over $10bn
                 id  market_cap_usd
    0       bitcoin    2.130493e+11
    1      ethereum    4.352945e+10
    2  bitcoin-cash    2.529585e+10
    3          iota    1.475225e+10


## 9. Most coins are tiny
<p>Note that many coins are not comparable to large companies in market cap. So let's divert from the original Investopedia definition by merging categories and close this analysis by classifying the cryptocurrencies into 3 categories.</p>




    <BarContainer object of 3 artists>




    
![svg](/assets/images/explorecrypto_files/explorecrypto_17_1.svg)
    


Where the market caps for 
+ <strong>Biggish</strong> is greater than USD 300 mn
+ <strong>Micro</strong> is greater than USD 50 mn and less than USD 300 mn, and 
+ <strong>Nano</strong> is less than USD 50 mn.

On that note, do your research and enter into the world of cryptocurrencies only after fully understanding the risks.

{% include /notebooks/nbviewer.html %}
