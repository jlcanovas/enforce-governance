import os

rule = os.environ.get('INPUT_RULE')

print(f'::set-output name=rule::{rule}')