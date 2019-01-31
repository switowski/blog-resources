from IPython.core.magic import Magics, magics_class, line_magic
import re


def _run_mypy(code_block, parameters):
    """Runs mypy on a code_block

    Parameters
    ----------
    code_block : str
        String of code to check
    parameters : list, optional
        List of parameters that mypy accepts

    Returns
    -------
    tuple
        (checking_report, error_report, exit_code)
    """
    try:
        from mypy.api import run
    except ImportError:
        return "'mypy' not installed. Did you run 'pip install mypy'?"

    return run(["-c", code_block, *parameters])


def _get_history(range_string):
    """Returns commands from a given history range

    Parameters
    ----------
    cells : str
        String representing the range of cells (the same one that %history
        accepts)

    Returns
    -------
    str
        String of concatenated history commands, separated by '\n'
    """
    ip = get_ipython()
    history = ip.history_manager.get_range_by_str(range_string)
    # history contains tuples with the following values:
    # (session_number, line_number, input value of that line)
    # We only need the input values concatenated into one string
    # with trailing whitespaces removed from each line
    return "\n".join([value.rstrip() for _, _, value in history])


# The class MUST call this class decorator at creation time
@magics_class
class MypyMagics(Magics):
    @line_magic
    def mypy_run(self, line):
        """Runs mypy type check on given lines from the history.

        It prints the report and errors and returns the exit code from mypy.

        Parameters
        ----------
        line : str
            String containing either parameters to mypy or cell numbers/ranges
            (e.g '1', '1 2 3, '1-5', '1 2-4 6')

        Returns
        -------
        int
            Integer with the exit code returned by mypy
        """
        if not line:
            return "You need to specify cell range, e.g. '1', '1 2' or '1-5'."

        args = line.split()
        # Parse parameters and separate mypy arguments from cell numbers/ranges
        mypy_arguments = []
        cell_numbers = []
        for arg in args:
            if re.fullmatch(r"\d+(-\d*)?", arg):
                # We matched either "1" or "1-2", so it's a cell number
                cell_numbers.append(arg)
            else:
                mypy_arguments.append(arg)

        # Get commands from a given range of history
        range_string = " ".join(cell_numbers)
        commands = _get_history(range_string)

        # Run mypy on that commands
        print("Running type checks on:")
        print(commands)

        result = _run_mypy(commands, mypy_arguments)

        if result[0]:
            print("\nType checking report:\n")
            print(result[0])  # stdout

        if result[1]:
            print("\nError report:\n")
            print(result[1])  # stderr

        # Return the mypy exit status
        return result[2]


ip = get_ipython()
ip.register_magics(MypyMagics)
