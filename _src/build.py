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
    'w7':     ('Women7', None, None, 'W7'),
    'eedf':   ('Éclaireuses Éclaireurs de France', 'https://www.eedf.fr', 'eedf.svg', ''),
    'ffme':   ('FFME', 'https://www.ffme.fr', 'ffme.svg', ''),
    'cam':    ('Cambridge University Press & Assessment', 'https://www.cambridgeenglish.org', 'cambridge.png', ''),
    'bellevue': ('Lycée Bellevue', None, None, 'LB'),
    'limosin':  ('Lycée Léonard Limosin', None, None, 'LL'),
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
    dict(id='airbus', ent='airbus',
         when={'fr': 'Févr. – juil. 2027 · 6 mois', 'en': 'Feb – Jul 2027 · 6 months'},
         role={'fr': "Projet de fin d'études", 'en': 'Final-year project'},
         badge={'fr': 'À venir', 'en': 'Upcoming'},
         text={'fr': "Évaluation d'outils de virtualisation pour l'infrastructure système : étude comparative, tests de performance et recommandations.",
               'en': 'Evaluating virtualisation tools for system infrastructure: comparative study, performance testing and recommendations.'},
         rows={'fr': [('Domaine', 'Virtualisation, administration système')],
               'en': [('Field', 'Virtualisation, system administration')]}),
    dict(id='prefecture', ent='pref',
         when={'fr': 'Juin – août 2026 · 11 semaines', 'en': 'Jun – Aug 2026 · 11 weeks'},
         role={'fr': 'Stage · SGCD, service SIC', 'en': 'Internship · SGCD, IT department (SIC)'},
         text={'fr': "Développement d'un site centralisant les annuaires des agents : six sources de données fusionnées en un annuaire unique et à jour. L'outil est en production, à usage interne.",
               'en': 'Built a website that centralises staff directories, merging six data sources into a single, up-to-date directory. The tool is in production for internal use.'},
         stats={'fr': [('~1 000', 'agents'), ('6', 'sources de données'), ('En production', 'usage interne')],
                'en': [('~1,000', 'staff'), ('6', 'data sources'), ('In production', 'internal use')]},
         rows={'fr': [('Technologies', 'Serveur LAMP (Linux, Apache, MySQL, PHP)')],
               'en': [('Stack', 'LAMP server (Linux, Apache, MySQL, PHP)')]}),
    dict(id='irt', ent='irt',
         when={'fr': 'Juin – juil. 2025 · 6 semaines', 'en': 'Jun – Jul 2025 · 6 weeks'},
         role={'fr': 'Stage de recherche', 'en': 'Research internship'},
         text={'fr': 'Travaux de recherche sur les LLM spécialisés en cybersécurité et sur les IDS/IPS fondés sur des réseaux de neurones.',
               'en': 'Research on cybersecurity-specialised LLMs and neural-network-based IDS/IPS.'},
         rows={'fr': [('Domaine', 'IA, cybersécurité')], 'en': [('Field', 'AI, cybersecurity')]}),
]

PROJ = [
    dict(id='grinp-web', ent='grinp',
         when={'fr': '2025 – aujourd\'hui', 'en': '2025 – present'},
         role={'fr': "Plateforme web du club d'escalade", 'en': 'Climbing club web platform'},
         text={'fr': "Reprise et maintenance de la plateforme du club Gr'INP, conçue en 2024 par un autre membre : comptes adhérents, calendrier et inscriptions aux séances, pour les quelque 200 adhérents.",
               'en': "Took over and maintain the Gr'INP club platform, first built in 2024 by another member: member accounts, calendar and session sign-ups for around 200 members."},
         links=[('grinp.inpt.fr', 'https://grinp.inpt.fr')]),
]

