# Step / cost / balance / balance_day
msg_remember = """
Terminé: {} sur 10
Revenus des messages envoyés: {} CHF.

💰 Le solde de votre compte: {} CHF.

Montant gagné aujourd'hui: {} CHF.
"""


msg_ask_vocal = """
🗣 Enregistrez un message vocal avec la phrase:
«{}»

"""

gpt_samples = [
    "GPT, appelle Alex.", 
    "GPT, éteins le rétroéclairage sous le téléviseur.",
    "GPT, la chanson suivante.",
    "GPT, crée une playlist",
    "GPT, ouvre le calendrier",
    "GPT, la situation boursière",
    "GPT, commande à manger.",
    "GPT, trouve des billets de cinéma.",
    "GPT, ouvre YouTube.",
    "GPT, commande de la nourriture au restaurant.",
    "GPT, envoie un message à Sarah.",
    "GPT, ajuste la température à 22 degrés.",
    "GPT, active le mode silencieux.",
    "GPT, joue ma playlist préférée.",
    "GPT, mets une alarme pour 7 heures.",
    "GPT, montre-moi les actualités du jour.",
    "GPT, éteins toutes les lumières.",
    "GPT, lance la machine à café.",
    "GPT, prends une note.",
    "GPT, démarre le minuteur de 10 minutes.",
    "GPT, active le mode nuit.",
    "GPT, allume la télévision.",
    "GPT, envoie un email à l'équipe.",
    "GPT, cherche une recette de lasagne.",
    "GPT, lance un appel vidéo avec Paul.",
    "GPT, réserve une table pour deux au restaurant.",
    "GPT, affiche la météo de demain.",
    "GPT, joue le dernier épisode de ma série.",
    "GPT, mets la musique en pause.",
    "GPT, trouve une salle de sport à proximité.",
    "GPT, change l'éclairage en bleu.",
    "GPT, ajuste le volume à 50%.",
    "GPT, trouve un tutoriel pour Python.",
    "GPT, ouvre l'application de messagerie.",
    "GPT, active le mode économie d'énergie.",
    "GPT, désactive les notifications.",
    "GPT, commande des fleurs.",
    "GPT, programme une réunion pour demain.",
    "GPT, trouve un taxi.",
    "GPT, recherche des vols pour Paris.",
    "GPT, démarre l'aspirateur.",
    "GPT, joue la radio.",
    "GPT, vérifie mon agenda pour la semaine.",
    "GPT, trouve un bon restaurant italien.",
    "GPT, ajoute du lait à ma liste de courses.",
    "GPT, télécharge un podcast.",
    "GPT, lance un film.",
    "GPT, ferme les volets.",
    "GPT, vérifie mes mails.",
    "GPT, active la fonction Bluetooth.",
    "GPT, donne-moi la définition de l'IA.",
    "GPT, appelle un plombier.",
    "GPT, affiche mon historique de navigation.",
    "GPT, mets la musique de fond.",
    "GPT, donne-moi un rappel de mes tâches.",
    "GPT, augmente le chauffage de 2 degrés.",
    "GPT, trouve un hôtel à proximité.",
    "GPT, déverrouille la porte.",
    "GPT, arrête la diffusion."
]


msg_gpt_lst = [""]

msg_finish_vocal = """
✅ Vous avez terminé 10 des 10 missions possibles!
De nouvelles tâches apparaîtront dans 24 heures...

Tant qu'il n'y a pas de missions, vous pouvez gagner de l'argent supplémentaire sur cette chaîne 👇

"""

btn_finish_vocal = "✅ GAGNER ✅"

link_finish_vocal = "https://t.me/+X_rNaEmzJd8xZmYy"


msg_my_profile = """
👤 Mon profil:

name: {}
Nom d'utilisateur: {}
Solde du compte: {} CHF
Messages vocaux envoyés: {}
Personnes invitées: {}

"""

msg_statistics = """
📊 Statistiques des robots

👤 Utilisateurs de robots: {}
💰 Gagné par les utilisateurs: {}
🧠 Messages vocaux envoyés: {}
"""

msg_more_money = """
Plus d'argent 

OBTENEZ 150 CHF POUR L'ABONNEMENT À LA CHAÎNE 
Abonnez-vous à la chaîne et regardez les derniers messages, puis cliquez sur le bouton "Obtenir un bonus".  Après cela, vous recevrez 150 CHF ! 

REMARQUE : Si vous vous désabonnez de la chaîne du sponsor, le retrait sera annulé.
""" 

btn_more_money_1 = "📲 Abonnez-vous à la chaîne"
link_more_money_1 = "https://t.me/+X_rNaEmzJd8xZmYy"

btn_more_money_2 = "💰 Obtenez un bonus"

msg_not_subscribed = "Vous n'êtes pas abonné à la chaîne"
msg_subscribed = "Vous avez reçu un bonus"

msg_referal = """
💼 Obtenez des bonus pour les amis invités
📲 Envoyer le lien à un ami - https://t.me/{}?start={}

50 CHF - vous obtenez pour chaque ami que vous invitez.


Vous avez invité: {} (Nombre de personnes)"""


msg_best_player = """
📣  Aujourd'hui, vous êtes dans {} à la place 🏆

🎁 Pour recevoir une récompense, vous devez faire partie des 3 meilleurs joueurs pour l'équilibre 🎁
------------------
 Top 🥇
  Besoin d'équilibre: 980 CHF
 Bounty: 100 CHF
------------------ 
 Main 🥈
 Besoin d'équilibre: 700 CHF
 Bounty: 50 CHF
------------------
 Top 🥉
 Besoin d'équilibre: 550 CHF
 Bounty: 25 CHF


  équilibre: {} CHF
le joueur qui est au-dessus dans {} a plutôt un équilibre de: {} CHF

"""

msg_selection_withdraw = "Sélectionnez une méthode du retrait"

msg_withdraw = """
Saisissez le montant du retrait 👇
Par exemple : « 1000 »."""

btn_withdraw_cancel = "❌ Annulation"

msg_withdraw_error = "❌ Le montant du retrait est supérieur à votre solde"

msg_withdraw_minimal = "❌ Le montant du retrait est inférieur à 250 CHF"

msg_withdraw_confirm = """
📤 Demande de retrait de {} CHF confirmée"""