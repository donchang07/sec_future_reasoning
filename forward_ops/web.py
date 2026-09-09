"""Read-only localhost monitoring; static allowlist, no filesystem browsing."""
import json
import re
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
from .runtime import operations_manifest

STATIC=Path(__file__).parent/'static'


def state(store):
    runs=store.runs()
    return {'runs':[{'run_id':r['system']['run_id'],'cutoff':r['system']['data_cutoff'],'kind':r['kind'],
        'case_key':r['case_key'],'horizons':r['system']['horizons'],'p0':r['system']['p0']} for r in runs],
        'evaluation':store.evaluation(),'logs':store.records('logs')[-15:],
        'position_records':len(store.records('positioning')),'event_records':len(store.records('events')),
        'frozen_baseline':'real-world-contract-v2.0.0','shadow_model_influence':False}


def handler(store):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path=urlsplit(self.path).path
            try:
                if path=='/api/state':body=json.dumps(state(store),ensure_ascii=False).encode();mime='application/json'
                elif re.fullmatch(r'/api/run/[0-9a-f-]{36}',path):
                    body=json.dumps(store.run(path.split('/')[-1]),ensure_ascii=False).encode();mime='application/json'
                elif path in ('/','/app.js','/style.css'):
                    file=STATIC/('index.html' if path=='/' else path[1:]);body=file.read_bytes()
                    mime={'/':'text/html','/app.js':'application/javascript','/style.css':'text/css'}[path]
                else:self.send_error(404);return
                self.send_response(200);self.send_header('Content-Type',mime+'; charset=utf-8')
                self.send_header('Content-Length',str(len(body)));self.send_header('Cache-Control','no-store')
                self.send_header('X-Content-Type-Options','nosniff')
                self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
                self.end_headers();self.wfile.write(body)
            except FileNotFoundError:self.send_error(404)
            except (ValueError,KeyError):self.send_error(422,'Invalid or corrupted record')
        def log_message(self,*args):pass
    return Handler


def serve(store,port=8677):
    ThreadingHTTPServer(('127.0.0.1',port),handler(store)).serve_forever()
