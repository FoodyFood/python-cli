import argparse
import logging
import sys
from .verbs import create_server, create_bucket, delete_server, delete_bucket, start_server, stop_server

def main():
    print("Python CLI - Version 1.0 - FoodyFood")
    print("")

    if not len(sys.argv) > 1:
        print("Please try 'python_cli --help' to see available commands")
        exit()


    parser = argparse.ArgumentParser(description="This Python CLI is a template created by FoodyFood")


    # The first argument parsed is the VERB - i.e. "python_cli create ..."
    verb_subparsers = parser.add_subparsers()
    create_parser   = verb_subparsers.add_parser('create', help='Create a resource')
    delete_parser   = verb_subparsers.add_parser('delete', help='Delete a resource')
    start_parser     = verb_subparsers.add_parser('start', help='Start a server')
    stop_parser     = verb_subparsers.add_parser('stop', help='Stop a server')
 

    # Subparsers within the create verb
    create_subparsers = create_parser.add_subparsers()
    create_server_parser   = create_subparsers.add_parser('server', help='Create a server')
    create_bucket_parser   = create_subparsers.add_parser('bucket', help='Create a bucket')


    # Subparsers within the delete verb
    delete_subparsers = delete_parser.add_subparsers()
    delete_server_parser   = delete_subparsers.add_parser('server', help='Delete a server')
    delete_bucket_parser   = delete_subparsers.add_parser('bucket', help='Delete an bucket')


    # Parser groups for args common to more than 1 command
    infra_parsers = [create_server_parser, create_bucket_parser, delete_server_parser, delete_bucket_parser]
    server_parsers = [start_parser, stop_parser]


    # Add the common args to the parser groups
    for p in infra_parsers:
        p.add_argument('-u', '--user-name', default='root', type=str, help='The name of the user who created the resource')
    for p in server_parsers:
        p.add_argument('-m', '--message',type=str, help='A message explaining why the resource is being started or stoped')



    # Add args specific to the create_subparsers
    create_server_parser.set_defaults(func=create_server)
    create_bucket_parser.set_defaults(func=create_bucket)
    create_bucket_parser.add_argument('-n', '--bucket-name', type=str, help='Create a bucket', default='my-bucket', required=False)


    # Add args specific to the delete_subparsers
    delete_server_parser.set_defaults(func=delete_server)
    delete_bucket_parser.set_defaults(func=delete_bucket)
    delete_bucket_parser.add_argument('-n', '--bucket-name', type=str, help='Delete a bucket', default='my-bucket', required=False)

    
    # Add args specific to the start_parser
    start_parser.set_defaults(func=start_server)
    start_parser.add_argument('-n', '--server-name', type=str, help='Starts a server', choices={'server1', 'server2'}, required=True)


    # Add args specific to the stop_parser
    stop_parser.set_defaults(func=stop_server)
    stop_parser.add_argument('-n', '--server-name', type=str, help='Stops a server', choices={'server1', 'server2'}, required=True)



    args = parser.parse_args()


    # Setup log output
    log_cfg = dict(
        level=logging.ERROR,
        format='[%(levelname)8s] %(filename)-20s %(lineno)3d %(msg)s')
    log_cfg['stream'] = sys.stdout
    logging.basicConfig(**log_cfg)


    # Call the associated verb based on subparser
    args.func(args)


if __name__ == '__main__':
    main()