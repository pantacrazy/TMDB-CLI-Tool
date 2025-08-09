import argparse
from app import run_server
from store_const import StoreConst
class CLI_app():
    def __init__(self):
        self.argparser=argparse.ArgumentParser(description='TMBDB CLI Tool')
        servergroup_server=self.argparser.add_argument_group('server')
        servergroup_server.add_argument('--port',help='Port to listen on.',type=int)
        servergroup_server.add_argument('--origin',type=str,help='Remote server get the information.')

        server_group=self.argparser.add_argument_group('Cache')
        server_group.add_argument('--clear-cache',help='Cache',action="store_true")
        
    def run(self):
        self.args=self.argparser.parse_args()
        self.commands()
    def commands(self):
        if self.args.clear_cache:
            self.cache()
        if self.args.port:
            self.server()
    def server(self):
        if self.args.origin:
            run_server(self.args.port,self.args.origin)
        else:
            print('server is missing')
    def cache(self):
        const=StoreConst()
        const.clear_cache()
if __name__=='__main__':
    app=CLI_app()
    app.run()