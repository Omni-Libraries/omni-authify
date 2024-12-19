import sys
import os
import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(BASE_DIR)
sys.path.insert(0, os.path.abspath(BASE_DIR))


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from omni_authify.providers.google import Google
from dotenv import load_dotenv

load_dotenv()


class RequestHandler(BaseHTTPRequestHandler):
    CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
    SCOPE = "openid email profile"
    
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        provider = Google(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI, scope=self.SCOPE)
        authorization_url = provider.get_authorization_url()
        
        if path == '/auth/':
            self.send_response(302)
            self.send_header('Location', authorization_url)
            self.end_headers()
            
        if path == '/':
            code = query_params.get('code')
            if not code:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid request.')
            else:    
                access_token = provider.get_access_token(code[0])
                user_info = provider.get_user_profile(access_token)
                user_info = json.dumps(user_info)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(user_info.encode('utf'))


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        print(f"Сервер запущен на http://localhost:{port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен пользователем.")
        httpd.shutdown()
        httpd.server_close()
        print("Сервер успешно завершил работу.")


if __name__ == '__main__':
    run()