from flask import Flask, render_template, request
import urllib.request, json

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

@app.route('/filmes/<parametros>')
def filmes(parametros):

	if parametros == 'populares':
		page_html = 'filmespopulares.html'
		url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1&api_key=74fdabc28b53a078461d75e8cd04eb28'
	if parametros == 'top_rated':
		page_html = 'filmetoprated.html'
		url = 'https://api.themoviedb.org/3/discover/tv?include_adult=false&language=en-US&page=1&sort_by=vote_average.desc&vote_count.gte=200&api_key=74fdabc28b53a078461d75e8cd04eb28'

	response = urllib.request.urlopen(url)

	dados = response.read()

	jsondata = json.loads(dados)

	return render_template(page_html, filmes=jsondata['results'])

if __name__ == '__main__':
	app.run(debug=True)		