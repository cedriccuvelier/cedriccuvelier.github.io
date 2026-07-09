
define i = Character("Instructions", color="#50CD33")
define cpc = Character("Pauline Bouysse", color="#0056f5")
define ien = Character("Jeanne Tille", color="#de00aa")
define directeur = Character("Pierre Haffeux", color="#2E86C1")

default score_pedagogique = 0
default score_max = 20

# Le jeu commence ici
label start:
stop music
scene ecrannoir
menu:
    "Chapitre 1":
        jump chapitre1
    "Chapitre 2":
        jump chapitre2
    "Chapitre 3":
        jump chapitre3
    "Chapitre 4":
        jump chapitre4
    "Chapitre 5":
        jump chapitre5

# Chapitre 1 #
label chapitre1:
play music "audio/oiseaux.mp3" volume 0.5
"Été 2027... "
scene universite
with Dissolve(2.0)
"Le soleil estival darde ses rayons à travers les vitres de la salle de classe. Le formateur annonce la fin du dernier cours de l'année."
with Dissolve(0.5)
"C'est votre dernier jour à l'INSPÉ de Valenciennes."
stop music
with Dissolve(0.5)
scene etudiants_en_classe
"Vous prenez quelques secondes pour regarder autour de vous les visages familiers de vos camarades de promotion. Certains sourient, d'autres semblent déjà ailleurs."
with Dissolve(0.5)
"Vous pensez à l'année qui vient de s'écouler, aux stages, aux réussites, à vos doutes aussi."
with Dissolve(0.5)
"Avec la fin de votre formation initiale, c'est une page importante de votre vie qui se tourne."
with Dissolve(0.5)
"Votre vie étudiante s'achève et, très bientôt, vous allez entrer pleinement dans la vie professionnelle."
scene vacances 
play music "audio/plage.mp3" volume 0.5
with Dissolve(0.5)
"Mais pour l'heure. Ce sont les vacances qui commencent. Et vous comptez profiter de ces jours de repos mérités qui s'annoncent."
with Dissolve(0.5)
"Face à la mer, sur le sable chaud vous pensez à la rentrée à venir."
with Dissolve(0.5)
"Où serez-vous affecté ? Quel niveau aurez-vous en charge ?"
with Dissolve(0.5)
"Vous vous endormez avec ces questions qui restent sans réponses..."
with Dissolve(0.5)
stop music
scene ecrannoir
with Dissolve(1.0)
"Quelques jours après votre retour..."
scene courrier
with Dissolve(2.0)
"Vous apercevez à la fenêtre la factrice qui distribue le courrier et dépose une enveloppe dans votre boîte aux lettres."
with Dissolve(0.5)
"Vous sortez chercher la lettre pour satisfaire votre curiosité, rentrez et ouvrez l'enveloppe sans attendre. "
with Dissolve(0.5)
scene affectation
with Dissolve(0.5)
"C'est votre affectation."
with Dissolve(0.5)
"Vous serez à la rentrée à l'école maternelle Baruch Spinoza à Jardincourt. Vous occuperez ce poste un jour par semaine." 
with Dissolve(0.5)
"Les autres affectations vous seront communiquées par la suite."
with Dissolve(0.5)
i "Demandez à monsieur Cuvelier le document Affectation et consultez le."
with Dissolve(0.5)
scene smartphone
with Dissolve(2.0)
play sound "audio/appel.mp3" volume 0.5
"Après une recherche rapide vous trouvez le numéro de l'école et vous tentez d'appeler en espérant que quelqu'un décroche."
with Dissolve(0.5)
stop sound
"Par chance le directeur est présent et répond à l'appel."
with Dissolve(0.5)
"Il s'exprime avec bienveillance. Vous vous présentez et demandez s'il est possible de visiter l'école."
with Dissolve(0.5)
"Malheureusement il doit s'absenter quelques jours et personne ne sera présent dans l'établissement."
with Dissolve(0.5)
"Il vous informe qu'il va vous envoyer par courrier les documents nécessaires pour commencer à préparer votre travail."
with Dissolve(0.5)
"Il vous communique également les coordonnées des collègues qui partageront la classe avec vous les autres jours de la semaine."
with Dissolve(0.5)
scene ecrannoir
with Dissolve(1.0) 
scene documents
with Dissolve(2.0)
"Quelques jours plus tard vous recevez une grande enveloppe. À l'intérieur, les documents envoyés par le directeur."
with Dissolve(0.5)
i "Demandez à monsieur Cuvelier de vous donner l'enveloppe, ouvrez-la puis passez à la page suivante."
with Dissolve(0.5)
i "Prenez les documents : liste des élèves, photos de l'école, plan de la classe et projet d'école. Prenez le temps de les lire et de relever les informations utiles."
with Dissolve(0.5)
scene smartphone
with Dissolve(2.0)
play sound "audio/appel.mp3" volume 0.5
"Vous contactez les collègues avec qui vous partagerez la classe pour organiser une rencontre de travail."
with Dissolve(0.5)
stop sound
"Tous acceptent de venir préparer la rentrée. Un rendez-vous est fixé."
with Dissolve(0.5)
play music "audio/sonnerie.mp3" volume 0.5
"Quelques heures après une conseillère pédagogique vous contacte." 
with Dissolve(0.5)
stop music
"Elle vous annonce qu'elle va vous accompagner cette année."
with Dissolve(0.5)
"Vous lui parlez de la rencontre programmée avec les collègues de l'école. Elle propose de venir vous aider car vous sortez tous de l'INSPÉ."
with Dissolve(0.5)
"Vous acceptez."
with Dissolve(0.5)
scene bureau
with Dissolve(1.0)
"Le jour du rendez-vous arrive."
with Dissolve(0.5)
"Vous êtes réunis pour la première fois avec les collègues qui partageront votre classe."
with Dissolve(0.5)
play music "audio/sonnerie.mp3" volume 0.5
"Après quelques minutes où vous vous présentez les uns aux autres, votre téléphone se met à sonner."
with Dissolve(0.5)
stop music
"C'est la conseillère pédagogique qui vous annonce son arrivée. Vous lui indiquez où vous êtes et elle vous rejoint. "
with Dissolve(0.5)
show viviane
cpc "Bonjour. Je suis Pauline Bouysse, conseillère pédagogique de l'IEN du Val du Cygne."
with Dissolve(0.5)
hide viviane
show viviane2
cpc "Je vais vous accompagner dans vos premiers pas et je vous propose de vous aider aujourd'hui."
with Dissolve(0.5)
cpc "Votre école a été choisie par l’inspection pour mener une expérimentation sur l’aménagement des espaces pour mieux apprendre et la mise en place de « pôles d’attractivité »"
with Dissolve(0.5)
cpc "C'est un projet dont nous parlerons plus tard."
with Dissolve(0.5)
cpc "Je viendrai vous rendre visite en classe plusieurs fois."
with Dissolve(0.5)
cpc "Vous devrez présenter ce que vous avez mis en oeuvre devant d'autres enseignants débutants à la fin de l'année."
with Dissolve(0.5)
hide viviane2
show viviane4
play sound "audio/clap.mp3" volume 0.5
cpc "Pour l'heure, il vous faut commencer à préparer la rentrée."
with Dissolve(0.5)
hide viviane4
show viviane2
cpc "En cours d'approches pédagogiques à l'INSPÉ, vous avez vu avec Monsieur Cuvelier où trouver des ressources institutionnelles."
with Dissolve(0.5)
# LABEL 1#
label inventaire:
scene bureau
show viviane3
with Dissolve(0.5)
cpc "Je vous demande de faire l'inventaire, de hiérarchiser et, si possible, de télécharger les documents qui vous seront utiles."
with Dissolve(0.5)
i "Vous devez créer sur Nextcloud un dossier partagé dans lequel vous copierez et classerez : les programmes, les guides, les livrets d'accompagnement des nouveaux programmes et tout ce qui vous semblera utile dans le cadre de cette affectation en maternelle."
with Dissolve(0.5)
hide viviane3
show viviane5
menu:
    cpc "Avez-vous terminé le travail demandé ?"
    "Oui":
        hide viviane5
        show viviane4
        play sound "audio/clap.mp3" volume 0.5
        cpc "Bravo. Je vous félicite. C'est un travail qui vous a sans doute pris du temps mais qui vous sera utile."
        with Dissolve(0.5)
        jump site_dsden
    "Non":
        hide viviane5
        show viviane
        cpc "Au travail. Si vous éprouvez des difficultés avec cet exercice, vous pouvez contacter monsieur Cuvelier pour vous aider."
        jump inventaire
