import asyncio
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container  

async def main():
    dsa_team