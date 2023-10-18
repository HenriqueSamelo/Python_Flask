from flask import Flask, render_template, request

app = Flask(__name__)

frutas = []
registros = []

@app.route('/', methods=["GET", "POST"])
def Home():
	#frutas = ['Morango','Uva','Laranja','Mamão','Maça']

	if request.method == "POST":
		if request.form.get("Fruta"):
			frutas.append(request.form.get("Fruta"))
	return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def Sobre():
	#notas = {'Henrique':10.0,'Matheus':8.0,'Ingrid':10000,'Cristina':1000000000}
	if request.method == "POST":
		if request.form.get("aluno") and request.form.get("nota"):
			registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
	return render_template("sobre.html", registros=registros)

if __name__ == '__main__':
	app.run(debug=True)		