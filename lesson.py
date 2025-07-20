from pywebio.input import input, actions
from pywebio.output import put_text, put_success
from pywebio import start_server

def app():
    name = input("ما اسمك؟")
    put_text(f"مرحباً، {name} 👋")

    action = actions('ماذا تريد أن تفعل؟', buttons=[
        {'label': 'قل مرحباً', 'value': 'hello'},
        {'label': 'خروج', 'value': 'exit'}
    ])

    if action == 'hello':
        put_success(f"مرحباً مرة أخرى يا {name}!")
    else:
        put_text("مع السلامة!")

# اجعل التطبيق يعمل على أي عنوان (0.0.0.0) والمنفذ يُحدد من البيئة
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    start_server(app, host='0.0.0.0', port=port)
