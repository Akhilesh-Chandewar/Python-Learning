tea_prices_inr = {
    "Masala chai" : 40,
    "Green tea" : 50,
    "Lemon tea" : 60,
    "Mint tea" : 70
}

tea_prices_usd = {tea : price * 0.012 for (tea , price) in tea_prices_inr.items()}
print(tea_prices_usd)