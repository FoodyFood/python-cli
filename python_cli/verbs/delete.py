from subprocess import call


def delete_server(args):
    print(f'Deleting server owned by: {args.user_name}')
    
def delete_bucket(args):
    print(f'Deleting bucket: {args.bucket_name}')
    print(f'Deleted by:      {args.user_name}')
    