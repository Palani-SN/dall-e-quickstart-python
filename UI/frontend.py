from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
app._static_folder = 'static'


@app.route('/')
def my_form():
    filename = 'index.html'
    return render_template(filename)


@app.route('/', methods=['POST'])
def my_form_post():
    prompt = request.form['Expression']
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    with open("templates/output.html", "r") as InpFile:
        init_html = InpFile.read()
    cond_html = init_html.replace("#COND_STR#", prompt)
    final_html = cond_html.replace("#IMAGE_URL#", image_url)
    return final_html


# main driver function
if __name__ == '__main__':

    import os

    filelist = [f for f in os.listdir("static/img/") if f != "About.JPG"]
    for f in filelist:
        os.remove(os.path.join("static/img/", f))

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
