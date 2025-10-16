from pathlib import Path
import os
from invoke import task
import shutil

@task
def build(c, serve: bool=True):
    cmd = "npx quartz build --output=docs"
    if serve:
        c.run(f'''
           {cmd} --serve &
        sleep 3 && open http://localhost:8080
              ''')
    else:
        c.run(cmd)

@task
def pub(c, fresh: bool=False):
    c.run('''git add . && git commit -m "update" && git push''')
    if fresh:
        c.run('''
            git reset $(git commit-tree "HEAD^{tree}" -m "🎉 A fresh tart")
            git push --force''')
    
@task
def snapshot(c, version: str):
    c.run(f"""
    git checkout --orphan {version}-snapshot
    git add -all; git commit -m "Snapshot {version}"
    git push --set-upstream origin {version}-snapshot
    git checkout master""")

