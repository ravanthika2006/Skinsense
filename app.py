from flask import Flask,request
app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
   if request.method == "POST": 
     oily = request.form.get("oily")
     dry = request.form.get("dry")
     acne = request.form.get("acne")
     flaky = request.form.get("flaky")
     if oily == "yes" and dry == "yes":
        result = "combination"
     elif oily == "yes" or acne == "yes":
        result = "oily"
     elif dry == "yes" or flaky == "yes":
        result = "dry"
     else:
        result = "normal"

     return f"<h2> Your skin type is {result}</h2> <a href = '/'>Go back</a>"

   return """
<h1> Welcome to SkinSense</h1>
<h2> Your skin care companian </h2> 

<form method = "post">  

   <p> Does your skin feel oily frequently?</p>
   <input type = "radio" name = "oily" value = "yes" required> Yes
   <input type = "radio" name = "oily" value = "no"> No 

   <p> Do you experience frequent acne formation? </p>
   <input type ="radio" name = "acne" value = "yes" required> Yes
   <input type = "radio" name = "acne" value = "no"> No 

   <p> Does your skin get dry easily? </p>
   <input type ="radio" name = "dry" value = "yes" required> Yes
   <input type = "radio" name = "dry" value = "no"> No

   <p> Does your skin feel flaky? </p>
   <input type ="radio" name = "flaky" value = "yes" required> Yes
   <input type= "radio" name = "flaky" value = "no"> No
 
<button type = "submit">Check</button> 
</form|> 
      """
if __name__ == "__main__":
   app.run(debug = True)


     
