from flask import Flask, request, abort
import hashlib

WECHAT_TOKEN = 'chenguang'
app = Flask(__name__)


@app.route('wechat8000')
def wechat():
    """对接微信公众号服务器"""
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')


    # 校验参数
    if not all([signature, timestamp, nonce, echostr]):
        abort(400)

    # 计算签名
    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    tmp_str = "".join(li)

    # 加密
    sign = hashlib.sha1(tmp_str).hexdigest()

    # 对比
    if signature != sign:
        abort(403)
    else:
        return echostr


if __name__ == '__main__':
    app.run(port=80, debug=True)
