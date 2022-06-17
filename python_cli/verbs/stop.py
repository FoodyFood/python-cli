from subprocess import call


def stop_server(args):
    print(f'Stopping:  {args.server_name}')
    print(f'Message:   {args.message}')
    