# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Theming for Qtile

from os import path
import subprocess
import json

from settings.path import qtile_path


def load_theme():
    theme = "dark-grey"

    config = path.join(qtile_path, "config.json")
    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            f.write(f'{{"theme": "{theme}"}}\n')


    theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


def fixer():

    command = 'ip addr'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()

    a = str(output[0])
    b = ''.join(a)
    c = b.split('\\n')

    print(c[6][3:24])
    if c[6][3:24] == 'enp13s0f1: <BROADCAST':
        return 'enp13s0f1' # nmcli
    else:
        return 'wlp12s0' # nmcli


if __name__ == "settings.theme":
    colors = load_theme()
