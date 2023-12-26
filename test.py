from auctionLogo import auction_logo

bidders = {}
print(auction_logo)
print("Vítejte v programu pro tichou dražbu.")

while True:
    name = input("Jaké je vaše jméno? ")
    money = input("Jaká je vaše nabídka v dolarech? ")
    bidders[name] = money
    ask = input("Jsou další nabízející? Napište 'ano' nebo 'ne'. ")
    if ask == "ano":
        continue
    else:
        break

highest_bid = sorted(bidders.items(), key=lambda x:int(x[1]), reverse = True)
winner_name = (highest_bid[0][0])
winner_price = (highest_bid[0][1])

print(f"Vítězem aukce je: {winner_name} s nabídkou {winner_price} dolarů.")



