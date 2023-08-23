
class Endpoint:
    @staticmethod
    def validate(request, controller):
        result = 'No endpoint found!'

        if request.startswith('/color/'):
            color = request.replace('/color/', '')
            result = controller.changeColor(color)

        elif request.startswith('/brightness/'):
            brightness = request.replace('/brightness/', '')
            result = controller.changeBrightness(brightness)

        elif request.startswith('/turn/'):
            decision = request.replace('/turn/', '')
            result = controller.toggleLeds(decision == 'on')

        head = f'HTTP/1.1 200 OK\r\nContent-type: application/json\r\n\r\n'
        response = { "status": 200, "message": "OK" }
        if result != 'OK':
            head = f'HTTP/1.1 400 Bad Request\r\nContent-type: application/json\r\n\r\n'
            response['status'] = 400
            response['message'] = result

        return head, response