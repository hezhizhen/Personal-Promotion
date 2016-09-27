function areyouhappy
    brew update; and brew upgrade; and brew cleanup; and brew doctor # brew更新、升级、清理、检查
    pip list --outdated | sed 's/(.*//g' | xargs -n1 pip install -U # pip自动更新
end
