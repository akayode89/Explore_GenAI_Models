def summarize_text(text):
    from transformers import pipeline
    text_summarizer = pipeline(task='summarization', model='t5-small', min_length=20, max_length=150,
                          model_kwargs={"cache_dir": "models"})
    results = text_summarizer(text)
    print(results)


if __name__ == '__main__':
    crypto_surge = """
The cryptocurrency market has experienced a significant surge following an announcement by U.S. President Donald Trump 
regarding the establishment of a U.S. Crypto Strategic Reserve. This reserve is intended to include major 
cryptocurrencies such as Bitcoin (BTC), Ethereum (ETH), XRP, Solana (SOL), and Cardano (ADA). The announcement has 
boosted investor confidence and led to substantial price increases across these assets.
Key Developments and Market Reaction
Price Increases: Bitcoin surged by over 10%, reaching a peak above $93,000, while Ethereum rose by around 11-13%136. 
Other alternative coins saw even more dramatic gains, with Cardano increasing by up to 66% and XRP by 28-40%167.
Market Capitalization: XRP's market capitalization surpassed that of USDT, becoming the third-largest cryptocurrency at 
$163.9 billion1.
Volume and Trading Activity: The total crypto market volume increased significantly, with Bitcoin's trading volume 
rising by over 140% in 24 hours4.
Investor Sentiment: The announcement has been seen as a positive development for the crypto sector, potentially opening 
doors for strategic capital and institutional adoption35.
Implications and Future Outlook
Regulatory Impact: The establishment of a Crypto Strategic Reserve could enhance the legitimacy of cryptocurrencies and 
influence global regulatory approaches5.
Potential for Global Adoption: This move might prompt other countries to consider similar reserves, leading to a more 
coordinated international regulatory environment5.
Market Speculation: Analysts predict further price increases if the bullish momentum continues, with some speculating 
that Bitcoin could reach between $125,000 and $250,000 by 202547.
Overall, Trump's announcement has injected optimism into the cryptocurrency market, signaling a potential shift towards 
greater institutional involvement and regulatory clarity. 
However, the operational details of the reserve remain unclear, and its long-term impact on the market is subject to 
ongoing speculation and analysis."""

    summarize_text(crypto_surge)
