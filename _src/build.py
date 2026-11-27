"""Génère toutes les pages HTML du site (FR à la racine, EN dans en/).

Usage : python _src/build.py   (depuis n'importe quel dossier)
Le contenu se modifie ici, pas dans les fichiers .html générés.
GitHub Pages ignore les dossiers commençant par « _ », ce script n'est donc pas publié.
"""
import os
from html import escape as e

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://arthursvz.github.io'
YEAR = 2026

# ---------------------------------------------------------------- Entités
# clé : (nom, url ou None, fichier logo ou None, style)  style: '' | 'bleed' | monogramme
ENT = {
    'n7':     ('ENSEEIHT · Toulouse INP', 'https://www.enseeiht.fr', 'enseeiht.png', 'bleed'),
    'laval':  ('Université Laval', 'https://www.ulaval.ca', 'ulaval.png', ''),
    'airbus': ('Airbus Defence and Space', 'https://www.airbus.com', 'airbus.svg', ''),
    'pref':   ('Préfecture de la Haute-Garonne', 'https://www.haute-garonne.gouv.fr', 'prefecture.png', ''),
    'irt':    ('IRT Saint Exupéry', 'https://www.irt-saintexupery.com', 'irt.png', ''),
    'pc':     ('Protection Civile', 'https://www.protection-civile.org', 'protection-civile.png', ''),
    'grinp':  ("Gr'INP", 'https://grinp.inpt.fr', 'grinp.png', ''),
    'net7':   ('net7', 'https://net7.dev', 'net7.svg', ''),
    'w7':     ('Women7', None, 'women7.png', ''),
    'eedf':   ('Éclaireuses Éclaireurs de France', 'https://www.eedf.fr', 'eedf.svg', ''),
    'ffme':   ('FFME', 'https://www.ffme.fr', 'ffme.svg', ''),
    'cam':    ('Cambridge University Press & Assessment', 'https://www.cambridgeenglish.org', 'cambridge.png', ''),
    'gdp':    ('MOOC GdP · Centrale Lille', None, 'mooc-gdp.png', ''),
    'bellevue': ('Lycée Bellevue', None, 'bellevue.png', ''),
    'limosin':  ('Lycée Léonard Limosin', None, 'limosin.png', ''),
}


def logo(k, p, size=''):
    name, url, img, style = ENT[k]
    cls = 'logo' + (' sm' if size == 'sm' else '')
    if img:
        if style == 'bleed':
            cls += ' bleed'
        inner = f'<img src="{p}assets/logos/{img}" alt="{e(name)}" loading="lazy">'
    else:
        cls += ' mono'
        inner = f'<span aria-hidden="true">{style}</span><span class="sr">{e(name)}</span>'
    if url:
        return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener" title="{e(name)}">{inner}</a>'
    return f'<span class="{cls}" title="{e(name)}">{inner}</span>'


def org(k, label=None):
    name, url, _, _ = ENT[k]
    label = e(label or name)
    if url:
        return f'<a class="ext" href="{url}" target="_blank" rel="noopener">{label}</a>'
    return label


# ---------------------------------------------------------------- Données
EXP = [
    dict(id='airbus', banner=('airbus',), ent='airbus',
         when={'fr': 'Févr. – juil. 2027 · 6 mois', 'en': 'Feb – Jul 2027 · 6 months'},
         role={'fr': "Projet de fin d'études", 'en': 'Final-year project'},
         badge={'fr': 'À venir', 'en': 'Upcoming'},
         text={'fr': "Stage de 6 mois (projet de fin d'études).",
               'en': '6-month internship (final-year project).'},
         stats={'fr': [('6 mois', 'de stage'), ('Févr. 2027', 'début'), ('Juil. 2027', 'fin')],
                'en': [('6 months', 'internship'), ('Feb 2027', 'start'), ('Jul 2027', 'end')]},
         rows={'fr': [('Cadre', "Projet de fin d'études, diplôme d'ingénieur ENSEEIHT")],
               'en': [('Context', 'Final-year project, ENSEEIHT engineering degree')]}),
    dict(id='prefecture', banner=('prefecture',), ent='pref',
         when={'fr': 'Juin – août 2026 · 11 semaines', 'en': 'Jun – Aug 2026 · 11 weeks'},
         role={'fr': 'Stage · SGCD, service SIC', 'en': 'Internship · SGCD, IT department (SIC)'},
         text={'fr': "Développement d'un site centralisant les annuaires des agents : six sources de données fusionnées en un annuaire unique et à jour. L'outil est en production, à usage interne.",
               'en': 'Built a website that centralises staff directories, merging six data sources into a single, up-to-date directory. The tool is in production for internal use.'},
         stats={'fr': [('~1 000', 'agents'), ('6', 'sources de données'), ('En production', 'usage interne')],
                'en': [('~1,000', 'staff'), ('6', 'data sources'), ('In production', 'internal use')]},
         rows={'fr': [('Technologies', 'Serveur LAMP (Linux, Apache, MySQL, PHP)')],
               'en': [('Stack', 'LAMP server (Linux, Apache, MySQL, PHP)')]}),
    dict(id='irt', banner=('irt',), ent='irt',
         when={'fr': 'Juin – juil. 2025 · 6 semaines', 'en': 'Jun – Jul 2025 · 6 weeks'},
         role={'fr': 'Stage de recherche', 'en': 'Research internship'},
         text={'fr': 'Travaux de recherche sur les LLM spécialisés en cybersécurité et sur les IDS/IPS fondés sur des réseaux de neurones.',
               'en': 'Research on cybersecurity-specialised LLMs and neural-network-based IDS/IPS.'},
         stats={'fr': [('6 semaines', 'de stage'), ('LLM', 'spécialisés en cybersécurité'), ('IDS/IPS', 'à base de réseaux de neurones')],
                'en': [('6 weeks', 'internship'), ('LLMs', 'specialised in cybersecurity'), ('IDS/IPS', 'based on neural networks')]},
         rows={'fr': [('Domaine', 'IA, cybersécurité')], 'en': [('Field', 'AI, cybersecurity')]}),
]

PROJ = [
    dict(id='net7-infra', banner=('net7-infra',), ent='net7',
         when={'fr': "2025 – aujourd'hui", 'en': '2025 – present'},
         role={'fr': 'Infrastructure de virtualisation net7', 'en': 'net7 virtualisation infrastructure'},
         text={'fr': "Administration du cluster Proxmox de l'association : six hyperviseurs, stockage distribué Ceph sur trois nœuds et migration à chaud des machines virtuelles. Une vingtaine de VM hébergent les services des étudiants.",
               'en': "Administering the association's Proxmox cluster: six hypervisors, Ceph distributed storage on three nodes and live migration of virtual machines. Around twenty VMs host the students' services."},
         stats={'fr': [('6', 'hyperviseurs en cluster'), ('3', 'nœuds Ceph'), ('~20', 'machines virtuelles')],
                'en': [('6', 'clustered hypervisors'), ('3', 'Ceph nodes'), ('~20', 'virtual machines')]},
         rows={'fr': [('Services', 'Git, mail, site web, pare-feu…')],
               'en': [('Services', 'Git, mail, website, firewall…')]}),
    dict(id='interconnexion', banner=('interco',), ent='n7',
         when={'fr': '2025 – 2026 · 2e année', 'en': '2025 – 2026 · 2nd year'},
         role={'fr': 'Projet Interconnexion', 'en': 'Network interconnection project'},
         text={'fr': "Conception et configuration du réseau complet d'une entreprise dans un environnement virtualisé : routage, VPN, serveurs web et services d'infrastructure.",
               'en': "Designed and configured a complete company network in a virtualised environment: routing, VPN, web servers and infrastructure services."},
         stats={'fr': [('6', "étudiants dans l'équipe"), ('VPN', 'et serveurs web'), ('100 %', 'virtualisé')],
                'en': [('6', 'students in the team'), ('VPN', 'and web servers'), ('100 %', 'virtualised')]},
         rows={'fr': [('Domaine', 'Réseaux, administration système')],
               'en': [('Field', 'Networking, system administration')]}),
    dict(id='reseaux-mobiles', banner=('mobile',), ent='n7',
         when={'fr': '2025 – 2026 · 2e année', 'en': '2025 – 2026 · 2nd year'},
         role={'fr': 'Projet Réseaux mobiles', 'en': 'Mobile networks project'},
         text={'fr': "Simulation d'un handover entre deux antennes 4G : reconfiguration d'une carte SIM et observation du basculement d'une cellule à l'autre.",
               'en': 'Simulated a handover between two 4G cells: reconfigured a SIM card and observed the switch from one cell to the other.'},
         stats={'fr': [('4G', 'LTE'), ('2', 'antennes'), ('SIM', 'reconfigurée')],
                'en': [('4G', 'LTE'), ('2', 'cells'), ('SIM', 'reconfigured')]},
         rows={'fr': [('Domaine', 'Réseaux mobiles, télécommunications')],
               'en': [('Field', 'Mobile networks, telecommunications')]}),
    dict(id='wifi', banner=('wifi',), ent='n7',
         when={'fr': '2025 – 2026 · 2e année', 'en': '2025 – 2026 · 2nd year'},
         role={'fr': 'Projet Couche physique Wi-Fi', 'en': 'Wi-Fi physical layer project'},
         text={'fr': "Simulation sous Matlab de la couche physique d'une liaison Wi-Fi (OFDM, IEEE 802.11a) avec la chaîne de codage du standard DVB-S : modulation QPSK et filtrage en racine de cosinus surélevé, code convolutif décodé par Viterbi (décision dure et souple), Reed-Solomon et entrelacement. Validation sur canal à bruit blanc gaussien, puis sur canal multi-trajets avec égalisation et prise en compte de l'état du canal (CSI) pour supprimer le plancher d'erreur.",
               'en': 'Matlab simulation of the physical layer of a Wi-Fi link (OFDM, IEEE 802.11a) with the DVB-S coding chain: QPSK modulation with root-raised-cosine filtering, convolutional code with Viterbi decoding (hard and soft decision), Reed-Solomon and interleaving. Validated on an additive white Gaussian noise channel, then on a multipath channel with equalisation and channel state information (CSI) to remove the error floor.'},
         stats={'fr': [('Solo', 'projet individuel'), ('802.11a', 'OFDM'), ('Viterbi', 'dur et souple')],
                'en': [('Solo', 'individual project'), ('802.11a', 'OFDM'), ('Viterbi', 'hard and soft')]},
         rows={'fr': [('Domaine', 'Télécommunications, codage canal')],
               'en': [('Field', 'Telecommunications, channel coding')]}),
    dict(id='grinp-web', banner=('grinp-web',), ent='grinp',
         when={'fr': '2025 – aujourd\'hui', 'en': '2025 – present'},
         role={'fr': "Plateforme web du club d'escalade", 'en': 'Climbing club web platform'},
         text={'fr': "Reprise et maintenance de la plateforme du club Gr'INP, conçue en 2024 par un autre membre : comptes adhérents, calendrier et inscriptions aux séances, pour les quelque 200 adhérents.",
               'en': "Took over and maintain the Gr'INP club platform, first built in 2024 by another member: member accounts, calendar and session sign-ups for around 200 members."},
         links=[('grinp.inpt.fr', 'https://grinp.inpt.fr')],
         stats={'fr': [('~200', 'adhérents'), ('Depuis 2025', 'maintenance'), ('En production', 'grinp.inpt.fr')],
                'en': [('~200', 'members'), ('Since 2025', 'maintenance'), ('In production', 'grinp.inpt.fr')]},
         rows={'fr': [('Fonctionnalités', 'Comptes adhérents, calendrier, inscriptions aux séances')],
               'en': [('Features', 'Member accounts, calendar, session sign-ups')]}),
]

