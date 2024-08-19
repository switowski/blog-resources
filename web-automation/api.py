import datetime
import logging
from typing import Optional

from .helpers import add_access_json, check_access_json, launch_browser, login, remove_access_json


async def add_access(script: str, user: str, trial: bool = False, date: Optional[str] = None):
    """Handle the logic for adding access to a script for a given user."""
    browser, page = await launch_browser()
    await login(page)

    resp = await check_access_json(page, script, user)
    if results := resp["results"]:
        if "expiration" not in results[0]:
            output = f"User '{user}' already has non-expiring access to script {script}!"
            await browser.close()
            logging.info(output)
            return output
        else:
            # Remove existing temporary access
            logging.info(f"User '{user}' has temporary access to script {script}")
            resp = await remove_access_json(page, script, user)
            if resp["status"] != "ok":
                error = f"Something went wrong when removing access to {script} from user {user}: {resp}"
                await browser.close()
                logging.info(error)
                return error
            logging.info("Temporary access REMOVED")

    if trial:
        end_date = datetime.date.today() + datetime.timedelta(days=8)
        expiration_str = f"{end_date.isoformat()}T23:59:59.999Z"
    elif date:
        try:
            end_date = datetime.datetime.strptime(date, "%Y%m%d").date()
        except ValueError:
            error = f"Invalid end date format: '{date}'! It should be like this: 20211231"
            await browser.close()
            logging.info(error)
            return error
        expiration_str = f"{end_date.isoformat()}T23:59:59.999Z"
    else:
        expiration_str = None

    resp = await add_access_json(page, script, user, expiration_str)
    if resp.get("status") == "ok":
        until = f"until {expiration_str}" if expiration_str else "non-expiring"
        output = f"Access to script {script} ADDED for user {user} [{until}]"
        await browser.close()
        logging.info(output)
        return output
    else:
        error = f"Something went wrong when adding access to {script} for user {user} [{expiration_str}]]: {resp}"
        await browser.close()
        logging.info(error)
        return error


async def check_access(script: str, user: str) -> str:
    """Check if a given user has access to a given script."""
    browser, page = await launch_browser()
    await login(page)

    resp = await check_access_json(page, script, user)
    results = resp["results"]

    output = ""
    if not results:
        output = f"User {user} DOESN'T HAVE access to script '{script}'"
    else:
        result = results[0]
        if result.get("username") == user:
            if "expiration" not in result:
                output = f"User {user} HAS non-expiring access to script '{script}'"
            else:
                expiration = result.get("expiration")
                output = f"User {user} HAS access until {expiration} to script '{script}'"

    await browser.close()
    logging.info(output)
    return output


async def remove_access(script: str, user: str) -> str:
    """Remove access from a given script for a given user."""
    browser, page = await launch_browser()
    await login(page)

    resp = await check_access_json(page, script, user)
    if not resp["results"]:
        output = f"User '{user}' ALREADY DOESN'T HAVE access to script {script}!"
        await browser.close()
        logging.info(output)
        return output

    resp = await remove_access_json(page, script, user)
    if resp["status"] == "ok":
        output = f"Access to script '{script}' REMOVED from user {user}"
        await browser.close()
        logging.info(output)
        return output
    else:
        error = f"Something went wrong when removing access to {script} from user {user}: {resp}"
        await browser.close()
        logging.info(error)
        return error