ENG = [
    dict(id='protection-civile', ent='pc', orgname={'fr': 'Protection Civile de la Haute-Garonne', 'en': 'Civil Protection, Haute-Garonne'},
         when={'fr': 'Sept. 2024 – aujourd\'hui', 'en': 'Sep 2024 – present'},
         role={'fr': "Équipier-secouriste, chef d'équipe, chef de poste", 'en': 'First-aid team member, team leader, post leader'},
         text={'fr': "Secours à personnes sur dispositifs prévisionnels de secours, déclenchements fédéraux et gardes SAMU. Aujourd'hui chef d'équipe et chef de poste : j'encadre les secouristes et coordonne les postes de secours.",
               'en': 'First aid at planned event cover, federal call-outs and SAMU (emergency medical service) shifts. Now a team leader and post leader: I lead first-aiders and coordinate first-aid posts.'},
         stats={'fr': [('600 h+', 'de bénévolat par an'), ('Des centaines', "d'activités"), ('PSE1 · PSE2 · APS1', 'certifications')],
                'en': [('600 h+', 'volunteering per year'), ('Hundreds', 'of activities'), ('PSE1 · PSE2 · APS1', 'certifications')]},
         tags={'fr': ['Incendies de Bordeaux (déclenchement fédéral)', 'Marathon de Toulouse', 'Gardes SAMU'],
               'en': ['Bordeaux wildfires (federal call-out)', 'Toulouse Marathon', 'SAMU shifts']},
         card={'fr': ('600 h+', 'de secours par an'), 'en': ('600 h+', 'of first aid per year')}),
    dict(id='grinp', ent='grinp', orgname={'fr': "Club Gr'INP · AS Toulouse INP", 'en': "Gr'INP club · AS Toulouse INP"},
         when={'fr': '2024 – aujourd\'hui', 'en': '2024 – present'},
         role={'fr': "Président du club d'escalade", 'en': 'President of the climbing club'},
         text={'fr': "Direction de la section : organisation des séances et des événements, gestion du budget et des adhésions, coordination de l'équipe de bénévoles et lien avec le bureau de l'AS. Initiateur escalade breveté FFME.",
               'en': 'Running the section: organising sessions and events, managing the budget and memberships, coordinating the volunteer team and liaising with the sports association board. FFME-certified climbing instructor.'},
         stats={'fr': [('200', 'adhérents'), ('14', 'bénévoles'), ('3 k€', 'de budget annuel')],
                'en': [('200', 'members'), ('14', 'volunteers'), ('€3k', 'annual budget')]},
         tags={'fr': ['Compétitions', "Soirées « Nuits de l'escalade »", 'Plateforme web du club'],
               'en': ['Competitions', "“Nuits de l'escalade” evenings", 'Club web platform']},
         card={'fr': ('200', 'adhérents, 14 bénévoles'), 'en': ('200', 'members, 14 volunteers')}),
    dict(id='net7', ent='net7', orgname={'fr': "net7, association informatique de l'ENSEEIHT", 'en': "net7, ENSEEIHT's IT association"},
         when={'fr': '2025 – aujourd\'hui', 'en': '2025 – present'},
         role={'fr': 'Administrateur systèmes et réseaux', 'en': 'Systems and network administrator'},
         text={'fr': "Administration système de l'ensemble de l'infrastructure de l'association : machines virtuelles sur les hyperviseurs Proxmox, infrastructure réseau, services hébergés pour les étudiants, supervision et sécurisation.",
               'en': "System administration across the association's whole infrastructure: virtual machines on Proxmox hypervisors, network infrastructure, services hosted for students, monitoring and security."},
         tags={'fr': ['Proxmox', 'Machines virtuelles', 'Réseau', 'Services étudiants'],
               'en': ['Proxmox', 'Virtual machines', 'Networking', 'Student services']},
         card={'fr': ('Proxmox', 'VM, réseau, services'), 'en': ('Proxmox', 'VMs, network, services')}),
    dict(id='women7', ent='w7', orgname={'fr': 'Women7 · ENSEEIHT', 'en': 'Women7 · ENSEEIHT'},
         when={'fr': 'Juin 2025 – juin 2026', 'en': 'Jun 2025 – Jun 2026'},
         role={'fr': 'Membre du bureau', 'en': 'Board member'},
         text={'fr': "Au sein d'un bureau de trois personnes, organisation de la journée annuelle d'accueil des collégiennes d'Occitanie à l'ENSEEIHT : découverte des métiers de l'ingénierie, pour les encourager à s'orienter vers les filières scientifiques.",
               'en': 'As one of a three-person board, organised the annual day welcoming middle-school girls from Occitanie to ENSEEIHT, introducing engineering careers to encourage them towards science.'},
         stats={'fr': [('200', 'collégiennes accueillies'), ('3', 'membres du bureau')],
                'en': [('200', 'girls welcomed'), ('3', 'board members')]},
         card={'fr': ('200', 'collégiennes accueillies'), 'en': ('200', 'girls welcomed')}),
    dict(id='ceve', ent='n7', orgname={'fr': "Conseil des études et de la vie étudiante · ENSEEIHT", 'en': 'Studies and Student Life Council · ENSEEIHT'},
         when={'fr': '2024 – aujourd\'hui', 'en': '2024 – present'},
         role={'fr': 'Représentant étudiant', 'en': 'Student representative'},
         text={'fr': "Porte-parole des étudiants auprès de l'équipe pédagogique et de l'administration. Je participe aux décisions sur les formations et la vie étudiante, dont le vote des modalités de contrôle des connaissances (MCC).",
               'en': 'Student spokesperson to the teaching staff and administration. I take part in decisions on programmes and student life, including voting on assessment rules (MCC).'},
         tags={'fr': ['Vote des MCC', 'Formations', 'Vie étudiante'], 'en': ['Assessment rules', 'Programmes', 'Student life']},
         card={'fr': ('Élu', 'vote des MCC'), 'en': ('Elected', 'votes on assessment rules')}),
    dict(id='eedf', ent='eedf', orgname={'fr': 'Éclaireuses Éclaireurs de France · Limoges', 'en': 'Éclaireuses Éclaireurs de France (scouts) · Limoges'},
         when={'fr': '2021 – 2022', 'en': '2021 – 2022'},
         role={'fr': "Responsable d'animation et assistant sanitaire", 'en': 'Activity leader and health officer'},
         text={'fr': "Pendant un an, encadrement et animation d'activités pour les jeunes du groupe, et suivi sanitaire en tant qu'assistant sanitaire.",
               'en': 'For a year, led activities for the young members of the group and handled health matters as health officer.'},
         card={'fr': ('1 an', "d'animation"), 'en': ('1 year', 'leading activities')}),
]