ENG = [
    dict(id='protection-civile', banner=('pc',), ent='pc', orgname={'fr': 'Protection Civile de la Haute-Garonne', 'en': 'Civil Protection, Haute-Garonne'},
         when={'fr': 'Sept. 2024 – aujourd\'hui', 'en': 'Sep 2024 – present'},
         role={'fr': "Équipier-secouriste, chef d'équipe, chef de poste", 'en': 'First-aid team member, team leader, post leader'},
         text={'fr': "Secours à personnes sur dispositifs prévisionnels de secours, déclenchements fédéraux et gardes SAMU. Aujourd'hui chef d'équipe et chef de poste : j'encadre les secouristes et coordonne les postes de secours.",
               'en': 'First aid at planned event cover, federal call-outs and SAMU (emergency medical service) shifts. Now a team leader and post leader: I lead first-aiders and coordinate first-aid posts.'},
         stats={'fr': [('600 h+', 'de bénévolat par an'), ('Des centaines', "d'activités"), ('PSE1 · PSE2 · AEP1', 'certifications')],
                'en': [('600 h+', 'volunteering per year'), ('Hundreds', 'of activities'), ('PSE1 · PSE2 · AEP1', 'certifications')]},
         rows={'fr': [('Missions marquantes', 'Incendies de Bordeaux (déclenchement fédéral), Marathon de Toulouse, gardes SAMU')],
               'en': [('Notable missions', 'Bordeaux wildfires (federal call-out), Toulouse Marathon, SAMU shifts')]},
         card={'fr': ('600 h+', 'de secours par an'), 'en': ('600 h+', 'of first aid per year')}),
    dict(id='grinp', banner=('grinp',), ent='grinp', orgname={'fr': "Club Gr'INP · AS Toulouse INP", 'en': "Gr'INP club · AS Toulouse INP"},
         when={'fr': '2024 – aujourd\'hui', 'en': '2024 – present'},
         role={'fr': "Président du club d'escalade", 'en': 'President of the climbing club'},
         text={'fr': "Direction de la section : organisation des séances et des événements, gestion du budget et des adhésions, coordination de l'équipe de bénévoles et lien avec le bureau de l'AS. Initiateur escalade breveté FFME.",
               'en': 'Running the section: organising sessions and events, managing the budget and memberships, coordinating the volunteer team and liaising with the sports association board. FFME-certified climbing instructor.'},
         stats={'fr': [('200', 'adhérents'), ('14', 'bénévoles'), ('3 k€', 'de budget annuel')],
                'en': [('200', 'members'), ('14', 'volunteers'), ('€3k', 'annual budget')]},
         rows={'fr': [('Événements', "Compétitions, soirées « Nuits de l'escalade »")],
               'en': [('Events', "Competitions, “Nuits de l'escalade” evenings")]},
         card={'fr': ('200', 'adhérents, 14 bénévoles'), 'en': ('200', 'members, 14 volunteers')}),
    dict(id='net7', banner=('net7',), ent='net7', orgname={'fr': "net7, association informatique de l'ENSEEIHT", 'en': "net7, ENSEEIHT's IT association"},
         when={'fr': '2025 – aujourd\'hui', 'en': '2025 – present'},
         role={'fr': 'Administrateur systèmes et réseaux', 'en': 'Systems and network administrator'},
         text={'fr': "Administration système de l'ensemble de l'infrastructure de l'association : machines virtuelles sur les hyperviseurs Proxmox, infrastructure réseau, services hébergés pour les étudiants, supervision et sécurisation.",
               'en': "System administration across the association's whole infrastructure: virtual machines on Proxmox hypervisors, network infrastructure, services hosted for students, monitoring and security."},
         stats={'fr': [('6', 'hyperviseurs en cluster'), ('3', 'nœuds Ceph'), ('~20', 'machines virtuelles')],
                'en': [('6', 'clustered hypervisors'), ('3', 'Ceph nodes'), ('~20', 'virtual machines')]},
         rows={'fr': [('Détails', '<a class="ext" href="experiences.html#net7-infra">Projet Infrastructure de virtualisation</a>')],
               'en': [('Details', '<a class="ext" href="experience.html#net7-infra">Virtualisation infrastructure project</a>')]},
         card={'fr': ('Proxmox', 'VM, réseau, services'), 'en': ('Proxmox', 'VMs, network, services')}),
    dict(id='women7', banner=('ceve',), ent='w7', orgname={'fr': 'Women7 · ENSEEIHT', 'en': 'Women7 · ENSEEIHT'},
         when={'fr': 'Juin 2025 – juin 2026', 'en': 'Jun 2025 – Jun 2026'},
         role={'fr': 'Membre du bureau', 'en': 'Board member'},
         text={'fr': "Au sein d'un bureau de trois personnes, organisation de la journée annuelle d'accueil des collégiennes d'Occitanie à l'ENSEEIHT : découverte des métiers de l'ingénierie, pour les encourager à s'orienter vers les filières scientifiques.",
               'en': 'As one of a three-person board, organised the annual day welcoming middle-school girls from Occitanie to ENSEEIHT, introducing engineering careers to encourage them towards science.'},
         stats={'fr': [('200', 'collégiennes accueillies'), ('3', 'membres du bureau'), ('1', 'journée par an')],
                'en': [('200', 'girls welcomed'), ('3', 'board members'), ('1', 'day each year')]},
         rows={'fr': [('Public', "Collégiennes d'Occitanie")],
               'en': [('Audience', 'Middle-school girls from Occitanie')]},
         card={'fr': ('200', 'collégiennes accueillies'), 'en': ('200', 'girls welcomed')}),
    dict(id='ceve', banner=('women7',), ent='n7', orgname={'fr': "Conseil des études et de la vie étudiante · ENSEEIHT", 'en': 'Studies and Student Life Council · ENSEEIHT'},
         when={'fr': '2024 – aujourd\'hui', 'en': '2024 – present'},
         role={'fr': 'Représentant étudiant', 'en': 'Student representative'},
         text={'fr': "Porte-parole des étudiants auprès de l'équipe pédagogique et de l'administration. Je participe aux décisions sur les formations et la vie étudiante, dont le vote des modalités de contrôle des connaissances (MCC).",
               'en': 'Student spokesperson to the teaching staff and administration. I take part in decisions on programmes and student life, including voting on assessment rules (MCC).'},
         stats={'fr': [('Élu', 'représentant étudiant'), ('MCC', 'votées en conseil'), ('Depuis 2024', 'mandat')],
                'en': [('Elected', 'student representative'), ('MCC', 'voted in council'), ('Since 2024', 'term')]},
         rows={'fr': [('Sujets', 'Formations, vie étudiante, modalités de contrôle des connaissances')],
               'en': [('Topics', 'Programmes, student life, assessment rules')]},
         card={'fr': ('Élu', 'vote des MCC'), 'en': ('Elected', 'votes on assessment rules')}),
    dict(id='eedf', banner=('eedf',), ent='eedf', orgname={'fr': 'Éclaireuses Éclaireurs de France · Limoges', 'en': 'Éclaireuses Éclaireurs de France (scouts) · Limoges'},
         when={'fr': '2021 – 2022', 'en': '2021 – 2022'},
         role={'fr': "Responsable d'animation et assistant sanitaire", 'en': 'Activity leader and health officer'},
         text={'fr': "Pendant un an, encadrement et animation d'activités pour les jeunes du groupe, et suivi sanitaire en tant qu'assistant sanitaire.",
               'en': 'For a year, led activities for the young members of the group and handled health matters as health officer.'},
         stats={'fr': [('1 an', "d'engagement"), ('Animation', 'des jeunes du groupe'), ('Sanitaire', 'suivi des jeunes')],
                'en': [('1 year', 'of commitment'), ('Activities', 'for young members'), ('Health', 'health officer')]},
         rows={'fr': [('Lieu', 'Limoges')], 'en': [('Location', 'Limoges')]},
         card={'fr': ('1 an', "d'animation"), 'en': ('1 year', 'leading activities')}),
]

