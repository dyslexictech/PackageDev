from ._view import append, clear


class OutputPanel(object):
    """This class represents an output panel (which are used for e.g. build systems).

        OutputPanel(window, panel_name, file_regex=None, line_regex=None, path=None)
            * window
                The window. This is usually ``self.window`` or
                ``self.view.window()``, depending on the type of your command.

            * panel_name
                The panel's name, passed to ``window.get_output_panel()``.

            * file_regex
                Important for Build Systems. The user can browse the errors you
                writewith F4 and Shift+F4 keys. The error's location is
                determined with 3 capturing groups:
                the file name, the line number and the column.
                The last two are optional.

                Example:
                    r"Error in file "(.*?)", line (\d+), column (\d+)"

            * line_regex
                Same style as ``file_regex`` except that it misses the first
                group for the file name.

                If ``file_regex`` doesn't match on the current line, but
                ``line_regex`` exists, and it does match on the current line,
                then walk backwards through the buffer until  a line matching
                file regex is found, and use these two matches
                to determine the file and line to go to; column is optional.

            * path
                This is only needed if you specify the file_regex param and
                will be used as the root dir for relative filenames when
                determining error locations.

        Useful attributes:

            view
                The view handle of the output panel. Can be passed to
                ``in_one_edit(output.view)`` to group modifications for example.

        Defines the following methods:

            set_path(path=None, file_regex=None, line_regex=None)
                Used to update ``path``, ``file_regex`` and ``line_regex`` if
                they are not ``None``, see the constructor for information
                about these parameters.

                The file_regex is updated automatically because it might happen
                that the same panel_name is used multiple times.
                If ``file_regex`` is omitted or ``None`` it will be reset to
                the latest regex specified (when creating the instance or from
                the last call of  set_regex/path).
                The same applies to ``line_regex``.

            set_regex(file_regex=None, line_regex=None)
                Subset of set_path. Read there for further information.

            write(text)
                Will just write appending ``text`` to the output panel.

            write_line(text)
                Same as write() but inserts a newline at the end.

            clear()
                Erases all text in the output panel.

            show()
            hide()
                Show or hide the output panel.
    """
    def __init__(self, window, panel_name, file_regex=None, line_regex=None, path=None):
        self.window = window
        self.panel_name = panel_name
        self.view = window.get_output_panel(panel_name)

        self.set_path(path, file_regex, line_regex)

    def set_path(self, path=None, file_regex=None, line_regex=None):
        """Update the view's result_base_dir pattern.
        Only overrides the previous settings if parameters are not None.
        """
        if path is not None:
            self.view.settings().set('result_base_dir', path)
        # Also update the file_regex
        self.set_regex(file_regex, line_regex)

    def set_regex(self, file_regex=None, line_regex=None):
        """Update the view's result_(file|line)_regex patterns.
        Only overrides the previous settings if parameters are not None.
        """
        if file_regex is not None:
            self.file_regex = file_regex
        if hasattr(self, 'file_regex'):
            self.view.settings().set('result_file_regex', self.file_regex)

        if line_regex is not None:
            self.line_regex = line_regex
        if hasattr(self, 'line_regex'):
            self.view.settings().set('result_line_regex', self.line_regex)
        # Call get_output_panel so that it'll be picked up as a result buffer
        self.window.get_output_panel(self.panel_name)

    def write(self, text):
        """Appends ``text`` to the output panel.
        Alias for ``sublime_lib.view.append(self.view, text)``.
        """
        append(self.view, text)

    def write_line(self, text):
        """Appends ``text`` to the output panel and starts a new line.
        """
        self.write(text + "\n")

    def clear(self):
        """Clears the output panel.
        Alias for ``sublime_lib.view.clear(self.view)``.
        """
        clear(self.view)

    def show(self):
        """Makes the output panel visible.
        """
        self.window.run_command("show_panel", {"panel": "output.%s" % self.panel_name})

    def hide(self):
        """Makes the output panel invisible.
        """
        self.window.run_command("hide_panel", {"panel": "output.%s" % self.panel_name})
