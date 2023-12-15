# DataCraft_PersonalShopper

En aquest repositori es troba la documentació del Projecte de final de semestre d'Enginyeria del Programari.
Aquest projecte té com objectiu realitzar tot el procés de desenvolupament d'una aplicació per a un client.

La nostra empresa DataCraft Consulting, té com a objectiu principal satisfer les necessitats del nostre client.

Els membres de l'empresa són:

- Pol Riubrogent (Product Owner)
- Marc Puigbó (SCRUM Master)
- Abril Batalla (Software Architect)
- Arnau Busquets (UI/UX Designer)
- Paula Macías (Software Developer)

El repositori té dues carpetes, la primera pertany a la primera entrega; on podem trobar la captura de requisits, diagrames d'activitat, diagrames de seqüència, i el document SRS. Per altra banda a la segona entrega, trobem contingut com Diagrames UML, els wireframes de la aplicació, i la pàgina web, i per ultim una implementació de codi que descriurem a continuació:

# Backend
## Installation Guide
```
python3 –m venv venv
source venv/bin/activate
pip install –r requirements.txt
```

## Running the backend
```
uvicorn app.main:app --reload
```
### Interactive API docs
http://127.0.0.1:8000/docs

# Frontend
## Installation Guide
```
npm i
```
## Running the frontend
```
npm run dev
```