# LABEL 2#
label site_dsden:
scene bureau
show viviane
cpc "La DSDEN du Nord a mis en ligne des ressources pour la maternelle. Je vous invite à les consulter."
with Dissolve(0.5)
hide viviane
show viviane5
menu:
    cpc "Avez-vous consulté le site ?"
    "Oui":
        hide viviane5
        show viviane4
        play sound "audio/clap.mp3" volume 0.5
        cpc "Très bien, retenez que vous pourrez y trouver des informations en complément du contenu d'Eduscol."
        with Dissolve(0.5)
        jump modalites
    "Non":
        hide viviane5
        show viviane
        cpc "Le site est à l'adresse https://pedagogie-nord.ac-lille.fr. Si vous éprouvez des difficultés avec cet exercice, vous pouvez contacter monsieur Cuvelier pour vous aider."
        jump site_dsden
# LABEL 3 #
label modalites:
scene bureau
show viviane
cpc "Je souhaite voir mises en oeuvre les différentes modalités d'apprentissage à l'école maternelle. Donnez des exemples de ce que vous pourriez proposer."
with Dissolve(0.5)
i "Essayez pour chaque modalité d'apprentissage de trouver des exemples de mise en pratique dans votre future classe."
hide viviane
show viviane5
menu:
    cpc "Avez-vous réussi l'exercice ?"
    "Oui":
        hide viviane5
        show viviane
        cpc "Très bien, passons à la suite."
        with Dissolve(0.5)
        jump docs_visite
    "Non":
        hide viviane5
        show viviane
        cpc "Relisez le cours et aidez-vous des ressources qui sont maintenant à votre disposition. Si vous éprouvez des difficultés avec cet exercice, vous pouvez contacter monsieur Cuvelier pour vous aider."
        jump modalites
# LABEL 4 #
label docs_visite :
scene bureau
show viviane5
cpc "D'après-vous, quels documents devrez-vous présenter lors de ma première visite ?"
with Dissolve(0.5)
menu:
    cpc "Pensez-vous avoir trouvé ?"
    "Oui":
        hide viviane5
        show viviane
        cpc "Très bien, vérifiez avec Monsieur Cuvelier votre réponse."
        with Dissolve(0.5)
        jump verif_docs_visite
    "Non":
        hide viviane5
        show viviane
        cpc "Aidez-vous d'internet. Vous devriez trouver. Vous pouvez appeler monsieur Cuvelier en cas de besoin."
        jump docs_visite
# LABEL 4_1 #
label verif_docs_visite:
hide viviane
show viviane5
menu:
    cpc "Monsieur Cuvelier a-t-il validé votre réponse ou vous a-t-il donné les éléments qui vous manquaient ?"
    "Oui":
        hide viviane5
        show viviane
        cpc "Très bien."
        with Dissolve(0.5)
        jump fin
    "Non":
        hide viviane5
        show viviane
        cpc "Continuez à chercher. Je suis persuadé que vous allez trouver. Vous pouvez consulter internet pour vous aider."
        jump docs_visite
# LABEL 5 #
label fin :
cpc "À présent je vous laisse réfléchir seuls. Commencez à penser à la manière dont vous allez organiser la classe et les apprentissages."
with Dissolve(0.5)
i "Terminez la séance en réfléchissant ensemble à l'aménagement et l'organisation de votre classe. N'oubliez pas que vous devrez présenter votre projet lors de la dernière séance."
cpc "À bientôt."
with Dissolve(0.5)
"Fin"
jump start

# Chapitre 2 #
label chapitre2:
"Plusieurs jours se sont écoulés depuis votre rencontre avec Pauline Bouysse, la conseillère pédagogique qui vous accompagne."
with Dissolve(0.5)
"Depuis, vous avez beaucoup pensé à votre classe et attendez avec impatience de pouvoir visiter l'école."
with Dissolve(0.5)
scene smartphone
with Dissolve(2.0)
play sound "audio/sonnerie.mp3" volume 0.5
"Votre téléphone sonne."
with Dissolve(0.5)
stop sound
"C'est Pauline Bouysse. Elle vous donne rendez-vous au lieu de votre précédente rencontre dans le cadre de votre accompagnement."
with Dissolve(0.5)
"Elle vous explique qu'elle a aussi invité les collègues qui partageront votre classe pour que vous puissiez travailler ensemble."
with Dissolve(0.5)
scene bureau
with Dissolve(1.0)
"Le jour du rendez-vous arrive."
with Dissolve(0.5)
"Vous rejoignez le lieu de la rencontre. Vos collègues et Pauline Bouysse sont déjà présents et vous attendaient."
with Dissolve(0.5)
show viviane2
cpc "Bonjour. C'est parfait vous êtes à l'heure. Nous allons pouvoir commencer."
with Dissolve(0.5)
cpc "Dans le cadre de votre accompagnement, je souhaite voir mis en place au moins un espace jeu symbolique dans votre classe."
with Dissolve(0.5)
cpc "De plus, je vous informe que vous présenterez cet espace à d'autres jeunes enseignants que j'accompagne également à la fin de cette année."
with Dissolve(0.5)
hide viviane2
show viviane5
menu:
    cpc "Avez-vous besoin de mon aide ?"
    "Oui":
        hide viviane5
        show viviane
        cpc "Très bien."
        with Dissolve(0.5)
        jump aide_coin_jeu
    "Non":
        hide viviane5
        show viviane
        cpc "Mauvaise réponse. N'oubliez pas que savoir identifier vos besoins de formation fait partie de votre référentiel de compétences."
        with Dissolve(0.5)
        jump aide_coin_jeu

label aide_coin_jeu:
hide viviane
show viviane2
cpc "J'avais animé avec Monsieur Cuvelier une formation sur l'aménagement des espaces de l'école il y a quelques temps."
with Dissolve(0.5)
cpc "Nous avions proposé aux enseignants plusieurs activités au choix, dont la création d'un espace jeu."
with Dissolve(0.5)
hide viviane2
show viviane6
cpc "Vous trouverez dans cette enveloppe une sélection de documents et d'outils qui proviennent de cette formation."
with Dissolve(0.5)
i "Demandez à monsieur Cuvelier de vous donner l'enveloppe, ouvrez-la puis passez à la page suivante."
with Dissolve(0.5)
hide viviane6
show viviane2
cpc "Vous disposez à présent de l'aide nécessaire pour commencer à réfléchir au coin jeu que vous devrez mettre en place."
with Dissolve(0.5)
hide viviane2
show viviane4
play sound "audio/clap.mp3" volume 0.5
cpc "Au travail !"
with Dissolve(0.5)
hide viviane4
show viviane
cpc "Je vous laisse réfléchir ensemble. N'hésitez pas à demander de l'aide en cas de besoin."
with Dissolve(0.5)
jump start

# Chapitre 3 #
label chapitre3:
play sound "audio/reveil.mp3" volume 0.5
scene rue_matin
"Une nouvelle semaine commence. Aujourd'hui, vous et vos jeunes collègues avez rendez-vous avec la conseillère pédagogique pour faire un point sur l'avancée de votre travail de préparation."
with Dissolve(0.5)
"Pauline Bouysse vous a donné rendez-vous dans son bureau, à l'inspection du Val du Cygne."
with Dissolve(0.5)
"Vous rassemblez vos affaires et prenez la route."
with Dissolve(0.5)
scene inspection_ext
"Le GPS indique que vous êtes arrivé."
with Dissolve(0.5)
"Vos collègues sont sur le parking, garés près de vous. Ils vous attendaient pour sonner."
with Dissolve(0.5)
"Vous sortez de la voiture et vous dirigez ensemble vers l'entrée du bâtiment."
with Dissolve(0.5)
stop sound
scene inspection_ext2
play sound "audio/sonnerie_porte.mp3"
pause
scene inspection 
show inspectrice6
ien "Bonjour, entrez donc !"
with Dissolve(0.5)
hide inspectrice6
show inspectrice5
ien "Je me présente : je suis Jeanne Tille, inspectrice de la circonscription du Val du Cygne. Je suis ravie de vous accueillir."
with Dissolve(0.5)
ien "Vous êtes bien les nouveaux enseignants que Pauline Bouysse reçoit aujourd’hui ?"
with Dissolve(0.5)
ien "Bienvenue parmi nous ! Vos débuts comptent beaucoup, et vous serez très bien accompagnés."
with Dissolve(0.5)
ien "Pauline vous attend dans son bureau pour faire le point avec vous. Suivez‑moi, je vais vous conduire jusqu’à elle."
with Dissolve(0.5)
scene viviane_bureau1
ien "Madame Bouysse ?"
with Dissolve(0.5)
scene viviane_bureau2
cpc "Oui, Madame l'Inspectrice ?"
with Dissolve(0.5)
ien "Voici les jeunes enseignants que vous attendiez. Je vous laisse travailler ensemble."
with Dissolve(0.5)
cpc "Merci, Madame l'Inspectrice."
with Dissolve(0.5)
scene bureau_cpc
show viviane
cpc "Bonjour. Je suis contente de vous revoir. Comment allez-vous depuis notre dernière rencontre ?"
with Dissolve(0.5)
"Pauline Bouysse vous observe avec un léger sourire. Son regard est à la fois bienveillant et attentif, comme si elle évaluait subtilement votre état d’esprit."
hide viviane
show viviane5
menu:
    cpc "Vous avez avancé sur votre travail de préparation pour la classe ?"
    with Dissolve(0.5)
    "Oui, nous avons bien avancé.":
        hide viviane5
        show viviane4
        cpc "Parfait. Je vous félicite. C’est un très bon point."
        with Dissolve(0.5)
        cpc "Voyons ensemble ce que ça donne."
        with Dissolve(0.5)
        jump S3Q2
    "Nous avons commencé... Mais nous ne sommes pas sûr d'avoir bien fait.":
        hide viviane5
        show viviane
        cpc "C’est normal à ce stade. Vous êtes encore de jeunes enseignants. Votre doute montre que vous vous posez des questions. C'est une bonne chose."
        with Dissolve(0.5)
        cpc "Je vais vous aider à clarifier vos idées. Nous allons reprendre point par point."
        with Dissolve(0.5)
        jump S3Q2
    "Non, nous avons eu du mal à nous y mettre.":
        hide viviane5
        show viviane
        with Dissolve(0.5)
        cpc "Je comprends. Le démarrage peut être difficile quand tout est nouveau."
        cpc "Le plus important, c’est que vous soyez là aujourd’hui, prêts à avancer. Et je suis là pour vous accompagner."
        cpc "On reprend ensemble, étape par étape. Vous verrez, cela va vite devenir plus clair."
        jump S3Q2



