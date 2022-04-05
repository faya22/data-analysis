import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes = "text-h2 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text = "These graphs")

    return wp
jp.justpy(app)

