from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rock_paper_scissors():
    if request.method == 'POST':
        user = request.form.get('choice')
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            result = "It's a tie!"
        elif is_winner(user, computer):
            result = "You won!"
        else:
            result = "You lost!"
        return render_template('game.html', result=result)
    return render_template('game.html', result=None)

def is_winner(player, opponent):
    if (player == "r" and opponent == "s") or \
       (player == "s" and opponent == "p") or \
       (player == "p" and opponent == "r"):
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