label S3Q2:
scene bureau_cpc
show viviane
cpc "Parlons du coin jeu symbolique que vous allez devoir mettre en place dans la classe et présenter à la fin de l'année."
with Dissolve(0.5)
cpc "C'est un élément essentiel à votre future classe."
with Dissolve(0.5)
cpc "J'aimerais savoir où vous en êtes."
with Dissolve(0.5)
label S3Q2a:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous choisi un univers de référence ?"
    with Dissolve(0.5)
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien. Un choix affirmé."
        with Dissolve(0.5)
        cpc "Nous allons vérifier ensemble sa pertinence pour vos élèves."
        with Dissolve(0.5)
        jump S3Q3
    "Non":
        hide viviane5
        show viviane
        cpc "Ce n'est pas grave, mais il faut vous décider maintenant."
        with Dissolve(0.5)
        cpc "Pour vous guider, pensez à ceci : un bon univers de référence parle à l’enfant, est lié à son vécu."
        with Dissolve(0.5)
        cpc "J'attends que vous ayez fait un choix. Revenez me voir quand vous aurez pris une décision."
        with Dissolve(0.5)
        jump S3Q2a

label S3Q3:
scene bureau_cpc
show viviane5
menu:
    cpc "Cet univers est-il proche du vécu de l'enfant ?"
    with Dissolve(0.5)
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien."
        show viviane4
        cpc "Il faut bien comprendre que le jeu sert les apprentissages : c’est un levier pour développer le langage, l’imaginaire et la socialisation."
        with Dissolve(0.5)
        jump S3Q4
    "Nous ne savons pas vraiment…":
        hide viviane5
        show viviane
        with Dissolve(0.5)
        cpc "C’est normal de douter. Le vécu des enfants varie énormément selon les contextes."
        with Dissolve(0.5)
        cpc "Rappelez-vous ceci : « Est-ce que les enfants peuvent se projeter spontanément dans cet univers ? »"
        with Dissolve(0.5)
        cpc "Si oui, vous êtes sur la bonne voie. Sinon, essayez d'en choisir un autre."
        with Dissolve(0.5)
        cpc "Votre hésitation semble indiquer que ce n'est sans doute pas le bon choix. Prenez le temps de réfléchir à un autre univers."
        with Dissolve(0.5)
        jump S3Q2a
    "Non, pas vraiment.":
        hide viviane5
        show viviane        
        cpc "C'est une erreur commune à beaucoup de jeunes enseignants."
        with Dissolve(0.5)
        cpc "On a parfois tendance à choisir un univers que l’on aime soi-même…"
        with Dissolve(0.5)
        cpc "...mais qui n’est pas forcément accessible à des enfants de 3 ou 4 ans."
        with Dissolve(0.5)
        cpc "Je vous invite à en choisir un autre, plus proche de leurs expériences de jeunes élèves."
        with Dissolve(0.5)
        cpc "J'attends que vous ayez fait un choix."
        with Dissolve(0.5)
        jump S3Q2a

scene bureau_cpc
show viviane
cpc "Parlons maintenant du corpus de mots."
with Dissolve(0.5)
cpc "En maternelle, le langage est un objectif prioritaire. Chaque coin jeu devrait permettre aux enfants d’entendre, d’utiliser et de réutiliser des mots variés."
with Dissolve(0.5)
cpc "Des noms, bien sûr… mais aussi des verbes, des adjectifs, des formules sociales, etc."
label S3Q4:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous construit un corpus de mots variés (noms, verbes, adjectifs, adverbes, etc) et courants associés à cet univers ?"
    with Dissolve(0.5)
    "Oui":
        hide viviane5
        show viviane4
        cpc "Bien. Vous allez donc pouvoir faire ce que je vais vous demander à présent."
        with Dissolve(0.5)
        jump S3Q5
    "Non":
        hide viviane5
        show viviane
        cpc "Alors vous devez en construire un maintenant. Vous pouvez vous aider des documents que je vous avais fournis la dernière fois."
        with Dissolve(0.5)
        cpc "J'attends que vous ayez terminé."
        with Dissolve(0.5)
        jump S3Q4

label S3Q5:
scene bureau_cpc
show viviane3
cpc "Inscrivez ce corpus noir sur blanc (ou sur votre ordinateur). Vous devrez le présenter en même temps que le coin jeu."
with Dissolve(0.5)
label S3Q5a:
scene bureau_cpc
show viviane5
with Dissolve(0.5)    
menu:
    cpc "Avez-vous choisi le coin jeu associé à votre univers de référence pour le mettre en place et le présenter à la fin de l'année ?"
    with Dissolve(0.5)
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien. Votre projet prend forme, et c’est très encourageant."
        with Dissolve(0.5)
        jump S3Q6
    "Pas encore, nous hésitons":
        hide viviane5
        show viviane
        cpc "Hésiter est normal."
        with Dissolve(0.5)
        cpc "Pensez à la cohérence entre : l’univers choisi, le corpus, et le vécu des enfants."
        with Dissolve(0.5)
        cpc "Demandez-vous quel coin jeu offre un bon potentiel de langage et d'apprentissage."
        with Dissolve(0.5)
        cpc "Essayez d'en choisir un maintenant. Vous pouvez vous aider des documents que je vous avais fournis la dernière fois. Vous pourrez changer d'avis plus tard si vous le souhaitez."
        with Dissolve(0.5)
        cpc "J'attends que vous ayez terminé."
        with Dissolve(0.5)
        jump S3Q5a
    "Non, nous sommes un peu perdus.":
        hide viviane5
        show viviane
        cpc "C’est tout à fait compréhensible. Réfléchir à un coin jeu peut prendre du temps."
        with Dissolve(0.5)
        cpc "Vous pouvez repartir des documents que je vous ai fournis pour vous aider. Certains contiennent des exemples dont vous pouvez vous inspirer."
        with Dissolve(0.5)
        cpc "J'attends que vous ayez terminé."
        with Dissolve(0.5)
        jump S3Q5a


label S3Q6:
scene bureau_cpc
show viviane4
cpc "Bravo, nous avons bien progressé."
with Dissolve(0.5)
label S3Q6a:
scene bureau_cpc
show viviane
with Dissolve(0.5)    
menu:
    cpc "Avez-vous imaginé des coins jeu à associer à celui que vous allez créer pour les faire fonctionner ensemble ou le faire évoluer ?"
    with Dissolve(0.5)
    "Oui":
        hide viviane
        show viviane4
        cpc "Très bien."
        with Dissolve(0.5)
        jump S3Q7
    "Non":
        hide viviane5
        show viviane
        cpc "Alors Je vous encourage à y réfléchir. Vous n'êtes pas obligé de les trouver maintenant mais pensez-y pour notre prochaine rencontre."
        with Dissolve(0.5)
        jump S3Q7

