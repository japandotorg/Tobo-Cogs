"""Sticky - Sticky messages to a channel."""
from .sticky import Sticky


async def setup(bot):
    """Load Sticky."""
    await bot.add_cog(Sticky(bot))
