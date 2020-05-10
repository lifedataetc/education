if __name__ == '__main__':
    import sys
    from support_funcs import *

    if len(sys.argv) != 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])

    cmd = sys.argv[1].lower()
    service = Daemon_Class('daemon_class', pid_dir='/tmp/')

    if cmd == 'start':
        service.start()
    elif cmd == 'stop':
        service.stop()
    elif cmd == 'status':
        if service.is_running():
            print("Service is running.")
        else:
            print("Service is not running.")
    else:
        sys.exit('Unknown command "%s".' % cmd)