label S3Q7 :
scene bureau_cpc
show viviane
cpc "Nous avons les bases nécessaires. Continuez à réfléchir à votre espace jeu symbolique en vous aidant des documents que j'avais mis à votre disposition."
with Dissolve(0.5)
hide viviane
show viviane2
cpc "Réfléchissez aussi à la manière dont vous aller aménager votre classe. Je vous rappelle que vous avez une classe à trois niveaux avec des enfants de moins de 3 ans dans l'effectif."
with Dissolve(0.5)
cpc "Lisez bien le projet d'école. Vous y découvrirez par exemple que vous allez devoir faire fonctionner la classe en pôles d'apprentissage."
with Dissolve(0.5)

label S3Q8:
scene bureau_cpc
show viviane5
with Dissolve(0.5)    
menu:
    cpc "Vous savez comment ça fonctionne ?"
    with Dissolve(0.5)
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien. Alors vous pouvez aussi y réfléchir dès à présent."
        with Dissolve(0.5)
        jump S3Q9
    "Non":
        hide viviane5
        show viviane
        cpc "Ne vous inquiétez pas. Vous aurez bientôt une formation à l'INSPÉ pour vous l'expliquer."
        with Dissolve(0.5)
        jump S3Q9

label S3Q9 :
scene bureau_cpc
show viviane
cpc "Très bien. Je pense que nous avons posé aujourd'hui les bases utiles pour aider à avancer sereinement."
with Dissolve(0.5)
cpc "Votre projet commence à prendre forme."
with Dissolve(0.5)
cpc "Ce travail ne se construit pas en une seule séance. Il mûrit, il évolue, et il se nourrit de vos échanges, de vos recherches et de vos discussions."
with Dissolve(0.5)
cpc "Je vous encourage donc à réfléchir ensemble. Confrontez vos idées. Questionnez‑vous. Parlez de vos hésitations, de vos idées, de vos découvertes."
with Dissolve(0.5)
cpc "Et surtout, n'oubliez pas que vous n'êtes pas seuls. Vos formateurs, vos collègues, et moi-même sommes là pour vous accompagner."
with Dissolve(0.5)
cpc "Faites de votre mieux pour avancer le plus possible. Le temps file très vite…"
with Dissolve(0.5)
cpc "Et bientôt, vous devrez me présenter votre travail, ainsi qu’aux autres jeunes enseignants de la circonscription."
with Dissolve(0.5)
cpc "Je vous fais confiance. Continuez sur cette lancée."
with Dissolve(0.5)
cpc "Je vous laisse réfléchir ensemble. N'hésitez pas à demander de l'aide aux formateurs qui vous suivent en cas de besoin."
with Dissolve(0.5)
cpc "À très bientôt."
with Dissolve(0.5)
jump start

# Chapitre 4 #
label chapitre4:
scene smartphone
with Dissolve(0.8)
play sound "audio/sonnerie.mp3" volume 0.6
"Votre téléphone sonne."
with Dissolve(0.5)
stop sound
directeur "Bonjour ! Pierre Haffeux à l’appareil, je suis le directeur de l’école maternelle Baruch Spinoza."
with Dissolve(0.5)
directeur "Je vous avais parlé au téléphone, il y a deux semaines."
with Dissolve(0.5)
directeur "J'espère que vous allez bien."
with Dissolve(0.5)
directeur "Je viens de rentrer. Si vous êtes disponible, je peux vous faire visiter l’école dès aujourd’hui."
with Dissolve(0.5)
menu:
    "Oui, je peux venir aujourd’hui.":
        $ dispo = "aujourd'hui"
    "Oui, mais dans l’après-midi.":
        $ dispo = "aprem"
    "Aujourd’hui c’est compliqué… demain ?":
        $ dispo = "demain"
if dispo == "aujourd'hui":
    directeur "Très bien, nous ne perdons pas de temps."
elif dispo == "aprem":
    directeur "Parfait, après-midi !"
else :
    directeur "D’accord pour demain."
directeur "Je vais contacter les collègues qui partagent votre classe aussi. Je préfèrerais vous voir tous ensemble."
with Dissolve(0.5)
directeur "Je vous attendrai devant l’entrée principale, en espérant que vous soyez tous là."
with Dissolve(0.5)
directeur "Notez bien l’adresse : 12 rue des Tilleuls, Jardincourt. Le bâtiment maternelle est l’extension bois à l’arrière de l’école. Je vous attends devant l’entrée principale."
with Dissolve(0.5)
"Vous raccrochez."
with Dissolve(0.5)
"Vous ressentez un léger mélange d’excitation et de responsabilité."
with Dissolve(0.5)
"Cette fois, ce n’est plus théorique."
with Dissolve(0.5)
"Vous allez découvrir votre classe."
with Dissolve(0.5)

# Trajet
scene rue_matin
with Dissolve(1.0)
play music "audio/oiseaux.mp3" volume 0.4
if dispo == "aujourd'hui":
    directeur "Quelques minutes plus tard, vous prenez la route."
elif dispo == "aprem":
    directeur "Arrive l'après-midi. Vous prenez la route."
else :
    directeur "Le lendemain, vous prenez la route."
"Vous entrez l’adresse dans le GPS."
with Dissolve(0.5)
"Temps estimé : 18 minutes..."
with Dissolve(0.5)
"Aujourd’hui, vous allez voir votre future classe pour la première fois."
with Dissolve(0.5)
stop music
with Dissolve(0.5)

# Extérieur école
scene ecole_ext
with Dissolve(1.0)
pause
"Vos collègues sont déjà présents dans la rue."
with Dissolve(0.5)
"Le directeur de l'école sort du bâtiment et se dirige vers vous."
with Dissolve(0.5)
show directeur4
directeur "Ah ! Vous voilà ! Je suis ravi de tous vous rencontrer."
with Dissolve(0.5)
hide directeur4
show directeur2
directeur "Merci de vous être déplacés. Une classe partagée, ça se pense ensemble."
with Dissolve(0.5)
hide directeur2
show directeur1
directeur "Comme vous pouvez le voir, le bâtiment maternelle est neuf."
with Dissolve(0.5)
directeur "Une salle de classe d’environ 64 m², un dortoir d’environ 74 m², et les sanitaires."
with Dissolve(0.5)
directeur "Avant, Jardincourt n’accueillait que les élèves de l’élémentaire. Pour aller à l'école maternelle, il fallait se rendre dans la commune voisine."
with Dissolve(0.5)
directeur "La mairie a décidé de faire construire une structure pour accueillir les enfants dès 2 ans dans le village."
with Dissolve(0.5)
directeur "Les GS sont intégrés dans le bâtiment de l’élémentaire cette année."
with Dissolve(0.5)
hide directeur1
show directeur6
directeur "Vous aviez bien regardé la liste des élèves ? "
with Dissolve(0.5)
i "Si vous ne l'aviez pas fait, observez les dates de naissance sur la liste des élèves."
with Dissolve(0.5)
hide directeur6
show directeur1
directeur "Vous l'avez compris, vous aurez une classe avec un triple niveau TPS-PS-MS."
with Dissolve(0.5)

#Hall
scene ecole1
with Dissolve(1.0)
"Vous vous dirigez vers l'entrée du bâtiment..."
with Dissolve(0.5)
scene ecole2
with Dissolve(1.0)
directeur "Ici, c’est le hall d'entrée. Les familles passeront par ici pour déposer les enfants."
with Dissolve(0.5)
scene ecole3
with Dissolve(1.0)
directeur "Les enfants déposeront leurs manteaux à cet endroit avant d'entrer en classe."
with Dissolve(0.5)
label visite:
menu :
    directeur "Que souhaitez vous visiter à présent ?"
    "Nous voudrions voir la salle polyvalente pour la motricité et la sieste." :
        scene ecole4
        with Dissolve(1.0)
        directeur "Voici la salle polyvalente."
        with Dissolve(0.5)
        directeur "Elle mesure 74m²."
        with Dissolve(0.5)
        directeur "Elle pourra servir à la fois pour la motricité le matin..."
        with Dissolve(0.5)
        scene ecole5
        with Dissolve(0.5)
        directeur "... Et pour la sieste en début d'après-midi."
        with Dissolve(0.5)
        directeur "Des employés de la mairie installeront à chaque fois les lits pendant la pause déjeuner."
        with Dissolve(0.5)
        directeur "Elle est très lumineuse mais des volets permettront de baisser la lumière pour favoriser l'endormissement."
        with Dissolve(0.5)
        directeur "Je vous laisse le temps de regarder."
        with Dissolve(0.5)
        pause
        jump visite
    "Nous aimerions visiter la salle de classe." :
        scene ecole8
        with Dissolve(1.0)
        directeur "Voici votre future salle de classe !"
        with Dissolve(0.5)
        directeur "Elle mesure un peu plus de 64 m²."
        with Dissolve(0.5)
        directeur "Elle est toute neuve et vide."
        with Dissolve(0.5)
        directeur "C'est à vous de lui donner une âme."
        with Dissolve(0.5)
        directeur "Comme vous pouvez le constater la pièce est très lumineuse."
        with Dissolve(0.5)
        scene ecole9
        with Dissolve(0.5)
        " Vous interrogez le directeur sur l'absence de mobilier. "
        with Dissolve(0.5)
        directeur "Pour le moment les meubles n'ont pas été achetés. Nous vous attendions pour passer la commande."
        with Dissolve(0.5)
        directeur "Je vous expliquerai juste après."
        with Dissolve(0.5)
        directeur "Prenez le temps de vous projeter. C'est ici que vous travaillerez cette année."
        with Dissolve(0.5)
        pause
        jump visite
    "Peut-on voir les toilettes ?" :
        scene ecole6
        with Dissolve(1.0)
        directeur "Voici les toilettes !"
        with Dissolve(0.5)
        directeur "Comme vous le voyez tout a été fait pour le confort et l'intimité des élèves."
        with Dissolve(0.5)
        directeur "Ils sont situés juste à côté de votre classe."
        with Dissolve(0.5)
        scene ecole7
        directeur "Et voici les lavabos."
        with Dissolve(0.5)
        pause
        jump visite
    "Nous avons tout vu" :
        directeur "Très bien discutons dehors à présent"

