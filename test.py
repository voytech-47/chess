from colored import bg, attr

moved = bg(101)
reset = attr('reset_background')

print (f"{moved}{[4, 7] == [4, 7]}{reset}")