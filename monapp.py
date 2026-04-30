import streamlit as st
st.set_page_config(page_title="Drea's Data Analyst Application",page_icon="💻️",
layout="wide",initial_sidebar_state="expanded")
import os as os
import pandas as pd
import plotly
import plotly.express as px

st.snow()

#Fonction d'enregistrement des donnees collectees
def enregistrer(fichier="donnees.csv"):
	
			if os.path.exists(fichier):
				return pd.read_csv(fichier)
			return pd.DataFrame()
#Css de mon app
#palette de couleurs a utiliser
fond="#ADD4ED"
accent="#2E86C1"
texte="#FFFFFF"
boutons="#E67E22"
css=f"""
<style>
html,body,[data-testid="stAppViewContainer"]{{
	background-color:{fond} !IMPORTANT;
	color:{texte}
	text-align:center;
h1,h2,h3{{
	color:{accent} !important;
	text-align:center !important;
	font-family:'serif';
}}

.stTextinput > div > div > input{{
	background-color:{fond} !important;
	color:"white" !important;
	border:1px solid {accent} !important;
}}

[data-testid="stSidebar"]{{
	background-color:{accent} !important;
}}

</style>
"""
st.markdown(css,unsafe_allow_html=True)


#NAVIGATION
st.sidebar.title("Navigation")
page=st.sidebar.radio("Aller à :",["Acceuil","Formulaire","Dashboard"])
bar=st.sidebar.progress(0)
for i in range(1,9):
	print(i*2)
	bar=i*2


#FORMMULAIRE
if page=="Formulaire" :
	st.header("📝 Questionnaire")
	st.write("En 2 minutes,participez à notre enquête sur les habitudes d'étude et aidez-nous à comprendre les clés de la réussite académique ! ")
	st.write("Veuillez remplir toutes les champs de ce formulaire")
	with st.form("Formulaire de collecte"):
		#prenom = st.text_input("Votre prenom :")
		age = st.slider("Votre âge :",15,40,18)
		niveau = st.radio("Niveau d'études actuel :",["Licence I","Licence II","Licence III","Master I","Master II"])
		Filière = st.text_input("Quelle est votre filière ? :")
		#Moyenne generale 
		moyenne=st.slider("Quelle était votre moyenne générale pondérée l'année précédente?:",0.00,20.00,10.00)
		#Nombre d'heures passees devant les ecrans
		tps_ecran=st.slider("Combien de temps passez-vous devant un écran par jour (en Heures)? ",0.00,24.00,3.00)
		#App distrayante
		app_dist=st.radio("App la plus distrayante ?:",["TikTok","Whatsapp","Facebook","YouTube","Autre"])
		#Methode d'apprentissage
		meth_appr=st.radio("Quelle est votre méthode d'apprentissage?",["Seul","En groupe","Tutoriels YouTube/Internet","Fiches de revisions","Autre"])
		#Heures d'etuddes par jour
		time_etu=st.slider("Vous pouvez étudier combien d'heures par jour?",0,24,3)
		ON=st.radio("Disposez-vous de tout ce dont vous avez besoin pour étudier séreinement?",["Oui","Non"])
		#Raison 
		raison_manque=st.multiselect("Cause du manque de temps d'études suffisant:",["Réseaux Sociaux","Travaux ménagers","Problèmes financiers","Manque de motivation","Emploi de temps chargé","Autre"])
		raison_manque = ",".join(raison_manque)
		if not raison_manque:
			st.warning("Ces informations sont importantes pour l'analyse")

		so=st.form_submit_button("Envoyer")
	if  not tps_ecran:
		st.warning("Cette information est importante pour l'analyse ")
	if not app_dist:
		st.warning("cette information est importante pour l'analyse")
	if not meth_appr:
		st.warning("Cette information est importante pour l'analyse")
	if not time_etu:
		st.warning("Cette information est importante pour l'analyse")	
	st.spinner("Enregistrement des données receuillies")

	
	if so:
		import pandas as pd
		import os as os
		donnees={"methode": meth_appr,"raison":raison_manque,"Heures_etudes":time_etu,"temps_ecran":tps_ecran,"niveau":niveau,"moy":moyenne,"app-distrayante":app_dist,"age":age}
		df=pd.DataFrame([donnees])
		df.to_csv("donnees.csv", mode ='a', header=not os.path.exists("donnees.csv"), index=False)
		
		st.success("Donnees Enregistrees avec succès !")
		#st.success("Envoyé avec succès")
		st.form(clear_on_subbmit=True)
		def savecsv(df):
			df.to_csv()
