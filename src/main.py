from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	f = open("raf.csv","r")
	redovi = f.readlines()	
	svi_predavaci = [red.split(',')[2] for red in redovi]
	uniqpredavaci = []
	for predavaci in svi_predavaci:
		if predavaci not in uniqpredavaci:
			uniqpredavaci.append(predavaci)	
	
	sve_ucionice = [red.split(',')[6] for red in redovi]
	uniqucionice = []
	for ucionica in sve_ucionice:
		if ucionica not in uniqucionice:
			uniqucionice.append(ucionica)

	svi_predavaci = uniqpredavaci.sort()
	sve_ucionice = uniqucionice.sort()

	return render_template("index.html",redovi = redovi,sve_ucionice = uniqucionice, svi_predavaci = uniqpredavaci)



if __name__ == '__main__':
	app.run()