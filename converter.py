def convert(milliseconds):
    seconds = int(('milliseconds' / 1000) % 60)
    minutes = int(('milliseconds' / (1000*60)) % 60)
    hours = int(('milliseconds' / (1000 * 60 * 60)) % 24)
    
    return hours, minutes, seconds

milliseconds = input('please enter the miliseconds:  ')
hours, minutes, seconds = convert(milliseconds)
print(f'{milliseconds} milliseconds is equal to {hours}, {minutes} minutes and {seconds} seconds')