rsync -avuz -e ssh --safe-links \
--exclude ".git" --exclude ".*.sw*" \
./ llimllib@billmill.org:~/static/pixastic