EDU = [
    dict(ent='laval', when={'fr': 'Automne 2026', 'en': 'Fall 2026'}, where='Québec',
         role={'fr': "Semestre d'échange", 'en': 'Exchange semester'},
         text={'fr': 'Gestion de projet, gouvernance de la sécurité, réseaux mobiles, cloud et DevOps.',
               'en': 'Project management, security governance, mobile networks, cloud and DevOps.'}),
    dict(ent='n7', when={'fr': '2024 – 2027', 'en': '2024 – 2027'}, where='Toulouse',
         role={'fr': "Diplôme d'ingénieur · Informatique et Télécommunications", 'en': 'Engineering degree · Computer Science and Telecommunications'},
         text={'fr': 'Département Sciences du Numérique.', 'en': 'Digital Sciences department.'}),
    dict(ent='bellevue', when={'fr': '2022 – 2024', 'en': '2022 – 2024'}, where='Toulouse',
         role={'fr': 'Classes préparatoires PCSI / PSI', 'en': 'Preparatory classes (CPGE) PCSI / PSI'},
         text={'fr': "Physique et sciences de l'ingénieur.", 'en': 'Physics and engineering sciences.'}),
    dict(ent='limosin', when={'fr': '2019 – 2022', 'en': '2019 – 2022'}, where='Limoges',
         role={'fr': 'Baccalauréat général, section européenne (anglais)', 'en': 'French baccalauréat, European section (English)'},
         text={'fr': 'Mathématiques, physique-chimie, mathématiques expertes.', 'en': 'Mathematics, physics and chemistry, advanced mathematics.'}),
]

CERTS = [
    ('pc', {'fr': "Équipier-secouriste PSE2", 'en': 'First-aid team member (PSE2)'}, {'fr': 'Mars 2026', 'en': 'Mar 2026'}),
    ('cam', {'fr': 'Linguaskill Business · 178 points', 'en': 'Linguaskill Business · 178 points'}, {'fr': 'Juin 2026', 'en': 'Jun 2026'}),
    ('pc', {'fr': 'Aide et écoute psychologique (APS1)', 'en': 'Psychological first aid and listening (APS1)'}, {'fr': 'Févr. 2025', 'en': 'Feb 2025'}),
    ('pc', {'fr': 'Secouriste PSE1', 'en': 'First aider (PSE1)'}, {'fr': 'Déc. 2024', 'en': 'Dec 2024'}),
    ('ffme', {'fr': "Brevet fédéral d'initiateur SAE (escalade)", 'en': 'Federal climbing instructor certificate (indoor walls)'}, {'fr': 'Oct. 2024', 'en': 'Oct 2024'}),
]
CERT_ORG = {'pc': {'fr': 'Fédération Nationale de Protection Civile', 'en': 'French Civil Protection Federation'},
            'cam': {'fr': 'Cambridge University Press & Assessment', 'en': 'Cambridge University Press & Assessment'},
            'ffme': {'fr': 'Fédération Française de la Montagne et de l\'Escalade', 'en': 'French Mountaineering and Climbing Federation'}}