#ACCEUIL
if page=="Acceuil" :
	st.title("FactoNotes")
	st.subheader("Qu'est ce qui influence ta moyenne?")
	#st.image("/home/santacamila/Téléchargements/ILLUSTRATION.jpg",caption="Illustration",use_container_width=True)
	#Sous-titre
	st.header("Bienvenue sur l'outil de collecte et d'analyse des données sur les facteurs liés à la réussite des étudiants .")
	col1,col2=st.columns(2)
	col1.metric("Collecte","✅ Active")
	col2.metric("Analyse","🚀 En temps réel")
	
	st.markdown("Alors , prêt pour la découverte de fonctionnalités de cette application qui vous fera découvrir les facteurs de la réussite académique?")
	st.markdown("Let's Go! ")
	col1,col2,col3=st.columns(3)
	with col1:
		st.info("Collecte De Données ")
		st.text("Procéder à la collecte des données à analyser à travers le remplissage des champs du formulaire ")
	#with col2:
		#st.info("")
		#st.text("Explorer comment fonctionne mon app avec des donnes de test")
	with col3:
		st.info("Analyse Et visualisation")
		st.text("Procéder au traitememt et à l'analyse des donnees préalablement collectées et observer une visualisation de representation de ces dernières")
	nom=st.text_input("Veuillez entrer votre nom")
	import datetime
	debut=datetime.datetime.now().hour
	if nom:
		if debut < 12:
			st.write("Bonjour",nom,"!")
		else:
			st.write("Bonsoir",nom,"!")

#DASHBOARD
if page == "Dashboard":
	st.title("Analyse des Données")

	df=enregistrer()

	if not df.empty:
		st.subheader("Aperçu des données")
		st.dataframe(df)

		
		col1,col2,col3=st.columns(3)
		with col1:
			st.write("Nombre Total De Repondants")
			st.metric("Déja au total",f"{df.shape[0]} étudiants")
		with col2:
			st.write("Moyenne d'heures d'etudes")
			st.metric("En moyenne",f"{df['Heures_etudes'].mean():.2f}h")
		with col3:
			st.write("Moyenne Des Heures D'Ecran")
			st.metric("En moyenne",f"{df['temps_ecran'].mean():.2f}h")

		st.subheader("📊 Statistiques Descriptives")
		st.markdown("Heures d'études")
		col1,col2,col3,col4=st.columns(4)
		col1.metric("Mediane:",f"{df['Heures_etudes'].median():.2f}h")
		col2.metric("Ecart-Type",f"{df['Heures_etudes'].std():.2f}h")
		col3.metric("Min",f"{df['Heures_etudes'].min():.2f}h")
		col4.metric("Max",f"{df['Heures_etudes'].max():.2f}h")

		st.markdown("Temps d'écran")
		col1,col2,col3,col4=st.columns(4)
		col1.metric("Mediane:",f"{df['temps_ecran'].median():.2f}h")
		col2.metric("Ecart-Type",f"{df['temps_ecran'].std():.2f}h")
		col3.metric("Min",f"{df['temps_ecran'].min():.2f}h")
		col4.metric("Max",f"{df['temps_ecran'].max():.2f}h")

		corr=df['Heures_etudes'].corr(df['temps_ecran'])
		st.metric("Correlation entre le temps devant les écrans et le temps d'études",corr)
		if corr>0.5:
			st.metric("Correlation positive forte: les étudiants qui passent plus de temps devant les écrans ont tendance à étudier plus longtemps.")
		elif corr<0.5:
			st.metric("Correlation negative forte: les étudiants qui passent plus de temps devant les écrans ont tendance à moins étudier.")
		else:
			st.info("Correlation faible: il n'y'a pas de lien significatif entre le temps d'étude et le temps devant les écrans.")	
		
		corr1=df['Heures_etudes'].corr(df['moyenne'])
		st.metric("Correlation entre le temps d'étude et la moyenne obtenue")
		if corr>0.5:
			st.metric("Correlationrrelation positive forte: les étudiants qui accordent le plus de leur temps à l'étude ont tendance à obtenir une Moyenne plus grande. ")
		elif corr<=0.5:
			st.info("Correlation negative forte: les etudiants qui consacre le plus temps aux études ont tendance à avoir une Moyenne faible")	
		else:
			st.info("Correlation faible: il n'y'a pas de lien significatif entre le temps devant les ecrans et la moyenne obtenue par un etudiant.")
		#Graphiques 
		st.subheader("Graphiques")
		#Camembert
		st.write("**Repartition des distractions**")
		fig = px.pie(df,names="app-distrayante",title="Camembert de distractions")
		st.plotly_chart(fig,use_container_width=True)

		#Diagrammes en barres methodes d'apprentissage
		st.write("**Barres des Méthodes d'Apprentissage**")
		freq_meth = df['methode'].value_counts().reset_index()
		freq_meth.columns=['methode','nombre d_étudiants']
		fig=px.bar(freq_meth,x="methode",y="nombre d_étudiants",title="Methodes d'apprentissage")
		st.plotly_chart(fig,use_container_width=True)

		#Diagrammes en barres raison manque de temps
		st.write("**Barres de raison de manque de temps pour l'etude**")
		freq_raison=df['raison'].value_counts().reset_index()
		freq_raison.columns=['raison','nombre d_étudiants']
		fig=px.bar(freq_raison,x="raison",y="nombre d_étudiants",title="Raison du manque d'etude")
		st.plotly_chart(fig,use_container_width=True)


		

		
				
	else:
		st.warning("Aucune données collectées pour le moment veuillez remplir le formulaire.")

	

st.caption("@ 2026 - Collecte et Analyse de données efficaces")
