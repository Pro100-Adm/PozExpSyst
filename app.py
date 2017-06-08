from cgi import parse_qs
from exp_syst_calc import *
html = """Введите значения в интервале от 0 до 1 в формате '0.1'.<br>
<form method="get">Вы предпочитаете телефон компании Samsung?<input name="Answer1"></input><br>
<form method="get">Вы предпочитаете телефон компании Apple?<input name="Answer2"></input><br>
<form method="get">Вы предпочитаете телефон компании Lenovo?<input name="Answer3"></input><br>
<form method="get">Укажите минимальный бюджет.<input name="Answer4"></input><br>
<form method="get">Укажите максималный бюджет.<input name="Answer5"></input><br>
<form method="get">Вам необходима модель последнего поколения?<input name="Answer6"></input><br>
<form method="get">Вы предпочитаете операционную систему Android?<input name="Answer7"></input><br>
<form method="get">Вы предпочитаете операционную систему iOS?<input name="Answer8"></input><br>
<button>OK</button></form>"""
def wsgi_app(environ, start_response): 
    response_headers = [('Content-type', 'text/html; charset=UTF-8')]
    response_body = html
    status = '200 OK'
    start_response(status, response_headers)
    yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
