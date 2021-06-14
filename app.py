from flask import Flask, jsonify, request
from lead import leads

# Prueba ping (Comprobar ruta 127.0.0.1:4000/ping)
app = Flask(__name__)
@app.route('/ping')
def ping():
    return jsonify({"message:":"pong!"})

@app.route('/leads')
def getLeads():
    return jsonify({"leads":leads, "message": "Lead's List"})

@app.route('/leads/<string:lead_name>')
def getLead(lead_name):
    leadsFound = [lead for lead in leads if lead['name'] == lead_name]
    if (len(leadsFound) > 0):
        return jsonify({"leads":leadsFound})
    return jsonify({"message:":"Leads not found"})

@app.route('/leads', methods=['POST'] )
def addLead():
    print(request.json)
    new_lead ={
        "name": request.json['name'],
        "email": request.json['email'],
        "messaje": request.json['messaje']
    }
    leads.append(new_lead)
    return jsonify({"message:":"Product added succesfully", "leads":leads})

@app.route('/leads/<string:lead_name>', methods=['PUT'])
def editLead(lead_name):
    leadsFound = [lead for lead in leads if lead['name'] == lead_name]
    if (len(leadsFound) > 0):
        leadsFound[0]['name'] = request.json['name']
        leadsFound[0]['email'] = request.json['email']
        leadsFound[0]['messaje'] = request.json['messaje']
        return jsonify({"message:":"Product edited succesfully", "leadsFound":leadsFound})
    return jsonify({"message:":"Leads not found"})

@app.route('/leads/<string:lead_name>', methods=['DELETE'])
def deleteLead(lead_name):
    leadsFound = [lead for lead in leads if lead['name'] == lead_name]
    if (len(leadsFound) > 0):
        leads.remove(leadsFound)
        return jsonify({"message:":"Product deleted succesfully", "leads":leads})
    return jsonify({"message:":"Leads not found"})

if __name__== '__main__':
    app.run(debug=True, port=4000)