scene ecole_ext
with Dissolve(1.0)
show directeur1
with Dissolve(0.5)
directeur "J'espère que vous avez apprécié la visite."
with Dissolve(0.5)
directeur "Souvenez-vous que vous avez toujours la possibilité de vous appuyer sur le plan que je vous avais envoyé par la poste."
with Dissolve(0.5)
scene plan
with Dissolve(1.0)
directeur "En voici un exemplaire."
with Dissolve(0.5)
directeur "C'est très pratique pour se projeter dans l'aménagement des pièces."
with Dissolve(0.5)
scene ecole_ext
show directeur1
with Dissolve(0.5)
directeur "Avant de vous laisser repartir, j’aimerais vous poser quelques questions."
with Dissolve(0.5)
hide directeur1
show directeur6
directeur "Vous avez déjà rencontré Madame Tille, l’inspectrice ?"
menu:
    "Avez-vous rencontré l'IEN ?"
    "Oui.":
        hide directeur6
        show directeur2
        directeur "Très bien."
        with Dissolve(0.5)
    "Non, pas encore.":
        hide directeur6
        show directeur3
        directeur "Étrange car elle m'avait signalé votre rencontre à l'inspection..."
        with Dissolve(0.5)
scene ecole_ext
show directeur6
directeur "Et Pauline Bouysse, la conseillère pédagogique, vous l’avez vue ?"
with Dissolve(0.5)
menu:
    "Avez-vous rencontré la CPC ?"
    "Oui.":
        hide directeur6
        show directeur2
        directeur "Parfait, elle est très investie dans l’accompagnement des débutants."
    "Non, pas encore.":
        hide directeur6
        show directeur3
        directeur "Pourtant je l'ai eu au téléphone avant que vous arriviez et elle m'a dit vous avoir rencontrés plusieurs fois..."
scene ecole_ext
show directeur1
directeur "Je vous avais envoyé une enveloppe avec plusieurs documents."
with Dissolve(0.5)
scene ecole_ext
show directeur6
directeur "Avez-vous pris le temps de les consulter ?"
with Dissolve(0.5)
menu:
    "Avez-vous consulté les documents envoyés ?"
    "Oui, nous les avons lus.":
        scene ecole_ext
        show directeur2
        directeur "Très bien. J'apprécie votre sérieux."
        with Dissolve(0.5)
    "Nous avons commencé, mais pas tout.":
        scene ecole_ext
        show directeur7
        directeur "Prenez le temps de tout lire. Vous avez besoin de les connaître."
        with Dissolve(0.5)
    "Pas vraiment.":
        scene ecole_ext
        show directeur3
        directeur "Je préfère être directif sur ce point : il faudra les lire. C'est important."
        with Dissolve(0.5)    
scene ecole_ext
show directeur1
directeur "Pour que ce soit bien clair, je vous rappelle le contexte."
with Dissolve(0.5)
directeur "Le bâtiment destiné aux élèves de la maternelle est neuf."
with Dissolve(0.5)
directeur "Mais comme vous l’avez vu, la classe est vide : tout reste à construire."
with Dissolve(0.5)
directeur "Et ce n’est pas tout."
with Dissolve(0.5)
directeur "L’école a été choisie, comme c'est écrit dans le projet d’école, pour expérimenter les pôles d’attractivité."
with Dissolve(0.5)
directeur "Cela veut dire que vous allez devoir penser l’aménagement pour favoriser l’engagement des élèves, l’autonomie, le langage, et les apprentissages."
with Dissolve(0.5)
hide directeur1
show directeur2
directeur "Bonne nouvelle : vous pourrez commander le mobilier et le matériel dont vous avez besoin."
with Dissolve(0.5)
hide directeur2
show directeur1
directeur "Vous avez accès à plusieurs catalogues spécialisés."
with Dissolve(0.5)
directeur "Wesco, Asco & Celda, Majuscule, Nathan..."
with Dissolve(0.5)
directeur "Et aussi : Manutan Collectivités, UGAP, Camif Collectivités..."
with Dissolve(0.5)
i "Vous consulterez réellement ces catalogues pour construire l'aménagement de votre classe."
with Dissolve(0.5)
directeur "Mais je vous le dis tout de suite : je ne peux pas commander au feeling."
with Dissolve(0.5)
directeur "Il me faudra un plan précis de la classe aménagée..."
with Dissolve(0.5)
directeur "... Et une explication des raisons de cet aménagement."
with Dissolve(0.5)
directeur "Le plan servira à justifier les achats auprès de la mairie."
with Dissolve(0.5)
directeur "Dites moi... :"
scene ecole_ext
show directeur6
with Dissolve(0.5)
directeur "Vous avez assisté à la formation à l’INSPÉ avec Monsieur Cuvelier sur l’aménagement en pôles d’attractivité ?"
menu:
    "Oui.":
        scene ecole_ext
        show directeur2
        directeur "Parfait. Alors vous avez déjà des repères solides pour vous mettre au travail."
        with Dissolve(0.5)
    "Oui, mais nous devons relire.":
        scene ecole_ext
        show directeur1
        directeur "Très bien. C’est normal. On oublie vite si on ne réactive pas. Utilisez vos notes."
        with Dissolve(0.5)
    "Non.":
        scene ecole_ext
        show directeur3
        directeur "D’accord. Alors il faudra vous mettre à jour rapidement : c’est central dans votre projet. Vous devriez assister à ces formations."
        with Dissolve(0.5)
scene ecole_ext
show directeur1
directeur "Si besoin, sachez que les livres et ressources sur l’aménagement des espaces peuvent être empruntés à la bibliothèque de l’INSPÉ de Valenciennes."
with Dissolve(0.5)
directeur "Vous y trouverez de quoi nourrir vos choix et justifier vos décisions."
with Dissolve(0.5)
directeur "Dernier point, qui m’intéresse beaucoup."
with Dissolve(0.5)
directeur "Pauline m’a parlé de votre espace de jeu symbolique, celui que vous préparez."
with Dissolve(0.5)
directeur "Je suis curieux de le voir prochainement."
with Dissolve(0.5)
directeur "Et surtout, j’aimerais que vous le fassiez évoluer."
with Dissolve(0.5)
directeur "Pas seulement un coin jeu…"
with Dissolve(0.5)
directeur "Mais un espace à scénario : un espace qui provoque des interactions, du langage, des rôles, des problèmes à résoudre."
with Dissolve(0.5)
directeur "Ça peut devenir un vrai levier pédagogique, surtout avec des TPS-PS-MS."
with Dissolve(0.5)
directeur "Je dois vous laisser car j'ai un rendez-vous important."
with Dissolve(0.5)
directeur "Je suis ravi de vous avoir rencontrés."
with Dissolve(0.5)
directeur "Je vous laisse vous mettre au travail."
with Dissolve(0.5)
directeur "N'oubliez pas de créer le plan de votre classe aménagée. J'en ai besoin."
with Dissolve(0.5)
scene ecole_ext
show directeur5
directeur "À bientôt."
with Dissolve(0.5)
jump start

