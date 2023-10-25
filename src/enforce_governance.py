import os

rule = os.environ.get('INPUT_RULE')

print(f'::set-output name=text::{rule}')