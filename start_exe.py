import socket
import threading
import webbrowser

from app import app


def freier_port():
    
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


if __name__ == "__main__":
    port = freier_port()
    url = f"http://127.0.0.1:{port}"

    
    threading.Timer(1.5, lambda: webbrowser.open(url)).start()

    print(f"TheButton läuft auf {url}")
    print("Dieses Fenster schließen, um das Spiel zu beenden.")
    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)