# Formation : un point par année scolaire (la plus récente en haut).
# ue : unités d'enseignement suivies, liste de U(...) ; liste vide = bloc masqué.
# Chaque UE a sa fiche sur la page « unités d'enseignement » (hors menu), ancrée par son id.
# sem : numéro du semestre (5, 6, 7…) ; les UE sont regroupées par semestre, dans l'ordre de la liste.
# proj : (page, ancre) d'un projet ou d'une expérience lié(e), affiché en lien sur la fiche.
def U(id, fr, en, dfr, den, sfr, sen, sem=None, proj=None):
    return dict(id=id, name={'fr': fr, 'en': en}, desc={'fr': dfr, 'en': den}, skills={'fr': sfr, 'en': sen}, sem=sem, proj=proj)


def by_sem(items):
    """[(semestre, [UE…]), …] dans l'ordre d'apparition."""
    groups = []
    for u in items:
        if groups and groups[-1][0] == u['sem']:
            groups[-1][1].append(u)
        else:
            groups.append((u['sem'], [u]))
    return groups


def sem_label(lang, n):
    return ('Semestre ' if lang == 'fr' else 'Semester ') + str(n)


EDU = [
    dict(ent='n7', future=True, when={'fr': 'Oct. 2027', 'en': 'Oct 2027'}, where='Toulouse',
         role={'fr': "Diplôme d'ingénieur · Informatique et Télécommunications", 'en': 'Engineering degree · Computer Science and Telecommunications'},
         text={'fr': "Fin du cursus ENSEEIHT, département Sciences du Numérique.", 'en': 'Completion of the ENSEEIHT programme, Digital Sciences department.'}),
    dict(ent='airbus', future=True, when={'fr': 'Févr. – juil. 2027', 'en': 'Feb – Jul 2027'}, where='',
         role={'fr': "3e année · Projet de fin d'études", 'en': '3rd year · Final-year project'},
         text={'fr': 'Stage de 6 mois en administration système chez Airbus Defence and Space.',
               'en': '6-month internship in system administration at Airbus Defence and Space.'}),
    dict(ent='laval', now=True, when={'fr': 'Automne 2026', 'en': 'Fall 2026'}, where='Québec',
         role={'fr': "3e année · Semestre d'échange", 'en': '3rd year · Exchange semester'},
         text={'fr': "Semestre d'automne à l'Université Laval, dans le cadre du cursus ENSEEIHT.",
               'en': 'Fall semester at Université Laval, as part of the ENSEEIHT programme.'},
         ue=[  # S9 validé avec Arthur (semestre en cours)
             U('cloud-devops', 'Applications infonuagiques natives et DevOps', 'Cloud-native applications and DevOps',
               "Applications natives infonuagiques et chaîne DevOps (intégration et déploiement continus), principalement avec Kubernetes. Présentation de travaux de recherche sur le sujet, centrée sur le découpage d'une application monolithique en microservices à l'aide d'un modèle neuronal.",
               'Cloud-native applications and the DevOps toolchain (continuous integration and delivery), mainly with Kubernetes. Presentation of research work on the topic, focused on splitting a monolithic application into microservices with a neural model.',
               ['Kubernetes', 'Conteneurs', 'Microservices', 'CI/CD', 'Veille scientifique'],
               ['Kubernetes', 'Containers', 'Microservices', 'CI/CD', 'Research review'], sem=9),
             U('ihm', 'Ingénierie des interfaces personnes-machines', 'Human-computer interface engineering',
               "Analyse des tâches et personas. Projet de conception d'interface : questionnaire et analyse des besoins, analyse hiérarchique des tâches (AHT), scénarios, maquette sous Figma, puis évaluation.",
               'Task analysis and personas. Interface design project: questionnaire and needs analysis, hierarchical task analysis (HTA), scenarios, Figma mock-up, then evaluation.',
               ['Analyse des besoins', 'Personas', 'Analyse des tâches (AHT)', 'Figma', "Évaluation d'interface"],
               ['Needs analysis', 'Personas', 'Task analysis (HTA)', 'Figma', 'Interface evaluation'], sem=9),
             U('reseaux-mobiles', 'Réseaux mobiles', 'Mobile networks',
               "Cours tourné vers les évolutions récentes : la 5G et les pistes de recherche actuelles, en complément des enseignements de l'ENSEEIHT.",
               'A course focused on recent developments: 5G and current research directions, complementing what I studied at ENSEEIHT.',
               ['5G', '4G / LTE', 'Veille technologique'],
               ['5G', '4G / LTE', 'Technology watch'], sem=9),
             U('gouvernance-securite', "Gouvernance de la sécurité de l'information", 'Information security governance',
               "Normes, analyse de risques, politiques de sécurité et conformité. Analyse individuelle d'un incident de sécurité réel, touchant une administration fiscale, et présentation en groupe de six sur la sécurité du vote par internet.",
               'Standards, risk analysis, security policies and compliance. Individual analysis of a real security incident affecting a tax administration, and a group presentation (six students) on the security of internet voting.',
               ['Analyse de risques', 'Politiques de sécurité', 'Conformité', "Analyse d'incident"],
               ['Risk analysis', 'Security policies', 'Compliance', 'Incident analysis'], sem=9),
             U('gestion-projet', 'Gestion de projet', 'Project management',
               "Gestion de projet classique : cadrage, planification, budget et suivi des risques. Projet d'équipe de six sur tout le semestre : le déploiement d'une application de covoiturage dans une nouvelle région du Québec.",
               "Traditional project management: scoping, planning, budget and risk tracking. A semester-long team project (six students): rolling out a carpooling app in a new region of Quebec.",
               ['Gestion de projet', 'Planification', 'Gestion des risques', 'Travail en équipe'],
               ['Project management', 'Planning', 'Risk management', 'Teamwork'], sem=9),
         ]),
    dict(ent='n7', when={'fr': '2025 – 2026', 'en': '2025 – 2026'}, where='Toulouse',
         role={'fr': '2e année · Département Sciences du Numérique (Parcours Réseau)', 'en': '2nd year · Digital Sciences Department (Networks track)'},
         text={'fr': 'Spécialisation en réseaux informatiques et systèmes.', 'en': 'Specialisation in computer networks and systems.'},
         ue=[  # S7 et S8 validés avec Arthur
             U('canaux-selectifs', 'Communications numériques sur canaux sélectifs', 'Digital communications over selective channels',
               "Transmission sur canaux sélectifs en fréquence : chaîne OFDM, intervalle de garde et préfixe cyclique, égalisation (forçage à zéro, maximum de vraisemblance), erreurs de synchronisation. Sous Matlab, avec un projet individuel : la couche physique du Wi-Fi.",
               'Transmission over frequency-selective channels: OFDM chain, guard interval and cyclic prefix, equalisation (zero forcing, maximum likelihood), synchronisation errors. In Matlab, with an individual project: the Wi-Fi physical layer.',
               ['OFDM', 'Égalisation', 'Wi-Fi (802.11)', 'Matlab'],
               ['OFDM', 'Equalisation', 'Wi-Fi (802.11)', 'Matlab'], sem=7, proj=('exp', 'wifi')),
             U('communications-codees', 'Communications numériques codées', 'Coded digital communications',
               "Codage de source et codage de canal : codes en blocs (Reed-Solomon), codes convolutifs et décodage de Viterbi, poinçonnage, entrelacement, turbo-codes, LDPC. Sous Matlab, et mis en application dans le projet Wi-Fi.",
               'Source coding and channel coding: block codes (Reed-Solomon), convolutional codes and Viterbi decoding, puncturing, interleaving, turbo codes, LDPC. In Matlab, and applied in the Wi-Fi project.',
               ['Codage de canal', 'Codage de source', 'Décodage de Viterbi', 'Matlab'],
               ['Channel coding', 'Source coding', 'Viterbi decoding', 'Matlab'], sem=7, proj=('exp', 'wifi')),
             U('reseaux-locaux', 'Réseaux locaux et de télécommunication', 'Local and telecommunication networks',
               "Réseaux locaux (Ethernet et VLAN, Wi-Fi, commutation) et réseaux d'opérateurs : MPLS, xDSL, fibre.",
               'Local area networks (Ethernet and VLANs, Wi-Fi, switching) and carrier networks: MPLS, xDSL, fibre.',
               ['Ethernet', 'VLAN', 'Commutation', 'MPLS'],
               ['Ethernet', 'VLAN', 'Switching', 'MPLS'], sem=7),
             U('internet-graphe', 'Internet et graphe', 'Internet and graphs',
               "Modèle OSI, routage IP (OSPF, BGP) et théorie des graphes appliquée aux réseaux : plus courts chemins, flots.",
               'The OSI model, IP routing (OSPF, BGP) and graph theory applied to networks: shortest paths, flows.',
               ['Modèle OSI', 'Routage IP', 'OSPF / BGP', 'Théorie des graphes'],
               ['OSI model', 'IP routing', 'OSPF / BGP', 'Graph theory'], sem=7),
             U('systemes-concurrents', 'Systèmes concurrents et communicants', 'Concurrent and communicating systems',
               "Threads, synchronisation (sémaphores, moniteurs), interblocage, sockets et communication entre processus, en C et en Go. Projet en C : un moteur faisant tourner deux processus en parallèle selon le schéma lecteurs-rédacteurs, avec deux lecteurs et deux rédacteurs.",
               'Threads, synchronisation (semaphores, monitors), deadlock, sockets and inter-process communication, in C and Go. C project: an engine running two processes in parallel on the readers-writers pattern, with two readers and two writers.',
               ['Programmation concurrente', 'C', 'Go', 'Sockets'],
               ['Concurrent programming', 'C', 'Go', 'Sockets'], sem=7),
             U('soft-human-skills-s7', 'Soft and Human Skills', 'Soft and Human Skills',
               "Allemand, et projet escalade évalué sur mon investissement au club Gr'INP. Dispensé du module Career Management au titre de mon engagement à la Protection Civile.",
               "German, and a climbing project assessed on my involvement in the Gr'INP club. Exempted from the Career Management module thanks to my commitment to the Civil Protection.",
               ['Gestion associative et budget', "Encadrement d'équipes"],
               ['Running an association and budget', 'Team leadership'], sem=7),
             U('idm-web', 'Ingénierie dirigée par les modèles et développement web', 'Model-driven engineering and web development',
               "Ingénierie dirigée par les modèles : métamodélisation et transformations de modèles avec les outils Eclipse (EMF, Sirius, Xtext, ATL). Développement web en HTML, CSS et Java.",
               'Model-driven engineering: metamodelling and model transformations with Eclipse tools (EMF, Sirius, Xtext, ATL). Web development in HTML, CSS and Java.',
               ['Métamodélisation', 'Eclipse EMF', 'HTML / CSS', 'Java'],
               ['Metamodelling', 'Eclipse EMF', 'HTML / CSS', 'Java'], sem=8),  # TODO : projet web (sujet à retrouver)
             U('science-reseaux', 'Science des réseaux et apprentissage', 'Network science and machine learning',
               "Analyse de graphes et de réseaux complexes (centralité, détection de communautés) et apprentissage automatique appliqué aux réseaux : détection d'anomalies, classification de trafic.",
               'Analysis of graphs and complex networks (centrality, community detection) and machine learning applied to networks: anomaly detection, traffic classification.',
               ['Réseaux complexes', 'Analyse de graphes', 'Apprentissage automatique', "Détection d'anomalies"],
               ['Complex networks', 'Graph analysis', 'Machine learning', 'Anomaly detection'], sem=8),
             U('interconnexions-modelisation', 'Interconnexions et modélisation des réseaux', 'Network interconnection and modelling',
               "Interconnexion de réseaux et évaluation de leurs performances : files d'attente, modélisation et simulation. Mis en pratique dans le projet Interconnexion : le réseau complet d'une entreprise, en environnement virtualisé.",
               "Network interconnection and performance evaluation: queueing theory, modelling and simulation. Put into practice in the Interconnection project: a company's complete network, in a virtualised environment.",
               ['Routage, commutation', 'VPN', "Files d'attente", 'Évaluation de performances'],
               ['Routing, switching', 'VPN', 'Queueing theory', 'Performance evaluation'], sem=8, proj=('exp', 'interconnexion')),
             U('telecom-sans-fil', 'Systèmes de télécom sans fil et mobiles', 'Wireless and mobile telecom systems',
               "Architecture des réseaux 4G et 5G, interface radio et Wi-Fi. Projet : simulation d'un handover entre deux antennes 4G.",
               'Architecture of 4G and 5G networks, radio interface and Wi-Fi. Project: simulating a handover between two 4G cells.',
               ['4G / LTE', '5G', 'Interface radio', 'Wi-Fi (802.11)'],
               ['4G / LTE', '5G', 'Radio interface', 'Wi-Fi (802.11)'], sem=8, proj=('exp', 'reseaux-mobiles')),
             U('mobile-securite', 'Systèmes, applications mobiles et sécurité', 'Systems, mobile applications and security',
               "Développement d'applications Android sous Android Studio, et bonnes pratiques de sécurité dans la conception des systèmes et des applications.",
               'Android application development with Android Studio, and security best practices in designing systems and applications.',
               ['Android', 'Android Studio', 'Sécurité des applications'],
               ['Android', 'Android Studio', 'Application security'], sem=8),
             U('soft-human-skills-s8', 'Soft and Human Skills', 'Soft and Human Skills',
               "Allemand et projet escalade, avec la même dispense de Career Management qu'au S7, au titre de mon engagement à la Protection Civile.",
               'German and a climbing project, with the same Career Management exemption as in S7, thanks to my commitment to the Civil Protection.',
               ['Gestion associative et budget', "Encadrement d'équipes"],
               ['Running an association and budget', 'Team leadership'], sem=8),
         ]),
    dict(ent='n7', when={'fr': '2024 – 2025', 'en': '2024 – 2025'}, where='Toulouse',
         role={'fr': '1re année · Département Sciences du Numérique (Général)', 'en': '1st year · Digital Sciences Department (General)'},
         text={'fr': 'Entrée au département Sciences du Numérique.', 'en': 'Joined the Digital Sciences department.'},
         ue=[  # S5 et S6 validés avec Arthur
             U('soft-human-skills', 'Soft and Human Skills', 'Soft and Human Skills',
               "Escalade, anglais et allemand, et accompagnement vers l'emploi : rédaction de CV, simulations d'entretien et mise en relation avec des entreprises.",
               'Climbing, English and German, plus career support: CV writing, mock interviews and introductions to companies.',
               ['Anglais', 'Projet professionnel', "Entretiens d'embauche", 'Communication'],
               ['English', 'Career planning', 'Job interviews', 'Communication'], sem=5),
             U('integration-probabilites', 'Intégration et applications – Probabilités', 'Integration and applications – Probability',
               "Deux volets : l'intégration (théorie de la mesure, intégrale de Lebesgue et ses applications) d'une part, les probabilités d'autre part.",
               'Two parts: integration (measure theory, the Lebesgue integral and its applications) on one side, probability on the other.',
               ['Théorie de la mesure', 'Intégrale de Lebesgue', 'Probabilités'],
               ['Measure theory', 'Lebesgue integral', 'Probability'], sem=5),
             U('programmation-imperative', 'Programmation impérative (Ada)', 'Imperative programming (Ada)',
               "Bases de la programmation impérative en Ada, avec une conception par raffinages et des tests. Projet : compression de fichiers par codage de Huffman.",
               'Foundations of imperative programming in Ada, with stepwise refinement and testing. Project: file compression with Huffman coding.',
               ['Ada', 'Algorithmique', 'Conception par raffinages', 'Tests'],
               ['Ada', 'Algorithms', 'Stepwise refinement', 'Testing'], sem=5),
             U('modelisation-architecture', 'Modélisation et architecture des ordinateurs', 'Computer modelling and architecture',
               "Modélisation informatique : spécification des opérations et preuves formelles sous CoqIDE. Architecture : conception de circuits numériques en SHDL, un langage de description matériel simplifié.",
               'Computer modelling: specifying operations and writing formal proofs in CoqIDE. Architecture: designing digital circuits in SHDL, a simplified hardware description language.',
               ['Preuves formelles', 'Coq', 'Logique numérique', 'Description matérielle (HDL)'],
               ['Formal proofs', 'Coq', 'Digital logic', 'Hardware description (HDL)'], sem=5),
             U('analyse-numerique-stats', 'Analyse numérique et statistique', 'Numerical analysis and statistics',
               "Méthodes numériques et optimisation continue, puis statistique : estimation et tests d'hypothèses. Travaux pratiques sous Matlab.",
               'Numerical methods and continuous optimisation, then statistics: estimation and hypothesis testing. Lab work in Matlab.',
               ['Méthodes numériques', 'Optimisation continue', 'Statistiques', 'Matlab'],
               ['Numerical methods', 'Continuous optimisation', 'Statistics', 'Matlab'], sem=5),
             U('automatique-donnees', 'Automatique et analyse de données', 'Control theory and data analysis',
               "Automatique : transformée de Laplace, fonctions de transfert, correcteurs PID, représentation d'état et machines à états. Analyse de données : ACP et classification. Travaux pratiques sous Matlab.",
               'Control theory: Laplace transform, transfer functions, PID controllers, state-space representation and state machines. Data analysis: PCA and classification. Lab work in Matlab.',
               ['Automatique', 'Machines à états', 'Analyse de données', 'Matlab'],
               ['Control theory', 'State machines', 'Data analysis', 'Matlab'], sem=5),
             U('soft-human-skills-s6', 'Soft and Human Skills', 'Soft and Human Skills',
               "Escalade et allemand, et option Leadership consacrée à la gestion de projet. En parallèle, j'ai suivi et réussi le MOOC Gestion de projet de Centrale Lille.",
               'Climbing and German, plus the Leadership option, focused on project management. Alongside it, I took and passed the Centrale Lille Project Management MOOC.',
               ['Gestion de projet', 'Leadership', 'Travail en équipe'],
               ['Project management', 'Leadership', 'Teamwork'], sem=6),
             U('telecom-signal', 'Télécommunications et traitement du signal', 'Telecommunications and signal processing',
               "Analyse de Fourier, échantillonnage, filtrage, modulations numériques et chaîne de transmission. Travaux pratiques sous Matlab.",
               'Fourier analysis, sampling, filtering, digital modulation and transmission chains. Lab work in Matlab.',
               ['Traitement du signal', 'Modulations numériques', 'Chaîne de transmission', 'Matlab'],
               ['Signal processing', 'Digital modulation', 'Transmission chain', 'Matlab'], sem=6),
             U('reseaux-1a', 'Réseaux', 'Networks',
               "Introduction aux réseaux : modèle TCP/IP, adressage IP, routage et Ethernet. Travaux pratiques sur de vraies machines et de vrais switchs, dans une salle au réseau isolé : configuration en Bash et analyse de trafic avec Wireshark.",
               'Introduction to networking: the TCP/IP model, IP addressing, routing and Ethernet. Hands-on labs on real machines and switches in an isolated network room: configuration in Bash and traffic analysis with Wireshark.',
               ['TCP/IP', 'Adressage IP', 'Bash', 'Wireshark'],
               ['TCP/IP', 'IP addressing', 'Bash', 'Wireshark'], sem=6),
             U('calcul-scientifique', 'Calcul scientifique et apprentissage', 'Scientific computing and machine learning',
               "Algèbre linéaire numérique (décompositions, valeurs propres, moindres carrés) et bases de l'apprentissage automatique : régression, classification, réseaux de neurones. En Python.",
               'Numerical linear algebra (decompositions, eigenvalues, least squares) and machine learning foundations: regression, classification, neural networks. In Python.',
               ['Algèbre linéaire numérique', 'Apprentissage automatique', 'Réseaux de neurones', 'Python'],
               ['Numerical linear algebra', 'Machine learning', 'Neural networks', 'Python'], sem=6),
             U('technologie-objet', 'Technologie objet (Java)', 'Object technology (Java)',
               "Programmation orientée objet en Java : modélisation UML, patrons de conception et tests avec JUnit. Projet en équipe de six : un jeu vidéo développé en méthode agile, dont j'étais le Scrum Master.",
               'Object-oriented programming in Java: UML modelling, design patterns and testing with JUnit. Team project of six: a video game built with agile methods, in which I was Scrum Master.',
               ['Java', 'UML', 'Patrons de conception', 'JUnit', 'Méthodes agiles (Scrum)'],
               ['Java', 'UML', 'Design patterns', 'JUnit', 'Agile methods (Scrum)'], sem=6),
             U('architecture-systemes', 'Architecture et systèmes', 'Architecture and systems',
               "Architecture : suite du SHDL, avec la conception d'un opérateur simple cadencé par une horloge. Systèmes : fonctionnement d'un système d'exploitation (processus, mémoire, ordonnancement) et programmation en C sous Linux.",
               'Architecture: continuing with SHDL, designing a simple clocked operator. Systems: how an operating system works (processes, memory, scheduling) and C programming on Linux.',
               ['Systèmes d\'exploitation', 'C', 'Linux', 'Logique séquentielle'],
               ['Operating systems', 'C', 'Linux', 'Sequential logic'], sem=6),
         ]),
    dict(ent='bellevue', when={'fr': '2022 – 2024', 'en': '2022 – 2024'}, where='Toulouse',
         role={'fr': 'Classes préparatoires PCSI / PSI', 'en': 'Preparatory classes (CPGE) PCSI / PSI'},
         text={'fr': "Physique, chimie et sciences de l'ingénieur : PCSI en première année, PSI en seconde, puis concours.",
               'en': 'Physics, chemistry and engineering sciences: PCSI in the first year, PSI in the second, then the competitive entrance exams.'}),
    dict(ent='limosin', when={'fr': '2021 – 2022', 'en': '2021 – 2022'}, where='Limoges',
         role={'fr': 'Baccalauréat général, section européenne (anglais)', 'en': 'French baccalauréat, European section (English)'},
         text={'fr': 'Spécialités mathématiques et physique-chimie, option mathématiques expertes. Lycée de 2019 à 2022.',
               'en': 'Mathematics and physics-chemistry majors, advanced mathematics option. High school from 2019 to 2022.'}),
]

