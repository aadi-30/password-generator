from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')


def password():
    length = int(request.args.get('length', 12))
    num_special_chars = int(request.args.get('num_special_chars', 2))
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    symbols = '!@#$%^&*()_+-='
    all = lower + upper + num
    temp = random.sample(all, length - num_special_chars)
    temp += random.sample(symbols, num_special_chars)
    random.shuffle(temp)
    password = "".join(temp)
    return render_template('password.html', password=password)

@app.route('/password', methods=["POST"])
def password2():
    #project 2
    digits =[]
    symbols =[]
    letters=[]
    password = " "
    num_letters = int(request.form.get('num_letters', 12))
    num_special_chars = int(request.form.get('num_special_chars', 2))
    num_digits = int(request.form.get('num_digits', 2))
    
    for k in range(num_digits): #0,1,2,3
        digits.append(random.choice(string.digits))#choice 0 to 9
    for k in range(num_special_chars):#0,1,2,3
        symbols.append(random.choice(string.punctuation)) # select random symbols
    for k in range(num_letters):# 0,1,2
        letters.append(random.choice(string.ascii_letters))# choice random letters a-z to A-Z
    key =digits+symbols+letters #4digits+3symbols+2letters
    random.shuffle(key)  # using shuffle also
    print(f"Key after shuffle: {key}")
    for i in key: 
        password +=i #4digits+3symbols+2letters
    print(password) # print the password

    return render_template('password.html', password1=password)


@app.route('/')
def password_ui():
    return render_template('password.html')

if __name__ == '__main__':
    app.run(debug=True)
