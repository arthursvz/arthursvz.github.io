document.addEventListener('DOMContentLoaded',function(){
  // Nav toggle (for small screens)
  const nav=document.getElementById('siteNav');
  const btn=document.getElementById('navToggle');
  if(btn && nav){
    btn.addEventListener('click',()=>{
      nav.classList.toggle('open');
    });
  }

  // Highlight the current page in the nav
  if(nav){
    const here = window.location.pathname.replace(/\/index\.html$/,'/').replace(/\/$/,'/');
    nav.querySelectorAll('a[href$=".html"]').forEach(a=>{
      const target = new URL(a.getAttribute('href'), window.location.href).pathname
        .replace(/\/index\.html$/,'/').replace(/\/$/,'/');
      if(target === here){ a.classList.add('active'); }
    });
  }

  // Theme toggle (light/dark) with persistence
  const themeToggle = document.getElementById('themeToggle');
  const root = document.documentElement;

  // Language toggle (FR/EN)
  const langToggle = document.getElementById('langToggle');

  const sunIcon = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>';
  const moonIcon = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';

  function applyTheme(theme){
    if(theme === 'light'){
      root.setAttribute('data-theme','light');
      if(themeToggle){ themeToggle.innerHTML = sunIcon; themeToggle.setAttribute('aria-pressed','true'); }
    } else {
      root.removeAttribute('data-theme');
      if(themeToggle){ themeToggle.innerHTML = moonIcon; themeToggle.setAttribute('aria-pressed','false'); }
    }
    try{ localStorage.setItem('site-theme', theme); }catch(e){}
  }

  // --- Internationalization ---
  const translations = {
    fr: {
      nav_home: 'Accueil', nav_cv: 'CV', nav_projects: 'Projets', nav_parcours: 'Parcours', nav_contact: 'Contact',
      hero_title: 'Étudiant Ingénieur N7 (3A) — Réseaux et Télécommunications',
      hero_lead: "Actuellement en 3e année à l'ENSEEIHT, en semestre d'échange à l'Université Laval (Québec) : gestion de projet, gouvernance de la sécurité, réseaux mobiles, applications cloud & DevOps. Passionné par l'aéronautique, le spatial et la cybersécurité.",
      btn_cv: 'Voir le CV', btn_contact: 'Me contacter',
      about_title: 'À propos', about_text: "Actuellement étudiant en 3e année d'ingénierie numérique à l'ENSEEIHT, en échange académique à l'Université Laval, je suis passionné par l'aéronautique, le spatial et la cybersécurité. Mon parcours académique combiné à mes engagements associatifs et secourisme montre ma capacité à travailler en équipe et à gérer des responsabilités dans des environnements exigeants. J'aspire à contribuer à des projets innovants en mettant à profit mes compétences en programmation et ma rigueur analytique.",
      formation_title: 'Formation', skills_title: 'Compétences', projects_title: 'Projets & stages',
      cv_title: 'Curriculum Vitae — Arthur Sauvezie', cv_role: 'Étudiant Ingénieur N7', cv_domain: 'Informatique & Télécommunications',
      btn_download_cv: 'Télécharger le CV (PDF)', btn_open_cv: 'Ouvrir dans un nouvel onglet',
      projects_intro: 'Code et démonstrations disponibles sur ',
      projet_irt_title: 'Stage IA / Cybersécurité — IRT Saint-Exupéry', projet_irt_desc: 'Stage de 6 semaines (terminé début août 2025) : travaux de recherche sur les LLM spécialisés en cybersécurité et sur des IDS/IPS basés sur réseaux de neurones. Contribution au projet de détection de pistes d\'atterrissage par IA.', projet_irt_date: '2025',
      projet_net7_title: 'Administrateur Systèmes — Net7 (Asso Info N7)', projet_net7_desc: 'Administrateur systèmes (accès root) : maintenance des serveurs associatifs de Toulouse INP.', projet_net7_date: "09.2025 – Aujourd'hui",
      projet_prefecture_title: 'Stage Services Informatiques — Préfecture de Haute-Garonne', projet_prefecture_desc: 'Stage de 11 semaines (juin – mi-août 2026) au sein des services informatiques de la Préfecture de Haute-Garonne.', projet_prefecture_date: '2026',
      tag_ml: 'Apprentissage automatique',
      parcours_title: 'Parcours', parcours_intro: 'Résumé chronologique des études et expériences.',
      contact_title: 'Contact', contact_intro: 'Pour toute question ou collaboration, contactez‑moi — je réponds généralement sous 48h.',
      label_name: 'Nom :', label_phone: 'Téléphone :', label_phone_value: 'disponible sur le CV', label_email: 'Email :', label_email_value: 'arthur.sauvezie [insert at] etu.inp-n7.fr', label_location: 'Localisation :', label_location_value: 'Toulouse, France - De préférence en région Toulousaine, mais disponible sur tout le territoire',
      footer_contact: 'Contact'
    },
    en: {
      nav_home: 'Home', nav_cv: 'CV', nav_projects: 'Projects', nav_parcours: 'Path', nav_contact: 'Contact',
      hero_title: 'Engineering Student N7 (Final Year) — Networks & Telecommunications',
      hero_lead: "Currently in my final year at ENSEEIHT, on academic exchange at Université Laval (Québec): project management, security governance, mobile networks, cloud applications & DevOps. Passionate about aeronautics, space and cybersecurity.",
      btn_cv: 'View CV', btn_contact: 'Contact me',
      about_title: 'About', about_text: "Currently in my final year of digital engineering at ENSEEIHT, on academic exchange at Université Laval, I am passionate about aeronautics, space and cybersecurity. My academic background combined with my associative and first-aid commitments demonstrates my ability to work in teams and handle responsibilities in demanding environments. I aspire to contribute to innovative projects by applying my programming skills and analytical rigor.",
      formation_title: 'Education', skills_title: 'Skills', projects_title: 'Projects & internships',
      cv_title: 'Curriculum Vitae — Arthur Sauvezie', cv_role: 'Engineering Student N7', cv_domain: 'Computer Networks & Telecommunications',
      btn_download_cv: 'Download CV (PDF)', btn_open_cv: 'Open in new tab',
      projects_intro: 'Code and demos available on ',
      projet_irt_title: 'AI / Cybersecurity Internship — IRT Saint-Exupéry', projet_irt_desc: '6-week internship (ended early August 2025): research work on LLMs specialized in cybersecurity and on IDS/IPS based on neural networks. Contribution to runway detection by AI.', projet_irt_date: '2025',
      projet_net7_title: 'Systems Administrator — Net7 (Asso Info N7)', projet_net7_desc: 'Systems administrator (root access): maintaining Toulouse INP associative servers.', projet_net7_date: '09.2025 – Present',
      projet_prefecture_title: 'IT Department Internship — Préfecture de Haute-Garonne', projet_prefecture_desc: '11-week internship (June – mid-August 2026) in the IT department of the Préfecture de Haute-Garonne.', projet_prefecture_date: '2026',
      tag_ml: 'Machine learning',
      parcours_title: 'Background', parcours_intro: 'Chronological summary of studies and experiences.',
      contact_title: 'Contact', contact_intro: 'For questions or collaboration, please contact me — I usually reply within 48h.',
      label_name: 'Name:', label_phone: 'Phone:', label_phone_value: 'available on the CV', label_email: 'Email:', label_email_value: 'arthur.sauvezie [insert at] etu.inp-n7.fr', label_location: 'Location:', label_location_value: 'Toulouse, France - Preferably in the Toulouse area, but available nationwide',
      footer_contact: 'Contact'
    }
  };

  // Extra translation keys for index content
  translations.fr.formation_content = "<p><strong>ENSEEIHT — 3A</strong><br>Semestre d'échange — Université Laval (Québec)<br>(2026 – Aujourd'hui)</p><p><strong>ENSEEIHT — 2A, Computer Networks</strong><br>2025–2026</p><p><strong>CPGE - PCSI/PSI</strong><br>Lycée Bellevue, Toulouse, 2022–2024</p><p><strong>BAC Général</strong><br>Maths, Physiques, Maths Expertes<br>Lycée Léonard Limosin, 2019–2022</p>";
  translations.en.formation_content = "<p><strong>ENSEEIHT — Final Year</strong><br>Exchange semester — Université Laval (Québec)<br>(2026 – Present)</p><p><strong>ENSEEIHT — 2nd Year, Computer Networks</strong><br>2025–2026</p><p><strong>CPGE - PCSI/PSI</strong><br>Lycée Bellevue, Toulouse, 2022–2024</p><p><strong>BAC Général</strong><br>Advanced Mathematics, Physics<br>Lycée Léonard Limosin, 2019–2022</p>";

  translations.fr.skill_1 = 'Python, Java, C, Matlab, <br> HTML, CSS, Ada, LaTeX';
  translations.en.skill_1 = 'Python, Java, C, Matlab, <br> HTML, CSS, Ada, LaTeX';
  translations.fr.skill_2 = 'Linux, Git, VSCode <br> Autres outils de bureautique';
  translations.en.skill_2 = 'Linux, Git, VSCode <br> Other office tools';
  translations.fr.skill_3 = 'Organisation, travail en équipe, <br> gestion de la pression';
  translations.en.skill_3 = 'Organization, teamwork, <br> stress management';
  translations.fr.skill_3a = 'Travail en équipe'; translations.en.skill_3a = 'Teamwork';
  translations.fr.skill_3b = 'Gestion de la pression'; translations.en.skill_3b = 'Stress management';

  translations.fr.hero_eyebrow = 'Toulouse, France'; translations.en.hero_eyebrow = 'Toulouse, France';
  translations.fr.fact_1 = 'ENSEEIHT — 3e année'; translations.en.fact_1 = 'ENSEEIHT — Final Year';
  translations.fr.fact_2 = 'Échange — Université Laval'; translations.en.fact_2 = 'Exchange — Université Laval';
  translations.fr.fact_3 = 'Réseaux & Cybersécurité'; translations.en.fact_3 = 'Networks & Cybersecurity';

  translations.fr.about_eyebrow = 'Qui suis-je'; translations.en.about_eyebrow = 'About me';
  translations.fr.overview_eyebrow = 'En bref'; translations.en.overview_eyebrow = 'At a glance';
  translations.fr.overview_title = 'Formation, compétences & expériences';
  translations.en.overview_title = 'Education, skills & experience';

  translations.fr.projects_eyebrow = 'Réalisations'; translations.en.projects_eyebrow = 'Work';
  translations.fr.cv_eyebrow = 'Profil'; translations.en.cv_eyebrow = 'Profile';
  translations.fr.parcours_eyebrow = 'Chronologie'; translations.en.parcours_eyebrow = 'Timeline';
  translations.fr.contact_eyebrow = 'Me contacter'; translations.en.contact_eyebrow = 'Get in touch';

  translations.fr.project_item_0 = 'Stage Services Informatiques — Préfecture de Haute-Garonne (2026)';
  translations.en.project_item_0 = 'IT Department Internship — Préfecture de Haute-Garonne (2026)';
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

  translations.fr.edu_0 = '3e Année — ENSEEIHT (2026 – Aujourd\'hui)';
  translations.en.edu_0 = 'Final Year — ENSEEIHT (2026 – Present)';
  translations.fr.edu_0b = 'Semestre d\'échange académique — Université Laval, Québec (Automne 2026) : gestion de projet, gouvernance de la sécurité, réseaux mobiles, applications cloud & DevOps, IHM';
  translations.en.edu_0b = 'Academic exchange semester — Université Laval, Québec (Fall 2026): project management, security governance, mobile networks, cloud applications & DevOps, HCI';
  translations.fr.edu_1 = 'Seconde Année, Computer Networks — ENSEEIHT (2025 – 2026)';
  translations.en.edu_1 = 'Second year, Computer Networks — ENSEEIHT (2025 – 2026)';
  translations.fr.edu_2 = 'CPGE — PCSI / PSI — Lycée Bellevue, Toulouse (2022–2024)';
  translations.en.edu_2 = 'Preparatory Classes — PCSI / PSI — Lycée Bellevue, Toulouse (2022–2024)';
  translations.fr.edu_3 = 'BAC Général, Maths Expertes — Lycée Léonard Limosin, Limoges (2019–2022)';
  translations.en.edu_3 = 'General Baccalaureate, Advanced Mathematics — Lycée Léonard Limosin, Limoges (2019–2022)';

  translations.fr.cv_experiences_title = 'Expériences & stages';
  translations.en.cv_experiences_title = 'Experiences & Internships';
  translations.fr.exp_0 = 'Stage Services Informatiques — Préfecture de Haute-Garonne, juin – mi-août 2026 (11 semaines)';
  translations.en.exp_0 = 'IT Department Internship — Préfecture de Haute-Garonne, June – mid-August 2026 (11 weeks)';
  translations.fr.exp_1 = 'Stage IA / Cybersécurité — IRT Saint-Exupéry (Projets CSS / DEEL), terminé début août 2025 — LLMs spécialisés cyber, IDS/IPS par réseaux de neurones';
  translations.en.exp_1 = 'AI / Cybersecurity Internship — IRT Saint-Exupéry (Projects CSS / DEEL), ended early August 2025 — LLMs specialized in cyber, IDS/IPS using neural networks';
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

  translations.fr.tag_networks = 'Réseaux'; translations.en.tag_networks = 'Networks';
  translations.fr.tag_cybersecurity = 'Cybersécurité'; translations.en.tag_cybersecurity = 'Cybersecurity';
  translations.fr.tag_databases = 'Bases de données'; translations.en.tag_databases = 'Databases';
  translations.fr.tag_organisation = 'Organisation'; translations.en.tag_organisation = 'Organization';
  translations.fr.tag_teamwork = 'Travail en équipe'; translations.en.tag_teamwork = 'Teamwork';
  translations.fr.tag_pressure = 'Gestion de la pression'; translations.en.tag_pressure = 'Stress management';
  translations.fr.tag_leadership = "Encadrement (club d'escalade)"; translations.en.tag_leadership = 'Leadership (climbing club)';

  translations.fr.cv_engagements_title = 'Engagements';
  translations.en.cv_engagements_title = 'Engagements';
  translations.fr.eng_1 = 'Ancien membre du Bureau Women7 — INP-ENSEEIHT (09.2025 – 2026, mandat terminé)';
  translations.en.eng_1 = 'Former member of the Women7 board — INP-ENSEEIHT (09.2025 – 2026, term ended)';
  translations.fr.eng_2 = 'Président du Club d\'Escalade — AS Toulouse INP (2024 – aujourd\'hui, mandat renouvelé) — Initiateur SAE FFME';
  translations.en.eng_2 = 'President of the Climbing Club — AS Toulouse INP (2024 – present, term renewed) — FFME SAE Instructor';
  translations.fr.eng_3 = 'Délégué au Conseil d\'Etude et de Vie Etudiante — INP-ENSEEIHT (2024–2025, renouvellement en attente)';
  translations.en.eng_3 = 'Delegate to the Study and Student Life Council — INP-ENSEEIHT (2024–2025, renewal pending)';
  translations.fr.eng_4 = 'Représentant Etudiant pour la constitution du dossier d\'accréditation à la CTI';
  translations.en.eng_4 = 'Student representative for the CTI accreditation file';
  translations.fr.eng_5 = 'Représentant Etudiant au comité de réflexion autour de la fraude de Toulouse INP';
  translations.en.eng_5 = 'Student representative on Toulouse INP\'s academic integrity committee';
  translations.fr.eng_6 = 'Équipier Secouriste, chef d\'équipe / chef de poste, gardes SAMU — Protection Civile de Haute Garonne (09.2024 – Aujourd\'hui)';
  translations.en.eng_6 = 'First responder team member, team/post leader, SAMU shifts — Protection Civile de Haute Garonne (09.2024 – Present)';

  translations.fr.cv_edu_0_date = "2026 – Aujourd'hui";
  translations.en.cv_edu_0_date = '2026 – Present';
  translations.fr.cv_edu_0_text = "ENSEEIHT — 3A, semestre d'échange à l'Université Laval (Québec) : gestion de projet, gouvernance de la sécurité, réseaux mobiles, applications cloud & DevOps, IHM";
  translations.en.cv_edu_0_text = 'ENSEEIHT — Final Year, exchange semester at Université Laval (Québec): project management, security governance, mobile networks, cloud applications & DevOps, HCI';

  translations.fr.cv_edu_1_date = '2025 – 2026'; translations.en.cv_edu_1_date = '2025 – 2026';
  translations.fr.cv_edu_1_text = 'ENSEEIHT — 2A, Computer Networks'; translations.en.cv_edu_1_text = 'ENSEEIHT — 2nd Year, Computer Networks';

  translations.fr.cv_edu_2_date = '2022 – 2024'; translations.en.cv_edu_2_date = '2022 – 2024';
  translations.fr.cv_edu_2_text = 'CPGE — PCSI / PSI, Lycée Bellevue, Toulouse'; translations.en.cv_edu_2_text = 'Preparatory Classes — PCSI / PSI, Lycée Bellevue, Toulouse';

  translations.fr.cv_edu_3_date = '2019 – 2022'; translations.en.cv_edu_3_date = '2019 – 2022';
  translations.fr.cv_edu_3_text = 'BAC Général, Maths Expertes — Lycée Léonard Limosin, Limoges';
  translations.en.cv_edu_3_text = 'General Baccalaureate, Advanced Mathematics — Lycée Léonard Limosin, Limoges';

  translations.fr.cv_exp_0_date = '2026'; translations.en.cv_exp_0_date = '2026';
  translations.fr.cv_exp_0_title = 'Stage Services Informatiques — Préfecture de Haute-Garonne';
  translations.en.cv_exp_0_title = 'IT Department Internship — Préfecture de Haute-Garonne';
  translations.fr.cv_exp_0_desc = '11 semaines (juin – mi-août 2026)';
  translations.en.cv_exp_0_desc = '11 weeks (June – mid-August 2026)';

  translations.fr.cv_exp_2_date = "09.2025 – Aujourd'hui"; translations.en.cv_exp_2_date = '09.2025 – Present';
  translations.fr.cv_exp_2_title = 'Administrateur Systèmes — Net7 (Asso Info N7)';
  translations.en.cv_exp_2_title = 'Systems Administrator — Net7 (Asso Info N7)';
  translations.fr.cv_exp_2_desc = 'Accès root, maintenance des serveurs associatifs de Toulouse INP';
  translations.en.cv_exp_2_desc = 'Root access, maintaining Toulouse INP associative servers';

  translations.fr.cv_exp_1_date = '2025'; translations.en.cv_exp_1_date = '2025';
  translations.fr.cv_exp_1_title = 'Stage IA / Cybersécurité — IRT Saint-Exupéry';
  translations.en.cv_exp_1_title = 'AI / Cybersecurity Internship — IRT Saint-Exupéry';
  translations.fr.cv_exp_1_desc = 'Projets CSS / DEEL — LLMs spécialisés cyber, IDS/IPS par réseaux de neurones (terminé début août 2025)';
  translations.en.cv_exp_1_desc = 'CSS / DEEL projects — LLMs specialized in cyber, IDS/IPS using neural networks (ended early August 2025)';

  translations.fr.footer_text = 'Arthur Sauvezie — Étudiant ENSEEIHT • ';
  translations.en.footer_text = 'Arthur Sauvezie — ENSEEIHT Student • ';

  // Page title for projects
  translations.fr.projects_page_title = 'Projets — Arthur Sauvezie';
  translations.en.projects_page_title = 'Projects — Arthur Sauvezie';

  // Parcours page translations
  translations.fr.parcours_page_title = 'Parcours — Arthur Sauvezie';
  translations.en.parcours_page_title = 'Background — Arthur Sauvezie';

  translations.fr.parcours_item_0_date = "2026 – Aujourd'hui";
  translations.en.parcours_item_0_date = "2026 – Present";
  translations.fr.parcours_item_0_text = "3e Année, ENSEEIHT (échange académique à l'Université Laval, Québec)";
  translations.en.parcours_item_0_text = "Final Year, ENSEEIHT (academic exchange at Université Laval, Québec)";

  translations.fr.parcours_item_prefecture_date = '2026';
  translations.en.parcours_item_prefecture_date = '2026';
  translations.fr.parcours_item_prefecture_text = 'Stage Services Informatiques, Préfecture de Haute-Garonne (juin – mi-août)';
  translations.en.parcours_item_prefecture_text = 'IT Department Internship, Préfecture de Haute-Garonne (June – mid-August)';

  translations.fr.parcours_item_1_date = '2025';
  translations.en.parcours_item_1_date = '2025';
  translations.fr.parcours_item_1_text = 'Stage IA / Cybersécurité, IRT Saint-Exupéry (projets CSS / DEEL), terminé début août';
  translations.en.parcours_item_1_text = 'AI / Cybersecurity Internship, IRT Saint-Exupéry (CSS / DEEL projects), ended early August';

  translations.fr.parcours_item_2_date = "2025 – Aujourd'hui";
  translations.en.parcours_item_2_date = '2025 – Present';
  translations.fr.parcours_item_2_text = 'Administrateur Systèmes, Net7 – Asso Info N7';
  translations.en.parcours_item_2_text = 'Systems Administrator, Net7 – Asso Info N7';

  translations.fr.parcours_item_3_date = '2025 – 2026';
  translations.en.parcours_item_3_date = '2025 – 2026';
  translations.fr.parcours_item_3_text = 'Seconde Année, Computer Networks, ENSEEIHT';
  translations.en.parcours_item_3_text = 'Second Year, Computer Networks, ENSEEIHT';

  translations.fr.parcours_item_4_date = '2022 – 2024';
  translations.en.parcours_item_4_date = '2022 – 2024';
  translations.fr.parcours_item_4_text = 'CPGE (PCSI → PSI), Lycée Bellevue, Toulouse';
  translations.en.parcours_item_4_text = 'Preparatory Classes (PCSI → PSI), Lycée Bellevue, Toulouse';

  translations.fr.parcours_item_5_date = '2019 – 2022';
  translations.en.parcours_item_5_date = '2019 – 2022';
  translations.fr.parcours_item_5_text = 'BAC Général (Maths expertes), Lycée Léonard Limosin, Limoges';
  translations.en.parcours_item_5_text = 'General Baccalaureate (Advanced Mathematics), Lycée Léonard Limosin, Limoges';

  translations.fr.engagements_title = 'Engagements citoyens & durabilité';
  translations.en.engagements_title = 'Civic Engagement & Sustainability';
  translations.fr.engagements_intro = 'Je m\'investis dans des actions de solidarité et d\'éducation, convaincu que l\'ingénieur a un rôle à jouer pour répondre aux défis sociaux et environnementaux.';
  translations.en.engagements_intro = 'I am involved in solidarity and educational actions, convinced that engineers have a role to play in addressing social and environmental challenges.';

  translations.fr.prot_title = 'Protection Civile — Équipier Secouriste';
  translations.en.prot_title = 'Civil Protection — First Responder Team Member';
  translations.fr.prot_desc = 'Volontaire à la Protection Civile de Haute-Garonne (depuis 09.2024), aujourd\'hui Équipier Secouriste : postes de secours, gardes SAMU et chefferie (chef d\'équipe, chef de poste). Cette expérience m\'a permis de développer des compétences en intervention d\'urgence, en encadrement d\'équipe et en gestion du stress, et renforce mon engagement pour la sécurité civile.';
  translations.en.prot_desc = 'Volunteer at the Haute-Garonne Civil Protection (since 09.2024), now a First Responder Team Member: first aid posts, SAMU shifts and team/post leadership. This experience helped me develop emergency response, team leadership and stress management skills, and strengthens my commitment to civil safety.';
  translations.fr.prot_link = 'En savoir plus sur la Protection Civile';
  translations.en.prot_link = 'Learn more about Civil Protection';

  translations.fr.eedf_title = 'Eclaireuses & Eclaireurs de France (EEDF) — Encadrement jeunesse (activité terminée)';
  translations.en.eedf_title = 'Eclaireuses & Eclaireurs de France (EEDF) — Youth Leadership (past activity)';
  translations.fr.eedf_desc = 'Ancien leader bénévole au sein des EEDF : accompagnement et encadrement d\'activités de plein air et de projets éducatifs pour les jeunes. Ce rôle m\'a permis d\'acquérir des compétences pédagogiques et d\'organisation, ainsi qu\'un sens renforcé de la responsabilité civique.';
  translations.en.eedf_desc = 'Former volunteer leader with EEDF: supporting and leading outdoor activities and educational projects for youth. This role allowed me to gain pedagogical and organizational skills, and a strong sense of civic responsibility.';
  translations.fr.eedf_link = 'En savoir plus sur les EEDF';
  translations.en.eedf_link = 'Learn more about EEDF';

  translations.fr.activities_title = 'Sports & autres activités';
  translations.en.activities_title = 'Sports & Other Activities';
  translations.fr.activities_intro = 'En parallèle de mes études, je suis très impliqué dans des activités sportives et culturelles qui complètent ma formation :';
  translations.en.activities_intro = 'Alongside my studies, I am actively involved in sports and cultural activities that complement my training:';

  translations.fr.climbing_title = 'Escalade — Président du club';
  translations.en.climbing_title = 'Climbing — Club President';
  translations.fr.climbing_desc = 'Je pratique régulièrement l\'escalade et je préside le club d\'escalade de l\'école (GrINP / AS Toulouse INP), mandat renouvelé. Titulaire du Brevet Fédéral Initiateur SAE (Structures Artificielles d\'Escalade) de la FFME, ce qui me permet d\'encadrer en toute sécurité et de partager cette passion.';
  translations.en.climbing_desc = 'I regularly practice climbing and preside over the school climbing club (GrINP / AS Toulouse INP), with a renewed term. I hold the FFME Federal Instructor Certificate for artificial structures (SAE), which allows me to safely supervise and share this passion.';
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
