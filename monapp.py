import streamlit as st
st.set_page_config(page_title="Drea's Data Analyst Application",page_icon="💻️",
layout="wide",initial_sidebar_state="expanded")
import os as os
import pandas as pd
import plotly
import plotly.express as px
import random as r



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
	text-align:center; !important;
	font-family:'serif';
}}

.stTextinput > div > div > input{{
	background-color:{fond} !important;
	color:"white" !important;
	border:1px solid {accent} !important;
}}

[data-testid="stSidebar"]{{
	background-color:{accent} !important;
[data-testid="stSidebar"]*{{
	color:white !important;
}}

</style>
"""
st.markdown(css,unsafe_allow_html=True)


#NAVIGATION
st.sidebar.title("Navigation")
page=st.sidebar.radio("Aller à :",["Acceuil","Formulaire","Dashboard"])
st.sidebar.divider()
st.sidebar.info("""
	**FactoNotes**


	Apllication de collecte et d'analyse descriptive des données sur les facteurs de réussite académique.

	Dévelopée par:
	**SIEWE SANTHE Audrey Camila**
	
	Matricule : 24G2854
	
	L2 Informatique S&R -- UY1

	TP INF 232 EC2 -- 2025/2026
	""")
	

#FORMULAIRE
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
		app_dist=st.radio("Parmi ces applications laquelle vous distrait le plus ?",["TikTok","Whatsapp","Facebook","YouTube","Autre"])
		#Methode d'apprentissage
		meth_appr=st.radio("Quelle est votre méthode d'apprentissage?",["Seul","En groupe","Tutoriels YouTube/Internet","Fiches de revisions","Autre"])
		#Heures d'etuddes par jour
		time_etu=st.slider("Vous pouvez étudier combien d'heures par jour?",0,24,3)
		ON=st.radio("Disposez-vous de tout ce dont vous avez besoin pour étudier séreinement?",["Oui","Non"])
		NO=st.radio("Dors-tu suffisamment?",["Oui","Non"])
		sommeil=st.slider("En moyenne,combien d'heures de sommeil as-tu par nuit durant les périodes de cours?",0,12,7)
		espace_calme=st.radio("As-tu un espace calme pour étudier?",["Oui","Non"])
		#Raison 
		raison_manque=st.multiselect("Cause du manque de temps d'études suffisant:",["Réseaux Sociaux","Travaux ménagers","Problèmes financiers","Manque de motivation","Emploi de temps chargé","Autre"])
		raison_manque = ",".join(raison_manque)
		if not raison_manque:
			st.warning("Ces informations sont importantes pour l'analyse")

		so=st.form_submit_button("Envoyer")
	
	
	if so:
		
		if  not tps_ecran:
			st.warning("Cette information est importante pour l'analyse ")
		if not app_dist:
			st.warning("cette information est importante pour l'analyse")
		if not meth_appr:
			st.warning("Cette information est importante pour l'analyse")
		if not time_etu:
			st.warning("Cette information est importante pour l'analyse")	
		st.spinner("Enregistrement des données receuillies")

		donnees={"methode": meth_appr,"raison":raison_manque,"Heures_etudes":time_etu,"temps_ecran":tps_ecran,"niveau":niveau,"moy":moyenne,"app-distrayante":app_dist,"age":age}
		df=pd.DataFrame([donnees])
		df.to_csv("donnees.csv", mode ='a', header=not os.path.exists("donnees.csv"), index=False)
		st.success("Donnees Enregistrees avec succès !")
		st.balloons()
		st.success("Merci d'avoir remplit le formulaire!")
		
		#Profil de reussite
		st.subheader("Ton Profil d'Étudiant")
		if time_etu >= 5 and tps_ecran <= 3:
			st.success("Tu es un Aigle ! Discipliné et focalisé — continue comme ça !")
		elif time_etu <= 2 and tps_ecran >= 5:
			st.info("Tu es un Paresseux ! Réduis ton temps d'écran et augmente tes heures d'étude !")
		elif sommeil < 6:
			st.info("Tu es un Noctambule ! Le manque de sommeil nuit à ta concentration !")
		else:
			st.success("Tu es un Équilibré ! Bonne balance entre étude et repos !")
		
		#Coach recommendation
		st.divider()
		st.subheader("Tes conseils personnalisés")
		c1,c2=st.columns(2)
		with c1:
			if tps_ecran > 4:
				st.warning(f"⚠️ Attention : {tps_ecran}h d'écran par jour peut nuire à ta concentration.")
			else:
				st.success("✅ Bonne gestion du temps d'écran !")
		with c2:
			if app_dist == "TikTok":
				st.info("💡 Conseil : TikTok est une application conçue pour être addictives. Essaie de l'utiliser uniquement en récompense *après* l'étude et chronomètre tes pauses !")
			elif app_dist=="Facebook":
				st.info("💡 Conseil : TikTok est une application conçue pour être addictives. Essaie de l'utiliser uniquement en récompense *après* l'étude et chronomètre tes pauses !")
			elif app_dist == "WhatsApp":
				st.info("💡 Conseil : Coupe les notifications des groupes de discussion pendant tes révisions.")
			else:
				st.info("🚀 Continue comme ça, reste focus sur tes objectifs !")
		
		#Comparaison personnelle
		st.divider()
		st.subheader("📊 Ta comparaison avec les autres")
		if os.path.exists("donnees.csv"):
			df_all = pd.read_csv("donnees.csv")
			moy_etu=df_all["Heures_etudes"].mean()
			if time_etu > moy_etu:
				st.success(f" TU étudies {time_etu}h/jour. La moyenne est {moy_etu:.1f}h — Tu es au-dessus ! 🔥 ")
			else:
				st.warning(f"Tu étudies {time_etu}h/jour. La moyenne est {moy_etu:.1f}h — Tu peux faire mieux ! 💪")	
	
		def savecsv(df):
			df.to_csv()


#ACCEUIL
if page=="Acceuil" :
	st.title("FactoNotes")
	st.subheader("Qu'est ce qui influence ta moyenne?")
	citations =["Le succès c'est tomber 7 fois et se relever 8.🌟","L'éducation est l'arme la plus puissante. - Nelson Mandela 💪","Chaque expert a été un débutant. 🎯","Travaille en silence, laisse ton succès faire du bruit. 🔥","La discipline est le pont entre les objectifs et les résultats. 📚"]
	st.info(r.choice(citations))
	st.image("ILLUSTRATION.jpg",caption="Stats",use_container_width=True)
	#Sous-titre
	st.header("Bienvenue sur l'outil de collecte et d'analyse des données sur les facteurs liés à la réussite des étudiants .")
	col1,col2=st.columns(2)
	col1.metric("Collecte","✅ Active")
	col2.metric("Analyse","🚀 En temps réel")

	if os.path.exists("donnees.csv"):
		df_count=pd.read_csv("donnees.csv")
		nb=df_count.shape[0]
		st.success(f"🎓 Rejoins les {nb} étudiants qui ont déjà répondu !")
	else:
		st.info("Sois le premier à répondre !")	
	
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
	st.snow()
	df=enregistrer()
	st.sidebar.subheader("Filtres")
	niveaux=["Tous"] + list(df['niveau'].unique())
	filtre_niveau = st.sidebar.selectbox("Filtrer par niveau :",niveaux)
	if filtre_niveau!="Tous":
		df=df[df['niveau']==filtre_niveau]
	

	if not df.empty:
		st.subheader("Aperçu des données")
		st.dataframe(df)
		st.download_button(label="Télécharger les données",data=df.to_csv(index=False),file_name="factonotes_data.csv",mime="text/csv")
		
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
		st.metric("Correlation entre le temps devant les écrans et le temps d'études",f"{corr:2f}")
		if corr>0.3:
			st.success("Correlation positive forte: les étudiants qui passent plus de temps devant les écrans ont tendance à étudier plus longtemps.")
		elif corr< -0.3:
			st.warning("Correlation negative forte: les étudiants qui passent plus de temps devant les écrans ont tendance à moins étudier.")
		else:
			st.info("Correlation faible: il n'y'a pas de lien significatif entre le temps d'étude et le temps devant les écrans.")	
		
		corr1=df['Heures_etudes'].corr(df['moy'])
		st.metric("Correlation entre le temps d'étude et la moyenne obtenue",f"{corr1:2f}")
		if corr1>0.5:
			st.success(" Forte correlation : Plus l'étudiant étudie, plus sa moyenne grimpe. C'est mathématique !")
		elif corr1<=0.5:
			st.warning("Correlation negative: Étonnant, l'étude semble nuire à la moyenne ? (Vérifie la qualité des révisions).")
		else:
			st.info("Correlation faible: il n'y'a pas de lien significatif entre le temps devant les ecrans et la moyenne obtenue par un etudiant. Donc le temps d'étude seul n'explique pas tout. La méthode compte aussi!")
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

		st.subheader("Tableau de Fréquences")

		st.markdown("**Méthodes d'apprentissage**")
		freq=df['methode'].value_counts().reset_index()
		freq.columns = ['Méthode', 'Effectif']
		freq['Fréquence (%)'] = (freq['Effectif'] / freq['Effectif'].sum() * 100).round(2)
		st.dataframe(freq)

		st.markdown("**Applications distrayantes**")
		freq_a = df['app-distrayante'].value_counts().reset_index()
		freq_a.columns = ['Application', 'Effectif']
		freq_a['Fréquence (%)'] = (freq_a['Effectif'] / freq_a['Effectif'].sum() * 100).round(2)
		st.dataframe(freq_a)

		st.markdown("**Raisons du manque de temps**")
		freq_r = df['raison'].value_counts().reset_index()
		freq_r.columns = ['Raison', 'Effectif']


		st.write("**Répartition des moyennes par niveau d'études**")
		fig2 = px.box(df, x="niveau", y="moy", points="all",color="niveau", title="Où se situent les meilleures notes ?")
		st.plotly_chart(fig2, use_container_width=True)
		
		st.write("**Relation entre heures d'étude et moyenne**")
		fig_scatter=px.scatter(df,x="Heures_etudes",y="moy",color="niveau",title="Heures d'étude vs Moyenne obtenue",labels = {"Heures_etudes":"Heures d_etude/jour","moy":"Moyenne /20"})
		st.plotly_chart(fig_scatter,use_container_width=True)

		
				
	else:
		st.warning("Aucune données collectées pour le moment veuillez remplir le formulaire.")

	

st.caption("@ 2026 - Collecte et Analyse de données efficaces")
