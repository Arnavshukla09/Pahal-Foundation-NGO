# Pahal Foundation QA Testing Report

Based on a thorough review of the live application and a static analysis of the codebase, I have compiled this Quality Assurance (QA) report. It highlights what is working well, functional bugs, and opportunities for UX improvement.

## 1. Functional Testing & Bugs

> [!WARNING]
> **Access Denied on Teacher Blog Creation**
> The most critical issue currently affecting the Teacher Dashboard.
> - **Issue**: When logged in as a Teacher, attempting to access `/dashboard/create_blog/` or `/dashboard/my_blogs/` results in an "Access Denied" page.
> - **Root Cause**: In `content/views_teacher.py`, both of these views are wrapped in the `@allowed_users(allowed_roles=['admin'])` decorator. This locks out standard users/teachers from creating blogs.
> - **Fix**: Update the decorator to `@allowed_users(allowed_roles=['admin', 'teacher'])` (or similar, depending on your exact group names) or remove the restriction to allow any authenticated user to create a blog post.

> [!CAUTION]
> **Database Limitations on Vercel**
> - **Issue**: Vercel is a serverless environment with a read-only filesystem. While we successfully implemented a `/tmp/db.sqlite3` workaround so the site doesn't crash on login, any data created by users (new blogs, attendance records) **will be wiped out** whenever Vercel spins down the serverless function (usually after a period of inactivity).
> - **Recommendation**: If you want data to persist permanently (e.g., actual student attendance, permanent blog posts), you must connect to an external database like Neon (Postgres) or Aiven/PlanetScale (MySQL). The current SQLite `/tmp` setup is only suitable as a **Demo System**.

## 2. Visual & UX Observations

> [!NOTE]
> **Login / Signup Portal Transition**
> - **Observation**: We recently reverted the Login, Signup, and Change Password pages back to their original standalone designs (with the dark, blurred background and orange buttons).
> - **Feedback**: While this design looks great on its own, it creates a slight visual disconnect from the main website, which uses a bright crimson and white color scheme. 
> - **Open to Change**: If you'd like, we can create a *new* set of CSS specifically tailored to seamlessly blend the frosted-glass login boxes with the crimson main-website layout, rather than keeping them entirely standalone.

> [!TIP]
> **Forum "Back" Button Behavior**
> - **Observation**: The Forum and Blog pages now have a simple red header with a `<- Back` button powered by `javascript:history.back()`. 
> - **Feedback**: If a user is sent a direct link to a blog post (e.g., from WhatsApp or LinkedIn) and clicks "Back", it will take them out of your website entirely (back to LinkedIn/WhatsApp) instead of taking them to the main Forum page.
> - **Fix**: Change the button logic. If on a specific blog post, the "Back" button should explicitly link to `/blogs/`. If on the main Forum page, it should explicitly link to `/`.

> [!NOTE]
> **Dead Links (Videos & Gallery)**
> - **Observation**: In the main navigation bar, the links for **Videos** and **Gallery** currently point directly to `/error404`. 
> - **Open to Change**: It is better UX to either hide these links entirely until the pages are built, or route them to a "Coming Soon" page rather than a 404 Error page, which implies something is broken.

## 3. Summary of Suggested Actions

If you approve, I can immediately execute the following fixes:
1. **Fix the Access Denied bug** in `views_teacher.py` so teachers can actually write blogs.
2. **Update the Forum Back Button** to route securely rather than using browser history.
3. **Hide the Videos/Gallery links** from the navbar until those features are ready.

Let me know which of these you would like me to tackle first!
