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


def logo(k, p, size='', link=True):
    name, url, img, style = ENT[k]
    cls = 'logo' + (' sm' if size == 'sm' else '')
    if img:
        if style == 'bleed':
            cls += ' bleed'
        inner = f'<img src="{p}assets/logos/{img}" alt="{e(name)}" loading="lazy">'
    else:
        cls += ' mono'
        inner = f'<span aria-hidden="true">{style}</span><span class="sr">{e(name)}</span>'
    if url and link:
        return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener" title="{e(name)}"{pop_attr(k)}>{inner}</a>'
    return f'<span class="{cls}" title="{e(name)}">{inner}</span>'


def org(k, label=None):
    name, url, _, _ = ENT[k]
    label = e(label or name)
    if url:
        return f'<a class="ext" href="{url}" target="_blank" rel="noopener"{pop_attr(k)}>{label}</a>'
    return label


def pop_attr(k):
    return f' data-pop="ent-{k}"' if k in ENT_INFO else ''


# Présentation des organisations (fiche ouverte depuis leurs liens, sur toutes les pages).
ENT_INFO = {
    'n7': {'fr': "École nationale supérieure d'électrotechnique, d'électronique, d'informatique, d'hydraulique et des télécommunications : une grande école d'ingénieurs publique de Toulouse, membre de Toulouse INP, dont les origines remontent à 1907. J'y suis le cursus du département Sciences du Numérique.",
           'en': "ENSEEIHT, a public engineering grande école in Toulouse, part of Toulouse INP, with roots going back to 1907. It covers electrical engineering, electronics, computer science, hydraulics and telecommunications. I study in its Digital Sciences department."},
    'laval': {'fr': "Université francophone de Québec, la plus ancienne université de langue française en Amérique du Nord, héritière du Séminaire de Québec fondé en 1663. J'y passe mon semestre d'échange.",
              'en': 'French-language university in Quebec City, the oldest French-speaking university in North America, descended from the Séminaire de Québec founded in 1663. I am spending my exchange semester there.'},
    'airbus': {'fr': "Division d'Airbus consacrée à la défense et au spatial : satellites, systèmes spatiaux, avions militaires et solutions de sécurité. C'est là que je réalise mon projet de fin d'études.",
               'en': "Airbus's defence and space division: satellites, space systems, military aircraft and security solutions. This is where I am doing my final-year project."},
    'pref': {'fr': "Représentation de l'État en Haute-Garonne, également préfecture de la région Occitanie. Son secrétariat général commun départemental (SGCD) gère les moyens mutualisés des services de l'État, dont le numérique.",
             'en': "The State's representation in Haute-Garonne, which is also the prefecture of the Occitanie region. Its joint departmental general secretariat (SGCD) manages the shared resources of State services, including IT."},
    'irt': {'fr': "Institut de recherche technologique installé à Toulouse, qui réunit industriels et laboratoires publics autour de l'aéronautique, du spatial et des systèmes embarqués.",
            'en': 'Technological research institute based in Toulouse, bringing together industry and public laboratories around aeronautics, space and embedded systems.'},
    'pc': {'fr': "Fédération d'associations de bénévoles, agréée de sécurité civile et reconnue d'utilité publique. Elle assure des missions de secours, de formation aux premiers secours et de soutien aux populations.",
           'en': 'Federation of volunteer associations, approved for civil security and recognised as being of public interest. It provides first-aid cover, first-aid training and support to the population.'},
    'grinp': {'fr': "Club d'escalade de l'association sportive de Toulouse INP, ouvert aux étudiants des écoles de l'institut. J'en suis le président.",
              'en': "Climbing club of the Toulouse INP sports association, open to students of the institute's schools. I am its president."},
    'net7': {'fr': "Association informatique de l'ENSEEIHT : elle héberge et administre des services pour les étudiants (Git, messagerie, sites web) sur sa propre infrastructure.",
             'en': "ENSEEIHT's IT association: it hosts and runs services for students (Git, email, websites) on its own infrastructure."},
    'eedf': {'fr': "Mouvement de scoutisme laïque fondé en 1911 et reconnu d'utilité publique, qui propose des activités éducatives et de plein air aux enfants et aux jeunes.",
             'en': 'Secular scouting movement founded in 1911 and recognised as being of public interest, offering educational and outdoor activities to children and young people.'},
    'ffme': {'fr': "Fédération française de la montagne et de l'escalade : elle organise la pratique de l'escalade et des sports de montagne en France, et forme les encadrants bénévoles.",
             'en': 'French mountaineering and climbing federation: it organises climbing and mountain sports in France, and trains volunteer instructors.'},
    'cam': {'fr': "Département de l'Université de Cambridge qui conçoit les examens d'anglais Cambridge English, dont le test Linguaskill.",
            'en': 'Department of the University of Cambridge that designs the Cambridge English exams, including the Linguaskill test.'},
}


