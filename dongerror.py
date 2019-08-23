import sys
import traceback

from dongerror import config


def donger_exception_handler(exc_type, exc_value, exc_traceback):

    new_exception = None

    for exc in exc_type.__mro__:

        exc_type_name = exc.__name__

        if exc_type_name in config.EXCEPTION_DONGERS:
            donger_icon = config.EXCEPTION_DONGERS[exc_type_name].decode()
            new_exception = type(
                "{exc_type_name} {donger_icon}".format(
                    exc_type_name=exc_type_name,
                    donger_icon=donger_icon),
                (exc_type,),
                dict(),
            )

        if new_exception:
            break

    f = traceback.format_exception(
        new_exception,
        new_exception(*exc_value.args),
        exc_traceback)

    f[-1] = f[-1].replace(
        '{mdl_name}.{exc_type_name}'.format(
            mdl_name=__name__,
            exc_type_name=exc_type_name),
        '({exc_type_name})'.format(
            exc_type_name=exc_type_name))

    sys.stderr.write(''.join(f))


sys.excepthook = donger_exception_handler
