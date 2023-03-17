#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


import openai


# In[ ]:


import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "5962a64ca9718cee44229006fb4f5c777a85c35c"
model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        p = request.form.get("txt")
        inputs = {"prompt":p}
        out = version.predict(**inputs)
        return(render_template("index.html",result=out[0]))
    else:
        return(render_template("index.html",result="waiting"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:




