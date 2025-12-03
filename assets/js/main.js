document.addEventListener('DOMContentLoaded',function(){
  // Nav toggle (for small screens)
  const nav=document.getElementById('siteNav');
  const btn=document.getElementById('navToggle');
  if(btn && nav){
    btn.addEventListener('click',()=>{
      if(nav.style.display==='flex'){nav.style.display='none'}
      else{nav.style.display='flex';nav.style.flexDirection='column';nav.style.gap='0.5rem'}
    });
  }

  // Theme toggle (light/dark) with persistence
  const themeToggle = document.getElementById('themeToggle');
  const root = document.documentElement;

  // Language toggle (FR/EN)
  const langToggle = document.getElementById('langToggle');

  function applyTheme(theme){
    if(theme === 'light'){
      root.setAttribute('data-theme','light');
      if(themeToggle){ themeToggle.textContent = '☀️'; themeToggle.setAttribute('aria-pressed','true'); }
    } else {
      root.removeAttribute('data-theme');
      if(themeToggle){ themeToggle.textContent = '🌙'; themeToggle.setAttribute('aria-pressed','false'); }
    }
    try{ localStorage.setItem('site-theme', theme); }catch(e){}
  }

  // --- Internationalization ---
  const translations = {
    fr: {
      nav_home: 'Accueil', nav_cv: 'CV', nav_projects: 'Projets', nav_parcours: 'Parcours', nav_contact: 'Contact',
      hero_title: 'Étudiant Ingénieur N7 — Informatique & Télécommunications',
      hero_lead: "Actuellement en seconde année d’ingénierie numérique à l'ENSEEIHT. Passionné par l'aéronautique, le spatial et la cybersécurité. Je me spécialise en Réseaux et Télécommunications.",
      btn_cv: 'Voir le CV', btn_contact: 'Me contacter',
      about_title: 'À propos', about_text: "Actuellement étudiant en seconde année d’ingénierie numérique à l'ENSEEIHT, je suis passionné par l'aéronautique, le spatial et la cybersécurité. Mon parcours académique combiné à mes engagements associatifs et secourisme montre ma capacité à travailler en équipe et à gérer des responsabilités dans des environnements exigeants. J'aspire à contribuer à des projets innovants en mettant à profit mes compétences en programmation et ma rigueur analytique.",
      formation_title: 'Formation', skills_title: 'Compétences', projects_title: 'Projets & stages',
      cv_title: 'Curriculum Vitae — Arthur Sauvezie', cv_role: 'Étudiant Ingénieur N7', cv_domain: 'Informatique & Télécommunications',
      btn_download_cv: 'Télécharger le CV (PDF)', btn_open_cv: 'Ouvrir dans un nouvel onglet',
      projects_intro: 'Code et démonstrations disponibles sur ',
      projet_irt_title: 'Stage IA / Cybersécurité — IRT Saint-Exupéry (2025)', projet_irt_desc: 'Stage de 6 semaines : travaux de recherche sur les LLM spécialisés en cybersécurité et sur des IDS/IPS basés sur réseaux de neurones. Contribution au projet de détection de pistes d\'atterrissage par IA.', projet_irt_tech_label: 'Technologies :', projet_irt_tech: 'Python, apprentissage automatique, réseaux',
      projet_net7_title: 'Administrateur Systèmes — Net7 (Asso Info N7)', projet_net7_desc: 'Aide à la maintenance des serveurs associatifs de Toulouse INP.',
      parcours_title: 'Parcours', parcours_intro: 'Résumé chronologique des études et expériences.',
      contact_title: 'Contact', contact_intro: 'Pour toute question ou collaboration, contactez‑moi — je réponds généralement sous 48h.',
      label_name: 'Nom :', label_phone: 'Téléphone :', label_phone_value: 'disponible sur le CV', label_email: 'Email :', label_email_value: 'arthur.sauvezie [insert at] etu.inp-n7.fr', label_location: 'Localisation :', label_location_value: 'Toulouse, France - De préférence en région Toulousaine, mais disponible sur tout le territoire',
      footer_contact: 'Contact'
    },
    en: {
      nav_home: 'Home', nav_cv: 'CV', nav_projects: 'Projects', nav_parcours: 'Path', nav_contact: 'Contact',
      hero_title: 'Engineering Student N7 — Computer Networks & Telecommunications',
      hero_lead: "Currently in the second year of digital engineering at ENSEEIHT. Passionate about aeronautics, space and cybersecurity. I specialize in Networks and Telecommunications.",
      btn_cv: 'View CV', btn_contact: 'Contact me',
      about_title: 'About', about_text: "Currently in the second year of digital engineering at ENSEEIHT, I am passionate about aeronautics, space and cybersecurity. My academic background combined with my associative and first-aid commitments demonstrates my ability to work in teams and handle responsibilities in demanding environments. I aspire to contribute to innovative projects by applying my programming skills and analytical rigor.",
      formation_title: 'Education', skills_title: 'Skills', projects_title: 'Projects & internships',
      cv_title: 'Curriculum Vitae — Arthur Sauvezie', cv_role: 'Engineering Student N7', cv_domain: 'Computer Networks & Telecommunications',
      btn_download_cv: 'Download CV (PDF)', btn_open_cv: 'Open in new tab',
      projects_intro: 'Code and demos available on ',
      projet_irt_title: 'AI / Cybersecurity Internship — IRT Saint-Exupéry (2025)', projet_irt_desc: '6-week internship: research work on LLMs specialized in cybersecurity and on IDS/IPS based on neural networks. Contribution to runway detection by AI.', projet_irt_tech_label: 'Technologies:', projet_irt_tech: 'Python, machine learning, networks',
      projet_net7_title: 'Systems Administrator — Net7 (Asso Info N7)', projet_net7_desc: 'Support for maintaining Toulouse INP associative servers.',
      parcours_title: 'Background', parcours_intro: 'Chronological summary of studies and experiences.',
      contact_title: 'Contact', contact_intro: 'For questions or collaboration, please contact me — I usually reply within 48h.',
      label_name: 'Name:', label_phone: 'Phone:', label_phone_value: 'available on the CV', label_email: 'Email:', label_email_value: 'arthur.sauvezie [insert at] etu.inp-n7.fr', label_location: 'Location:', label_location_value: 'Toulouse, France - Preferably in the Toulouse area, but available nationwide',
      footer_contact: 'Contact'
    }
  };

  // Extra translation keys for index content
  translations.fr.formation_content = "<strong>ENSEEIHT</strong> <br> Seconde année, Computer Networks <br> (2024 – Aujourd'hui)<br><strong>CPGE - PCSI/PSI</strong><br> Lycée Bellevue, Toulouse, 2022–2024<br><strong>BAC Général</strong> <br>Maths, Physiques, Maths Expertes <br>Lycée Léonard Limosin, 2019–2022";
  translations.en.formation_content = "<strong>ENSEEIHT</strong> <br> Second year, Computer Networks <br> (2024 – Present)<br><strong>CPGE - PCSI/PSI</strong><br> Lycée Bellevue, Toulouse, 2022–2024<br><strong>BAC Général</strong> <br>Advanced Mathematics, Physics <br>Lycée Léonard Limosin, 2019–2022";

  translations.fr.skill_1 = 'Python, Java, C, Matlab, <br> HTML, CSS, Ada, LaTeX';
  translations.en.skill_1 = 'Python, Java, C, Matlab, <br> HTML, CSS, Ada, LaTeX';
  translations.fr.skill_2 = 'Linux, Git, VSCode <br> Autres outils de bureautique';
  translations.en.skill_2 = 'Linux, Git, VSCode <br> Other office tools';
  translations.fr.skill_3 = 'Organisation, travail en équipe, <br> gestion de la pression';
  translations.en.skill_3 = 'Organization, teamwork, <br> stress management';

  translations.fr.project_item_1 = 'Stage IA / Cybersécurité — IRT Saint-Exupéry (2025)';
  translations.en.project_item_1 = 'AI / Cybersecurity Internship — IRT Saint-Exupéry (2025)';
  translations.fr.project_item_2 = 'Administrateur Systèmes — Net7 (Asso Info N7), 09.2025 – aujourd\'hui';
  translations.en.project_item_2 = 'Systems Administrator — Net7 (Asso Info N7), 09.2025 – present';

  // CV translations
  translations.fr.cv_note = 'CV original fourni (PDF). Vous pouvez le visualiser ci-dessous ou le télécharger :';
  translations.en.cv_note = 'Original CV provided (PDF). You can preview it below or download it:';

  translations.fr.cv_contact_title = 'Contact';
  translations.en.cv_contact_title = 'Contact';
  translations.fr.cv_contact_line = 'Email: arthur.sauvezie [insert at] etu.inp-n7.fr • Toulouse, France';
  translations.en.cv_contact_line = 'Email: arthur.sauvezie [insert at] etu.inp-n7.fr • Toulouse, France';

  translations.fr.edu_1 = 'Seconde Année, Computer Networks — ENSEEIHT (2024 – Aujourd\'hui)';
  translations.en.edu_1 = 'Second year, Computer Networks — ENSEEIHT (2024 – Present)';
  translations.fr.edu_2 = 'CPGE — PCSI / PSI — Lycée Bellevue, Toulouse (2022–2024)';
  translations.en.edu_2 = 'Preparatory Classes — PCSI / PSI — Lycée Bellevue, Toulouse (2022–2024)';
  translations.fr.edu_3 = 'BAC Général, Maths Expertes — Lycée Léonard Limosin, Limoges (2019–2022)';
  translations.en.edu_3 = 'General Baccalaureate, Advanced Mathematics — Lycée Léonard Limosin, Limoges (2019–2022)';

  translations.fr.cv_experiences_title = 'Expériences & stages';
  translations.en.cv_experiences_title = 'Experiences & Internships';
  translations.fr.exp_1 = 'Stage IA / Cybersécurité — IRT Saint-Exupéry (Projets CSS / DEEL), 2025 — LLMs spécialisés cyber, IDS/IPS par réseaux de neurones';
  translations.en.exp_1 = 'AI / Cybersecurity Internship — IRT Saint-Exupéry (Projects CSS / DEEL), 2025 — LLMs specialized in cyber, IDS/IPS using neural networks';
  translations.fr.exp_2 = 'Administrateur Systèmes — Net7 (Asso Info N7), 09.2025 – aujourd\'hui';
  translations.en.exp_2 = 'Systems Administrator — Net7 (Asso Info N7), 09.2025 – present';

  translations.fr.cv_competences_title = 'Compétences';
  translations.en.cv_competences_title = 'Skills';
  translations.fr.comp_languages_title = 'Langages & frameworks';
  translations.en.comp_languages_title = 'Languages & frameworks';
  translations.fr.comp_languages = 'Python (bonne maîtrise), Java (assez bonne maîtrise), C (assez bonne maîtrise), Matlab, Ada, HTML/CSS, LaTeX';
  translations.en.comp_languages = 'Python (strong), Java (good), C (good), Matlab, Ada, HTML/CSS, LaTeX';
  translations.fr.comp_tools_title = 'Outils & environnements';
  translations.en.comp_tools_title = 'Tools & environments';
  translations.fr.comp_tools = 'Linux, Git, VSCode, Docker, ROS, réseaux, cybersécurité, bases de données';
  translations.en.comp_tools = 'Linux, Git, VSCode, Docker, ROS, networks, cybersecurity, databases';
  translations.fr.comp_soft_title = 'Compétences humaines';
  translations.en.comp_soft_title = 'Soft skills';
  translations.fr.comp_soft = 'Organisation, travail en équipe, gestion de la pression, encadrement (club d\'escalade)';
  translations.en.comp_soft = 'Organization, teamwork, stress management, leadership (climbing club)';

  translations.fr.cv_engagements_title = 'Engagements';
  translations.en.cv_engagements_title = 'Engagements';
  translations.fr.eng_1 = 'Membre du Bureau Women7 — INP-ENSEEIHT (depuis 09.2025)';
  translations.en.eng_1 = 'Member of the Women7 board — INP-ENSEEIHT (since 09.2025)';
  translations.fr.eng_2 = 'Président du Club d\'Escalade — AS Toulouse INP (2024 – aujourd\'hui)';
  translations.en.eng_2 = 'President of the Climbing Club — AS Toulouse INP (2024 – present)';
  translations.fr.eng_3 = 'Délégué au Conseil d\'Etude et de Vie Etudiante — INP-ENSEEIHT (2024–2025)';
  translations.en.eng_3 = 'Delegate to the Study and Student Life Council — INP-ENSEEIHT (2024–2025)';
  translations.fr.eng_4 = 'Représentant Etudiant pour la constitution du dossier d\'accréditation à la CTI';
  translations.en.eng_4 = 'Student representative for the CTI accreditation file';
  translations.fr.eng_5 = 'Représentant Etudiant au comité de réflexion autour de la fraude de Toulouse INP';
  translations.en.eng_5 = 'Student representative on Toulouse INP\'s academic integrity committee';
  translations.fr.eng_6 = 'Secouriste — Protection Civile de Haute Garonne (09.2024 – Aujourd\'hui)';
  translations.en.eng_6 = 'First responder — Protection Civile de Haute Garonne (09.2024 – Present)';

  translations.fr.footer_text = 'Arthur Sauvezie — Étudiant ENSEEIHT • ';
  translations.en.footer_text = 'Arthur Sauvezie — ENSEEIHT Student • ';

  // Page title for projects
  translations.fr.projects_page_title = 'Projets — Arthur Sauvezie';
  translations.en.projects_page_title = 'Projects — Arthur Sauvezie';

  // Parcours page translations
  translations.fr.parcours_page_title = 'Parcours — Arthur Sauvezie';
  translations.en.parcours_page_title = 'Background — Arthur Sauvezie';

  translations.fr.parcours_item_1 = '2025 — Stage IA / Cybersécurité, IRT Saint-Exupéry (projets CSS / DEEL)';
  translations.en.parcours_item_1 = '2025 — AI / Cybersecurity Internship, IRT Saint-Exupéry (CSS / DEEL projects)';
  translations.fr.parcours_item_2 = '2025 — Administrateur Systèmes, Net7 – Asso Info N7';
  translations.en.parcours_item_2 = '2025 — Systems Administrator, Net7 – Asso Info N7';
  translations.fr.parcours_item_3 = "2024 – Aujourd'hui — Seconde Année, Computer Networks, ENSEEIHT";
  translations.en.parcours_item_3 = '2024 – Present — Second Year, Computer Networks, ENSEEIHT';
  translations.fr.parcours_item_4 = '2022 – 2024 — CPGE (PCSI → PSI), Lycée Bellevue, Toulouse';
  translations.en.parcours_item_4 = '2022 – 2024 — Preparatory Classes (PCSI → PSI), Lycée Bellevue, Toulouse';
  translations.fr.parcours_item_5 = '2019 – 2022 — BAC Général (Maths expertes), Lycée Léonard Limosin, Limoges';
  translations.en.parcours_item_5 = '2019 – 2022 — General Baccalaureate (Advanced Mathematics), Lycée Léonard Limosin, Limoges';

  translations.fr.engagements_title = 'Engagements citoyens & durabilité';
  translations.en.engagements_title = 'Civic Engagement & Sustainability';
  translations.fr.engagements_intro = 'Je m\'investis dans des actions de solidarité et d\'éducation, convaincu que l\'ingénieur a un rôle à jouer pour répondre aux défis sociaux et environnementaux.';
  translations.en.engagements_intro = 'I am involved in solidarity and educational actions, convinced that engineers have a role to play in addressing social and environmental challenges.';

  translations.fr.prot_title = 'Protection Civile — Secouriste';
  translations.en.prot_title = 'Civil Protection — First Responder';
  translations.fr.prot_desc = 'Volontaire à la Protection Civile de Haute-Garonne (depuis 09.2024) : postes de secours, gardes SAMU et maraudes. Cette expérience m\'a permis de développer des compétences en intervention d\'urgence et en gestion du stress, et renforce mon engagement pour la sécurité civile.';
  translations.en.prot_desc = 'Volunteer at the Haute-Garonne Civil Protection (since 09.2024): first aid posts, SAMU shifts and outreach. This experience helped me develop emergency response and stress management skills, and strengthens my commitment to civil safety.';
  translations.fr.prot_link = 'En savoir plus sur la Protection Civile';
  translations.en.prot_link = 'Learn more about Civil Protection';

  translations.fr.eedf_title = 'Eclaireuses & Eclaireurs de France (EEDF) — Encadrement jeunesse';
  translations.en.eedf_title = 'Eclaireuses & Eclaireurs de France (EEDF) — Youth Leadership';
  translations.fr.eedf_desc = 'Leader bénévole au sein des EEDF : accompagnement et encadrement d\'activités de plein air et de projets éducatifs pour les jeunes. Ce rôle m\'a permis d\'acquérir des compétences pédagogiques et d\'organisation, ainsi qu\'un sens renforcé de la responsabilité civique.';
  translations.en.eedf_desc = 'Volunteer leader with EEDF: supporting and leading outdoor activities and educational projects for youth. This role allowed me to gain pedagogical and organizational skills, and a strong sense of civic responsibility.';
  translations.fr.eedf_link = 'En savoir plus sur les EEDF';
  translations.en.eedf_link = 'Learn more about EEDF';

  translations.fr.activities_title = 'Sports & autres activités';
  translations.en.activities_title = 'Sports & Other Activities';
  translations.fr.activities_intro = 'En parallèle de mes études, je suis très impliqué dans des activités sportives et culturelles qui complètent ma formation :';
  translations.en.activities_intro = 'Alongside my studies, I am actively involved in sports and cultural activities that complement my training:';

  translations.fr.climbing_title = 'Escalade — Club et formation';
  translations.en.climbing_title = 'Climbing — Club & Training';
  translations.fr.climbing_desc = 'Je pratique régulièrement l\'escalade et je suis investi dans le club d\'escalade de l\'école (GrINP / AS Toulouse INP). Je prépare actuellement le Brevet Fédéral Initiateur SAE (Structure Artificielles d\'Escalade) afin de pouvoir encadrer en toute sécurité et partager cette passion.';
  translations.en.climbing_desc = 'I regularly practice climbing and am involved in the school climbing club (GrINP / AS Toulouse INP). I am currently preparing the Federal Instructor Certificate for artificial structures (SAE) to safely supervise and share this passion.';
  translations.fr.climbing_link = 'En savoir plus sur la FFME';
  translations.en.climbing_link = 'Learn more about FFME';

  translations.fr.music_title = 'Musique — Conservatoire';
  translations.en.music_title = 'Music — Conservatory';
  translations.fr.music_desc = 'J\'ai étudié la trompette et le solfège pendant 12 ans au Conservatoire National de Limoges. Cette pratique musicale a développé ma discipline, ma créativité et l\'esprit de groupe.';
  translations.en.music_desc = 'I studied trumpet and music theory for 12 years at the Conservatory of Limoges. This musical practice developed my discipline, creativity and team spirit.';
  translations.fr.music_link = 'En savoir plus sur le Conservatoire de Limoges';
  translations.en.music_link = 'Learn more about the Conservatory of Limoges';

  function applyLanguage(lang){
    const map = translations[lang] || translations.fr;
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if(!key) return;
      const txt = map[key];
      if(typeof txt === 'undefined') return;
      // If translation contains HTML tags, set innerHTML (used for formatted strings)
      if(String(txt).includes('<')){
        el.innerHTML = txt;
        return;
      }
      // If the element contains child elements (links, buttons), try to replace only the text node
      const hasChildren = el.children && el.children.length > 0;
      if(hasChildren){
        // find first text node among childNodes and replace its value
        const textNode = Array.from(el.childNodes).find(n => n.nodeType === Node.TEXT_NODE);
        if(textNode){
          textNode.nodeValue = txt;
        } else {
          // fallback: replace textContent
          el.textContent = txt;
        }
      } else {
        // no child elements: safe to set textContent
        el.textContent = txt;
      }
    });
    // Set document language for accessibility and update lang toggle label
    try{ document.documentElement.lang = lang; }catch(e){}
    if(langToggle){
      langToggle.textContent = lang === 'en' ? 'EN' : 'FR';
      langToggle.setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
    }
    try{ localStorage.setItem('site-lang', lang); }catch(e){}
  }

  // Initialize language (default to French unless user has a stored preference)
  try{
    const storedLang = localStorage.getItem('site-lang');
    let initialLang = storedLang || 'fr';
    applyLanguage(initialLang);
  }catch(e){ applyLanguage('fr'); }

  if(langToggle){
    langToggle.addEventListener('click', ()=>{
      const current = (localStorage.getItem('site-lang') === 'en') ? 'en' : 'fr';
      const next = current === 'en' ? 'fr' : 'en';
      applyLanguage(next);
    });
  }

  // Sync language across tabs/windows
  window.addEventListener('storage', (ev) => {
    if(ev.key === 'site-lang'){
      const newLang = ev.newValue === 'en' ? 'en' : 'fr';
      applyLanguage(newLang);
    }
  });

  // Initialize theme from localStorage; default to light if none
  try{
    const stored = localStorage.getItem('site-theme');
    if(stored){ applyTheme(stored); }
    else { applyTheme('light'); }
  }catch(e){ /* ignore */ }

  if(themeToggle){
    themeToggle.addEventListener('click', ()=>{
      const current = root.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
      const next = current === 'light' ? 'dark' : 'light';
      applyTheme(next);
    });
  }

  // Sync theme across tabs/windows: listen for storage changes
  window.addEventListener('storage', (ev) => {
    if(ev.key === 'site-theme'){
      const newTheme = ev.newValue === 'light' ? 'light' : 'dark';
      applyTheme(newTheme);
    }
  });
});
