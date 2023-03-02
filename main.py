import openai
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
    except Exception as e:

        print(e)
        return e
    return response["choices"][0]["message"]["content"]

@server.route("/chat")
def home():
    return render_template("chat.html")

@server.route("/chat/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
