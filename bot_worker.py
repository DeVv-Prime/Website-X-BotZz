#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Discord Bot Worker for Vectro Cloud
"""

import os
import sys
import time
import logging

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_bot():
    from app import bot, Config
    
    if not Config.DISCORD_BOT_TOKEN:
        logger.error("DISCORD_BOT_TOKEN not set!")
        return
    
    logger.info("Starting Vectro Bot...")
    
    while True:
        try:
            bot.run(Config.DISCORD_BOT_TOKEN)
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
            break
        except Exception as e:
            logger.error(f"Bot crashed: {e}")
            logger.info("Restarting in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    run_bot()