CERTS = [
    ('pc', {'fr': "Équipier-secouriste PSE2", 'en': 'First-aid team member (PSE2)'}, {'fr': 'Mars 2026', 'en': 'Mar 2026'}),
    ('cam', {'fr': 'Linguaskill Business · 178 points', 'en': 'Linguaskill Business · 178 points'}, {'fr': 'Juin 2026', 'en': 'Jun 2026'}),
    ('gdp', {'fr': 'MOOC Gestion de projet', 'en': 'Project Management MOOC'}, {'fr': 'Avr. 2025', 'en': 'Apr 2025'}),
    ('pc', {'fr': 'Aide et écoute psychologique (AEP1)', 'en': 'Psychological first aid and listening (AEP1)'}, {'fr': 'Févr. 2025', 'en': 'Feb 2025'}),
    ('pc', {'fr': 'Secouriste PSE1', 'en': 'First aider (PSE1)'}, {'fr': 'Déc. 2024', 'en': 'Dec 2024'}),
    ('ffme', {'fr': "Brevet fédéral d'initiateur SAE (escalade)", 'en': 'Federal climbing instructor certificate (indoor walls)'}, {'fr': 'Oct. 2024', 'en': 'Oct 2024'}),
]
CERT_ORG = {'pc': {'fr': 'Fédération Nationale de Protection Civile', 'en': 'French Civil Protection Federation'},
            'cam': {'fr': 'Cambridge University Press & Assessment', 'en': 'Cambridge University Press & Assessment'},
            'ffme': {'fr': 'Fédération Française de la Montagne et de l\'Escalade', 'en': 'French Mountaineering and Climbing Federation'},
            'gdp': {'fr': 'Centrale Lille · MOOC GdP de Rémi Bachelet', 'en': 'Centrale Lille · MOOC GdP by Rémi Bachelet'}}