def ent_templates(lang, p):
    """Fiches de présentation des organisations, avec ce que j'y ai fait et le lien vers leur site."""
    fr = lang == 'fr'
    out = ''
    for k, desc in ENT_INFO.items():
        name, url, _, _ = ENT[k]
        mine = [(d['role'][lang], d['when'][lang]) for d in EDU + EXP + PROJ + ENG if d.get('ent') == k]
        mine += [(n[lang], dt[lang]) for kk, n, dt, *_ in CERTS if kk == k]
        lst = ''.join(f'<li>{e(r)} <span>· {w}</span></li>' for r, w in mine)
        did = "Ce que j'y ai fait" if fr else 'What I did there'
        lst = (f'<div class="ue-skills"><span>{did}</span>'
               f'<ul class="pop-list">{lst}</ul></div>') if mine else ''
        host = url.split('//', 1)[-1].rstrip('/')
        out += (f'<template id="tpl-ent-{k}"><div class="ue-ctx">{logo(k, p, "sm", link=False)}<div>'
                f'<div class="ue-when">{e(host.removeprefix("www."))}</div></div></div><h3 id="ue-dialog-title">{e(name)}</h3><p>{e(desc[lang])}</p>{lst}'
                f'<a class="site-link" href="{url}" target="_blank" rel="noopener">{"Visiter le site" if fr else "Visit the website"} · {e(host)} '
                f'<span aria-hidden="true">↗</span></a></template>')
    return out


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
    if isinstance(n, str):
        return n
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
         text={'fr': "Deux années intensives de mathématiques, physique-chimie et sciences de l'ingénieur, rythmées par les colles et les devoirs surveillés, pour préparer les concours des grandes écoles d'ingénieurs : PCSI puis PSI.",
               'en': 'Two intensive years of mathematics, physics, chemistry and engineering sciences, paced by weekly oral examinations (colles) and timed written exams, preparing for the competitive entrance exams to the French engineering grandes écoles: PCSI, then PSI.'},
         # Matières d'après les programmes officiels (BO spécial n° 1 du 11 février 2021 ; thèmes de français-philosophie et de TIPE au BO).
         ue=[
             U('maths-pcsi', 'Mathématiques', 'Mathematics',
               "Construction rigoureuse de l'analyse et de l'algèbre, fondée sur la démonstration : nombres réels et complexes, suites, continuité, dérivabilité et développements limités, intégration, séries numériques, équations différentielles, polynômes, espaces vectoriels, applications linéaires, matrices et déterminants, probabilités.",
               'A rigorous, proof-based construction of analysis and algebra: real and complex numbers, sequences, continuity, differentiability and Taylor expansions, integration, numerical series, differential equations, polynomials, vector spaces, linear maps, matrices and determinants, probability.',
               ['Analyse', 'Algèbre linéaire', 'Probabilités'],
               ['Analysis', 'Linear algebra', 'Probability'], sem='PCSI · 2022 – 2023'),
             U('physique-chimie-pcsi', 'Physique-chimie', 'Physics and chemistry',
               "Modélisation des phénomènes physiques et résolution de problèmes, en cours comme en travaux pratiques : mécanique du point et du solide, électrocinétique et filtrage, signaux et ondes, optique, thermodynamique, induction. En chimie : architecture de la matière, cinétique, équilibres en solution (acide-base, précipitation, oxydoréduction).",
               'Modelling physical phenomena and solving problems, in lectures and in lab work: mechanics of particles and rigid bodies, circuits and filtering, signals and waves, optics, thermodynamics, induction. Chemistry: structure of matter, kinetics, equilibria in solution (acid-base, precipitation, redox).',
               ['Mécanique', 'Électrocinétique', 'Thermodynamique', 'Chimie'],
               ['Mechanics', 'Electric circuits', 'Thermodynamics', 'Chemistry'], sem='PCSI · 2022 – 2023'),
             U('sii-pcsi', "Sciences industrielles de l'ingénieur", 'Engineering sciences',
               "Démarche d'ingénieur appliquée à des systèmes industriels réels : analyse et modélisation en SysML, modélisation et analyse des systèmes asservis, cinématique et statique des mécanismes, systèmes logiques. Option SI au second semestre, vers la PSI.",
               'Engineering approach applied to real industrial systems: analysis and SysML modelling, modelling and analysis of control systems, kinematics and statics of mechanisms, logic systems. Engineering option in the second semester, leading to PSI.',
               ['SysML', 'Asservissement', 'Cinématique', 'Modélisation des systèmes'],
               ['SysML', 'Control systems', 'Kinematics', 'Systems modelling'], sem='PCSI · 2022 – 2023'),
             U('info-pcsi', 'Informatique', 'Computer science',
               "Algorithmique et programmation en Python, avec preuves de correction et analyse de complexité : récursivité, algorithmes de tri, représentation des nombres, graphes, parcours et plus courts chemins.",
               'Algorithms and programming in Python, with correctness proofs and complexity analysis: recursion, sorting algorithms, number representation, graphs, traversals and shortest paths.',
               ['Python', 'Algorithmique', 'Graphes'],
               ['Python', 'Algorithms', 'Graphs'], sem='PCSI · 2022 – 2023'),
             U('francais-pcsi', 'Français-philosophie', 'French and philosophy',
               "Étude approfondie de trois œuvres, littéraires et philosophiques, autour du thème « Le travail », et entraînement aux épreuves des concours : dissertation et résumé de texte en temps limité.",
               'In-depth study of three literary and philosophical works on the theme “Work”, and training for the entrance exam papers: timed essay writing and text summary.',
               ['Dissertation', 'Résumé de texte', 'Argumentation'],
               ['Essay writing', 'Text summary', 'Argumentation'], sem='PCSI · 2022 – 2023'),
             U('anglais-pcsi', 'Anglais', 'English',
               "Anglais de niveau concours sur l'actualité du monde anglophone : synthèse de documents, essai argumenté, traduction et colles orales.",
               'Exam-level English based on current affairs in the English-speaking world: document synthesis, argumentative essays, translation and oral examinations.',
               ['Anglais'], ['English'], sem='PCSI · 2022 – 2023'),
             U('maths-psi', 'Mathématiques', 'Mathematics',
               "Approfondissement théorique en vue des concours : réduction des endomorphismes, espaces préhilbertiens et euclidiens, suites et séries de fonctions, séries entières, intégration sur un intervalle quelconque et intégrales à paramètre, systèmes différentiels, calcul différentiel à plusieurs variables, variables aléatoires discrètes.",
               'Advanced theory for the entrance exams: reduction of endomorphisms, inner product and Euclidean spaces, sequences and series of functions, power series, integration over arbitrary intervals and parameter-dependent integrals, systems of differential equations, multivariable calculus, discrete random variables.',
               ['Algèbre linéaire', 'Analyse', 'Probabilités'],
               ['Linear algebra', 'Analysis', 'Probability'], sem='PSI · 2023 – 2024'),
             U('physique-chimie-psi', 'Physique-chimie', 'Physics and chemistry',
               "Physique des milieux continus, avec un fort usage de l'analyse vectorielle : électromagnétisme et équations de Maxwell, ondes et propagation, électronique, mécanique des fluides, thermodynamique et machines thermiques, conversion électromécanique de puissance. En chimie : thermochimie et électrochimie.",
               'Continuum physics, making heavy use of vector calculus: electromagnetism and Maxwell’s equations, waves and propagation, electronics, fluid mechanics, thermodynamics and heat engines, electromechanical power conversion. Chemistry: thermochemistry and electrochemistry.',
               ['Électromagnétisme', 'Électronique', 'Mécanique des fluides', 'Thermodynamique'],
               ['Electromagnetism', 'Electronics', 'Fluid mechanics', 'Thermodynamics'], sem='PSI · 2023 – 2024'),
             U('sii-psi', "Sciences industrielles de l'ingénieur", 'Engineering sciences',
               "Analyse et synthèse des systèmes asservis (stabilité, précision, rapidité) et dimensionnement de correcteurs, dynamique des systèmes de solides, chaînes de puissance et d'énergie, confrontation des modèles aux mesures en TP.",
               'Analysis and design of control systems (stability, accuracy, speed) and controller tuning, dynamics of multi-body systems, power and energy chains, comparing models with lab measurements.',
               ['Asservissement', 'Correcteurs', 'Dynamique des solides'],
               ['Control systems', 'Controllers', 'Dynamics of solids'], sem='PSI · 2023 – 2024'),
             U('info-psi', 'Informatique', 'Computer science',
               "Dictionnaires et tables de hachage, programmation dynamique, bases de données relationnelles et SQL, apprentissage supervisé et non supervisé (k plus proches voisins, k-moyennes), jeux sur graphes et algorithme minimax, recherche heuristique (A*).",
               'Dictionaries and hash tables, dynamic programming, relational databases and SQL, supervised and unsupervised learning (k-nearest neighbours, k-means), graph games and the minimax algorithm, heuristic search (A*).',
               ['Python', 'SQL', 'Programmation dynamique'],
               ['Python', 'SQL', 'Dynamic programming'], sem='PSI · 2023 – 2024'),
             U('francais-psi', 'Français-philosophie', 'French and philosophy',
               "Étude approfondie de trois œuvres, littéraires et philosophiques, autour du thème « Faire croire », et épreuves des concours : dissertation et résumé de texte en temps limité.",
               'In-depth study of three literary and philosophical works on the theme “Making believe”, and the entrance exam papers: timed essay writing and text summary.',
               ['Dissertation', 'Résumé de texte', 'Argumentation'],
               ['Essay writing', 'Text summary', 'Argumentation'], sem='PSI · 2023 – 2024'),
             U('anglais-psi', 'Anglais', 'English',
               "Préparation des épreuves d'anglais des concours, à l'écrit et à l'oral : synthèse de documents, essai argumenté, traduction, commentaire d'articles de presse en colle.",
               'Preparation for the English papers of the entrance exams, written and oral: document synthesis, argumentative essays, translation, press article commentary in oral examinations.',
               ['Anglais'], ['English'], sem='PSI · 2023 – 2024'),
             U('tipe', 'TIPE', 'TIPE (supervised personal research project)',
               "Travail d'initiative personnelle encadré, sur le thème « Jeux, sports ». Mon sujet : l'étude de la transmission d'information à travers le faisceau d'un laser game. Mesures en conditions réelles dans une salle, puis réalisation d'un prototype à base de diode et de photodiode, avec lequel nous avons comparé différentes modulations. Présenté à l'oral des concours.",
               'Supervised personal research project on the theme “Games, sports”. My topic: studying how information is transmitted through a laser tag beam. Measurements in a real laser tag arena, then a prototype built with a diode and a photodiode, used to compare different modulation schemes. Presented at the oral entrance exams.',
               ["Transmission de l'information", 'Modulation du signal', 'Prototypage électronique', 'Démarche expérimentale'],
               ['Information transmission', 'Signal modulation', 'Electronic prototyping', 'Experimental method'], sem='PSI · 2023 – 2024'),
         ]),
    dict(ent='limosin', when={'fr': '2021 – 2022', 'en': '2021 – 2022'}, where='Limoges',
         role={'fr': 'Baccalauréat général, section européenne (anglais)', 'en': 'French baccalauréat, European section (English)'},
         text={'fr': 'Spécialités mathématiques et physique-chimie, option mathématiques expertes. Lycée de 2019 à 2022.',
               'en': 'Mathematics and physics-chemistry majors, advanced mathematics option. High school from 2019 to 2022.'}),
]

