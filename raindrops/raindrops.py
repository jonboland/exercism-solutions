def convert(number):
    """Convert int to string containing raindrop sounds."""
    raindrops = []
    
    if number % 3 == 0:
        raindrops.append('Pling')     
    if number % 5 == 0:
        raindrops.append('Plang')  
    if number % 7 == 0:
        raindrops.append('Plong')   
    if not raindrops:
        return str(number)
    
    return ''.join(raindrops)
