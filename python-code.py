from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database (in-memory list)
budgets = []

@app.route('/')
def index():
    return render_template('index.html', budgets=budgets)

@app.route('/add_budget', methods=['POST'])
def add_budget():
    name = request.form.get('name')
    amount = float(request.form.get('amount'))

    budget = {'name': name, 'amount': amount}
    budgets.append(budget)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