CERTS = [
    ('pc', {'fr': "Équipier-secouriste PSE2", 'en': 'First-aid team member (PSE2)'}, {'fr': 'Mars 2026', 'en': 'Mar 2026'}, 'pse2'),
    ('cam', {'fr': 'Linguaskill Business · 178 points', 'en': 'Linguaskill Business · 178 points'}, {'fr': 'Juin 2026', 'en': 'Jun 2026'}, 'linguaskill'),
    ('gdp', {'fr': 'MOOC Gestion de projet', 'en': 'Project Management MOOC'}, {'fr': 'Avr. 2025', 'en': 'Apr 2025'}, 'gdp'),
    ('pc', {'fr': 'Aide et écoute psychologique (AEP1)', 'en': 'Psychological first aid and listening (AEP1)'}, {'fr': 'Févr. 2025', 'en': 'Feb 2025'}, 'aep1'),
    ('pc', {'fr': 'Secouriste PSE1', 'en': 'First aider (PSE1)'}, {'fr': 'Déc. 2024', 'en': 'Dec 2024'}, 'pse1'),
    ('ffme', {'fr': "Brevet fédéral d'initiateur SAE (escalade)", 'en': 'Federal climbing instructor certificate (indoor walls)'}, {'fr': 'Oct. 2024', 'en': 'Oct 2024'}, 'isae'),
]
# Fiches détaillées des certifications (fenêtre sur la page Parcours).
# about : le diplôme ; can : ce que je sais faire ; field : (page, ancre) de la mise en pratique.
CERT_INFO = {
    'pse1': dict(
        about={'fr': "Certificat de compétences de secouriste, défini par un référentiel national de sécurité civile (formation d'au moins 35 heures). Il permet d'intervenir comme secouriste au sein d'une association agréée de sécurité civile, et s'entretient par une formation continue annuelle.",
               'en': 'Certificate of first-aid competence, defined by a national civil-security framework (at least 35 hours of training). It qualifies me to act as a first-aider within an approved civil-security association, and is kept up to date through annual refresher training.'},
        can={'fr': ["Assurer la protection de la victime, des témoins et de l'équipe",
                    "Réaliser un bilan et le transmettre au médecin régulateur du SAMU",
                    "Prendre en charge une urgence vitale : hémorragie, obstruction des voies aériennes, perte de connaissance, arrêt cardiaque (réanimation, défibrillateur)",
                    "Prendre en charge les malaises, traumatismes, plaies et brûlures",
                    "Administrer de l'oxygène et appliquer les règles d'hygiène et d'asepsie"],
             'en': ['Protect the casualty, bystanders and the team',
                    'Assess the casualty and report to the SAMU (emergency medical service) doctor',
                    'Manage life-threatening emergencies: bleeding, choking, unconsciousness, cardiac arrest (CPR, defibrillator)',
                    'Manage illnesses, injuries, wounds and burns',
                    'Administer oxygen and apply hygiene and infection-control rules']},
        field=('eng', 'protection-civile')),
    'pse2': dict(
        about={'fr': "Complète le PSE1 et permet d'exercer comme équipier secouriste : prendre en charge une victime en équipe, avec le matériel d'un poste de secours ou d'un véhicule de premiers secours à personnes (VPSP). Formation continue annuelle obligatoire.",
               'en': 'Builds on the PSE1 and qualifies me as a first-aid team member: caring for a casualty as a team, with the equipment of a first-aid post or an ambulance (VPSP). Annual refresher training is mandatory.'},
        can={'fr': ["Immobiliser une victime de traumatisme : attelles, collier cervical, matelas immobilisateur à dépression",
                    "Relever et brancarder une victime en vue de son transport",
                    "Conduire un bilan complet en équipe et le transmettre",
                    "Faire face à des situations particulières : souffrance psychique, victimes multiples"],
             'en': ['Immobilise an injured casualty: splints, cervical collar, vacuum mattress',
                    'Lift and carry a casualty on a stretcher for transport',
                    'Lead a full assessment as a team and report it',
                    'Handle specific situations: psychological distress, multiple casualties']},
        field=('eng', 'protection-civile')),
    'linguaskill': dict(
        about={'fr': "Test d'anglais professionnel de Cambridge University Press & Assessment, en contexte business, passé sur les modules de compréhension écrite et de compréhension orale. Les résultats sont donnés sur l'échelle Cambridge English, alignée sur le CECRL : de 160 à 179 points pour le B2, à partir de 180 pour le C1.",
               'en': 'Cambridge University Press & Assessment workplace English test, in a business context, taken on the reading and listening modules. Results are given on the Cambridge English Scale, aligned with the CEFR: 160 to 179 points for B2, 180 and above for C1.'},
        meter=dict(lo=140, hi=200, bands=[('B1', 140, 160), ('B2', 160, 180), ('C1', 180, 200)],
                   rows=[({'fr': 'Compréhension orale', 'en': 'Listening'}, 189),
                         ({'fr': 'Compréhension écrite', 'en': 'Reading'}, 167),
                         ({'fr': 'Score global', 'en': 'Overall'}, 178)],
                   label={'fr': "Niveau C1 en compréhension orale, B2 avancé au global.",
                          'en': 'C1 level in listening, upper B2 overall.'}),
        can={'fr': ["Suivre sans difficulté une réunion, une présentation ou une conférence en anglais",
                    "Saisir les nuances, l'implicite et les points de vue dans un échange",
                    "Comprendre des documents professionnels détaillés : rapports, articles, documentation technique",
                    "Travailler au quotidien avec des sources et de la documentation en anglais"],
             'en': ['Follow meetings, presentations and talks in English with ease',
                    'Grasp nuance, implicit meaning and points of view in a discussion',
                    'Understand detailed professional documents: reports, articles, technical documentation',
                    'Work daily with sources and documentation in English']},
        note={'fr': "Une pratique de longue date : baccalauréat en section européenne anglais.",
              'en': 'A long-standing practice: French baccalauréat in the European section (English).'}),
    'gdp': dict(
        about={'fr': "MOOC de gestion de projet créé par Rémi Bachelet à Centrale Lille, l'un des premiers MOOC certifiants en France. Il couvre les fondamentaux de la gestion de projet, avec des exercices pratiques évalués et un examen final, validés par une attestation de réussite.",
               'en': 'Project management MOOC created by Rémi Bachelet at Centrale Lille, one of the first certifying MOOCs in France. It covers the fundamentals of project management, with graded practical exercises and a final exam, leading to a certificate of achievement.'},
        can={'fr': ["Cadrer un projet : objectifs, périmètre, livrables et parties prenantes",
                    "Découper le travail et planifier : organigramme des tâches, diagramme de Gantt",
                    "Estimer et suivre un budget",
                    "Identifier et maîtriser les risques d'un projet",
                    "Animer une équipe projet et organiser son pilotage"],
             'en': ['Scope a project: objectives, boundaries, deliverables and stakeholders',
                    'Break down the work and plan it: work breakdown structure, Gantt chart',
                    'Estimate and track a budget',
                    'Identify and control project risks',
                    'Lead a project team and organise its steering']},
        note={'fr': "Suivi en parallèle de l'option Leadership du S6, consacrée à la gestion de projet.",
              'en': 'Taken alongside the S6 Leadership option, focused on project management.'},
        field=('ue', 'gestion-projet')),
    'isae': dict(
        about={'fr': "Brevet fédéral de la FFME qui permet d'encadrer bénévolement et en autonomie l'escalade sur structure artificielle (blocs et voies), dans un club ou une structure affiliée. Formation d'au moins 20 heures, évaluations et stage pratique, puis recyclage tous les 4 ans.",
               'en': 'FFME federal certificate qualifying me to supervise climbing on artificial walls (bouldering and roped routes) as a volunteer and on my own, in a club or affiliated facility. At least 20 hours of training, assessments and a practical placement, then a refresher every 4 years.'},
        can={'fr': ["Encadrer en autonomie un groupe de grimpeurs sur mur d'escalade",
                    "Faire respecter la sécurité : vérification des équipements, encordement, assurage",
                    "Préparer et animer des séances d'initiation et de progression",
                    "Transmettre les bases techniques : assurage, placement, lecture de voie"],
             'en': ['Supervise a group of climbers on a climbing wall, on my own',
                    'Enforce safety: equipment checks, tying in, belaying',
                    'Plan and lead beginner and progression sessions',
                    'Teach the technical basics: belaying, body positioning, route reading']},
        field=('eng', 'grinp')),
    'aep1': dict(  # TODO : contenu à valider avec Arthur (pas de source officielle en ligne)
        about={'fr': "Formation de la Protection Civile à l'aide et à l'écoute psychologique : accueillir et soutenir les personnes touchées par un événement difficile, qu'elles soient victimes, témoins ou proches.",
               'en': 'Civil Protection training in psychological support and listening: welcoming and supporting people affected by a distressing event, whether casualties, witnesses or relatives.'},
        can={'fr': ["Pratiquer l'écoute active auprès d'une personne en détresse",
                    "Repérer les réactions de stress et adapter mon attitude",
                    "Accompagner les victimes, les témoins et les proches"],
             'en': ['Practise active listening with a person in distress',
                    'Recognise stress reactions and adapt my approach',
                    'Support casualties, witnesses and relatives']},
        field=('eng', 'protection-civile')),
}
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
<link rel="canonical" href="{url(lang, key)}">
<link rel="alternate" hreflang="fr" href="{url('fr', key)}">
<link rel="alternate" hreflang="en" href="{url('en', key)}">
<link rel="alternate" hreflang="x-default" href="{url('fr', key)}">
<meta property="og:type" content="{'profile' if key == 'home' else 'website'}">
<meta property="og:site_name" content="Arthur Sauvezie">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(t['desc'][key])}">
<meta property="og:url" content="{url(lang, key)}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{'Arthur Sauvezie, élève ingénieur à l’ENSEEIHT' if lang == 'fr' else 'Arthur Sauvezie, engineering student at ENSEEIHT'}">
<meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if lang == 'fr' else 'fr_FR'}">
<meta name="twitter:card" content="summary_large_image">
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
{ent_templates(lang, p)}<dialog class="ue-dialog" aria-labelledby="ue-dialog-title"><div class="ue-card" tabindex="-1" autofocus><button class="ue-close icon-btn" type="button" aria-label="{'Fermer' if lang == 'fr' else 'Close'}">{MENU_CLOSE}</button><div class="ue-body"></div></div></dialog>
<script src="{p}js/ue.js" defer></script>
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
    by_url = {ENT[k][1]: k for k in ENT_INFO}
    links = ''.join(f' · <a class="ext" href="{u}" target="_blank" rel="noopener"{pop_attr(by_url[u]) if u in by_url else ""}>{e(l)}</a>'
                    for l, u in d.get('links', []))
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
        f'<a class="card" href="{eng_file}#{d["id"]}"><div class="card-top">{logo(d["ent"], p, link=False)}'
        f'<div><h3>{e(d["role"][lang])}</h3><div class="sub">{e(d["orgname"][lang])}</div></div></div>'
        f'<div class="fig"><b>{e(d["card"][lang][0])}</b>{e(d["card"][lang][1])}</div></a>'
        for d in ENG[:3])
    exp_file = FILE[lang]['exp']
    items = EXP + PROJ[:2]
    lst = ''.join(
        f'<a class="withlogo" href="{exp_file}#{d["id"]}">{logo(d["ent"], p, "sm", link=False)}'
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
            chips = ''.join(f'<li><a href="#ue-{u["id"]}" data-pop="ue-{u["id"]}">{e(u["name"][lang])}</a></li>' for u in group)
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
                chips.append(f'<a class="chip proof" href="#ue-{uid}" data-pop="ue-{uid}" title="{e(tip)}">{e(label)}</a>')
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
        lis = ''
        for k, name, d, *cid in CERTS:
            if k not in keys:
                continue
            cid = cid[0] if cid and cid[0] in CERT_INFO else None
            title = (f'<a class="cert-link" href="#cert-{cid}" data-pop="cert-{cid}">{e(name[lang])}</a>' if cid else e(name[lang]))
            lis += (f'<li{" class=" + chr(34) + "has-pop" + chr(34) if cid else ""}>{logo(k, p)}<div class="t">{title}'
                    f'<span>{org(k, CERT_ORG[k][lang])}</span></div><div class="d">{d[lang]}</div></li>')
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
            if isinstance(u.get('sem'), str):
                ctx = u['sem']
            else:
                ctx = ' · '.join(x for x in (sem_label(lang, u['sem']) if u.get('sem') else '', d['when'][lang]) if x)
            tpls += (f'<template id="tpl-ue-{u["id"]}"><div class="ue-ctx">{logo(d["ent"], p, "sm")}<div>'
                     f'<div class="ue-when">{ctx}</div><div class="org">{e(d["role"][lang])}</div></div></div>'
                     f'<h3 id="ue-dialog-title">{e(u["name"][lang])}</h3><p>{e(u["desc"][lang])}</p>'
                     f'<div class="ue-skills"><span>{"Compétences" if fr else "Skills"}</span><div class="chips">{chips}</div></div>{proj}</template>')
    # Certifications détaillées
    places = {d['id']: d['orgname'][lang] for d in ENG if 'orgname' in d}
    for k, name, d, *cid in CERTS:
        if not cid or cid[0] not in CERT_INFO:
            continue
        info = CERT_INFO[cid[0]]
        items = ''.join(f'<li>{e(x)}</li>' for x in info['can'][lang])
        meter = ''
        if info.get('meter'):
            m = info['meter']
            span = m['hi'] - m['lo']
            bars = ''
            for lab, score in m['rows']:
                segs = ''.join(f'<span class="seg{" on" if a <= score < b else ""}" style="width:{(b - a) / span * 100:.4g}%">{lv}</span>'
                               for lv, a, b in m['bands'])
                pos = (min(score, m['hi']) - m['lo']) / span * 100
                bars += (f'<div class="meter-row"><div class="meter-name">{e(lab[lang])}<b>{score}</b></div>'
                         f'<div class="meter-bar" role="img" aria-label="{e(lab[lang])} : {score}">{segs}'
                         f'<span class="mark" style="left:{pos:.4g}%"></span></div></div>')
            meter = f'<div class="meter">{bars}<p class="meter-label">{e(m["label"][lang])}</p></div>'
        note = f'<p class="pop-note">{e(info["note"][lang])}</p>' if info.get('note') else ''
        field = ''
        if info.get('field') and info['field'][0] == 'ue':
            uid = info['field'][1]
            uname = next(u['name'][lang] for d2 in EDU for u in d2.get('ue') or [] if u['id'] == uid)
            field = (f'<a class="ue-proj" href="#ue-{uid}" data-pop="ue-{uid}">{"Mis en pratique :" if fr else "Put into practice:"} '
                     f'{e(uname)} <span aria-hidden="true">→</span></a>')
        elif info.get('field'):
            pg, anchor = info['field']
            field = (f'<a class="ue-proj" href="{FILE[lang][pg]}#{anchor}">{"Sur le terrain :" if fr else "In the field:"} '
                     f'{e(places.get(anchor, NAV[lang][pg]))} <span aria-hidden="true">→</span></a>')
        tpls += (f'<template id="tpl-cert-{cid[0]}"><div class="ue-ctx">{logo(k, p, "sm")}<div>'
                 f'<div class="ue-when">{d[lang]}</div><div class="org">{e(CERT_ORG[k][lang])}</div></div></div>'
                 f'<h3 id="ue-dialog-title">{e(name[lang])}</h3><p>{e(info["about"][lang])}</p>{meter}'
                 f'<div class="ue-skills"><span>{"Ce que je sais faire" if fr else "What I can do"}</span><ul class="pop-list">{items}</ul></div>{note}{field}</template>')
    return tpls


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


def not_found():
    """Page 404 bilingue. Servie par GitHub Pages à n'importe quelle profondeur :
    <base href="/"> rend tous les liens relatifs valables depuis la racine."""
    body = ('<section class="wrap hero nf"><div class="hero-text"><div class="bar"></div>'
            '<h1>404</h1>'
            '<p class="lead">Cette page n’existe pas, ou plus. Elle a peut-être changé d’adresse.</p>'
            '<p class="lead" lang="en">This page does not exist, or no longer does. It may have moved.</p>'
            '<div class="actions"><a class="btn primary" href="index.html">Retour à l’accueil</a>'
            '<a class="btn" href="en/index.html" lang="en">Back to home (EN)</a></div>'
            '</div></section>')
    s = page('fr', 'home', 'Page introuvable', body)
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="/">\n<meta name="robots" content="noindex">', 1)
    s = s.replace('<title>Arthur Sauvezie · E-portfolio</title>', '<title>Page introuvable · Arthur Sauvezie</title>', 1)
    # ni canonical ni alternates : ce n'est pas l'accueil
    s = '\n'.join(l for l in s.split('\n') if not l.startswith(('<link rel="canonical"', '<link rel="alternate"', '<meta property="og:url"')))
    return s.replace(' aria-current="page"', '', 1)


def sitemap():
    out = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    for k in PAGES:
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l, k)}"/>' for l in ('fr', 'en'))
        for lang in ('fr', 'en'):
            out += f'<url><loc>{url(lang, k)}</loc>{alts}</url>\n'
    return out + '</urlset>\n'


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
    write('404.html', not_found())
    write('sitemap.xml', sitemap())
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
