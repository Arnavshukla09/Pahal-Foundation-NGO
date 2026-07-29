# Pahal Foundation NGO Web Application ✨

Welcome to the official repository for the Pahal Foundation's web application. This platform is a comprehensive tool designed to support the foundation's mission of empowering underprivileged students by providing educational resources, managing operations, and fostering a community of support.

Website link - [pahal-foundation-ngo.vercel.app](https://pahal-foundation-ngo-git-master-arnavshukla0925-2353s-projects.vercel.app)

## 🌟 About

Pahal Foundation is a non-profit organization committed to empowering underprivileged students, particularly the children of workers at VIT Bhopal. Our mission is to provide quality education and ensure their well-being through various initiatives. This web application serves as a central hub for our activities, helping us manage our programs, connect with volunteers, and engage with our community.

## 🚀 Key Features

-   **Homepage:** A welcoming landing page with an image slider, mission statement, and key statistics to showcase our impact.
-   **User Authentication:** Secure login and registration system for staff and administrators.
-   **Donation Portal:** Integrated with Razorpay for seamless and secure online donations.
-   **Content Management:**
    -   **Blog/Forum:** A platform for teachers and admins to create, edit, and publish articles. Includes a rich text editor and a commenting system for community engagement.
-   **Student Management System:**
    -   **Admissions:** An easy-to-use form for enrolling new students.
    -   **Student Database:** A central place to view and manage detailed student information.
    -   **Attendance Tracking:** Functionality for teachers to take and record daily attendance.
-   **Volunteer Management:**
    -   **Enrollment:** A dedicated form for new volunteers to register and join our cause.
    -   **Volunteer Database:** A directory of all volunteers and their information.
-   **Role-Based Access Control:**
    -   **Admin Dashboard:** Provides full access to all management features, including student and volunteer data, content management, and site settings.
    -   **Teacher Dashboard:** A tailored dashboard for teachers to manage their students, take attendance, and contribute to the blog.
-   **Responsive Design:** Ensures a seamless experience across desktops, tablets, and mobile devices.

## 🖼️ Screenshots

| Homepage | Volunteer Page |
| :---: |:---:|
| ![Homepage](screenshots/Screenshot%20(33).png) | ![Volunteer page](screenshots/Screenshot%20(35).png) |
| **Donation Page** | **Dashboard** |
| ![Donation page](screenshots/Screenshot%20(36).png) | ![Dashboard](screenshots/Screenshot%20(37).png) |

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (Configured to run in `/tmp` for Vercel's Serverless environment)
* **File Storage:** AWS S3 for media files (Optional/Configurable)
* **Payment Gateway:** RazorPay (Optional/Configurable)
* **Deployment:** Git, GitHub, **Vercel**

## 📂 Project Structure

The project is organized into two main Django apps: `pahal` for the public-facing site and user authentication, and `content` for the internal dashboard and content management.

```
Pahal-Foundation-NGO/
├── .env.example
├── .gitignore
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── build_files.sh
├── requirements.txt
├── vercel.json
├── screenshots/
└── PahalFoundation/
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── seed_demo_data.py
    ├── PahalFoundation/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── content/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── forms.py
    │   ├── static/content/
    │   └── templates/content/
    └── pahal/
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── static/pahal/
        └── templates/pahal/
```

## 🚀 Deploying to Vercel

1. Fork / clone this repository
2. Go to [vercel.com](https://vercel.com) → New Project → Import from GitHub
3. Select this repository and do NOT override the Root Directory (keep it as default)
4. Add the following **Environment Variables** in Vercel project settings (optional depending on your setup):

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` |
| `AWS_ACCESS_KEY_ID` | AWS S3 access key (optional) |
| `AWS_SECRET_ACCESS_KEY` | AWS S3 secret key (optional) |
| `AWS_STORAGE_BUCKET_NAME` | S3 bucket name (optional) |
| `RAZORPAY_API_KEY` | Razorpay key (optional) |
| `RAZORPAY_API_SECRET` | Razorpay secret (optional) |

5. Click **Deploy** ✅

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please read `CODE_OF_CONDUCT.md` for details on our code of conduct and the process for submitting pull requests to us.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