# Chapitre 5 #
label chapitre5:
scene ecrannoir
with Dissolve(1.0)
"Quelques jours ont passé depuis la visite de l’école maternelle Baruch Spinoza."
with Dissolve(0.5)
"Depuis, vous repensez souvent à la classe vide, lumineuse, encore sans mobilier."
with Dissolve(0.5)
"Peu à peu, ce lieu commence à prendre forme dans votre esprit."
with Dissolve(0.5)
"Vous échangez avec vos collègues, relisez vos notes, consultez les documents transmis par le directeur et les ressources vues à l’INSPÉ."
with Dissolve(0.5)

scene smartphone
with Dissolve(1.0)
play sound "audio/sonnerie.mp3" volume 0.5
"Votre téléphone sonne."
with Dissolve(0.5)
stop sound
cpc "Bonjour. C’est Pauline Bouysse."
with Dissolve(0.5)
cpc "Je vous appelle pour faire un point sur l’avancée de votre réflexion concernant l’aménagement de la classe."
with Dissolve(0.5)
cpc "J’aimerais que nous nous retrouvions pour travailler cela ensemble."
with Dissolve(0.5)
cpc "Cette fois, nous allons nous intéresser à l'espace jeux symbolique et à l’organisation concrète de l’espace."
with Dissolve(0.5)
cpc "L’objectif est que vous puissiez présenter votre coin jeu et produire un premier plan d’aménagement cohérent, justifié et adapté aux élèves de TPS-PS-MS."
with Dissolve(0.5)

scene bureau_cpc
show viviane
with Dissolve(1.0)
"Le jour du rendez-vous arrive."
with Dissolve(0.5)
"Vous retrouvez Pauline Bouysse avec vos collègues pour une nouvelle séance de travail."
with Dissolve(0.5)
cpc "Bonjour, je suis très heureuse de vous revoir ."
with Dissolve(0.5)
cpc "Cette séance est importante."
with Dissolve(0.5)
cpc "C’est notre dernière rencontre avant votre présentation devant les autres enseignants débutants."
with Dissolve(0.5)
cpc "Nous allons vérifier ensemble que votre projet est solide."
with Dissolve(0.5)

label ch5_choix:
scene bureau_cpc
show viviane5
menu:
    cpc "Quel sujet souhaitez-vous aborder ?"
    "La présentation du travail devant les autres enseignants.":
        hide viviane5
        show viviane4
        cpc "D'accord."
        with Dissolve(0.5)
        jump ch5_presentation
    "L'aménagement de la classe.":
        hide viviane5
        show viviane4
        cpc "D'accord."
        with Dissolve(0.5)
        jump ch5_amenagement
    "Nos connaissances sur la maternelle.":
        hide viviane5
        show viviane4
        cpc "Bonne idée."
        jump ch5_quiz_intro
    "Je pense que nous avons tout abordé.":
        hide viviane5
        show viviane
        cpc "Très bien"
        with Dissolve(0.5)
        cpc "Pour notre prochaine rencontre, je veux que vous soyez capables de présenter et de justifier votre plan, vos choix d’aménagement et votre espace de jeu symbolique."
        with Dissolve(0.5)
        cpc "Il faudra aussi présenter un scénario possible pour ce coin jeu."
        with Dissolve(0.5)
        cpc "Continuez à travailler ensemble. Prenez le temps de confronter vos idées."
        with Dissolve(0.5)
        cpc "À très bientôt."
        jump start

label ch5_amenagement:
menu:
    cpc "Avez-vous déjà commencé à réfléchir à l’aménagement de la classe ?"
    "Oui, nous avons déjà quelques idées.":
        hide viviane
        show viviane4
        cpc "Très bien. Nous allons voir ensemble comment les organiser."
        with Dissolve(0.5)
        jump ch5_besoins
    "Un peu, mais nous ne savons pas par où commencer.":
        hide viviane
        show viviane
        cpc "C’est normal. Nous allons reprendre les choses dans l’ordre."
        with Dissolve(0.5)
        jump ch5_besoins
    "Pas vraiment.":
        hide viviane
        show viviane
        cpc "Alors cette séance va vous être très utile. L’aménagement d’une classe ne s’improvise pas."
        with Dissolve(0.5)
        jump ch5_besoins


label ch5_besoins:
scene bureau_cpc
show viviane
cpc "Avant de parler du mobilier, il faut d’abord penser aux besoins des élèves."
with Dissolve(0.5)
cpc "Vous allez accueillir des enfants de TPS, PS et MS."
with Dissolve(0.5)
cpc "Ils n’ont pas tous le même degré d’autonomie et ont des besoins à prendre en compte."
with Dissolve(0.5)
hide viviane
show viviane7
cpc "Réfléchissez aux besoins essentiels des élèves : sécurité affective, circulation, repos, langage, manipulation, jeux, regroupement, autonomie..."
with Dissolve(0.5)

label ch5_besoins_q:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous identifié les principaux besoins à prendre en compte pour aménager la classe ?"
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien. C’est la base de votre réflexion."
        with Dissolve(0.5)
        jump ch5_zones
    "Pas complètement":
        hide viviane5
        show viviane
        cpc "Alors reprenez vos cours d'INSPÉ."
        with Dissolve(0.5)
        cpc "Vous y trouverez les informations dont vous avez besoin."
        with Dissolve(0.5)
        jump ch5_besoins_q

label ch5_zones:
scene bureau_cpc
show viviane2
cpc "À présent, réfléchissons aux pôles d'attractivité que vous mettrez en place dans la classe."
with Dissolve(0.5)
cpc "Par exemple : un espace sensoriel, un espace jeu de construction, un espace motricité fine, un espace mathématiques, etc."
with Dissolve(0.5)
cpc "L’idée est de penser ces espaces comme participant à votre pédagogie. Ils doivent contribuer à la réussite de tous les élèves."
with Dissolve(0.5)
hide viviane2
show viviane7
cpc "Si vous ne l'avez pas déjà fait, sur une feuille ou un ordinateur, listez les pôles d'apprentissage que vous souhaitez faire apparaître dans la classe."
with Dissolve(0.5)

label ch5_zones_q:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous défini les pôles d'attractivité de votre classe ?"
    "Oui":
        hide viviane5
        show viviane4
        cpc "Parfait."
        with Dissolve(0.5)
        jump ch5_circulation
    "Non":
        hide viviane5
        show viviane
        cpc "Reprenez calmement. Pensez aux programmes de l'école maternelle."
        with Dissolve(0.5)
        cpc "Vous pouvez utiliser les ressources vues en cours à l'INSPÉ."
        with Dissolve(0.5)
        jump ch5_zones_q

scene bureau_cpc
show viviane
cpc "Pensez aussi qu'un aménagement efficace, ce n’est pas seulement une juxtaposition d'espaces."
with Dissolve(0.5)
cpc "Il faut aussi penser à la circulation."
with Dissolve(0.5)
cpc "Les élèves doivent pouvoir se déplacer facilement, voir ce qu’ils peuvent faire, comprendre où trouver le matériel et où le ranger."
with Dissolve(0.5)
cpc "Il faut penser la classe comme un espace vivant dans lequel les élèves se déplacent."
with Dissolve(0.5)
label ch5_circulation:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous réfléchi à la circulation des élèves dans la classe ?"
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien. C’est un point essentiel."
        with Dissolve(0.5)
        jump ch5_poles
    "Pas encore":
        hide viviane5
        show viviane
        cpc "Alors faites-le maintenant."
        with Dissolve(0.5)
        cpc "Imaginez les déplacements d’un enfant de 2 ou 3 ans dans la classe."
        with Dissolve(0.5)
        cpc "Peut-il comprendre facilement où aller ? Peut-il circuler et travailler sans gêner les autres ?"
        with Dissolve(0.5)
        jump ch5_circulation

scene bureau_cpc
show viviane2
cpc "Revenons maintenant aux pôles d’attractivité."
with Dissolve(0.5)
cpc "Un pôle d’attractivité est un espace pensé pour donner envie d’agir, d’explorer, de parler et d’apprendre."
with Dissolve(0.5)
cpc "Il ne s’agit pas simplement de proposer du matériel, mais de créer des conditions favorables à l’engagement des élèves."
with Dissolve(0.5)
cpc "Vous devez donc vous demander ce que chaque espace permet réellement de faire apprendre."
with Dissolve(0.5)
label ch5_poles:
scene bureau_cpc
show viviane5
menu:
    cpc "Savez-vous relier chaque espace prévu à une intention d’apprentissage ?"
    "Oui":
        hide viviane5
        show viviane4
        cpc "Excellent. C’est exactement ce qui donnera de la cohérence à votre projet."
        with Dissolve(0.5)
        jump ch5_justification
    "Pas vraiment":
        hide viviane5
        show viviane
        cpc "Alors il faut encore approfondir votre réflexion."
        with Dissolve(0.5)
        cpc "Pour chaque espace, posez-vous cette question simple : qu’est-ce que les élèves vont apprendre ici ?"
        with Dissolve(0.5)
        jump ch5_poles

