import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT), Handler) as httppd:
    print("server is on at port", PORT)
    httppd.serve_forever()