# Compétences : (libellé, (page, ancre) ou None). Une ancre = là où la compétence a été mise en œuvre.
SKILLS = {
    'fr': [
        ('Systèmes et virtualisation', [('Linux', None), ('Windows', None), ('Proxmox VE', ('exp', 'net7-infra')), ('Ceph', ('exp', 'net7-infra')), ('Migration à chaud', ('exp', 'net7-infra'))]),
        ('Réseaux', [('TCP/IP', None), ('Routage, commutation', ('exp', 'interconnexion')), ('VPN', ('exp', 'interconnexion')), ('4G / LTE', ('exp', 'reseaux-mobiles')), ('5G', None), ('Wireshark', None)]),
        ('DevOps et web', [('Git', None), ('CI/CD', None), ('Bash', None), ('Serveur LAMP', ('exp', 'prefecture')), ('Plateforme web', ('exp', 'grinp-web')), ('Figma', None)]),
        ('Cybersécurité et IA', [('LLM spécialisés', ('exp', 'irt')), ('IDS / IPS', ('exp', 'irt')), ('Pare-feu', ('exp', 'net7-infra'))]),
        ('Langages', [('Python', None), ('Java', None), ('C', None), ('Matlab', None), ('PHP', ('exp', 'prefecture'))]),
        ('Langues', [('Français · natif', None), ('Anglais · B2/C1', ('bg', 'certifications'))]),
        ('Transversales', [("Gestion de l'urgence", ('eng', 'protection-civile')), ("Encadrement d'équipes", ('eng', 'protection-civile')), ('Communication en situation critique', ('eng', 'protection-civile')), ('Gestion associative et budget', ('eng', 'grinp')), ('Méthodes agiles (Scrum)', None)]),
    ],
    'en': [
        ('Systems and virtualisation', [('Linux', None), ('Windows', None), ('Proxmox VE', ('exp', 'net7-infra')), ('Ceph', ('exp', 'net7-infra')), ('Live migration', ('exp', 'net7-infra'))]),
        ('Networking', [('TCP/IP', None), ('Routing, switching', ('exp', 'interconnexion')), ('VPN', ('exp', 'interconnexion')), ('4G / LTE', ('exp', 'reseaux-mobiles')), ('5G', None), ('Wireshark', None)]),
        ('DevOps and web', [('Git', None), ('CI/CD', None), ('Bash', None), ('LAMP stack', ('exp', 'prefecture')), ('Web platform', ('exp', 'grinp-web')), ('Figma', None)]),
        ('Cybersecurity and AI', [('Specialised LLMs', ('exp', 'irt')), ('IDS / IPS', ('exp', 'irt')), ('Firewall', ('exp', 'net7-infra'))]),
        ('Programming', [('Python', None), ('Java', None), ('C', None), ('Matlab', None), ('PHP', ('exp', 'prefecture'))]),
        ('Languages', [('French · native', None), ('English · B2/C1', ('bg', 'certifications'))]),
        ('Soft skills', [('Emergency management', ('eng', 'protection-civile')), ('Team leadership', ('eng', 'protection-civile')), ('Communication under pressure', ('eng', 'protection-civile')), ('Running an association and budget', ('eng', 'grinp')), ('Agile methods (Scrum)', None)]),
    ],
}
CERT_GROUPS = [({'fr': 'Secourisme', 'en': 'First aid'}, ['pc']),
               ({'fr': 'Langues', 'en': 'Languages'}, ['cam']),
               ({'fr': 'Gestion de projet', 'en': 'Project management'}, ['gdp']),
               ({'fr': 'Encadrement sportif', 'en': 'Sports instruction'}, ['ffme'])]

