def trade_decision() :
    pair = input('Pair name: ')
    entry = float(input('Entry price: '))
    stop_loss = float(input('Stop loss: '))
    take_profit = float(input('Take profit: '))

    risk = entry - stop_loss

    if risk <= 0 :
        print('Error! Invalid risk!')
        return

    reward = take_profit - entry
    rr_ratio = reward/risk

    print('Pair: ', pair)
    print('Your reward: ', reward)
    print('Your risk: ', risk)
    print('Your RRR: ', rr_ratio)

    if rr_ratio >= 2:
        print('Good trade setup.')
    elif rr_ratio >= 1:
        print('Average setup.')
    else:
        print('Avoid this trade!')

trade_decision()




