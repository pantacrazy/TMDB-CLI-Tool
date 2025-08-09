from flask import Flask, jsonify, request, Response
import requests
from store_const import StoreConst
app = Flask(__name__)
cache_const=StoreConst()
@app.route('/<path:path>',methods=['GET'])
def method_name(path):
    cache_key=request.url
    conditional,result=find_element_cache(cache_key)
    if conditional:
        response=jsonify(result)
        response.headers['X-Cache']='HIT'
        return response
    else:
        result=requests.get(f'{app.config["ORIGIN_URL"]}/{path}')
        if result.status_code==200:
                try:
                    json_result=result.json()
                    add_cache(json_result,cache_key)
                    response=jsonify(json_result)
                    response.headers['X-Cache']= 'MISS'
                    return response
                except ValueError: 
                    return Response(
                        result.content,
                        mimetype=result.headers.get('Content-Type', 'application/octet-stream'))
        else:
            response=jsonify({'error':'Cannot obtain the info'})
            response.headers['X-Cache']= 'MISS'
        return response
    
def find_element_cache(key):
    total_cache=cache_const.get_store_cache()
    if total_cache != None:
        for cache_key in total_cache:
            if key in cache_key:
                return True,cache_key[key]
    return False,None
def add_cache(cache,key):
    conditional,result=find_element_cache(key)
    if not conditional:
        total_cache=cache_const.get_store_cache()
        if result != None:
            total_cache.append({key:cache})
        else:
            total_cache={key:cache}
        cache_const.set_store_cache(total_cache)
def run_server(port,origin_url):
    cache_const=StoreConst()
    cache_const.get_store_cache()
    app.config['ORIGIN_URL']=origin_url
    app.run(debug=True,port=port)
    
if __name__=='__main__':
    run_server(port=5000,origin_url='http://dummyjson.com')