# Bannières (assets/banners/) : clé -> (fichier, crédit). Images libres de droits (Wikimedia Commons).
C = 'https://commons.wikimedia.org/wiki/File:'
BANNERS = {
    'airbus':     ('airbus.jpg', 'ESA', 'CC BY-SA 3.0 IGO', C + 'ESA_and_Airbus_engineers_test_Smile_spacecraft_boom_ESA506838.png'),
    'prefecture': ('prefecture.jpg', 'Chatsam', 'CC BY-SA 3.0', C + 'Pr%C3%A9fecture_de_Haute-Garonne_(Toulouse)_106.jpg'),
    'irt':        ('irt.jpg', 'Frédéric Neupont', 'CC BY-SA 4.0', C + 'Toulouse_-_Immeuble_B612.jpg'),
    'net7-infra': ('net7.jpg', 'NOIRLab/NSF/AURA/T. Slovinský', 'CC BY 4.0', C + 'NOIRLab_HQ_Server_Racks_(6V6A0402-CC).jpg'),
    'interco':    ('interconnexion.jpg', 'Inisheer', 'CC BY-SA 3.0', C + 'CERN-20060225-01.jpg'),
    'pc':         ('protection-civile.jpg', 'Auriane T-D, APC21', 'CC BY 4.0', C + 'VPSP_Protection_Civile_21.jpg'),
    'grinp':      ('grinp.jpg', 'Ka23 13', 'CC BY-SA 4.0', C + 'ClimbingHolds_20211103_145113.jpg'),
    'net7':       ('net7-asso.jpg', 'NOIRLab/NSF/AURA/T. Slovinský', 'CC BY 4.0', C + 'NOIRLab_HQ_Server_Racks_(6V6A0395-CC).jpg'),
    'women7':     ('women7.jpg', 'Romainbehar', 'CC0', C + 'Lyon_7e_-_Universit%C3%A9_Lyon_2_-_Palais_Hirsch_-_Grand_amphith%C3%A9%C3%A2tre_01.jpg'),
    'ceve':       ('ceve.jpg', 'Breather', 'CC0', C + 'Minimalist_meeting_room_(Unsplash).jpg'),
    'eedf':       ('eedf.jpg', 'US Forest Service', {'fr': 'domaine public', 'en': 'public domain'}, C + 'Meadow_Creek_Campfire_(9194201298).jpg'),
    'wifi':       ('wifi.jpg', 'Solijon Solayev', 'CC BY-SA 4.0', C + 'Wi-fi_router.jpg'),
    'mobile':     ('reseaux-mobiles.jpg', 'Wikideas1', 'CC0', C + 'Lattice_cell_tower-2.jpg'),
    'grinp-web':  ('grinp-web.jpg', 'Vatealyo', 'CC0', C + 'Gorliz_sports_center_climbing_gym.jpg'),
}

# ---------------------------------------------------------------- Textes UI
PAGES = ['home', 'exp', 'eng', 'bg', 'cv', 'contact']
FILE = {'fr': {'home': 'index.html', 'exp': 'experiences.html', 'eng': 'engagements.html', 'bg': 'parcours.html', 'cv': 'cv.html', 'contact': 'contact.html'},
        'en': {'home': 'index.html', 'exp': 'experience.html', 'eng': 'commitments.html', 'bg': 'background.html', 'cv': 'cv.html', 'contact': 'contact.html'}}
NAV = {'fr': {'home': 'Accueil', 'exp': 'Expériences', 'eng': 'Engagements', 'bg': 'Parcours', 'cv': 'CV', 'contact': 'Contact'},
       'en': {'home': 'Home', 'exp': 'Experience', 'eng': 'Commitments', 'bg': 'Background', 'cv': 'CV', 'contact': 'Contact'}}
T = {
    'fr': dict(navlabel='Navigation principale', theme='Changer de thème', menu='Ouvrir le menu', other='en', otherlabel='English version', otherkey='EN',
               desc={'home': "E-portfolio d'Arthur Sauvezie, élève ingénieur à l'ENSEEIHT en informatique et télécommunications : expériences, engagements et parcours.",
                     'exp': 'Stages, projet de fin d\'études et projets.',
                     'eng': 'Secourisme, vie associative et représentation étudiante.',
                     'bg': "De la classe préparatoire à l'ENSEEIHT, avec un semestre d'échange à l'Université Laval.",
                     'cv': 'Mon CV complet et à jour, en PDF.',
                     'contact': 'Une offre, un projet, une question : écrivez-moi.'}),
    'en': dict(navlabel='Main navigation', theme='Switch theme', menu='Open menu', other='fr', otherlabel='Version française', otherkey='FR',
               desc={'home': 'E-portfolio of Arthur Sauvezie, engineering student at ENSEEIHT in computer science and telecommunications: experience, commitments and background.',
                     'exp': 'Internships, final-year project and projects.',
                     'eng': 'First aid, student associations and student representation.',
                     'bg': 'From preparatory classes to ENSEEIHT, with an exchange semester at Université Laval.',
                     'cv': 'My complete, up-to-date CV as a PDF.',
                     'contact': 'A job offer, a project, a question: get in touch.'}),
}

ICONS = ('<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
         '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z"/></svg>')
MENU = ('<svg class="i-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
        '<svg class="i-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>')

MENU_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'

LINKEDIN = 'https://www.linkedin.com/in/arthur-s-911855264/'
GITHUB = 'https://github.com/arthursvz'
# adresse stockée à l'envers, reconstituée en JS au clic (anti-robots)
MAIL_REV = 'em.mp@ruhtra.eizevuas'


def url(lang, key):
    return f"{SITE}/{'en/' if lang == 'en' else ''}{FILE[lang][key]}"


def page(lang, key, title, body):
    t = T[lang]
    p = '../' if lang == 'en' else ''
    other = t['other']
    op = '../' if lang == 'en' else 'en/'
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{FILE[lang][k]}"{cur if k == key else ""}>{NAV[lang][k]}</a>' for k in PAGES)
    nav += f'<a class="lang" href="{op}{FILE[other][key]}" lang="{other}" aria-label="{t["otherlabel"]}">{t["otherkey"]}</a>'
    full = 'Arthur Sauvezie · E-portfolio' if key == 'home' else f'{title} · Arthur Sauvezie'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(t['desc'][key])}">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{p}assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<meta name="theme-color" content="#1F5F5B">
<link rel="alternate" hreflang="fr" href="{url('fr', key)}">
<link rel="alternate" hreflang="en" href="{url('en', key)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="{p}css/style.css">
<script src="{p}js/theme.js"></script>
</head>
<body>
<div class="ambient" aria-hidden="true"><div class="layer"><i class="b b1"></i><i class="b b2"></i><i class="b b3"></i></div><i class="cursor"></i></div>
<header class="site-header">
<div class="wrap">
<a class="brand" href="index.html">Arthur Sauvezie</a>
<nav class="nav" id="site-nav" aria-label="{t['navlabel']}">{nav}</nav><div class="tools"><button id="theme-toggle" class="icon-btn" type="button" aria-label="{t['theme']}">{ICONS}</button><button class="icon-btn menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="{t['menu']}">{MENU}</button></div>
</div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<span>© {YEAR} Arthur Sauvezie</span>
<span><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a> · <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a> · <a href="contact.html">Contact</a></span>
</div>
</footer>
</body>
</html>
'''


def head(title, sub):
    return f'<section class="wrap page-head"><div class="bar"></div><h1 class="page">{title}</h1><p>{sub}</p></section>'


def stats(items):
    if not items:
        return ''
    return '<ul class="stats">' + ''.join(f'<li><b>{e(a)}</b>{e(b)}</li>' for a, b in items) + '</ul>'


def tags(items):
    if not items:
        return ''
    return '<ul class="tags">' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul>'


def rows(items):
    if not items:
        return ''
    return '<ul class="rows">' + ''.join(f'<li><span>{e(a)}</span><span>{b}</span></li>' for a, b in items) + '</ul>'


def entry(lang, p, d, orglabel=None):
    """Bloc détaillé : logo + dates à gauche, contenu à droite."""
    badge = f'<span class="badge">{d["badge"][lang]}</span>' if 'badge' in d else ''
    links = ''.join(f' · <a class="ext" href="{u}" target="_blank" rel="noopener">{e(l)}</a>' for l, u in d.get('links', []))
    where = f' · {d["where"]}' if 'where' in d else ''
    idattr = f' id="{d["id"]}"' if 'id' in d else ''
    ban = ''
    if 'banner' in d and d['banner'][0] in BANNERS:
        f, who, lic, src = BANNERS[d['banner'][0]]
        lic = lic[lang] if isinstance(lic, dict) else lic
        ban = (f'<figure class="banner"><img src="{p}assets/banners/{f}" alt="" loading="lazy">'
               f'<figcaption><a href="{src}" target="_blank" rel="noopener">{"Photo :" if lang == "fr" else "Photo:"} {e(who)} · {lic}</a></figcaption></figure>')
    return (f'<article class="eng{" has-banner" if ban else ""}"{idattr}>{ban}<div class="side">{logo(d["ent"], p)}<div class="when">{d["when"][lang]}{where}</div></div>'
            f'<div class="body"><h3>{e(d["role"][lang])}{badge}</h3><div class="org">{org(d["ent"], orglabel)}{links}</div>'
            f'<p>{e(d["text"][lang])}</p>{stats(d.get("stats", {}).get(lang))}{tags(d.get("tags", {}).get(lang))}{rows(d.get("rows", {}).get(lang))}</div></article>')


# ---------------------------------------------------------------- Pages
def home(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    lead = ("Élève ingénieur en dernière année à l'ENSEEIHT, en informatique et télécommunications, actuellement en échange à l'Université Laval. Passionné par l'aéronautique, le spatial et la cybersécurité, je m'investis aussi comme secouriste et responsable associatif."
            if fr else
            "Final-year engineering student at ENSEEIHT in computer science and telecommunications, currently on exchange at Université Laval. Passionate about aeronautics, space and cybersecurity, and committed as a first-aider and student association leader.")
    strip = [
        ('Formation' if fr else 'Education', logo('n7', p, 'sm'), 'ENSEEIHT, Informatique et Télécom.' if fr else 'ENSEEIHT, CS and Telecom'),
        ('En ce moment' if fr else 'Currently', logo('laval', p, 'sm'), 'Échange, Université Laval' if fr else 'Exchange, Université Laval'),
        ('Recherche' if fr else 'Looking for', '', 'Premier emploi, dès septembre 2027' if fr else 'First job, from September 2027'),
    ]
    strip_html = ''.join(f'<div><span class="k">{k}</span><span class="v">{v}</span></div>' for k, _, v in strip)
    eng_file = FILE[lang]['eng']
    cards = ''.join(
        f'<a class="card" href="{eng_file}#{d["id"]}"><div class="card-top">{logo(d["ent"], p).replace("<a ", "<span ").replace("</a>", "</span>") if ENT[d["ent"]][1] else logo(d["ent"], p)}'
        f'<div><h3>{e(d["role"][lang])}</h3><div class="sub">{e(d["orgname"][lang])}</div></div></div>'
        f'<div class="fig"><b>{e(d["card"][lang][0])}</b>{e(d["card"][lang][1])}</div></a>'
        for d in ENG[:3])
    exp_file = FILE[lang]['exp']
    items = EXP + PROJ[:2]
    lst = ''.join(
        f'<a class="withlogo" href="{exp_file}#{d["id"]}">{logo(d["ent"], p, "sm").replace("<a ", "<span ").replace("</a>", "</span>") if ENT[d["ent"]][1] else logo(d["ent"], p, "sm")}'
        f'<span class="t">{e(d["role"][lang])}</span><span class="m">{e(ENT[d["ent"]][0])} · {d["when"][lang].split(" · ")[0]}</span><span class="go" aria-hidden="true">→</span></a>'
        for d in items)
    body = f'''<section class="wrap hero">
