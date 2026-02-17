
# Deploy AlchemyDB Website
# Automates the full pipeline: Database -> JSON -> Build -> Deploy

Write-Host "STARTING ALCHEMYDB DEPLOYMENT SEQUENCE..." -ForegroundColor Cyan

# 1. Check Git Status
$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "Uncommitted changes detected. Committing first..." -ForegroundColor Yellow
    git add .
    git commit -m "Auto-commit before deployment"
    git push origin main
}
else {
    Write-Host "Git is clean." -ForegroundColor Green
}

# 2. Export Database
Write-Host "Exporting Database to JSON..." -ForegroundColor Cyan
python scripts/export_lexicon_json.py
if ($LASTEXITCODE -ne 0) { Write-Error "Database export failed!"; exit 1 }

# 3. Build Dashboard
Write-Host "Building Dashboard..." -ForegroundColor Cyan
Set-Location dashboard
npm run build
if ($LASTEXITCODE -ne 0) { Write-Error "Build failed!"; exit 1 }

# 4. Copy Lexicon to Dist
Write-Host "Copying Lexicon to Dist..." -ForegroundColor Cyan
Copy-Item public/lexicon.json dist/lexicon.json -Force

# 5. Deploy to GitHub Pages (Manual Branch Method)
Write-Host "Deploying to GitHub Pages (gh-pages-manual)..." -ForegroundColor Cyan

# Create a temporary deployment folder
$deployDir = "..\temp_deploy"
if (Test-Path $deployDir) { Remove-Item $deployDir -Recurse -Force }
New-Item -ItemType Directory -Path $deployDir | Out-Null

# Copy build artifacts
Copy-Item -Recurse dist\* $deployDir

# Initialize git in temp dir
Set-Location $deployDir
git init
git remote add origin https://github.com/t3dy/AlchemyDB.git
git checkout -b gh-pages-manual
git add .
git commit -m "Deploy AlchemyDB Website $(Get-Date -Format 'yyyy-MM-dd HH:mm')"

# Push to manual branch
git push origin gh-pages-manual --force

# Cleanup
Set-Location ..\dashboard
Remove-Item $deployDir -Recurse -Force
Set-Location ..

Write-Host "DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "Live URL: https://t3dy.github.io/AlchemyDB/" -ForegroundColor Green
Write-Host "Don't forget to clear your browser cache!" -ForegroundColor Yellow