label ch5_justification:
scene bureau_cpc
show viviane
cpc "Le directeur vous demandera un plan, mais aussi une justification."
with Dissolve(0.5)
cpc "Vous devrez être capables d’expliquer vos choix."
with Dissolve(0.5)
cpc "Pourquoi cet espace ? Pourquoi ce coin jeu à cet endroit ? Pourquoi ce choix de meubles ? Pourquoi ce matériel ?"
with Dissolve(0.5)
cpc "Chaque décision doit pouvoir être reliée aux besoins des élèves et aux objectifs de l’école maternelle."
with Dissolve(0.5)
hide viviane
show viviane7
cpc "Commencez à rédiger quelques arguments pour justifier vos choix d’aménagement."
with Dissolve(0.5)

label ch5_justification_q:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous commencé à formuler des justifications pour vos choix ?"
    "Oui":
        hide viviane5
        show viviane4
        cpc "Très bien. Vous avancez dans la bonne direction. Pensez que vous devrez expliquer votre aménagement."
        with Dissolve(0.5)
        jump ch5_plan
    "Non":
        hide viviane5
        show viviane
        cpc "Alors il faut le faire."
        with Dissolve(0.5)
        cpc "Un bon aménagement n’est pas seulement intuitif : il doit pouvoir être expliqué."
        with Dissolve(0.5)
        jump ch5_justification_q

label ch5_plan:
scene bureau_cpc
show viviane2
cpc "Nous arrivons maintenant à l’étape importante : le plan."
with Dissolve(0.5)
cpc "Je vous demande de produire un premier schéma de la classe aménagée."
with Dissolve(0.5)
cpc "Il n’a pas besoin d’être parfait tout de suite."
with Dissolve(0.5)
cpc "Mais il doit déjà faire apparaître les espaces, le mobilier principal, les zones de circulation et les choix importants."
with Dissolve(0.5)
hide viviane2
show viviane7
cpc "Réalisez un premier plan de la classe aménagée à partir du plan transmis par le directeur."
with Dissolve(0.5)

label ch5_plan_q:
scene bureau_cpc
show viviane5
menu:
    cpc "Avez-vous réalisé un premier plan d’aménagement ?"
    "Oui":
        hide viviane5
        show viviane4
        cpc "Bravo. C’est une étape décisive."
        with Dissolve(0.5)
        jump ch5_fin
    "Non":
        hide viviane5
        show viviane
        cpc "Alors mettez-vous au travail."
        with Dissolve(0.5)
        cpc "Appuyez-vous sur le plan du directeur, vos notes de formation, les catalogues et vos échanges de groupe."
        with Dissolve(0.5)
        jump ch5_plan_q


label ch5_fin:
scene bureau_cpc
show viviane4
cpc "Je vous félicite. Vous avez désormais une première base de travail."
with Dissolve(0.5)
hide viviane4
show viviane
cpc "Bien sûr, ce plan évoluera encore."
with Dissolve(0.5)
cpc "Vous allez l’ajuster, le discuter, le tester mentalement, peut-être même le modifier plusieurs fois."
with Dissolve(0.5)
cpc "Mais vous êtes entrés dans une véritable démarche de conception de l'espace."
with Dissolve(0.5)
jump ch5_choix

# RESTITUTION

label ch5_presentation:

scene bureau_cpc
show viviane

cpc "Nous allons parler de la restitution finale de votre travail."
with Dissolve(0.5)

cpc "Vous devrez présenter votre projet devant d'autres enseignants débutants."
with Dissolve(0.5)

hide viviane
show viviane7

cpc "Votre présentation devra comporter trois éléments principaux :"

cpc "1. La présentation de votre espace de jeu symbolique."
cpc "2. Le dossier pédagogique qui accompagne cet espace."
cpc "3. L'aménagement complet de la classe en pôles d'apprentissage."

with Dissolve(0.5)


# ESPACE JEU

scene bureau_cpc
show viviane2

cpc "Tout d'abord, vous devrez présenter l'espace de jeu symbolique que vous avez conçu."
with Dissolve(0.5)
cpc "Vous expliquerez l'univers choisi, les rôles possibles pour les élèves et les apprentissages visés."
with Dissolve(0.5)
cpc "Cet espace devra favoriser le langage, les interactions et l'engagement des élèves."
with Dissolve(0.5)
cpc "Il devra permettre aux élèves de jouer, d’explorer et d’apprendre."
with Dissolve(0.5)

# DOSSIER PEDAGOGIQUE

scene bureau_cpc
show viviane

cpc "Vous devrez également présenter le dossier pédagogique qui accompagne cet espace."
with Dissolve(0.5)

hide viviane
show viviane7

cpc "Ce dossier devra comporter :"

cpc "la description de l'espace,"
cpc "les objectifs d'apprentissage,"
cpc "les besoins satisfaits,"
cpc "le corpus de mots travaillé,"
cpc "les rôles possibles pour les élèves,"
cpc "le matériel utilisé,"
cpc "un exemple de scénario pédagogique,"
cpc "les évolutions possibles de l'espace."

with Dissolve(0.5)


# AMENAGEMENT CLASSE

scene bureau_cpc
show viviane
cpc "Enfin, vous devrez présenter l'aménagement global de votre classe."
with Dissolve(0.5)
cpc "Cet aménagement devra être organisé en pôles d'apprentissage."
with Dissolve(0.5)
hide viviane
show viviane7
cpc "Votre plan de classe devra faire apparaître les différents pôles d'attractivités et leur aménagement."
with Dissolve(0.5)
cpc "Vous devrez également justifier vos choix."
with Dissolve(0.5)
jump ch5_choix

# QIZZ

label ch5_quiz_intro:

scene bureau_cpc
show viviane

$ score_pedagogique = 0

cpc "Avant votre présentation finale, je voudrais vérifier vos connaissances sur l'école maternelle."
with Dissolve(0.5)
cpc "Je vais vous poser quelques questions."
with Dissolve(0.5)
cpc "Aucune n’est là pour vous piéger."
with Dissolve(0.5)
cpc "Mais j’attends de vous un raisonnement de futurs enseignants."
with Dissolve(0.5)
jump quiz_cas_1

label quiz_cas_1:

scene bureau_cpc
show viviane5
menu:
    cpc "Dans une classe de PS-MS, des élèves jouent dans un espace marchande. Ils doivent tenir un rôle, résoudre un petit problème de commande, réutiliser du vocabulaire travaillé et jouer plusieurs fois la situation. Quelle analyse est la plus juste ?"

    "Cette situation relève uniquement d’« apprendre en jouant ».":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane2
        cpc "Le jeu est bien présent, mais votre analyse reste incomplète."
        cpc "Une même situation peut mobiliser plusieurs modalités d’apprentissage."
        jump quiz_cas_2

    "Cette situation peut relever à la fois du jeu, de la résolution de problème, de l’exercice et de la remémoration.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Exactement."
        cpc "À l’école maternelle, les modalités d’apprentissage ne sont pas exclusives les unes des autres."
        jump quiz_cas_2

    "Cette situation est trop complexe pour être vraiment pertinente en maternelle.":
        scene bureau_cpc
        show viviane
        cpc "Non. Elle peut être très pertinente si elle est pensée à hauteur d’enfant et accompagnée."
        jump quiz_cas_2

label quiz_cas_2:

scene bureau_cpc
show viviane5

menu:
    cpc "Après une activité, un élève de PS ne réussit pas complètement la tâche attendue. L’enseignante hésite entre plusieurs réactions. Laquelle est la plus cohérente avec l’évaluation à l’école maternelle ?"

    "Noter l’échec pour garder une trace claire et objective.":
        scene bureau_cpc
        show viviane
        cpc "Non. L’évaluation en maternelle n’entre ni une logique de note ni dans une logique de sélection. Il est question d'évaluation positive."
        jump quiz_cas_3

    "Observer ce que l’élève a compris, repérer ses progrès et ajuster ensuite les situations proposées.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Très bien."
        cpc "L’évaluation est d’abord un outil de régulation fondé sur l’observation et l’interprétation."
        jump quiz_cas_3

    "Comparer sa performance à celle des autres élèves du groupe pour le situer dans le groupe classe.":
        scene bureau_cpc
        show viviane
        cpc "Non. On s’intéresse d’abord au cheminement de l’enfant et à ses progrès par rapport à lui-même."
        jump quiz_cas_3

label quiz_cas_3:

scene bureau_cpc
show viviane5