<div class="hero-text">
<div class="bar"></div>
<h1>Arthur<br>Sauvezie</h1>
<p class="lead">{lead}</p>
<div class="actions"><a class="btn primary" href="cv.html">{'Voir le CV' if fr else 'View CV'}</a><a class="btn" href="contact.html">{'Me contacter' if fr else 'Contact me'}</a></div>
</div>
<div class="photo"><img src="{p}assets/photo.jpg" alt="{'Portrait d’Arthur Sauvezie' if fr else 'Portrait of Arthur Sauvezie'}"></div>
</section>
<div class="wrap"><section class="strip">{strip_html}</section></div>
<section class="wrap section">
<div class="shead"><h2>{'Expériences et projets' if fr else 'Experience and projects'}</h2><a href="{exp_file}">{'Détails →' if fr else 'Details →'}</a></div>
<div class="list">{lst}</div>
</section>
<section class="wrap section tight">
<div class="shead"><h2>{'Engagements' if fr else 'Commitments'}</h2><a href="{eng_file}">{'Tout voir →' if fr else 'See all →'}</a></div>
<div class="cards">{cards}</div>
</section>'''
    return page(lang, 'home', NAV[lang]['home'], body)


def experiences(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    body = head('Expériences' if fr else 'Experience', T[lang]['desc']['exp'])
    body += f'<section class="wrap block-sm"><h2>{"Expériences professionnelles" if fr else "Professional experience"}</h2>' + ''.join(entry(lang, p, d) for d in EXP) + '</section>'
    body += f'<section class="wrap block"><h2>{"Projets" if fr else "Projects"}</h2>' + ''.join(entry(lang, p, d) for d in PROJ) + '</section>'
    return page(lang, 'exp', NAV[lang]['exp'], body)


def engagements(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    sub = ("Secourisme, vie associative et représentation étudiante : ce que je fais en dehors des cours, et ce que ça m'apprend sur l'encadrement, l'urgence et le travail en équipe."
           if fr else
           "First aid, student associations and student representation: what I do outside class, and what it teaches me about leadership, emergencies and teamwork.")
    body = head('Engagements' if fr else 'Commitments', sub)
    body += '<section class="wrap block">' + ''.join(entry(lang, p, d, d['orgname'][lang]) for d in ENG) + '</section>'
    return page(lang, 'eng', NAV[lang]['eng'], body)


def timeline(lang, p):
    fr = lang == 'fr'

    def flag(d):
        if d.get('now'):
            return f'<span class="flag">{"En cours" if fr else "Now"}</span>'
        if d.get('future'):
            return f'<span class="flag">{"À venir" if fr else "Upcoming"}</span>'
        return ''

    def state(d):
        return ' future' if d.get('future') else (' now' if d.get('now') else '')

    def ues(d):
        items = d.get('ue') or []
        if not items:
            return ''
        label = "Unités d'enseignement" if fr else 'Courses taken'
        inner = ''
        for sem, group in by_sem(items):
            chips = ''.join(f'<li><a href="#ue-{u["id"]}" data-ue="{u["id"]}">{e(u["name"][lang])}</a></li>' for u in group)
            inner += (f'<div class="ue-sem">{sem_label(lang, sem)}</div>' if sem else '') + f'<ul>{chips}</ul>'
        return f'<details class="ue"><summary>{label} <span>{len(items)}</span></summary>{inner}</details>'

    def where(d):
        return f' · {d["where"]}' if d.get('where') else ''

    out = []
    for d in EDU:
        badge = f'<span class="badge">{d["badge"][lang]}</span>' if 'badge' in d else ''
        text = f'<p>{e(d["text"][lang])}</p>' if d.get('text') else ''
        cls = state(d).strip()
        out.append(f'<li{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}><span class="dot" aria-hidden="true"></span>'
                   f'<div class="when">{d["when"][lang]}{flag(d)}</div>'
                   f'<div class="what"><div class="head">{logo(d["ent"], p, "sm")}<div><h3>{e(d["role"][lang])}{badge}</h3>'
                   f'<div class="org">{org(d["ent"])}{where(d)}</div></div></div>{text}{ues(d)}</div></li>')
    return '<ol class="tl">' + ''.join(out) + '</ol>'


def ue_index(lang):
    """Libellé de compétence -> UE où elle a été vue en premier, chronologiquement (id, nom)."""
    idx = {}
    for d in reversed(EDU):
        for u in d.get('ue') or []:
            for k in u['skills'][lang]:
                idx.setdefault(k, (u['id'], u['name'][lang]))
    return idx


def skill_proof(lang):
    """Libellé de compétence -> (page, ancre) de sa preuve sur la page Parcours."""
    return {label: ref for _, items in SKILLS[lang] for label, ref in items if ref}


def skills(lang):
    fr = lang == 'fr'
    taught = ue_index(lang)
    cols = []
    for cat, items in SKILLS[lang]:
        chips = []
        for label, ref in items:
            if ref:
                pg, anchor = ref
                tip = ('Voir où : ' if fr else 'See where: ') + NAV[lang][pg]
                chips.append(f'<a class="chip proof" href="{FILE[lang][pg]}#{anchor}" title="{e(tip)}">{e(label)}</a>')
            elif label in taught:
                uid, uname = taught[label]
                tip = ('Vu en cours : ' if fr else 'Studied in: ') + uname
                chips.append(f'<a class="chip proof" href="#ue-{uid}" data-ue="{uid}" title="{e(tip)}">{e(label)}</a>')
            else:
                chips.append(f'<span class="chip">{e(label)}</span>')
        cols.append(f'<div><h3>{e(cat)}</h3><div class="chips">{"".join(chips)}</div></div>')
    note = ("Les compétences marquées d'un point renvoient à l'expérience, à l'engagement ou au cours où je les ai mises en œuvre." if fr
            else 'Skills marked with a dot link to the experience, commitment or course where I put them into practice.')
    return f'<p class="legend"><span class="dotmark" aria-hidden="true"></span>{e(note)}</p><div class="cols skills">{"".join(cols)}</div>'


def parcours(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    body = head('Parcours' if fr else 'Background', T[lang]['desc']['bg'])
    body += f'<section class="wrap block-sm"><h2>{"Formation" if fr else "Education"}</h2>{timeline(lang, p)}</section>'
    body += ue_dialogs(lang, p)
    groups = ''
    for gname, keys in CERT_GROUPS:
        lis = ''.join(f'<li>{logo(k, p)}<div class="t">{e(name[lang])}<span>{org(k, CERT_ORG[k][lang])}</span></div><div class="d">{d[lang]}</div></li>'
                      for k, name, d in CERTS if k in keys)
        groups += f'<div class="cgroup"><h3>{gname[lang]}</h3><ul class="certs">{lis}</ul></div>'
    body += f'<section class="wrap block-sm" id="certifications"><h2>Certifications</h2>{groups}</section>'
    body += f'<section class="wrap block"><h2>{"Compétences" if fr else "Skills"}</h2>{skills(lang)}</section>'
    return page(lang, 'bg', NAV[lang]['bg'], body)


def ue_dialogs(lang, p):
    """Fiches des UE (templates) + la fenêtre qui les affiche, pour la page Parcours."""
    fr = lang == 'fr'
    proofs = skill_proof(lang)
    roles = {d['id']: d['role'][lang] for d in EXP + PROJ + ENG}
    tpls = ''
    for d in EDU:
        for u in d.get('ue') or []:
            chips = ''
            for k in u['skills'][lang]:
                if k in proofs:
                    pg, anchor = proofs[k]
                    tip = ('Mise en pratique : ' if fr else 'Put into practice: ') + NAV[lang][pg]
                    chips += f'<a class="chip proof" href="{FILE[lang][pg]}#{anchor}" title="{e(tip)}">{e(k)}</a>'
                else:
                    chips += f'<span class="chip">{e(k)}</span>'
            proj = ''
            if u.get('proj'):
                pg, anchor = u['proj']
                proj = (f'<a class="ue-proj" href="{FILE[lang][pg]}#{anchor}">'
                        f'{"Projet lié :" if fr else "Related project:"} {e(roles.get(anchor, NAV[lang][pg]))} <span aria-hidden="true">→</span></a>')
            ctx = ' · '.join(x for x in (sem_label(lang, u['sem']) if u.get('sem') else '', d['when'][lang]) if x)
            tpls += (f'<template id="tpl-ue-{u["id"]}"><div class="ue-ctx">{logo(d["ent"], p, "sm")}<div>'
                     f'<div class="ue-when">{ctx}</div><div class="org">{e(d["role"][lang])}</div></div></div>'
                     f'<h3 id="ue-dialog-title">{e(u["name"][lang])}</h3><p>{e(u["desc"][lang])}</p>'
                     f'<div class="ue-skills"><span>{"Compétences" if fr else "Skills"}</span><div class="chips">{chips}</div></div>{proj}</template>')
    close = 'Fermer' if fr else 'Close'
    return (tpls + f'<dialog class="ue-dialog" aria-labelledby="ue-dialog-title"><div class="ue-card" tabindex="-1" autofocus>'
            f'<button class="ue-close icon-btn" type="button" aria-label="{close}">{MENU_CLOSE}</button><div class="ue-body"></div></div></dialog>'
            f'<script src="{p}js/ue.js" defer></script>')


CV_UPDATED = {'fr': 'novembre 2026', 'en': 'November 2026'}


def cv(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    pdf = f'{p}assets/CV_Arthur_SAUVEZIE.pdf'
    sub = (f'Mon CV complet, en français et en anglais dans un seul PDF. Mis à jour en {CV_UPDATED[lang]}.' if fr
           else f'My complete CV, in French and English in a single PDF. Updated {CV_UPDATED[lang]}.')
    body = head('CV', sub)
    actions = (f'<div class="actions"><a class="btn primary" href="{pdf}" download>{"Télécharger le CV (PDF)" if fr else "Download CV (PDF)"}</a>'
               f'<a class="btn" href="{FILE[lang]["bg"]}">{"Voir le parcours" if fr else "See background"}</a></div>')
    body = body.replace('</p></section>', f'</p>{actions}</section>')
    kpis = [(str(len(EXP)), 'stages, dont le PFE' if fr else 'internships, incl. final-year project'),
            (str(len(PROJ)), 'projets' if fr else 'projects'),
            ('600 h+', 'de secours par an' if fr else 'of first aid per year'),
            ('2', 'langues · FR, EN' if fr else 'languages · FR, EN')]
    body += '<section class="wrap block-sm"><ul class="kpis">' + ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in kpis) + '</ul></section>'
    pages = [('fr', 1, 'Version française', 'French version'), ('en', 2, 'Version anglaise', 'English version')]
    if not fr:
        pages.reverse()
    open_lbl = 'Ouvrir' if fr else 'Open'
    prev = ''.join(
        f'<a class="cvprev" href="{pdf}#page={n}" target="_blank" rel="noopener">'
        f'<span class="sheet"><img src="{p}assets/cv-preview-{code}.jpg" alt="{e(lf if fr else le)} du CV" loading="lazy" width="760" height="1075"><span class="open">{open_lbl} ↗</span></span>'
        f'<span class="cap">{lf if fr else le}<span>Page {n}</span></span></a>'
        for code, n, lf, le in pages)
    body += f'<section class="wrap block"><h2>{"Aperçu" if fr else "Preview"}</h2><div class="cvgrid">{prev}</div></section>'
    return page(lang, 'cv', 'CV', body)


# Où je suis en ce moment (fuseau IANA pour l'heure locale affichée sur la page Contact)
NOW_PLACE = {'fr': 'Québec', 'en': 'Quebec City', 'tz': 'America/Toronto',
             'note': {'fr': "en échange jusqu'en décembre 2026, puis Toulouse", 'en': 'on exchange until December 2026, then Toulouse'}}

SEEK = {
    'fr': [('Postes', 'Ingénieur systèmes, réseaux et télécoms', ''),
           ('Secteurs', 'Défense, aéronautique, spatial', ''),
           ('Lieu', 'Toulouse ou Paris', ''),
           ('À terme', 'Évoluer vers la cybersécurité', 'Pas forcément dès le premier poste')],
    'en': [('Roles', 'Systems, network and telecoms engineer', ''),
           ('Sectors', 'Defence, aeronautics, space', ''),
           ('Location', 'Toulouse or Paris', ''),
           ('Longer term', 'Move into cybersecurity', 'Not necessarily in my first role')],
}
PRACTICAL = {
    'fr': [('Langues', 'Français, anglais'), ('Permis', 'Permis B'), ('Nationalité', 'Française uniquement')],
    'en': [('Languages', 'French, English'), ('Driving licence', 'Full licence (B)'), ('Nationality', 'French only')],
}

IC_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/></svg>'
IC_IN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V16M8 7.6v.1M12 16v-5.5M12 13c0-1.6 1-2.6 2.3-2.6S16.5 11.2 16.5 13v3"/></svg>'
IC_GH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 9l-4 3 4 3M16 9l4 3-4 3M13.5 6l-3 12"/></svg>'


def contact(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    sub = ("Je cherche un premier emploi à partir de septembre 2027, après mon projet de fin d'études (diplôme d'ingénieur en octobre 2027). Une offre, une question, un échange : écrivez-moi."
           if fr else
           "I'm looking for my first job from September 2027, after my final-year project (engineering degree awarded in October 2027). An offer, a question, a chat: get in touch.")
    body = (f'<section class="wrap page-head contact-head"><div class="bar"></div><h1 class="page">{"Discutons" if fr else "Let’s talk"}</h1>'
            f'<p>{sub}</p><div class="avail"><span class="live" aria-hidden="true"></span>{"Disponible à partir de septembre 2027 · diplômé en octobre 2027" if fr else "Available from September 2027 · graduating October 2027"}</div></section>')
    mail = (f'<div class="ccard"><span class="ic">{IC_MAIL}</span><span class="cc-t"><span class="k">E-mail</span>'
            f'<span class="v"><button type="button" class="mail-btn js-mail" data-m="{MAIL_REV}" data-copy="{"Copier" if fr else "Copy"}" data-copied="{"Copié" if fr else "Copied"}">{"Afficher l’adresse" if fr else "Show address"}</button></span></span></div>')
    li = (f'<a class="ccard" href="{LINKEDIN}" target="_blank" rel="noopener"><span class="ic">{IC_IN}</span><span class="cc-t"><span class="k">LinkedIn</span><span class="v">Arthur Sauvezie</span></span><span class="go" aria-hidden="true">↗</span></a>')
    gh = (f'<a class="ccard" href="{GITHUB}" target="_blank" rel="noopener"><span class="ic">{IC_GH}</span><span class="cc-t"><span class="k">GitHub</span><span class="v">arthursvz</span></span><span class="go" aria-hidden="true">↗</span></a>')
    body += f'<section class="wrap block-sm"><div class="ccards">{mail}{li}{gh}</div></section>'
    seek = SEEK[lang]
    body += (f'<section class="wrap block-sm"><h2>{"Ce que je recherche" if fr else "What I’m looking for"}</h2><ul class="seek">'
             + ''.join(f'<li><span class="k">{e(k)}</span><span class="v">{e(v)}</span>{f"<span class=n>{e(n)}</span>" if n else ""}</li>' for k, v, n in seek)
             + '</ul></section>')
    place = NOW_PLACE[lang]
    body += (f'<section class="wrap block"><div class="cfoot">'
             f'<div><span class="k">{"En ce moment" if fr else "Right now"}</span><span class="v">{place} · {NOW_PLACE["note"][lang]}'
             f'<span class="clock js-clock" data-tz="{NOW_PLACE["tz"]}" data-lang="{lang}" hidden></span></span></div>'
             + ''.join(f'<div><span class="k">{e(k)}</span><span class="v">{e(v)}</span></div>' for k, v in PRACTICAL[lang]) +
             f'<div><span class="k">CV</span><span class="v"><a class="ext-int" href="{FILE[lang]["cv"]}">{"Voir et télécharger mon CV" if fr else "View and download my CV"} →</a></span></div>'
             f'</div></section>')
    return page(lang, 'contact', 'Contact', body)


def redirect(target):
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}"><title>→</title></head><body><a href="{target}">{target}</a></body></html>\n'


def write(rel, s):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    print('écrit', rel)


if __name__ == '__main__':
    gens = {'home': home, 'exp': experiences, 'eng': engagements, 'bg': parcours, 'cv': cv, 'contact': contact}
    for lang in ('fr', 'en'):
        for k, g in gens.items():
            write(('en/' if lang == 'en' else '') + FILE[lang][k], g(lang))
    # anciennes URL
    write('projets.html', redirect('experiences.html'))
    write('en/projects.html', redirect('experience.html'))
