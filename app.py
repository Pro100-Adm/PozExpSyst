from cgi import parse_qs
def calc(x):
    ver_var_Sams_A3 = {0:0.1, 1:1, 2:0, 3:0, 6:0, 7:1}
    ver_var_Sams_A5 = {0:0.1, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_Sams_S7 = {0:0.5, 1:1, 2:0, 3:0, 6:0, 7:1}
    ver_var_Sams_S8 = {0:0.3, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_Iphone_6S = {0:0.1, 1:0, 2:1, 3:0, 6:0, 8:1}
    ver_var_Iphone_7 = {0:0.1, 1:0, 2:1, 3:0, 6:1, 8:1}
    ver_var_Len_K5 = {0:0.1, 1:0, 2:0, 3:1, 6:0, 7:1}
    ver_var_Len_K6 = {0:0.1, 1:0, 2:0, 3:1, 6:1, 7:1}
    ver_var_Len_X = {0:0.1, 1:0, 2:0, 3:1, 6:0, 7:1}
    ver_var_Len_Z = {0:0.1, 1:0, 2:0, 3:1, 6:1, 7:1}
    for i in range(0,len(x)-1):
        for j in range(0,len(ver_var_Sams_A3)-1):
            if i==list(ver_var_Sams_A3.keys())[j]:
                Sams_A3 = x[i]*list(ver_var_Sams_A3.values())[j]
        for k in range(0,len(ver_var_Sams_A5)-1):
            if i==list(ver_var_Sams_A5.keys())[k]:
                Sams_A5 = x[i]*list(ver_var_Sams_A5.values())[k]
        for l in range(0,len(ver_var_Sams_S7)-1):
            if i==list(ver_var_Sams_S7.keys())[l]:
                Sams_S7 = x[i]*list(ver_var_Sams_S7.values())[l]
        for m in range(0,len(ver_var_Sams_S8)-1):
            if i==list(ver_var_Sams_S8.keys())[m]:
                Sams_S8 = x[i]*list(ver_var_Sams_S8.values())[m]
        for n in range(0,len(ver_var_Iphone_6S)-1):
            if i==list(ver_var_Iphone_6S.keys())[n]:
                Iphone_6S = x[i]*list(ver_var_Iphone_6S.values())[n]
        for o in range(0,len(ver_var_Iphone_7)-1):
            if i==list(ver_var_Iphone_7.keys())[o]:
                Iphone_7 = x[i]*list(ver_var_Iphone_7.values())[o]
        for p in range(0,len(ver_var_Len_K5)-1):
            if i==list(ver_var_Len_K5.keys())[p]:
                Len_K5 = x[i]*list(ver_var_Len_K5.values())[p]
        for q in range(0,len(ver_var_Len_K6)-1):
            if i==list(ver_var_Len_K6.keys())[q]:
                Len_K6 = x[i]*list(ver_var_Len_K6.values())[q]
        for r in range(0,len(ver_var_Len_X)-1):
            if i==list(ver_var_Len_X.keys())[r]:
                Len_X = x[i]*list(ver_var_Len_X.values())[r]
        for s in range(0,len(ver_var_Len_Z)-1):
            if i==list(ver_var__Len_Z.keys())[s]:
                Len_Z = x[i]*list(ver_var_Len_Z.values())[s]
    y=[str(Sams_A3),str(Sams_A5),str(Sams_S7),str(Sams_S8),str(Iphone_6S),str(Iphone_7),str(Len_K5),str(Len_K6),str(Len_X),str(Len_Z)]
    return y
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
    x = []
    good=0
    d = parse_qs(environ['QUERY_STRING'])
    Answer1 = d.get('Answer1',[None])[0]
    Answer2 = d.get('Answer2',[None])[0]
    Answer3 = d.get('Answer3',[None])[0]
    Answer4 = d.get('Answer4',[None])[0]
    Answer5 = d.get('Answer5',[None])[0]
    Answer6 = d.get('Answer6',[None])[0]
    Answer7 = d.get('Answer7',[None])[0]
    Answer8 = d.get('Answer8',[None])[0]
    x.append(Answer1)
    x.append(Answer2)
    x.append(Answer3)
    x.append(Answer4)
    x.append(Answer5)
    x.append(Answer6)
    x.append(Answer7)
    x.append(Answer8)
    if Answer1 and Answer2 and Answer3 and Answer4 and Answer5 and Answer6 and Answer7 and Answer8:
        try:
            for i in range(0,len(x)-1):
                x[i]=float(x[i])
            response_body=x[0]
            start_response(status, response_headers)
            yield response_body.encode()
        except:
            response_body="Пожалуйста, введите корректные значения.<br>"
            start_response(status, response_headers)
            yield response_body.encode()
    
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