menu:
    cpc "Une enseignante explique : « Je laisse le jeu aux temps où je dois être disponible ailleurs ; les apprentissages sérieux commencent ensuite. » Quelle analyse vous paraît la plus juste ?"

    "C’est vrai : le jeu sert surtout à occuper les élèves.":
        scene bureau_cpc
        show viviane
        cpc "Non. Le jeu ne peut pas être pensé comme un simple temps d’occupation."
        jump quiz_cas_4

    "C’est cohérent : le jeu offre l'avantage de se rendre disponible dans les pôles d'attractivité.":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane
        cpc "Le jeu offre effectivement l'avantage de pouvoir rendre l'adulte disponible dans les pôles d'aprentissage mais il doit être aussi et surtout pensé comme un moyen d'apprendre. "
        jump quiz_cas_4

    "C’est discutable : à l’école maternelle, le jeu fait partie des situations d’apprentissage, qu’il soit libre ou structuré.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Exactement."
        cpc "Le jeu libre ou structuré, avec des objectifs précis, sert de levier aux apprentissages. "
        jump quiz_cas_4

label quiz_cas_4:

scene bureau_cpc
show viviane5

menu:
    cpc "Deux groupes d’étudiants vous présentent leur projet. Le premier a reservé le temps de langage au regroupement. Le second a prévu de le travailler dans plusieurs pôles. Quel projet paraît le plus cohérent ?"

    "Le premier, car le regroupement est le moment naturel du langage.":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane2
        cpc "Le regroupement peut y contribuer, bien sûr."
        cpc "Mais le langage ne doit pas être limité à ce seul moment."
        jump quiz_cas_5

    "Le second, car le langage doit traverser l’ensemble des situations de classe.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Très bien."
        cpc "Le langage est au cœur des apprentissages et concerne tous les espaces."
        jump quiz_cas_5

    "Aucun des deux : le langage se construit surtout de manière spontanée, sans intervention de l'adulte.":
        scene bureau_cpc
        show viviane
        cpc "Non. Le développement du langage a besoin d’être pensé, soutenu et enrichi."
        jump quiz_cas_5

label quiz_cas_5:

scene bureau_cpc
show viviane5

menu:
    cpc "Vous observez deux espaces de jeu symbolique. Le premier est très décoré mais offre peu d’objets et peu de possibilités d’action. Le second est plus sobre, mais permet de jouer des rôles, de manipuler, d’interagir et de mobiliser un vocabulaire précis. Lequel est le plus pertinent ?"

    "Le premier, car un espace attractif doit d’abord être visuellement séduisant.":
        scene bureau_cpc
        show viviane
        cpc "La dimension esthétique est importante, mais cela ne suffit pas à rendre l’espace pédagogiquement riche."
        jump quiz_cas_6

    "Le second, car il permet de véritables interactions et des apprentissages.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Exactement."
        cpc "Un espace de jeu symbolique doit soutenir des interactions et des apprentissages, pas seulement une ambiance."
        cpc "Il faut cependant veiller à rendre l'espace attractif."
        jump quiz_cas_6

    "Les deux se valent, si les élèves sont contents d’y aller.":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane2
        cpc "L’adhésion des élèves compte, mais elle ne suffit pas à elle seule."
        jump quiz_cas_6

label quiz_cas_6:

scene bureau_cpc
show viviane5

menu:
    cpc "Une équipe prévoit, pour simplifier l’organisation, les mêmes activités, au même moment et pendant la même durée pour tous les élèves. Quelle analyse vous paraît la plus pertinente ?"

    "C’est une bonne solution, car elle garantit l’égalité.":
        scene bureau_cpc
        show viviane
        cpc "Non. Cela ne respecte ni les rythmes, ni le développement, ni l’hétérogénéité des élèves."
        jump quiz_cas_7

    "C’est problématique, car cela ne tient pas suffisamment compte des besoins et des rythmes des enfants.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Très bien."
        cpc "Une organisation pertinente part bien des besoins des enfants."
        jump quiz_cas_7

    "C’est acceptable seulement si l’ATSEM et l'enseignant gèrent une partie du groupe pour aider les élèves en difficulté.":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane2
        cpc "Cette réponse reste insuffisante."
        cpc "Le problème tient d’abord à la conception globale de l’organisation."
        jump quiz_cas_7

label quiz_cas_7:

scene bureau_cpc
show viviane5

menu:
    cpc "Pourquoi un univers de jeu doit-il être proche du vécu de l’enfant ?"

    "Parce que cela facilite la compréhension, l’engagement et la mobilisation du langage de l’enfant." :
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Très bien."
        jump quiz_cas_8

    "Parce que les univers imaginaires sont trop compliqués pour tous les enfants.":
        scene bureau_cpc
        show viviane
        cpc "C'est une mauvaise raison : les univers imaginaires ont leur place, mais ils demandent un accompagnement spécifique. Ils ne sont pas interdits."
        jump quiz_cas_8


label quiz_cas_8:

scene bureau_cpc
show viviane5

menu:
    cpc "Dans une classe accueillant des moins de 3 ans, un plan prévoit des meubles hauts qui cloisonnent fortement les espaces. Quelle analyse est la plus juste ?"

    "C’est positif, car cela cadre mieux les déplacements.":
        scene bureau_cpc
        show viviane
        cpc "Non. Cela peut nuire à la sécurité affective en empêchant le contact visuel avec l’adulte."
        jump quiz_cas_9

    "C’est problématique, car les très jeunes enfants ont besoin de pouvoir voir l’adulte et d’évoluer dans des espaces lisibles.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Exactement."
        cpc "Avec les moins de 3 ans, l’aménagement joue un rôle essentiel dans la sécurité affective et l’entrée dans les apprentissages."
        jump quiz_cas_9

    "Cela dépend seulement du caractère des enfants.":
        scene bureau_cpc
        show viviane
        cpc "Non. La question est d’abord développementale et liée au besoin de sécurité affective des élèves."
        jump quiz_cas_9

label quiz_cas_9:

scene bureau_cpc
show viviane5

menu:
    cpc "Pourquoi l'aménagement de la classe est-il important ?"

    "Parce qu'une classe doit être belle et agréable.":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane
        cpc "L'esthétique est importante, mais ce n’est pas l’objectif principal."
        jump quiz_cas_10

    "Parce qu'il influence l'engagement et les apprentissages":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Très bien."
        jump quiz_cas_10

    "Pour que tous les élèves restent assis et bougent le moins possible.":
        scene bureau_cpc
        show viviane2
        cpc "Pas du tout. L’aménagement devrait viser justement la circulation, l’autonomie et l’exploration."
        jump quiz_cas_10

label quiz_cas_10:

scene bureau_cpc
show viviane5

menu:
    cpc "Vous voulez faire évoluer votre coin jeu en espace à scénario. Quelle transformation paraît la plus pertinente ?"

    "Ajouter davantage d’objets et de décoration, sans modifier le fonctionnement.":
        $ score_pedagogique += 1
        scene bureau_cpc
        show viviane2
        cpc "L'enrichissement de la décoration et du matériel peut soutenir l’intérêt des élèves, mais cela ne suffit pas à créer un espace à scénario."
        jump quiz_resultats

    "Penser une situation précise, des rôles, des interactions attendues, un vocabulaire ciblé et un scénario pédagogique possible.":
        $ score_pedagogique += 2
        scene bureau_cpc
        show viviane4
        cpc "Parfait."
        cpc "C’est bien cette structuration pédagogique qui distingue un espace à scénario d’un simple coin jeu."
        jump quiz_resultats

    "Laisser les élèves improviser entièrement, sans intention pédagogique définie.":
        scene bureau_cpc
        show viviane
        cpc "Non. L’espace à scénario suppose une pensée pédagogique explicite."
        jump quiz_resultats

label quiz_resultats:

scene bureau_cpc
show viviane

cpc "Très bien. Regardons maintenant ce que montrent vos réponses."
with Dissolve(0.5)

cpc "Vous avez obtenu [score_pedagogique] points sur [score_max]."

if score_pedagogique >= 16:
    scene bureau_cpc
    show viviane4
    cpc "Votre raisonnement est très solide."
    cpc "Vous mobilisez les concepts importants sans rester à la surface des choses."

elif score_pedagogique >= 11:
    scene bureau_cpc
    show viviane7
    cpc "Votre préparation est sérieuse."
    cpc "Les fondements sont là, mais certains choix devront être mieux justifiés à l’oral."

elif score_pedagogique >= 7:
    scene bureau_cpc
    show viviane
    cpc "Votre projet est intéressant, mais plusieurs repères restent encore fragiles."
    cpc "Je vous conseille de retravailler les liens entre besoins des élèves, aménagement et apprentissages."

else:
    scene bureau_cpc
    show viviane
    cpc "Je vous encourage à reprendre plusieurs points importants avant la présentation finale."
    cpc "Vous avez encore besoin de consolider vos repères pédagogiques."

jump ch5_choix

