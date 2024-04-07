from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'any secret string'

def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'Tie' 
    return None  

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = [' ' for _ in range(9)]
        session['turn'] = 'X'
        session['result'] = None  
    elif 'result' not in session:  
        session['result'] = None  
    return render_template('index.html', board=session['board'], turn=session['turn'], result=session['result'])

@app.route('/move/<int:cell>')
def move(cell):
    if session['board'][cell] == ' ' and session['result'] is None:
        session['board'][cell] = session['turn']
        winner = check_winner(session['board'])
        if winner:
            session['result'] = f"{winner} wins!"
        elif winner == 'Tie':
            session['result'] = "It's a tie!"
        session['turn'] = 'O' if session['turn'] == 'X' else 'X'
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('board', None)
    session.pop('turn', None)
    session.pop('result', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
