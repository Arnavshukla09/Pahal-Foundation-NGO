# Pahal Foundation VITB

Welcome to the official repository for the **Pahal Foundation VITB** web application. This platform is a modern, comprehensive tool designed to support the foundation's mission of empowering underprivileged students—particularly the children of workers at VIT Bhopal—by providing educational resources, managing operations, and fostering a community of support.

**Live Website**: [pahal-foundation-ngo.vercel.app](https://pahal-foundation-ngo.vercel.app/)

## 🌟 About the Foundation

Pahal Foundation is a non-profit organization committed to empowering underprivileged students. We believe every child deserves access to education. Together, we nurture dreams and build brighter futures through digital literacy workshops, scholarship funds, community awareness events, and daily schooling.

This web application serves as our digital headquarters—handling everything from public engagement and donations to internal volunteer and student management.

## 🚀 Key Features

### Public Portal
- **Modern Landing Page:** A welcoming interface featuring our mission statement, real-time statistics, and our upcoming events.
- **Secure Donations:** A dedicated donation portal designed to facilitate secure online contributions to our causes.
- **Community Forum:** A public-facing blog/forum where educators, volunteers, and admins can publish updates, share thoughts, and engage with the community.
- **Volunteer Registration:** A seamless onboarding form for passionate individuals to join our movement.

### Internal Dashboard (Role-Based Access)
- **Teacher Portal:** A tailored, secure dashboard for educators to manage their assigned students, take daily attendance, and contribute to the community forum.
- **Admin Management:** Full access to site settings, encompassing volunteer tracking, student admissions, and complete database oversight.
- **Student Information System:** Centralized tracking of enrolled students, their attendance records, and educational progress.

## 🛠️ Technology Stack

Our platform is built to be fast, scalable, and responsive:

* **Backend:** Python & Django (providing a robust framework for authentication, routing, and data modeling)
* **Frontend:** HTML5, Vanilla CSS3, & JavaScript (utilizing a modern crimson & white design system with frosted-glass UI elements)
* **Database:** SQLite (Dynamically configured to run in `/tmp` for Vercel's serverless environment)
* **Deployment:** Vercel (CI/CD connected directly to GitHub)
* **Design Aesthetics:** Animate.css for micro-interactions, FontAwesome for iconography, and Google Fonts (Inter & Outfit) for premium typography.

## 📂 Project Structure

The project is structured entirely within Django, separated into two core apps:
- `pahal`: Manages public-facing views (Home, About, Contact, Donate) and secure Authentication (Login, Signup, Password Management).
- `content`: Manages the internal Dashboard, Student/Volunteer data structures, and the Community Forum / Blogs.

```text
Pahal-Foundation-NGO/
├── .env.example
├── .gitignore
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── build_files.sh          # Vercel deployment script
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel serverless routing configuration
└── PahalFoundation/        # Django Root
    ├── db.sqlite3          # Ephemeral SQLite database (for demo purposes)
    ├── manage.py
    ├── seed_demo_data.py   # Script to populate demo data
    ├── PahalFoundation/    # Django Settings
    ├── content/            # Dashboard & Forum App
    └── pahal/              # Public Site & Auth App
```

## 🚀 Deploying to Vercel

This repository is pre-configured for seamless deployment to Vercel.

1. Fork or clone this repository to your GitHub account.
2. Go to [vercel.com](https://vercel.com) → **Add New Project** → Import from GitHub.
3. Select this repository. **Do NOT override the Root Directory** (leave it blank/default).
4. Vercel will automatically detect the `vercel.json` and `build_files.sh` at the root.
5. In the **Environment Variables** section, you may optionally add a `DJANGO_SECRET_KEY` or `DEBUG=False`. 
6. Click **Deploy** ✅.

*Note: Because Vercel uses a read-only filesystem, the application dynamically copies the SQLite database into Vercel's temporary writable `/tmp` folder upon initialization. This means the deployment functions as a perfect Demo System that resets itself periodically.*

## 🤝 Contributing & Developer

This project is actively maintained. Contributions, bug reports, and feature requests are always welcome! 

**Developer:** Arnav Shukla
- [LinkedIn Profile](https://www.linkedin.com/in/arnav-shukla-19615128a/)

Please read `CODE_OF_CONDUCT.md` for details on our code of conduct.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