SKILLS = {
    'fr': [('Systèmes et virtualisation', 'Linux, Windows, hyperviseurs Proxmox.'),
           ('Réseaux', 'TCP/IP, routage, commutation.'),
           ('DevOps et web', 'Git, CI/CD, Bash, serveur LAMP.'),
           ('Langages', 'Python, Java, C, PHP.'),
           ('Langues', 'Français natif, anglais B2/C1 (Linguaskill 178).'),
           ('Transversales', "Gestion du stress et de l'urgence, encadrement d'équipes, communication en situation critique.")],
    'en': [('Systems and virtualisation', 'Linux, Windows, Proxmox hypervisors.'),
           ('Networking', 'TCP/IP, routing, switching.'),
           ('DevOps and web', 'Git, CI/CD, Bash, LAMP stack.'),
           ('Languages', 'Python, Java, C, PHP.'),
           ('Spoken languages', 'French (native), English B2/C1 (Linguaskill 178).'),
           ('Soft skills', 'Stress and emergency management, team leadership, clear communication in critical situations.')],
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
<link rel="alternate" hreflang="fr" href="{url('fr', key)}">
<link rel="alternate" hreflang="en" href="{url('en', key)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="{p}css/style.css">
<script src="{p}js/theme.js"></script>
</head>
<body>
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
    return (f'<article class="eng"{idattr}><div class="side">{logo(d["ent"], p)}<div class="when">{d["when"][lang]}{where}</div></div>'
            f'<div class="body"><h3>{e(d["role"][lang])}{badge}</h3><div class="org">{org(d["ent"], orglabel)}{links}</div>'
            f'<p>{e(d["text"][lang])}</p>{stats(d.get("stats", {}).get(lang))}{tags(d.get("tags", {}).get(lang))}{rows(d.get("rows", {}).get(lang))}</div></article>')


# ---------------------------------------------------------------- Pages
def home(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    lead = ("Élève ingénieur en dernière année à l'" + org('n7', 'ENSEEIHT') + ", en informatique et télécommunications, actuellement en échange à l'" + org('laval') + ". Passionné par l'aéronautique, le spatial et la cybersécurité, je m'investis aussi comme secouriste et responsable associatif."
            if fr else
            "Final-year engineering student at " + org('n7', 'ENSEEIHT') + " in computer science and telecommunications, currently on exchange at " + org('laval') + ". Passionate about aeronautics, space and cybersecurity, and committed as a first-aider and student association leader.")
    strip = [
        ('Formation' if fr else 'Education', logo('n7', p, 'sm'), 'ENSEEIHT, Informatique et Télécom.' if fr else 'ENSEEIHT, CS and Telecom'),
        ('En ce moment' if fr else 'Currently', logo('laval', p, 'sm'), 'Échange, Université Laval' if fr else 'Exchange, Université Laval'),
        ('Recherche' if fr else 'Looking for', '', 'Premier emploi, après mon PFE (juil. 2027)' if fr else 'First job, after my final-year project (Jul 2027)'),
    ]
    strip_html = ''.join(f'<div><span class="k">{k}</span><span class="v">{l}{v}</span></div>' for k, l, v in strip)
    eng_file = FILE[lang]['eng']
    cards = ''.join(
        f'<a class="card" href="{eng_file}#{d["id"]}"><div class="card-top">{logo(d["ent"], p).replace("<a ", "<span ").replace("</a>", "</span>") if ENT[d["ent"]][1] else logo(d["ent"], p)}'
        f'<div><h3>{e(d["role"][lang])}</h3><div class="sub">{e(d["orgname"][lang])}</div></div></div>'
        f'<div class="fig"><b>{e(d["card"][lang][0])}</b>{e(d["card"][lang][1])}</div></a>'
        for d in ENG)
    exp_file = FILE[lang]['exp']
    items = EXP + PROJ
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
<div class="shead"><h2>{'Engagements' if fr else 'Commitments'}</h2><a href="{eng_file}">{'Tout voir →' if fr else 'See all →'}</a></div>
<p class="kicker">{"Secouriste, président de club, administrateur système bénévole : en parallèle de mes études, je prends des responsabilités sur le terrain." if fr else "First-aider, club president, volunteer sysadmin: alongside my studies, I take on hands-on responsibilities."}</p>
<div class="cards">{cards}</div>
</section>
<section class="wrap section tight">
<div class="shead"><h2>{'Expériences et projets' if fr else 'Experience and projects'}</h2><a href="{exp_file}">{'Détails →' if fr else 'Details →'}</a></div>
<div class="list">{lst}</div>
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


def parcours(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    body = head('Parcours' if fr else 'Background', T[lang]['desc']['bg'])
    body += f'<section class="wrap block-sm"><h2>{"Formation" if fr else "Education"}</h2>' + ''.join(entry(lang, p, d) for d in EDU) + '</section>'
    certs = ''.join(f'<li>{logo(k, p)}<div class="t">{e(name[lang])}<span>{org(k, CERT_ORG[k][lang])}</span></div><div class="d">{d[lang]}</div></li>' for k, name, d in CERTS)
    body += f'<section class="wrap block-sm"><h2>{"Certifications" if fr else "Certifications"}</h2><ul class="certs">{certs}</ul></section>'
    cols = ''.join(f'<div><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in SKILLS[lang])
    body += f'<section class="wrap block"><h2>{"Compétences" if fr else "Skills"}</h2><div class="cols">{cols}</div></section>'
    return page(lang, 'bg', NAV[lang]['bg'], body)


def cv(lang):
    p = '../' if lang == 'en' else ''
    fr = lang == 'fr'
    body = head('CV', T[lang]['desc']['cv'] + (' Le fichier contient la version française et la version anglaise.' if fr else ' The file includes both the French and English versions.'))
    body = body.replace('</p></section>', f'</p><div class="actions"><a class="btn primary" href="{p}assets/{"cv.pdf" if fr else "cv-en.pdf"}" download>{"Télécharger le CV (PDF)" if fr else "Download CV (PDF)"}</a><a class="btn" href="{FILE[lang]["bg"]}">{"Voir le parcours" if fr else "See background"}</a></div></section>')
    cols = [('Formation' if fr else 'Education', 'ENSEEIHT, Informatique et Télécommunications. Échange à l\'Université Laval.' if fr else 'ENSEEIHT, Computer Science and Telecommunications. Exchange at Université Laval.'),
            ('Expériences' if fr else 'Experience', 'Airbus Defence and Space (PFE), Préfecture de la Haute-Garonne, IRT Saint Exupéry.'),
            ('Engagements' if fr else 'Commitments', "Protection Civile, Gr'INP, net7, Women7, CEVE." if fr else "Civil Protection, Gr'INP, net7, Women7, student council.")]
    body += '<section class="wrap section tight"><div class="cols">' + ''.join(f'<div><h3>{a}</h3><p>{e(b)}</p></div>' for a, b in cols) + '</div></section>'
    return page(lang, 'cv', 'CV', body)


def contact(lang):
    fr = lang == 'fr'
    body = head('Contact', T[lang]['desc']['contact'])
    mail = (f'<button type="button" class="mail-btn js-mail" data-m="{MAIL_REV}">{"Afficher l’adresse" if fr else "Show address"}</button>')
    li = [('E-mail' if fr else 'Email', mail),
          ('LinkedIn', f'<a class="ext" href="{LINKEDIN}" target="_blank" rel="noopener">Arthur Sauvezie</a>'),
          ('GitHub', f'<a class="ext" href="{GITHUB}" target="_blank" rel="noopener">arthursvz</a>'),
          ('Localisation' if fr else 'Location', 'Toulouse · Québec (automne 2026)' if fr else 'Toulouse · Quebec City (fall 2026)')]
    body += '<section class="wrap block"><ul class="rows flush">' + ''.join(f'<li><span>{a}</span><span>{b}</span></li>' for a, b in li) + '</ul></section>'
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
