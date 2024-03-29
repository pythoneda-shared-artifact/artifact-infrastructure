# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/artifact/infrastructure/cli/artifact_repository_folder_cli.py

This file defines the ArtifactRepositoryFolderCli.

Copyright (C) 2023-today rydnr's https://github.com/pythoneda-shared-artifact/artifact-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import abc
import argparse
from pythoneda.shared import BaseObject, PrimaryPort


class ArtifactRepositoryFolderCli(BaseObject, PrimaryPort, abc.ABC):

    """
    A PrimaryPort used to gather the repository folder information.

    Class name: ArtifactRepositoryFolderCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the artifact repository folder.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
    """

    def priority(self) -> int:
        """
        Retrieves the priority of this port.
        :return: The priority.
        :rtype: int
        """
        return 90

    @classmethod
    @property
    def is_one_shot_compatible(cls) -> bool:
        """
        Retrieves whether this primary port should be instantiated when
        "one-shot" behavior is active.
        It should return False unless the port listens to future messages
        from outside.
        :return: True in such case.
        :rtype: bool
        """
        return True

    async def accept(self, app):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: PythonEDA
        """
        parser = argparse.ArgumentParser(
            description="Provide the repository folder of the artifact"
        )

        parser.add_argument(
            "-r", "--repository-folder", required=True, help="The repository folder"
        )

        args, unknown_args = parser.parse_known_args()

        app.accept_repository_folder(args.repository_folder)
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
