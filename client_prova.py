import os
import websocket
import _thread as thread

PORT = int(os.environ.get('PORT', 12345))


def on_open(ws):
    def run(*args):
        inp = 's'
        while inp != 'exit':
            inp = input('inserire input:\t')
            if inp != 'exit':
                ws.send(inp)
        ws.close()
    thread.start_new_thread(run, ())


def on_close(ws):
    print('closed')


def on_error(ws,  error):
    print(f'errore:\t{error}\nalla socket:\t{ws}')


def on_message(ws, message):
    print(message)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:"+str(PORT)+'/', on_close=on_close,
                                on_message=on_message, on_error=on_error)
    ws.on_open = on_open
    ws.run_forever()
