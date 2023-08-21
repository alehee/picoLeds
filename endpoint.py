
class Endpoint:
    @staticmethod
    def validate(request):
        print('kurwa mac')

        if request.find('/Leds?') == -1:
            return (400, 'Endpoint not exists or missing parameter')
        if request.find('color=') == -1:
            return (400, 'Color must be set')

        # Color validation
        colorStart = request.index('color=') + 6
        color = request[colorStart : colorStart + 6]
        for ch in color:
            chu = ch.upper()
            if '0123456789ABCDEF'.index(chu) == -1:
                return (400, 'Color not valid')
        
        # Brightness validation
        brightness = None
        if request.find('brightness='):
            brightnessStart = request.index('brightness=') + 11
            brightness = request[brightnessStart : brightnessStart + 1]
            if not brightness.isnumeric():
                return (400, 'Brightness not valid')
        
        return (200, 'OK', (color, brightness))