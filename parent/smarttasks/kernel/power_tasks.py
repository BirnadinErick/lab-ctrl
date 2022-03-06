# Imports
import logging
import asyncio

import aiohttp

from smarttasks.kernel.utils import construct_request

# BEGIN

# begin send_code --------------------------------------------------------
async def __send_code(session:aiohttp.ClientSession, target:str, code:int, log:logging.Logger):
    request = construct_request({"code":code})
    try:
        log.debug(f"Requesting {target}...")
        response = await session.post(f"http://{target}:42004/act", json=request)
        if response.status != 202:
            log.error(f"{target} returned: {response.status}")
            log.error(f"{target}'s response body:{response.json()}")
        else:
            log.info(f"Child {target} returned 202")
            json_res = await response.json()
            if json_res["msg"] != 1:
                log.error(f"Something went wrong with {target} ")
    except Exception as e:
        log.error(f"Exception raised when processing {target}" + e.__str__())
        return False, target
    else:
        return True, target
# end send_code ----------------------------------------------------------


# begin shutdown_task --------------------------------------------------------
async def shutdown(targets:list):
    log = logging.getLogger("smarttasks.power_tasks::shutdown")
    log.info(f"Shutdown initiated on {targets}...")

    # broadcast the msg
    async with aiohttp.ClientSession() as session:
        ops = []
        for target in targets:
            log.debug(f"spawning target {target}...")
            status, _ = await asyncio.ensure_future(
                __send_code(session, target, 1, log)
            )
            ops.append((status, _))
        log.debug("Starting to request shutdown...")
        ops_done = await asyncio.gather(*ops)
        log.debug("Done requesting shutdown!")
    
    for status, target in ops_done:
        if status:
            log.info(f"{target} shutdown initiated")
        else:
            log.error(f"{target} refused the request")
# end shutdown_task ----------------------------------------------------------

# END

if __name__ == '__main__':
    pass