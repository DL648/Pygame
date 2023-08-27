#!/bin/bash

# 指定远程仓库的 URL 和分支
remote_url="git@github.com:DL648/Pygame.git"
branch="master"

# 添加需要提交的文件或目录
git add .

# 提交并添加提交信息
read -p "提交信息: " commit_msg
git commit -m "$commit_msg"

# 推送到远程仓库
git push $remote_url $branch