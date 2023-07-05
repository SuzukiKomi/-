#作成したソースコード　
#サーバーのエンドポイントURL　https://us-central1-fibonacci-391904.cloudfunctions.net/fib?n=<正の整数>
#フレームワークはFlaskを使用する。
from flask import Flask, request, jsonify

app = Flask(__name__)

#フィボナッチ数を計算する関数を定義
def fibonacci(n):
    if n == 1:
        return 1 #nの値が1のときは1を返す
    elif n == 2:
        return 1 #nの値が2のときは1を返す
    else:
        #nの値が3以上のときはフォボナッチ数を返す
        return(fibonacci(n-1) + fibonacci(n-2))  

#エンドポイント'/fib'におけるデコレータ
@app.route('/', methods=["GET"])
def fib(request):
    n = request.args.get('n')  # リクエストパラメータ 'n' の値を取得
    if n is None:
        #クエリパラメータ'n'が指定されていないときにエラーを表示
        return 'Request parameter \'n\' is not specified.'
    if not n.isdigit():
        #nの値が0以上の整数ではないときにエラーを表示
        #nに数値以外が入力されたときもここでエラーを表示
        return 'Please enter a positive integer.'
    if int(n) < 1:
        #nの値が1未満のときにエラーを表示
        return 'Please enter a positive integer.'
    #nに1以上の正の整数が入力されたときにフィボナッチ数を返す
    result = fibonacci(int(n))
    #フィボナッチ数が返されたときに、フィボナッチ数と入力されたnの値を表示
    #JSON形式でフィボナッチ数と入力されたnの値を表示
    return jsonify({
        'n': int(n),
        'fibonacci_result': result
    })

#スクリプトが直接実行された場合にFlaskが開発用Webサーバーを起動し、
#アプリケーションを実行する。
if __name__ == '__main__':
    app.run(debug=False, host ='0.0.0.0', port=80)
