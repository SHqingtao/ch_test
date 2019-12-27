from flask import Flask, request, abort
import hashlib
import xmltodict
import time

WECHAT_TOKEN = 'chenguang'
app = Flask(__name__)


@app.route('/wx', methods=['GET', "POST"])
def wechat():
    """对接微信公众号服务器"""
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    # echostr = request.args.get('echostr')


    # 校验参数
    if not all([signature, timestamp, nonce]):
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
        if request.metnod == 'GTE':
            echostr = request.args.get('echostr')
            if not echostr:
                abort(400)
            return echostr
        if request.metnod == 'POST':  # 服务器转发消息
            xml_data = request.data
            if not xml_data:
                abort(400)
            xml_dict = xmltodict.parse(xml_data)
            msg_type = xml_dict.get('MsgType')

            if msg_type == 'text':
                resp_dict = {
                    "xml": {
                        "ToUserName": xml_dict.get('FromUserName'),
                        "FromUserName": xml_dict.get('ToUserName'),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": xml_dict.get('Content'),
                    }
                }
                resp_xml_str = xmltodict.unparse(resp_dict)
                return resp_xml_str
            else:
                resp_dict = {
                    "xml": {
                        "ToUserName": xml_dict.get('FromUserName'),
                        "FromUserName": xml_dict.get('ToUserName'),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": "",
                    }
                }
                resp_xml_str = xmltodict.unparse(resp_dict)
                return resp_xml_str


if __name__ == '__main__':
    app.run(port=80)
