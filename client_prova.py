import time
import websocket
import _thread as thread


def on_open(ws):
    c = [True]

    def run(*args):
        inp = 's'
        while inp != 'exit':
            inp = input('inserire input:\t')
            if inp != 'exit':
                ws.send(inp)
        ws.close()
        c[0] = False

    def keep_opened(*args):
        while c[0]:
            ws.send('ping555')
            time.sleep(30)

    def keep_alive(*args):
        while c[0]:
            webs = websocket.create_connection("ws://servergarecatta.herokuapp.com/")
            webs.send('ping555')
            print(f'ping:{webs.recv()}')
            webs.close()
            time.sleep(600)

    thread.start_new_thread(run, ())
    thread.start_new_thread(keep_opened, ())
    thread.start_new_thread(keep_alive, ())


def on_close(ws):
    print('closed')


def on_error(ws, error):
    print(f'errore:\t{error}\nalla socket:\t{ws}')


def on_message(ws, message):
    if message != 'pong555':
        print(message)


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://servergarecatta.herokuapp.com/", on_close=on_close,
                                on_message=on_message, on_error=on_error, on_open=on_open)
    ws.run_forever()
