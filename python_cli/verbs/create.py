from subprocess import call
from pathlib import Path


def create_server(args):
    print(f'Creating server for: {args.user_name}')
    
def create_bucket(args):
    print(f'Create bucket: {args.bucket_name}')
    print(f'Created by:    {args.user_name}')

    # Accessing a template or a file is done like this, they files get packaged with the WHL
    # see options.package_data in setup.cfg to include files. The reason we need to calculate
    # its path after the install is because we don't know where it is installed
    current_path = Path(__file__).parent.parent.absolute()
    with open(f"{current_path}/templates/bucket.yaml", 'r') as f:
        print(f.read())

   