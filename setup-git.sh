# when you initialize into alfred, you don't have git
# use this script to initialize git with the correct upstream
# this script will attempt to preserve changes
git init
git commit --allow-empty -m 'initial commit'
git remote add origin git@github.com:mxbaylee/email-generator.git
git fetch origin
git reset --hard origin/main
