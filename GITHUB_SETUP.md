# How to Push to GitHub

## Step 1: Initialize Git Repository (if not already done)

Open PowerShell or Git Bash in your project directory and run:

```bash
cd "z:\Cursor Projects\InsideAirbnbAnalysis"
git init
```

## Step 2: Add All Files

```bash
git add .
```

This will add all files except those in `.gitignore` (like `venv/`, CSV files, etc.)

## Step 3: Make Your First Commit

```bash
git commit -m "Initial commit: Inside Airbnb Analysis project"
```

## Step 4: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **+** icon in the top right → **New repository**
3. Name it (e.g., `InsideAirbnbAnalysis`)
4. **Don't** initialize with README, .gitignore, or license (you already have these)
5. Click **Create repository**

## Step 5: Connect Local Repository to GitHub

GitHub will show you commands. Use the "push an existing repository" option:

```bash
git remote add origin https://github.com/YOUR_USERNAME/InsideAirbnbAnalysis.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 6: Verify

Refresh your GitHub repository page - you should see all your files!

---

## What Gets Pushed?

Based on your `.gitignore`, these will **NOT** be pushed:
- ✅ `venv/` (virtual environment)
- ✅ `*.csv` files (data files - too large)
- ✅ `__pycache__/` (Python cache)
- ✅ `.ipynb_checkpoints/` (Jupyter checkpoints)
- ✅ `*.egg-info/` (package metadata)

These **WILL** be pushed:
- ✅ All source code (`src/inside_airbnb/`)
- ✅ Notebooks (`notebooks/`)
- ✅ `setup.py`, `requirements.txt`
- ✅ `README.md`
- ✅ `.gitignore`
- ✅ Project structure files

---

## Future Updates

After making changes:

```bash
git add .
git commit -m "Description of your changes"
git push
```

---

## Troubleshooting

### If git is not recognized:
- Install Git from: https://git-scm.com/download/win
- Or use GitHub Desktop: https://desktop.github.com/

### If you need to update .gitignore:
Edit `.gitignore`, then:
```bash
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
```

### Authentication Issues:
- GitHub now requires a Personal Access Token instead of password
- Generate one at: https://github.com/settings/tokens
- Use the token as your password when pushing
