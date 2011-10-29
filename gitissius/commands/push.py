import commands
import gitshelve

class Command(commands.GitissiusCommand):
    """
    Push issues to repo
    """
    name = "push"
    aliases = []
    help = "Push issues to origin remote"

    def _execute(self, options, args):
        gitshelve.git('push', 'origin', 'gitissius')
